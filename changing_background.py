import cv2
import os
import numpy as np


if __name__ == '__main__':

    image_name_list = os.listdir('dataset_stack/images')
    backgrounds = os.listdir('backgrounds')
    i = 0

    for image_name in image_name_list:

        print(image_name)

        current_background_path = 'backgrounds/' + backgrounds[i]
        current_background = cv2.imread(current_background_path)
        current_background = cv2.resize(current_background, (1920,1080))

        image_path = 'dataset_stack/images/' + image_name
        image = cv2.imread(image_path)
        image=cv2.resize(image,(1920,1080))

        mask_path = 'dataset_stack/masks/' + image_name
        mask = cv2.imread(mask_path)
        mask=cv2.resize(mask,(1920,1080))

        new_image = np.where(mask==0, current_background, image)
        new_image_path = 'dataset_new_background/images/' + image_name
        cv2.imwrite(new_image_path, new_image)

        new_mask_path = 'dataset_new_background/masks/' + image_name
        cv2.imwrite(new_mask_path, mask)

        i = i + 1