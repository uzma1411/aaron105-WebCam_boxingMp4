import cv2

vid = cv2.VideoCapture("boxing.mp4")

if(vid.isOpened() == False):
    print("Unable to open webcam...plz check!")
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(vid.get(cv2.CAP_PROP_FPS))

out = cv2.VideoWriter("b2.mp4",cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))


print(height,width,fps)

while True:

    ret,frame = vid.read()
    
    cv2.imshow("web cam using py",frame)
    out.write(frame)

    if cv2.waitKey(25) == 32:
        break
    
vid.release()
out.release()



