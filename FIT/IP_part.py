# FIT: 画像処理部のプログラム
# 生成した画像の平均をとり，結果を出力するプログラム
# ライブラリをインポート
import cv2
import numpy as np
import glob

# 定数
WIDTH = 255 # 画像の横幅
HEIGHT = 255 # 画像の縦幅
CHANNEL = 3 # 画像のチャネル数

def a_mean(img): # 算術平均による重ね合わせ
    result = np.zeros((WIDTH, HEIGHT, CHANNEL)) # 結果用の配列宣言
    for i in range(IMAGE_NUM):
        result += img[i] // IMAGE_NUM # 算術平均をとる(数で除算しつつ，足し合わせ)
    cv2.imwrite('./result/output1.bmp', result) # 画像を出力

def w_mean(img): # 加重平均による重ね合わせ
    result = np.zeros((WIDTH, HEIGHT, CHANNEL)) # 結果用の配列宣言
    weight = np.zeros((IMAGE_NUM)) # 重み格納用の配列宣言
    sum = 0 # 全画素の合計格納用変数
    for i in range(IMAGE_NUM):
        sum += np.sum(img[i]) # 総和を計算
    for i in range(IMAGE_NUM):
        weight[i] = np.sum(img[i]) / sum # 重みを計算
    for i in range(IMAGE_NUM):
        result += weight[i] * img[i]
    cv2.imwrite('./result/output2.bmp', result) # 画像を出力

def loadImage(): # 画像のロードを行う関数
    global IMAGE_NUM, image # モデルの数(それぞれのモデルより得る超解像画像の数)，画像(リストとして)を格納する配列をグローバル宣言
    files = glob.glob('./data/*.bmp') # 生成した超解像画像のファイルパスを全て取得
    IMAGE_NUM = len(files) # 画像の数を取得

     # 画像の枚数分格納できる配列を作成
    image = np.zeros((IMAGE_NUM, WIDTH, HEIGHT, CHANNEL))
    for i in range(IMAGE_NUM): # 画像の枚数分，繰り返す
        image[i] = cv2.imread(files[i]) # 画像を読み込み，配列として別のリスト(image配列)に格納
    
    a_mean(image) # 算術平均による重ね合わせ
    w_mean(image) # 加重平均による重ね合わせ

def error_process(): # 原画像のリサイズを行う関数
    file = './data/butterfly_GT.bmp' # リサイズする画像のパスを取得
    img = cv2.imread(file) # 画像の読み込み
    img = cv2.resize(img, (WIDTH, HEIGHT)) # リサイズ
    cv2.imwrite('./data/buttefly_GT.bmp', img) # 書き出し

if __name__ == '__main__': # メイン関数
    error_process()
    loadImage()