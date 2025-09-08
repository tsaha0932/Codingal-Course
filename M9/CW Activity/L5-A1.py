#Import all the necessary libraries
#PIL (Python Imaging Library) provides image editing capabilities to the python interpreter 
from tkinter import *
from PIL import Image, ImageTk

# Create a window with a title bar and set its geometry as well
root = Tk()
root.title('image')
root.geometry('500x500')

# Now use Image.open to open and identify the given image file
upload = Image.open("img.jpg")

# Convert this Image to Tkinter compatible image
image = ImageTk.PhotoImage(upload)

#Add image to Tkinter Label
label = Label(root, image=image, height=450, width=400)
label.place(x=50, y=0)
label2 = Label(root, text="This is how you add an image in Tkinter Window")
label2.place(x=50, y=420)

#run the application
root.mainloop()