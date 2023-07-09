import cv2
import time
# x=rd.randint(1,10)
# print(x)

# lst = ['ABC','XYZ','Abbas']
# v = rd.choice(lst)
# print(v)

#Building Game Rock-Paper-Scissor
# GameOver = False
#
#
# lst = ['Rock','Paper','Sciccor']
# comp = rd.choice(lst)
# user = print('Enter user value: ')
# print(f'computer: {comp}')
# if(user == comp):
#     print('Draw')
# elif(user == 'Rock' and comp == 'Paper'):
#     print('Computer wins')
# elif(user == 'Rock' and comp == 'Scissor'):
#     print('User wins')
# elif(user == 'Paper' and comp == 'Rock'):
#     print('User wins')
# elif(user == 'Paper' and comp == 'Scissor'):
#     print('Computer wins')
# elif(user == 'Scissor' and comp == 'Paper'):
#     print('User wins')
# elif(user == 'Scissor' and comp == 'Rock'):
#     print('Computer wins')




# i=0
# while(True):
#     print(i)
#     i+=1
#     if(i==5):
#         break
#     if(i==3):
#         continue
#     print('....')

cam = cv2.VideoCapture(0)
total = 0
while(True):
    success , img = cam.read()
    qrd = cv2.QRCodeDetector()
    a,b,c = qrd.detectAndDecode(img)
    if(a!=''):
        print(a)
        if (a == 'Laptop'):
            total += 45000
            print('45000 for Laptop')
            print(f'Your total bill is {total}')
        elif (a == 'Computer'):
            total += 80000
            print('80000 for Computer')
            print(f'Your total bill is {total}')
        elif (a == 'Keyboard'):
            total += 1500
            print('1500 for Keyboard')
            print(f'Your total bill is {total}')
        elif (a == 'Mouse'):
            total += 900
            print('900 for Mouse')
            print(f'Your total bill is {total}')
        elif (a == 'LCD'):
            total += 17000
            print('17000 for LCD')
            print(f'Your total bill is {total}')
            time.sleep(2)
            continue
    cv2.imshow('Img1',img)
    if(cv2.waitKey(1)==27):
        break

# cam = cv2.VideoCapture(0)
# total = 0
# while(True):
#     success, img = cam.read()
#     qrd = cv2.QRCodeDetector()
#     a,b,c = qrd.detectAndDecode(img)
#     if(a!=''):
#         print(a)-
#         if(a == 'Laptop'):
#             total += 45000
#             print('45000 for Laptop')
#             print(f'Your total bill is {total}')
#
#         cv2.imshow('Image',img)
#         if(cv2.waitKey(1)==27):
#             break