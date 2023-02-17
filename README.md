# Belle AcneAI predictions on ACNE04 public dataset

[ACNE04 dataset](https://github.com/xpwu95/LDL)

`AcneAI_prediction_ACNE04_v1.json` is a json format file containing the predictions of the model from our paper "Belle AcneAI: A new acne severity assessment method using digital images and deep learning"(link soon) on the open source dataset ACNE04 from the paper  [Joint Acne Image Grading and Counting via Label Distribution Learning, Wu et al. ICCV 2019](https://openaccess.thecvf.com/content_ICCV_2019/html/Wu_Joint_Acne_Image_Grading_and_Counting_via_Label_Distribution_Learning_ICCV_2019_paper.html) released in 2019. The format of the json file is inspired from the coco annotations format.

- **"images"** is a list of dictionnaries, each element corresponding to one image. Each dictionnary is composed of several fields : image `id` , name of the image `file_name`, image size information (`height` and `width`), and  `image_severity_score` calculated based on our AI algorithm. This last field relies on the severity of all the acne lesions present on the image. 
- **"annotations"** is a list of dictionnaries, each element corresponding to one acne lesion. Basically, for each image, there are several annotations related. The different fields of each dictionnary are : annotation `id`, `image_id` which is the id in the of the source image in the **"images"** corresponding dictionnary, center `coordinates` and `radius` of the acne lesion on the image, and `severity` of the lesion.
- **"info"** is a dictionnary containing information about this file : the predictions `version`, a brief `description`, the release `year`, and the names of the `contributors`.

The file `draw_acne_from_json.py` is one example of how to plot te cicles of acne on the images.
