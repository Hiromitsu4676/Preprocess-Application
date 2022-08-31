import tkinter as tk
import glob
import pandas as pd

def btn_click():
    #最初のGUIの画面に戻る
    def return_view():
        baseGround_new_csv.destroy()

    baseGround_new_csv = tk.Tk()
    # GUIの画面サイズ
    baseGround_new_csv.geometry('500x300')

    #GUIの画面タイトル
    baseGround_new_csv.title('結果')

    #ディレクトリのパス
    path=input1.get()

    #CSVファイルのパスのリスト
    csv_files = glob.glob(path+'/*.csv')

    #csvファイルの中身を追加していくリストを用意
    data_list = []

    #読み込むファイルのリストを走査
    for file in csv_files:
        data_list.append(pd.read_csv(file,encoding='cp932'))

    #リストを全て行方向に結合
    df = pd.concat(data_list, axis=0)

    #結合ファイルの保存
    df.to_csv("{}/merged.csv".format(input1.get()),index=False,encoding='cp932')

    lbl_result = tk.Label(baseGround_new_csv, text='完了')
    lbl_result.pack()
    
    # ボタン
    btn_return = tk.Button(baseGround_new_csv, text='前のGUIの画面に戻る', command=return_view)
    btn_return.pack()
    baseGround_new_csv.mainloop()

baseGround = tk.Tk()

# GUIの画面サイズ
baseGround.geometry('600x180')
#GUIの画面タイトル
baseGround.title('CSV merge  ver1.0')
label1 = tk.Label(baseGround, text="フォルダ内の複数のcsvファイルを結合します")
label1.pack(anchor=tk.W,padx=5,pady=5)
label2 = tk.Label(baseGround, text="実行後に'merged.csv'が作成されます")
label2.pack(anchor=tk.W,padx=5)
label3 = tk.Label(baseGround, text="フォルダの絶対パスを入力してください")
label3.pack(anchor=tk.W,padx=5,pady=5)
input1 = tk.Entry(width=90)
input1.pack(anchor=tk.W,padx=5,pady=5)

# ボタン
btn = tk.Button(baseGround, text='実行', command=btn_click)
btn.pack(anchor=tk.W,padx=5,pady=5)

#表示
baseGround.mainloop()