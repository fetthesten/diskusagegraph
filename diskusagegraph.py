import os, sys

class DiskUsageGraph:

    def __init__(self, path = None):
        self.error = None
        self.dir_map = {
                'path': path,
                'is_dir': True,
                'is_file': False,
                'stat_size': 0,
                'dir': self.scandir_recursive(path)}

    def scandir_recursive(self, path = False):
        with os.scandir(path) as it:
            result = {}
            dir_size = 0
            for entry in it:
                is_dir = entry.is_dir()
                is_file = entry.is_file()
                stat_size = entry.stat().st_size if is_file else 0

                subdir = None if is_file else self.scandir_recursive(entry.path)
                dir_size += stat_size if is_file else subdir['dir_size']
                
                result[entry.name] = {
                    'path': entry.path,
                    'is_dir': is_dir,
                    'is_file': is_file,
                    'stat_size': stat_size,
                    'dir': subdir
                    }
            result['dir_size'] = dir_size
            return result

    def get_dir(self, path = False, named = False):
        if path:
            path = path.split('\\')
        else:
            path = ''
        current_dir = self.dir_map
        current_dir_name = ''
        for next_dir in path:
            if current_dir:
                current_dir = current_dir['dir'].get(next_dir)
                current_dir_name = next_dir
        if named:
            return {next_dir: current_dir}
        else:
            return current_dir

    def sizeof_fmt(num, suffix='B'):
        for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
            if abs(num) < 1024.0:
                return "%3.1f%s%s" % (num, unit, suffix)
            num /= 1024.0
        return "%.1f%s%s" % (num, 'Yi', suffix)
