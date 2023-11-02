class PATHS:
    BASE_PATH = "/kaggle/input/rsna-2023-abdominal-trauma-detection"

    OUTPUT_BASE = f'/kaggle/working/output/'

    CONTRAIL_MODEL_BASE = f'{BASE_PATH}/src_contrails/'
    COAT_PRETRAINED = f'{BASE_PATH}/coat_pretrained/'

    SEGMENTOR_SAVE_FOLDER = '/kaggle/input/preprocess-data-seg/Data/KAGGLE_SUBMISSION/segmentation_data_v1'

    TOTAL_SEGMENTOR_FOLDER = f'{BASE_PATH}/TotalSegmentor/Totalsegmentator_dataset/'
    TOTAL_SEGMENTOR_SAVE_FOLDER = '/kaggle/input/preprocess-data-seg/Data/KAGGLE_SUBMISSION/total_data_v1'

    SEGMENTATION_MODEL_SAVE = '/kaggle/input/preprocess-data-seg/Data/KAGGLE_SUBMISSION/SEG_MODELS'

    INFO_DATA_SAVE = '/kaggle/working/output/KAGGLE_SUBMISSION/info_data1_processed_v1.csv'

    THEO_DATA_PATH = f'{BASE_PATH}/theo_images/'
    THEO_SAVE_PATH = f'{BASE_PATH}/KAGGLE_SUBMISSION/theo_data/'

    OURDATA_VOL_SAVE_PATH = f'{BASE_PATH}/KAGGLE_SUBMISSION/our_data/'

    MODEL_SAVE = f'{OUTPUT_BASE}/models/'
    


