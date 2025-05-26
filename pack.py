import zipfile
import os
import fnmatch
from datetime import datetime

class ProjectZipper:
    def __init__(self):
        self.exclude_patterns = self.get_gitignore_patterns()

    @staticmethod
    def get_gitignore_patterns():
        """读取.gitignore文件中的规则"""
        patterns = []
        if os.path.exists('.gitignore'):
            with open('.gitignore', 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        patterns.append(line)
        # 添加默认要排除的文件模式
        patterns.extend(['*.zip', '*.rar', '*.tar', '*.gz', '*.7z'])
        return patterns

    def should_exclude(self, path):
        """检查文件是否应该被排除"""
        # 转换为相对路径
        rel_path = os.path.relpath(path)
        
        # 检查是否是 __pycache__ 目录
        if '__pycache__' in path.split(os.sep):
            return True
            
        # 检查是否符合任何 gitignore 模式
        for pattern in self.exclude_patterns:
            # 处理目录模式（以 / 结尾的模式）
            if pattern.endswith('/'):
                if fnmatch.fnmatch(rel_path + '/', pattern):
                    return True
            # 处理普通文件模式
            elif fnmatch.fnmatch(rel_path, pattern):
                return True
            # 处理 **/ 模式
            elif '**/' in pattern:
                pattern = pattern.replace('**/', '')
                if fnmatch.fnmatch(os.path.basename(rel_path), pattern):
                    return True
        
        return False

    def generate_unique_filename(self, base_filename):
        """生成带有时间戳的唯一文件名"""
        # 分离文件名和扩展名
        name, ext = os.path.splitext(base_filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # 构造新文件名
        new_filename = f"{name}_{timestamp}{ext}"
        
        # 如果文件已存在，添加数字后缀
        counter = 1
        while os.path.exists(new_filename):
            new_filename = f"{name}_{timestamp}_{counter}{ext}"
            counter += 1
            
        return new_filename

    def create_zip(self, source_dir, output_filename):
        """创建压缩文件，排除指定的文件和目录"""
        # 生成唯一的输出文件名
        final_output_filename = self.generate_unique_filename(output_filename)
        
        # 确保输出目录存在
        output_dir = os.path.dirname(final_output_filename)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        print(f'Creating zip file: {final_output_filename}')
        added_files = 0
        
        with zipfile.ZipFile(final_output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source_dir):
                # 从后向前遍历，这样可以安全地从列表中删除项目
                dirs[:] = [d for d in dirs if not self.should_exclude(os.path.join(root, d))]
                
                for file in files:
                    file_path = os.path.join(root, file)
                    # 跳过输出的zip文件本身
                    if os.path.abspath(file_path) == os.path.abspath(final_output_filename):
                        continue
                    # 检查是否应该排除该文件
                    if not self.should_exclude(file_path):
                        arcname = os.path.relpath(file_path, source_dir)
                        print(f'Adding: {arcname}')
                        zipf.write(file_path, arcname)
                        added_files += 1

        # 打印汇总信息
        print(f'\nZip file created successfully:')
        print(f'- Location: {os.path.abspath(final_output_filename)}')
        print(f'- Files added: {added_files}')
        print(f'- Size: {self.get_file_size(final_output_filename)}')

    @staticmethod
    def get_file_size(file_path):
        """返回人类可读的文件大小"""
        size = os.path.getsize(file_path)
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} TB"

def main():
    try:
        # 设置默认输出文件名
        output_zip = 'project.zip'
        
        # 创建打包器实例并执行打包
        zipper = ProjectZipper()
        zipper.create_zip('.', output_zip)
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        # 如果压缩过程被中断，删除可能未完成的压缩文件
        if os.path.exists(output_zip):
            os.remove(output_zip)
    except Exception as e:
        print(f"\nError occurred: {str(e)}")

if __name__ == '__main__':
    main()