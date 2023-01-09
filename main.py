import glob
import cv2


# 이미지 파일을 모두 img_files 리스트에 추가
# 1. glob 함수 이용
# 특정 패턴의 문자열에 있는 파일들을 다 불러옴 images 폴더 밑에 jpg로 끝나는 파일을 다 불러옴
# img_files = glob.glob('.\\Right_images\\*.jpg')
img_files = glob.glob('.\\Left_images\\*')


# 전체 화면으로 'image' 창 생성
cv2.namedWindow('image',cv2.WND_PROP_FULLSCREEN)

# 상단바 없애기, cv2. WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN을 이용하여 전체화면 속성으로 변경
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# 화면 사이즈와 , 위치 선정
# cv2.resizeWindow('image', width=960, height=1080)
# cv2.moveWindow('image', x=2880, y=0)
cv2.resizeWindow('image', width=777, height=874)
cv2.moveWindow('image', x=1997, y=16)


# 사진을 다 보면 처음 사진으로 돌아가게 하기
cnt = len(img_files)
idx = 0

# 무한 루프 실행
while True:
    img = cv2.imread(img_files[idx])

    if img is None: # 이미지가 없는 경우
        print('Image load failed!')
        break

    cv2.imshow('image', img)
    if cv2.waitKey(10000) >= 0: # 1초 동안 사진보여주는데 만약에 키보드 입력이 있으면 종료
        break

    # 사진을 다 보면 첫번째 사진으로 돌아감
    idx += 1
    if idx >= cnt:
        idx = 0

cv2.destroyAllWindows()