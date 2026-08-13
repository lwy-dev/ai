from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang="ch")

img_path = r"C:\Users\lwy86\OneDrive\Desktop\test.png"

result = ocr.ocr(img_path)

for line in result[0]:
    print(line[1][0])