# import cv2
# image=input("enter image location : ")
# Image=cv2.imread(image)
# if Image is None:
#     print("Error! image not loaded..")
# else:
#     print("image loaded successfully")
#     gray=cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
    
#     ask=input("enter image 'save' or 'show': ")
#     if ask=="show":
#       #  cv2.imshow("image showing ",image)
#         cv2.imshow("Image showing", gray)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#     else:
#         Output_name=input("enter image output name : ")
#         success=cv2.imwrite(Output_name,Image)
#         if success:
#             print("image save successfully")
#         else:
#             print("image not save try again") 

#image trasformation & manipulation

# import cv2
# image_input=input("enter image location....")
# image=cv2.imread(image_input)
# if image is not None:
#     print("image loaded successfully")
#     resize=cv2.resize(image,(100,100))
#     cropped=resize[100:300,300:400]
#     cv2.imshow("orginal image",image)
#     cv2.imshow("resize image",resize)
#     cv2.imshow("cropped image",cropped)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("error! image not loaded,try again")    

#image rotation&flipping


# import cv2
# image=cv2.imread("Trish.jpeg")
# if image is not None:
#     print("loaded successfully")
#     (h,w)=image.shape[:2]
#     center=[w//2,h//2]
#     m=cv2.getRotationMatrix2D(center,45,1)
#     rotation=cv2.warpAffine(image,m,(h,w))
#     cv2.imshow("orginal image: ",image)
#     cv2.imshow("rotation image: ",rotation)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("error!")    

#flipping

# import cv2
# image=cv2.imread("Trish.jpeg")
# if image is None:
#     print("Error!")
# else:
#     flipped_Horizontal=cv2.flip(image,1)
#     flipped_vertical=cv2.flip(image,0)
#     flipped_both=cv2.flip(image,-1)
#     cv2.imshow("hori",flipped_Horizontal)
#     cv2.imshow("ver",flipped_vertical)
#     cv2.imshow("both",flipped_both)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#basic image drawing Tech

# import cv2
# image=cv2.imread("Trish.jpeg")
# if image is None:
#     print("opps!")
# else:
#     print("image loaded successfully")
#     p1=(100,100)
#     p2=(400,200)
#     color=(0,0,255)
#     thikness=4
#     cv2.line(image,p1,p2,color,thikness)
#     cv2.rectangle(image,p1,p2,color,thikness)
#     cv2.circle(image,(150,150),50,(0,0,255),-1)
#     cv2.putText(image, "riya", (130, 120), cv2.FONT_HERSHEY_SIMPLEX, 6, (0, 0, 255), thikness)
#     cv2.imshow("line drawing:",image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()    


# # Load a small, fast YOLOv11 model
# from ultralytics import YOLO


# model = YOLO("yolo11n.pt")

# # Run detection on a sample image from the internet
# results = model.predict(source="C:\\Users\\Trishita Sarkar\\opencv\\tanu.jpeg", save=True)

# print("Success! Check the 'runs' folder in your sidebar to see the result.")

from ultralytics import YOLO
import cv2

# 1. Load the YOLOv11 model (downloads once, then runs offline)
model = YOLO("yolo11n.pt") 

# 2. Path to your image (Make sure this file is in your folder!)
# Replace 'my_image.jpg' with the actual name of your photo
image_path = r"C:\Users\Trishita Sarkar\OneDrive\Pictures\Screenshots\picock.png" 

# 3. Run Detection
# save=True creates a folder with the result
# conf=0.5 means it only shows objects it is 50% sure about
results = model.predict(source=image_path, save=True, conf=0.5)

# 4. Show the result on screen
for result in results:
    result.show()

print(f"Detection finished! Check the 'runs/detect' folder for the saved image.")