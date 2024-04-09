def create_sudoku():
    from keras.preprocessing import image
    import tensorflow as tf
    tf.get_logger().setLevel('ERROR')
    from keras.models import load_model
    import cv2
    import numpy as np
    
    nums = []
    cnn = load_model('number_identifier')
    # path = "number_images/" + str(77) + ".jpg"
    # test_image = image.load_img(path, target_size = (28, 28))
    # test_image = image.img_to_array(test_image)
    # test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
    # test_image = np.expand_dims(test_image, axis = 0)
    # result = list(cnn.predict(test_image, verbose= 0)[0])
    # print(result.index(max(result)))
    for i in range(81):
        path = "number_images/" + str(i) + ".jpg"
        test_image = image.load_img(path, target_size = (28, 28))
        test_image = image.img_to_array(test_image)
        test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
        test_image = np.expand_dims(test_image, axis = 0)
        result = list(cnn.predict(test_image, verbose= 0)[0])
        num = str(result.index(max(result)))
        if num == "0":
            nums.append("")
        else:
            nums.append(num)
    nums = np.reshape(nums, (9,9))
    return nums