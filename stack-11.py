import re

item_dict = {
    "okay": ("Mythical", "50000"),
    "hello": ("Mythical", "17500"),
    "hi": ("Legendary", "14500"),
    "good": ("Legendary", "11600"),
    "very bad": ("Common", "1"),
    }

msg = input("Enter ")
# type(msg)
# print(msg)
new_list = []
idx_list = []

for x in item_dict:
    if x in msg:
        index_matcher = re.search(x, msg).span(0)[0]
        obj_cnt = len(new_list)

        if obj_cnt < 1: 
            idx_list.append(index_matcher)
            new_list.append(x)
        else:
            if idx_list[-1] < index_matcher:
                idx_list.append(index_matcher)
                new_list.append(x)
            elif idx_list[0] > index_matcher:
                idx_list.insert(0, index_matcher)
                new_list.insert(0, x)
            else:
                first_index = 0
                last_index = obj_cnt - 1
                while first_index <= last_index:
                    mid_index = (first_index + last_index)// 2
                    if idx_list[mid_index] > index_matcher:
                        last_index = mid_index - 1
                    elif idx_list[mid_index] < index_matcher:
                        first_index = mid_index + 1
                    else:
                        idx_list.insert(mid_index, index_matcher)
                        new_list.insert(mid_index, x)
                
                idx_list.insert(mid_index, index_matcher)
                new_list.insert(mid_index, x)

        
print(new_list)