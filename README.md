# Text Utility Script

コマンドラインからテキストファイルの操作を行うPythonスクリプトです。

## 使い方

python script.py <コマンド> [引数...]

### 1. 逆転 (reverse)
入力ファイルを反転して出力します。
python script.py reverse <入力> <出力>

### 2. コピー (copy)
ファイルをコピーします。
python script.py copy <入力> <出力>

### 3. 複製 (duplicate)
ファイルの内容を指定回数繰り返して上書きします。
python script.py duplicate <ファイル> <回数>

### 4. 文字列置換 (replace-string)
ファイル内の文字列を検索・置換して上書きします。
python script.py replace-string <ファイル> <検索ワード> <新しい文字列>
