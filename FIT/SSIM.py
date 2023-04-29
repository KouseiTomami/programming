# 評価手法: SSIM
# 参考: https://tecsingularity.com/opencv/imageeval/
import cv2
import sys

def main():
        
    print("OpenCV Version: " + str(cv2.__version__))    

    # Loading image data (COLOR)
    filename1 = "./data/butterfly_GT.bmp" # オリジナル画像
    filename2 = "./result/output1.bmp" # アンサンブル学習により得た画像
    filename3 = "./result/output2.bmp"
    
    image1 = cv2.imread(filename1, cv2.IMREAD_COLOR)
    # オリジナル画像を256x256から255x255へサイズダウン(追加部分)
    image1 = cv2.resize(image1, (255, 255))
    image2 = cv2.imread(filename2, cv2.IMREAD_COLOR)
    image3 = cv2.imread(filename3, cv2.IMREAD_COLOR)
    
    if image1 is None:
        print("Cannot find image1 : " + filename1)
        sys.exit()
    if image2 is None:
        print("Cannot find image2 : " + filename2)
        sys.exit()

    SSIMEval(image1, image2)
    SSIMEval(image1, image3) 

def SSIMEval(image1, image2):
    SSIM_opencv, _ = cv2.quality.QualitySSIM_compute(image1, image2)
    print("SSIM Evaluation Results")
    print("   SSIM OpenCV (Blue): " + str(SSIM_opencv[0]))
    print("   SSIM OpenCV (Green): " + str(SSIM_opencv[1]))
    print("   SSIM OpenCV (Red): " + str(SSIM_opencv[2]))
    print("   SSIM OpenCV (RGB Average): " + str((SSIM_opencv[0] + SSIM_opencv[1] + SSIM_opencv[2]) / 3)) # 本当に見るのはここ

if __name__ == "__main__":
    main()