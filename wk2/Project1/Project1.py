import cv2
import matplotlib.pyplot as plt




adaora_image=cv2.imread("adaora.jpg")
chris_image=cv2.imread("chris_ogbechie.jpg")
darlington_image=cv2.imread("darlington_sst.jpg")
enase_image=cv2.imread("enase_okonedo.jpg")
ikechukwu_image=cv2.imread("ikechukwu_don.png")
nneka_png=cv2.imread("NNEKA.png")
obiaya_image=cv2.imread('obiaya.jpg')
peter_image=cv2.imread("peter_bamkole.jpg")
sola_pic=cv2.imread("sola_oni.jpg")


Pathdictionary={
 "Adaora" : adaora_image,
 "Chris":chris_image,
 "Darlington": darlington_image,
 "Enase":enase_image,
 "Donatus": ikechukwu_image,
 "Nneka":nneka_png,
 "Ikechukwu":obiaya_image,
 "Peter":peter_image,
 "Sola":sola_pic

}
emptylist=[]
for i in Pathdictionary.keys():
    emptylist.append(i)
print(Pathdictionary.keys())

print(f"The list is {emptylist}")

LastNameDictionary={


}
last_name=["Onaga","Ogbechie","Agholor","Okonedo","Ogbuike", "Okekearu","Obiaya", "Bamkole","Oni"]


for x in range(len(emptylist)):
    LastNameDictionary[emptylist[x]]=last_name[x]

#print(f"The last name dict is {LastNameDictionary}")

password_dict={}

for x in range(len(emptylist)):
    password_dict[emptylist[x]]=len(LastNameDictionary[emptylist[x]])
#print(f"Password dict test  {password_dict}")
print()
var=input("Enter in your name :     ")
if var not in emptylist:
    print("Name does not exist in database")
else:
    pass_var=int(input("Enter in your password  "))
    if password_dict[var]==pass_var:
        cv2.imshow(var,Pathdictionary[var])
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error")





'''
adaora_image=cv2.imread("adaora.jpg")



cv2.imshow("Adaora",adaora_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
'''

