"""
文件辅助类
"""
import json
import codecs

class fileUtil(object):
    def __init__(self):
        pass

    def open_file(self, filePath):
        try:
            self.file = codecs.open(filePath, 'w', encoding='utf-8')
        except Exception as ex:
            print(ex)
        finally:
            print("file opened. ...........................")

    def write_to_Json(self,item):
        try:
            lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.file.write(lines)
        except Exception as e:
            print(e)
        finally:
            print("json writed ............................")
            pass

    def close_file(self):
        try:
            self.file.close()
        except Exception as ex:
            print(ex)
        finally:
            print("file closed .........................")
