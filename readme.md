# ⌨️ (00:00) Introduction
- source code
  - https://github.com/herbertech/bash-intro-tutorial
- bashスクリプトとpythonスクリプトの違い
  - 環境への依存性
    - bash はほとんどの Unix ベースのシステムにデフォルトでインストールされている
    - Python はインストールして適切なバージョンを使用する必要があります。
    - このため、環境が制限されている場合や、スクリプトをすぐに実行したい場合は、bash が適している場合がある
  - シェルコマンドとの相互作用
    - bash はシェルスクリプト言語であるため、シェルコマンドの実行やパイプ処理が直感的
    - Python でも subprocess モジュールを使用してシェルコマンドを実行できますが、構文が長くなることがある
  - 起動速度
    - bash スクリプトは、通常、Python スクリプトよりも起動が速く、軽量
    - しかし、大規模なプロジェクトや高度な機能が必要な場合、Python の方が適している
  - エラー処理とデバッグ
    - Python はより強力なエラー処理とデバッグ機能を提供し、コードの品質と保守性が向上
    - bash はこれらの機能に関しては限定的
  - まとめ
    - bashで作れそうなスクリプトはまずbashで作成してみる
    - 作れなさそうだったら，pythonで作る
  - ex.) pythonとbashで作成した同様の処理を行うスクリプト
```python
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
    file_name = input("検索ワードを入力＞")

    file_paths = find_files(file_name)

    if not file_paths:
        print("\nファイルが見つかりませんでした")
        return

    print("\n検索結果")
    for i, path in enumerate(file_paths):
        print(f'{i+1}. {path}')

    confirmed_index = int(input("編集するファイルを選択（番号指定）＞")) - 1

    if confirmed_index < 0 or confirmed_index >= len(file_paths):
        print("\n無効な番号が入力されました．スクリプトを実行し直してください")
        return

    change_text_into_headline(file_paths[confirmed_index])

if __name__ == '__main__':
    main()
```
```sh
#!/bin/bash

read -r -p "検索ワードを入力＞" search_word

# ディレクトリ配下を再帰的に検索し，結果を配列に変換して格納
IFS=$'\n' readarray -t matching_files < <(find . -type f -name "*$search_word*")

if [ ${#matching_files[@]} -eq 0 ]; then
  echo "ファイルが見つかりませんでした"
  exit 1
fi

echo -e "\n検索結果"
for i in "${!matching_files[@]}"; do
  echo "$((i+1)). ${matching_files[i]}"
done

read -r -p "編集するファイルを選択（番号指定）＞" selected_index

if [[ $selected_index -lt 1 ]] || [[ $selected_index -gt ${#matching_files[@]} ]]; then
  echo "無効な番号が入力されました. スクリプトを実行し直してください"
  exit 1
fi

selected_file="${matching_files[$((selected_index-1))]}"
sed -i 's/^/# /' "$selected_file"
```
# ⌨️ (03:24) Basic commands
- vim
  - 変更を無視してquitしたい場合
    - :q!
# ⌨️ (06:21) Writing your first bash script
- ホームディレクトリ
  - `~/<directory name>`は現在のホームディレクトリにいることを示している
- shebang(`#!/bin/bash`)の必要性
  - インタープリタの指定
    - shebangは、スクリプトを実行するのに適切なインタープリタをOSに知らせます。
  - ポータビリティの向上
    - shebangがあることで、スクリプトが異なるシステムでも同じように実行されるようになります。
  - 実行可能ファイルとしてのスクリプト
    - shebangがあることで、スクリプトを実行可能ファイルとして扱うことができます。
    - スクリプトに実行権限を付与し、直接実行することができます。
      - ex.) ./myscript.sh のように実行することが可能
        - shebangがない場合、スクリプトを実行するには、bash myscript.sh のように、明示的にインタープリタを指定する必要があります。
# ⌨️ (14:55) Positional arguments
- 位置引数
  - スペースで区切られる
# ⌨️ (16:23) Output/Input redirection
- パイピング`|`
  - 左のコマンドの出力を右のコマンドに転送する
  - ex.) `ls -l /usr/bin | grep bash`
    - bashというワードとマッチするものだけ抽出する
- 出力リダイレクト`>` `>>`
  - 左のコマンドの出力を右のファイルへ送信する
    - `>`
      - 上書き
    - `>>`
      - 追加（次の行へ） 
    - ex.) `echo Hello World > hello.txt`
