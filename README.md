# 4i_analysis

A set of notebooks to align 4i data coming from a Nikon widefield.

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

| myRound | Hoechst | AF488 | AF647 |
| --- | --- | --- | --- |
| 00 | DNA | pRb | RB |
| 01 | DNA | p27 | p53|

   - where 'Hoechst', 'AF488' and 'AF647' are the names of the optical configurations (OC)
   - it is ok to leave the spots empty if a given OC was not used in some rounds


### Analysis flow:

##### 00_preprocess_data.ipynb
   * creates data frames with the info for a given well
   * saves images prepared for the alignment
 




