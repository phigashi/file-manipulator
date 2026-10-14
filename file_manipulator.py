import sys

def do_reverse(inputpath, outputpath):
    try:
        with open(inputpath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"エラー: {inputpath} が見つかりません")
        return

    reversed_content = content[::-1]

    try:
        with open(outputpath, 'w', encoding='utf-8') as f:
            f.write(reversed_content)
        print(f"{outputpath} に書き込み成功しました")
    except Exception as e:
        print(f"書き込みに失敗しました：{e}")

def do_copy(inputpath, outputpath):
    try:
        with open(inputpath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"エラー: {inputpath} が見つかりません")
        return

    copy_content = content

    try:
        with open(outputpath, 'w', encoding='utf-8') as f:
            f.write(copy_content)
        print(f"{outputpath} に書き込み成功しました")
    except Exception as e:
        print(f"書き込みに失敗しました：{e}")

def do_duplicate(inputpath, n):
    try:
        with open(inputpath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"エラー: {inputpath} が見つかりません")
        return

    duplicate_content = content * int(n)

    try:
        with open(inputpath, 'w', encoding='utf-8') as f:
            f.write(duplicate_content)
        print(f"{inputpath} の上書きに成功しました")
    except Exception as e:
        print(f"書き込みに失敗しました：{e}")

def replace_string(inputpath, needle, newstring):
    try:
        with open(inputpath, 'r', encoding='utf-8') as f:
            content = f.read()

        keyword = needle

        if keyword in content:
            replace = content.replace(keyword, newstring)
            try:
                with open(inputpath, 'w', encoding='utf-8') as f:
                    f.write(replace)
                print(f"{inputpath} に文字の置き換え成功しました")
            except Exception as e:
                print(f"書き込みに失敗しました：{e}")
        else:
            print(f"{keyword} は {inputpath} 内には含まれていませんでした")
    except FileNotFoundError:
        print(f"エラー: {inputpath} が見つかりません")
        return



if __name__ == "__main__":
    args = sys.argv
    if len(args) >= 4 and args[1] == "reverse":
        inputpath = args[2]
        outputpath = args[3]
        do_reverse(inputpath, outputpath)
    elif len(args) >= 4 and args[1] == "copy":
        inputpath = args[2]
        outputpath = args[3]
        do_copy(inputpath, outputpath)
    elif len(args) >= 4 and args[1] == "duplicate":
        inputpath = args[2]
        n = args[3]
        do_duplicate(inputpath, n)
    elif len(args) >= 5 and args[1] == "replace-string":
        inputpath = args[2]
        needle = args[3]
        newstring = args[4]
        replace_string(inputpath, needle, newstring)
    else:
        print("正しい引数の渡し方をしてください")