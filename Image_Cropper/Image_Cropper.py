import streamlit as st
from io import BytesIO
from PIL import Image
from zipfile import ZipFile 
import time

st.header("Pradeep's Image Cropper")

# Set parameters

# Accept original image

original_image = st.file_uploader('Upload full legth image',accept_multiple_files=False)
if original_image:
    original_image = Image.open(original_image)
    width_o,hight_o = original_image.size
    st.write(f"Original image size {width_o} X {hight_o}")
else:
    pass

# Accept cropped image
cropped_image = st.file_uploader("Upload cropped image")
if cropped_image:
    cropped_image = Image.open(cropped_image)
    width_c,hight_c = cropped_image.size
    st.write(f"Cropped image size {width_c} X {hight_c}")

    width_diff = (width_o-width_c)/2 # each side left right equally
    hight_diff = (hight_o-hight_c)/2 # each side top bottom equally

    left=width_diff
    upper = hight_diff
    lower = hight_o-hight_diff
    right = width_o-width_diff
else:
    pass

if st.button(label="Set parameters"):
    st.write("Parameters set!")
else:
    st.subheader("Select batch of images!")

images = st.file_uploader("Select images ",accept_multiple_files=True)
zip_buffer = BytesIO()
with ZipFile(zip_buffer,'a') as file:
    for name,i in enumerate(images):
        r = Image.open(i)
        r = r.crop((left, upper, right, lower))
        img_byte = BytesIO()
        r.save(img_byte,format='JPEG')
        img_byte.seek(0)
        file.writestr(zinfo_or_arcname=f"{name}.jpg",data=img_byte.read())
zip_buffer.seek(0)

    
if st.button(label="Crop"):
    bar = st.progress(0)

    for i in range(101):
        t = time.sleep(0.05)
        bar.progress(i)
    bar.success("Done!")

    st.download_button("Download cropped images ",file_name="Cropped.zip",data=zip_buffer,
                            mime="application/zip")
  

