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
# ⌨️ (45:11) SED