def min_max_norm (a, min_new, max_new):
        #sort the list in ascending order 
        sorted_list = sorted(a)
        #find the  min value
        min_val = min(sorted_list)
        #find the  max value
        max_val = max(sorted_list)
        print (" the min for the data set is: ",min_val)
        print (" the max for the data set is: ",max_val)
        print (f"The new Range for this data is {min_new}, {max_new}")
        
        #intilize the lists with no data but the length of sorted list 
        normalized_value_list = [None] * len(sorted_list)
        new_range_normalized_value_list  = [None] * len(sorted_list)
        #interate through each index of sorted list
        for i in range(len(sorted_list)):
                #calculate the normalized min_ max value for each value at index i, round to 3 decimal places
                #Normalized Value = (Value - Min) / (Max - Min) 
                normalized_value_list[i] = round((sorted_list[i] - min_val) / (max_val - min_val),3)
                #calculate the new range of the normalized min max value for each value at index i, rounding to 3 decimal places
                #Normalized = min_new + (max_new - min_new) * ((value - Min) / (Max - Min))
                new_range_normalized_value_list[i] = round(min_new +( max_new - min_new) *( (sorted_list[i] - min_val)) / (max_val - min_val),3)
                # print off the values showing the original, normal min max set and the new range 
                print(f"Original: {sorted_list[i]}\t Normalized: {normalized_value_list[i]:.3f}\t Normalized New Range: {new_range_normalized_value_list[i]:.3f}")
                
        
#dataset of single demension array  age
age = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
#call function and pass values and dataset to function 
min_max_norm(age, 1.0, 2.0)