- 入力リダイレクト
  - `<`
    - 右のファイルを左のコマンドに受け渡す
  - ex.)
    - hello.txt
      - `Hello World Good day to you`
    - `wc -w hello.txt`
      - `6 hello.txt`
        - `-w`オプションは単語数カウントモード
    - `wc -w < hello.txt`
      - `6`
        - こっちだと数字だけ出力される
  - `<<`（ヒアドキュメント）
    - 複数行の文字列を扱える
    - ex.)
      - `cat << EOF \ これはヒアドキュメントの例です。\ 複数行にわたるテキストを簡単に扱うことができます。\ EOF`
  - `<<<`（ヒアストリング）
    - 単一行の文字列を扱える
    - ex.)
      - `read -r first_line <<< "EOS \これはヒアドキュメントの例です。\ 複数行にわたるテキストを簡単に扱うことができます。\ EOS" \ echo "最初の行: $first_line"`
# ⌨️ (23:23) Test operators
- 式がtrue(=0)かfalse(=1)かを返す
- ex.)
  - `[ hello = hello ]`
    - すべてのスペースが必須
      - `[]`の間と`=`の間
    - 比較するものがint型の場合，`=`は`-eq`と記述することも可能
      - ex.)
        - `[ 1 -eq 1]`
  - `echo $?`
    - $?
      - 最後に実行されたコマンドを返す
  - `0`を出力
# ⌨️ (25:19) If/Elif/Else
- `${1,,}`
  - 1つ目の位置引数を全て小文字に変換する
# ⌨️ (32:16) Arrays
- ex.)
  - `LIST=(one two three four five)`
  - `echo $LIST`
  - `one`のみ出力される
  - `echo ${LIST[@]}`
  - `one two three four five`が出力される
    - `echo $LIST[@]`
    - `one[@]`が出力される
# ⌨️ (34:12) For loop
- `for item in ${LIST[@]}; do echo -n $item | wc -c; done`
  - `for item in ${LIST[@]}; do ...; done`
    - 配列`LIST`の各要素に対して繰り返し処理を実行
  - `echo -n $item`
    - `-n`
      - 改行なしで出力
  - `wc -c`
    - `-c`
      - 文字数カウントモード
# ⌨️ (36:03) Functions
- `up=$(uptime -p | cut -c4-)`
  - `uptime -p`
    - システムのアップタイムを "up X hours, Y minutes" の形式で表示
  - `cut -c4-`
    - 先頭の`"up "`を取り除く
- `since=$(uptime -s)`
  - `uptime -s`
    - システムが起動した時刻を表示
- uptimeを使用するには，WSLを使ってBashスクリプトを実行する必要がある
- 関数内の変数がグローバル変数になってしまっている問題
```diff
# スクリプト
#!/bin/bash

up="up"
since="since"
echo $up
echo $since

showuptime(){
-   up=$(uptime -p | cut -c4-)
+   local up=$(uptime -p | cut -c4-)
-   since=$(uptime -s)
+   local since=$(uptime -s)
    cat << EOF
----------
This machine has been up for ${up}
It has been running since ${since}
----------
EOF
}

showuptime

echo $up
echo $since

# 出力
up
since
    ----------
    This machine has been up for 23 minutes
    It has been running since 2023-05-13 15:43:19
    ----------
- 23 minutes
+ up
- 2023-05-13 15:43:19
+ since
```
# ⌨️ (42:30) AWK
- テキスト処理ツール
- ex.)
  - `echo one two three > testfile.txt`
  - `awk '{print $1}' testfile.txt`
    - `'{print $1}'`
      - awkアクション．各行の1番目のフィールド（デフォルトではスペースやタブで区切られた単語）を出力する
  - `one`を出力する
- ex.)
  - `echo one,two,three > csvtest.csv`
  - `awk -F, '{print $1}' csvtest.csv`
    - フィールドセパレータが`,`に変更される
  - `one`を出力する
- ex.)
  - `echo "Just get this word: Hello" | awk '{print $5}'`
  - `Hello`が出力される
- ex.)
  - `echo "Just get this word: Hello" | awk -F: '{print $2}'`
  - `Hello`が出力される
# ⌨️ (45:11) SED