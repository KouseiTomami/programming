"""未完成"""
# Model ensemble(モデルアンサンブル)による画像の重ね合わせ
# 複数のモデルから最良の超解像画像を選定する
# よりよい超解像画像を得るためのプログラム
# ライブラリをインポート
import os
import cv2
import numpy as np

path = './result' # 結果を出力するディレクトリ

os.makedirs(path, exist_ok=True) # ディレクトリがなければ作る

IMAGE_NUM = 3 # 合算する画像の枚数

all = np.zeros((255, 255, 3)) # 大きさ255x255x3のnumpy配列を作成、全画素の重みを計算後使用する
weight = np.zeros((3)) # 各画素の重みを代入するための配列

def calc_R(img1, img2, img3): # R成分の計算
    print(type(img1))
    
def calc_G(img1, img2, img3): # G成分の計算
    pass
    
def calc_B(img1, img2, img3): # B成分の計算
    pass

def addWeight(image1, image2, image3): # 重みをつけて画像を足し合わせる
    all = (image1 // 3) + (image2 // 3) + (image3 // 3) # 単に算術平均
    cv2.imwrite('./result/output1.bmp', all)
    print(np.max(all))
    # 加重平均
    image = np.array([np.sum(image1), np.sum(image2), np.sum(image3)])
    # 1. 全要素の重み
    print(np.sum(image1))
    print(np.sum(image2))
    print(np.sum(image3))
    for i in range(IMAGE_NUM):
        weight[i] = image[i] / (np.sum(image1) + np.sum(image1) + np.sum(image3))
        print(weight[i])
    # 2. 加重平均により画像を作成
    all = (weight[0] * image1) + (weight[1] * image2) + (weight[2] * image3)
    cv2.imwrite('./result/output2.bmp', all)

def loadImage(): # 複数の画像データを読み込み
    img_org = cv2.imread('./data/butterfly_GT.bmp') # 元の画像
    img_org = cv2.resize(img_org, (255, 255)) # オリジナル画像を256x256から255x255にリサイズ
    print(img_org.shape)
    img_bic = cv2.imread('./data/butterfly_GT_bicubic_x3.bmp') # バイキュービック補間により得た画像
    img_ens = cv2.imread('./data/butterfly_GT_srcnn_x3.bmp') # アンサンブル学習により得た画像
    image = np.array([img_org, img_bic, img_ens])
    print(np.shape(image))
    cv2.imwrite('./test/test1.bmp', img_org)
    cv2.imwrite('./test/test2.bmp', img_bic)
    cv2.imwrite('./test/test3.bmp', img_ens)
    # BGR形式からRGB形式に変換(いらない?)
    # img_org = cv2.cvtColor(img_org, cv2.COLOR_BGR2RGB)
    # img_bic = cv2.cvtColor(img_bic, cv2.COLOR_BGR2RGB)
    # img_ens = cv2.cvtColor(img_ens, cv2.COLOR_BGR2RGB)
    addWeight(img_org, img_bic, img_ens) # 読み込んだ画像を加重平均により合算

if __name__ == "__main__": # メイン関数
    loadImage() # 画像データを読み込み
    