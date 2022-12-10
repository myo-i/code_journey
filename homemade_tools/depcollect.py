import re
import os
import shutil
TEST_FILE_PATH = "適当なCOBOLファイルのパス"

COPY = re.compile("(COPY|copy)\s{1,}(\s+|\.)([^\. ]+)")

# call
CALL = re.compile("(CALL|call)\s{1,}'([\S]+)'")

FILENAME = re.compile(r"([^\\]+)\.(cbl|CBL)")

# ファイルパスのリスト
filepath_list = []

# 外部ファイル名のリスト
exfile_list = []



def main():
    """
    メイン処理\n
    """
    # for fd_path, sb_folder, sb_file in os.walk('depget'):
    #     for fol in sb_folder:
    #         run(fd_path + '\\' + fol + '\\' + fol + ".java")
    # run(TEST_FILE_PATH)
    
    # ここでディレクトリ配下全てのCOBOLソールのパスを生成すれば完成
    filename_collect(TEST_FILE_PATH)
    makedir_movefile(TEST_FILE_PATH)
    # search_filepath("ZASB870")
    
        
# 出来た
def filename_collect(TEST_FILE_PATH):
    """
    指定したファイルで呼び出されている外部ファイル名を収集\n
    arg => 依存関係を収集したいファイルのパス\n
    このソースに存在しないファイルは持ってこれません
    """
    with open(TEST_FILE_PATH, "r") as f:
        lines = f.readlines()
        
        copy_list = []
        call_list = []
        
        # 正規表現とマッチする文字列をリストに格納
        # 1つにまとめた方が良いかも
        for line in lines:
            # print(line)
            match_copy = re.search(COPY, line)
            match_call = re.search(CALL, line)
            if match_copy:
                copy = match_copy.group(3)
                exfile_list.append(copy)
            elif match_call:
                call = match_call.group(2)
                exfile_list.append(call)
                
                
    # リストの重複を削除
    copy_list = sorted(set(copy_list), key=copy_list.index)
    call_list = sorted(set(call_list), key=call_list.index)
        
                
# 出来た
def makedir_movefile(TEST_FILE_PATH):
    """パスに指定したファイルと同名のディレクトリを作成し移動させる"""
    match_filename = re.search(FILENAME, TEST_FILE_PATH)
    # ディレクトリを作成
    if match_filename:
        main_filename = match_filename.group(1)
        os.makedirs(name=f"test_depcollect\\{main_filename}")
        shutil.move(TEST_FILE_PATH, f"test_depcollect\\{main_filename}\\{main_filename}.cbl")
        
        # 作成したディレクトリに依存関係のファイルをコピー
        for exfile in exfile_list:
            search_filepath(exfile, main_filename)
   
# 出来た     
# コピーしたいファイル名
# メインのファイルパス
def search_filepath(filename, main_filename):
    """
    ファイル名からファイルのパスを検索してコピーして移動
    """
    # ファイル名からファイルのパスを検索してリストに格納
    for root, dirs, files in os.walk(top='develop\patch\cobol'):
        for file in files:
            if file != f"{filename}.cbl" and file != f"{filename}.CBL":
                continue
            
            filepath_list.append(os.path.join(root, file))
            # for aa in filepath_list:
            #     print(aa)
            
    # ファイルのコピー
    for filepath in filepath_list:
        shutil.copy(filepath, f"test_depcollect\{main_filename}")
        
                
        
if __name__ == "__main__":
    main()