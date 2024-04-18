import os
import numpy as np
import shutil
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from multiprocessing import Pool

def augment_image(class_name, image_file, input_dir, output_dir, datagen,num_augmented_images_per_input):
    try:
        img_path = os.path.join(input_dir, class_name, image_file)
        img = load_img(img_path)
        img_array = img_to_array(img)

        img_array = img_array[2:-2, 2:-2, :] #adding this line of code solved 4 hours of debugging. Ask me why.

        
        img_array = img_array.reshape((1,) + img_array.shape)


        output_class_dir = os.path.join(output_dir, class_name)
        os.makedirs(output_class_dir, exist_ok=True)

        i = 0
        for batch in datagen.flow(img_array, batch_size=1, save_to_dir=output_class_dir, save_prefix=f'aug_{image_file[:-4]}_', save_format='jpeg'):
            i += 1
            if i >= num_augmented_images_per_input:
                break          
    except Exception as e:   
        logging.error(f"Error processing {image_file}: {e}\n{traceback.format_exc()}")            
            
def worker(task):
    augment_image(*task)