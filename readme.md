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
# ⌨️ (23:23) Test operators
# ⌨️ (25:19) If/Elif/Else
# ⌨️ (28:37) Case statements
# ⌨️ (32:16) Arrays
# ⌨️ (34:12) For loop
# ⌨️ (36:03) Functions
# ⌨️ (41:31) Exit codes
# ⌨️ (42:30) AWK
# ⌨️ (45:11) SED