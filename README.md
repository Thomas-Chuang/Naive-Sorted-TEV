# Naive-Sorted-TEV
The main object is to obtain the **overlapping and non-overlapping** data of Sorted and Naive library of wtTEV and PE10-TEV

## 2021-05-23
### Functions that are used:
- converting txt file to list
- converting csv file to dictionary
- forming dataframe with dictionaries comparing to the list

### Steps of finding overlap and non-overlap data (wtTEV as the example)
1. Covert the txt file of Naive and Sorted library (*'wtTEV-naive_full.txt' and 'wtTEV-sorted_full.txt'*) into a list of sequence
2. Convert the two *lists* into *sets*, and find out *(Sorted&Naive)*, *Naive-(Sorted&Naive)*, *Sorted-(Sorted&Naive)*
3. Convert the csv files of Naive and Sorted library (*'wtTEV-naive_full.csv' and 'wtTEV-sorted_full.csv'*) into two dictionaries
4. Use the set:*Sorted&Naive* to tranverse the dictionary of Sorted and Naive, and update the countings into 2 dictionaries with: {keys:Sequence, values: countings)
5. Similarly, use *Naive-(Sorted&Naive)* and *Sorted-(Sorted&Naive)* sets to form two non-overlapping dictionaries
6. Convert the dictionaries into a csv file
7. Copy and Paste Transposly in a excel file and reaarange the data.

The overlap and non-overlap data are storded in *wt_Scatter_Total.xlsx*.

### Improvemnent in PE10-TEV data


As I process the data at step 5, I found that all the sequence will locate in one row and all countings in the other one, which is so confusing so that I have to re-arrange the data mannuallly in an excel file, so I decide to update the method for *PE10-Data* with dataframe from pandas.

The previous 3 steps are basically the same, but this time on step 4, instead of creating new dictionaries, I store the *Sequences* in *list1* and *coutings* in *list2* respectively using for loop appening. Then use these two lists to create a new dataframe. 
1. overlapTotal
2. NonOverlap_Naive
3. NonOverlap_Sorted

Then I used pd.ExcelWriter to write in the above three dataframes in separate sheets in the excel file: *PE10ScatterData.xlsx*.
