import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

record = False
flip = False

while True:
    ret, img = cap.read()

    if ret == False:
        break

    # flip
    if flip:
        img = cv2.flip(img, 1)

    # record
    if record:
        out.write(img)
        cv2.circle(img, (30,30), 10, (0,0,255), -1)

    cv2.imshow('img', img)

    key = cv2.waitKey(1) & 0xFF

    # space → record on/off
    if key == 32:
        record = not record

    # capture
    if key == ord('c'):
        cv2.imwrite('screenshot.jpg', img)

    # flip on/off
    if key == ord('f'):
        flip = not flip

    # esc → exit
    if key == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()