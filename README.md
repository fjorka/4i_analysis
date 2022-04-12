# 4i_analysis

A set of notebooks to align 4i data coming from a Nikon widefield.

### Analysis flow:

General idea:
- in each round an image that is easy for segmentation is selected
- these images are segmented using Cellpose
- masks are aligned using StackReg and transformations are saved
- transformations are applied to all channels 
- aligned images are stored as single channels tiffs

##### 00_preprocess_data.ipynb
   * creates data frames with the info for a given well (ex. df)
   * saves images prepared for the segmentation (ex. im_to_segment)
   * output directories will be created automatically (if their parent directories exist)

##### 01_cellpose_segmentation_local.ipynb (01_cellpose_segmentation_colab.ipynb)
   * uses [Cellpose](https://github.com/MouseLand/cellpose) segmentation
   * segments and saves masks (ex. im_to_segment)
   * this segmentation is performed on the local workstation
   * output directory will be created automatically (if its parent directory exist)

##### 02_find_transforms_on_segmentation_df.ipynb
   * calculate transformations to align segmented images
   * allows calculation of transformations on downscaled images
   * output directory will be created automatically (if its parent directory exist)

##### 03_find_transformation_manually.ipynb
   * uses [Affinder](https://github.com/jni/affinder) to find a transformation a the problematic well/round
   * replaces transformation in the pkl file

##### 04_align_from_transform_single.ipynb (04_align_from_transform_list.ipynb)
   * applies transformations to all original images
   * works for a single well 
   * allows visualization of alignment
   * output directory will be created automatically (if its parent directory exist)

##### 05_create_mask.ipynb 
   * enables creation of punchmask (a mask of regions to be excluded from the analysis because of the artefacts)
   * ex. output subdirectory - masks
   * output directory will be created automatically (if its parent directory exist)

##### 06_calculate_cell_properties.ipynb
   * calculates properties of individual segmented nuclei through all the intensity channels
   * ex. output subdirectory - cell_data
   * output directory will be created automatically (if its parent directory exist)

Alternatively:
##### 01_cellpose_segmentation_colab.ipynb
   * segments and saves masks (ex. im_to_segment)
   * this notebook is adjusted to be run on Google Colab (while data are temporarily stored on Google Drive)
   * the advantage is access to GPU which will usually speed up segmentation 5-10 times
   * output directory will be created automatically (if its parent directory exist)

##### 04_align_from_transform_list.ipynb
   * enables processing of a list of wells
   * doesn't support visualization of the alignment
   * output directory will be created automatically (if its parent directory exist)


### Starting data structure:

- a set of correctly stitched nd2 files
- these stitched images may be of slightly different sizes (as stitching in Elements software corrects for the imperfections of a microscope stage position). However, if the sizes are totally different, please check your dataset.
- images are divided into subdirectories according to rounds (names of subdirectories contain names of the rounds in a form: 'Round_ROUNDNAME_WHATEVERADDITIONALINFO' )
- please make sure that the names of the rounds are unique (ex. no subdirectories as 'Round_00_bad' and 'Round_00_good')
- keep names of the rounds numeric
- assuming standard names of stitched nd2 files (starting with 'WellA1_Channel...', where 'A1' is the well name)
- you can keep individual files of tiles in the same subdirectories as they will be ignored (tiled images usually have names starting with 'WellA1_Point...')

### Info file:

* a csv file that translates names of optical configurations (OC) used in specific rounds into desired names for the channels (ex. names of the antibodies)
* for example:

| myRound | Hoechst | AF488 | AF555 | AF647 |
| --- | --- | --- | --- | --- |
| 00 | DNA | pRb |  | RB |
| 01 | DNA | p27 | p53|  |

   - where 'Hoechst', 'AF488' and 'AF647' are the names of the optical configurations (OC)
   - it is ok to leave the spots empty if a given OC was not used in some rounds

### Example input data structure:

- data
   * Round_00_DNA_pBB_RB
      - WellA1_Channel___.nd2
      - WellA2_Channel___.nd2
   * Round_01_DNA_p27_p53
      - WellA1_Channel___.nd2
      - WellA2_Channel___.nd2
- info_exp.csv

### Example output data structure:

- data
- df
   * df_A1.pkl
   * df_A2.pkl
   * tmat_A1.pkl
   * tmat_A2.pkl
- im_to_segment
   * A1
      - im2segment_A1_round_00.tif
      - im2segment_A1_round_01.tif
   * A2
      - im2segment_A2_round_00.tif
      - im2segment_A2_round_01.tif
- im_segmented
   * A1
      - labels_A1_round_00.tif
      - labels_A1_round_01.tif
   * A2
      - labels_A2_round_00.tif
      - labels_A2_round_01.tif
- aligned_tiffs
   * A1
      - Round_00_wellA1_DNA.tif
      - Round_00_wellA1_pRB.tif
      - Round_00_wellA1_RB.tif
      - Round_01_wellA1_DNA.tif
      - Round_01_wellA1_p27.tif
      - Round_01_wellA1_p53.tif
   * A2
      - Round_00_wellA2_DNA.tif
      - Round_00_wellA2_pRB.tif
      - Round_00_wellA2_RB.tif
      - Round_01_wellA2_DNA.tif
      - Round_01_wellA2_p27.tif
      - Round_01_wellA2_p53.tif
- masks
   * mask_A1.pkl
   * mask_A2.pkl
- cell_data
   * cell_data_A1.pkl
   * cell_data_A2.pkl
- info_exp.csv
