import os
import random
from PIL import Image


def check_pixel_pink(pix, x, y):
    '''Method to check, if pixel is pink'''

    if pix[x, y][0] == 250 and pix[x, y][1] == 14 and pix[x, y][2] == 191:
        return True


def check_pixel_black(pix, x, y):
    '''Method to check, if pixel is black'''

    if pix[x, y] == 0:
        return True


def stacking(first_image, second_image, first_mask, second_mask):
    '''Method put two images with masks on top of each other (stacking)'''

    # Accessing the image pixels
    pix_img_1 = first_image.load()
    pix_img_2 = second_image.load()
    pix_mask_1 = first_mask.load()
    pix_mask_2 = second_mask.load()

    # Looping through every pixel of the image
    for x in range(1920):
        for y in range(1080):
            # If the pixel of the first image is black and the second is white, replace the pixel of the first image
            # with the pixel of of the second image (for image and mask)
            if check_pixel_black(pix_mask_1, x, y) and not check_pixel_black(pix_mask_2, x, y):
                pix_mask_1[x, y] = pix_mask_2[x, y]
                pix_img_1[x, y] = pix_img_2[x, y]

    # return the image and mask
    return first_image, first_mask


def create_path_to_folder(number_of_objects):
    '''This method creates lists of the paths to the images and masks. it also creates a list of the lengths of the
    folders'''

    # Creating empty lists
    list_images_dir = []
    list_masks_dir = []
    list_lengths = []

    # Number of objects for stacking. Looping through them so that lengths of folders list_image_dir and list_masks_dir
    # are equal to number_of_objects
    for i in range(number_of_objects):
        # Incrementing i, because it starts with 0
        i = i + 1
        # Path to images and masks
        dir_image_name = 'dataset_' + str(i) + '/images'
        dir_mask_name = 'dataset_' + str(i) + '/masks'
        # size of folder images
        length = len(os.listdir(dir_image_name))
        list_images_dir.append(dir_image_name)
        list_masks_dir.append(dir_mask_name)
        list_lengths.append(length)

    # Accessing on image to get width and height of the images and masks
    sample_image_for_with_height = Image.open(list_images_dir[0] + '/' + os.listdir(list_images_dir[0])[0])
    width = sample_image_for_with_height.size[0]
    height = sample_image_for_with_height.size[1]

    # Return the filled lists and the width and height
    return list_images_dir, list_masks_dir, list_lengths, width, height


def image_mask_open(number_of_objects, list_lengths, list_images_dir, list_masks_dir):
    '''Opening a random image from the mask and image folder for every object (every dataset)'''

    # Creating empty lists
    image_list = []
    mask_list = []

    # Looping through
    for i in range(number_of_objects):
        # Initializing a random number that is in the range of 0 and the size of the folder the images are in
        random_nr = int(random.random() * list_lengths[i])
        # Opening image and mask and appending it to the lists image-list and mask_list
        image = Image.open(list_images_dir[i] + '/' + os.listdir(list_images_dir[i])[random_nr])
        mask = Image.open(list_masks_dir[i] + '/' + os.listdir(list_masks_dir[i])[random_nr])
        image_list.append(image)
        mask_list.append(mask)

    # Returning image_List and mask_list
    return image_list, mask_list


def img_msk_name_list(number_of_objects, image_name_list, mask_name_list):
    '''Method to create a list of image-mask tuples including a tuple for every object'''

    # Creating empty list
    image_mask_name_list = []

    # Looping through every object and appending the image-mask tuple of every object to image_mask_name_list
    for i in range(number_of_objects):
        image_mask_name_list.append((image_name_list[i], mask_name_list[i]))

    # Returning the filled image_mask_name_list
    return image_mask_name_list


def images_masks_order(image_mask_name_list):
    '''Method to suffle the list with the image-mask tuples and appending the images and masks to separate lists'''

    # shuffle the list image_mask_list
    random.shuffle(image_mask_name_list)

    # Creating empty lists for the images and masks
    shuffled_image_list = []
    shuffled_mask_list = []

    # Appending the images and masks from the shuffled image_mask_list to shuffled_image_list and shuffled_mask_list
    for i in range(len(image_mask_name_list)):
        shuffled_image_list.append(image_mask_name_list[i][0])
        shuffled_mask_list.append(image_mask_name_list[i][1])

    # Returning the lists shuffled_image_list and shuffled_mask_list
    return shuffled_image_list, shuffled_mask_list