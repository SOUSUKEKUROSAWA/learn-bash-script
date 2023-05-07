"""
使い方
1. ファイル検索を行いたいディレクトリをすべて含む，親ディレクトリに移動する
2. このスクリプトの相対パスを取得する
3. python <相対パス>/change-text-into-headline.py
"""
import os
import fnmatch

def find_files(filename, search_path='.'):
    result = []
    for root, _, files in os.walk(search_path):
        for name in files:
            if fnmatch.fnmatch(name, f'*{filename}*'):
                result.append(os.path.join(root, name))
    return result

def change_text_into_headline(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.readlines()

    with open(file_path, 'w', encoding='utf-8') as f:
        for line in content:
            f.write(f'# {line}')

def main():
    print("====================================================================")
    print("このスクリプトは選択したファイルの各行を見出し行に変更するスクリプトです")
    print("====================================================================")
    
    file_name = input("\n検索ワードを入力してください: ")

    file_paths = find_files(file_name)

    if not file_paths:
        print("\nファイルが見つかりませんでした")
        return

    print("\n検索ワードにマッチするファイルが見つかりました:")
    for i, path in enumerate(file_paths):
        print(f'{i+1}. {path}')

    confirmed_index = int(input("\n編集するファイルパスに一致する番号を入力してください: ")) - 1

    if confirmed_index < 0 or confirmed_index >= len(file_paths):
        print("\n無効な番号が入力されました．スクリプトを実行し直してください")
        return

    change_text_into_headline(file_paths[confirmed_index])

if __name__ == '__main__':
    main()