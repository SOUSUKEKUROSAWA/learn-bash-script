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
