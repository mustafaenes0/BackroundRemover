# Importing Required Modules
from rembg import remove

# Store path of the image in the variable input_path
input_path="C:\A\B\C.jpg"
# Store path of the output image in the variable output_path
output_path="C:\A\B\C.png"

#Processing the image
with open(input_path,'rb') as i :
    with open(output_path,'wb') as o:
        input_file = i.read()
        output_file = remove(input_file)
        o.write(output_file)
print("Program Finished")
