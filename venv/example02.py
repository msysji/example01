import cv2
from pathlib import Path

path = Path('/Users/jun/PycharmProjects/example01/venv/images')
pngs = path.glob('*.png')
for p in pngs:
    # 画像を読み込む。
    img = cv2.imread(str(p))

    # Canny エッジ検出を行う。
    edges = cv2.Canny(img, 100, 400)

    # 結果を保存する。
    cv2.imwrite("/Users/jun/PycharmProjects/example01/venv/edges/" + p.name, edges)
