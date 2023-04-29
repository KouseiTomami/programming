# 評価手法: PSNR
# 参考: https://note.nkmk.me/python-opencv-skimage-numpy-psnr/
import cv2

# テスト
img0 = cv2.imread('./data/butterfly_GT.bmp') # 元の画像
img1 = cv2.imread('./result/output1.bmp') # 1つ目
img2 = cv2.imread('./result/output2.bmp') # 2つ目

# オリジナル画像を256x256から255x255へサイズダウン
img0 = cv2.resize(img0, (255, 255))

print(cv2.PSNR(img0, img1)) # PSNRの値を算出し表示
print(cv2.PSNR(img0, img2)) # PSNRの値を算出し表示