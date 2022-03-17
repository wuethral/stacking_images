from methods import create_path_to_folder, image_mask_open, img_msk_name_list, images_masks_order, stacking


if __name__ == '__main__':

    # Number of objects to be stacked
    number_of_objects = 3

    # Creating lists of the paths to the image and mask folders, accessing images width and height
    list_images_dir, list_masks_dir, list_lengths, width, height = create_path_to_folder(number_of_objects)

    # Initializing variables counter to count number of loops below
    counter = 0

    # Number of stacked images
    number_of_images_stacks = 3

    for i in range(number_of_images_stacks):

        # Incrementing counter
        counter += 1

        # Getting list of images and masks including every object (dataset) once
        image_list, mask_list = image_mask_open(number_of_objects, list_lengths, list_images_dir, list_masks_dir)

        # Creating tuple of image and mask from image_mask_list and shuffling it, so that order is random for later
        # stacking
        image_mask_list = img_msk_name_list(number_of_objects, image_list, mask_list)

        # Creating separate image and mask list form image_mask_list
        shuffled_image_list, shuffled_mask_list = images_masks_order(image_mask_list)

        # Initializing the image stack with the first image and mask
        image_stack = shuffled_image_list[0]
        mask_stack = shuffled_mask_list[0]

        # Stacking all images and masks in list shuffled_image_list and shuffled_mask_list
        for i in range(number_of_objects-1):
            image_stack, mask_stack = stacking(image_stack, shuffled_image_list[i + 1], mask_stack,
                                               shuffled_mask_list[i + 1])

        # Saving the image and mask stacks
        image_direction = 'dataset_stack/images/image_' + str(counter) + '.png'
        mask_direction = 'dataset_stack/masks/image_' + str(counter) + '.png'
        image_stack.save(image_direction)
        mask_stack.save(mask_direction)
