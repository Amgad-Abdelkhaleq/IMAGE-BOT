import re
import os
from text_extraction import *
import pprint as pp


def split_page(text,min_length=200):
    include_line_breaks=False
    paragraphs = re.split("\n\n(?=\u2028|[A-Z-0-9])", text)
    list_par = []
    temp_para = ""  # variable that stores paragraphs with length<min_length
                # (considered as a line)
    for p in paragraphs:
                    if not p.isspace():  # checking if paragraph is not only spaces
                        if include_line_breaks:  # if True, check length of paragraph
                            if len(p) >= min_length:
                                if temp_para:
                                    # if True, append temp_para which holds concatenated
                                    # lines to form a paragraph before current paragraph p
                                    list_par.append(temp_para.strip())
                                    temp_para = (
                                        ""
                                    )  # reset temp_para for new lines to be concatenated
                                    list_par.append(
                                        p.replace("\n", "")
                                    )  # append current paragraph with length>min_length
                                else:
                                    list_par.append(p.replace("\n", ""))
                            else:
                                # paragraph p (line) is concatenated to temp_para
                                line = p.replace("\n", " ").strip()
                                temp_para = temp_para + f" {line}"
                        else:
                            # appending paragraph p as is to list_par
                            list_par.append(p.replace("\n", ""))
                    else:
                        if temp_para:
                            list_par.append(temp_para.strip())
    return list_par




paragraphs=[]
page_threshold=200
folder=os.path.join(os.getcwd(),"static/images/text-based")
for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder,filename))
    page = extract_text(img)
    if (len(page) > page_threshold) :
       # dic={"image":filename , "page":page}
        paragraphs= split_page(page)
        for p in paragraphs:    
                data_dict= {"image":filename ,"body":p}
                print(data_dict,"\n")
                fname =  os.path.join(os.getcwd(),"static\KB\output.json")
                if os.path.isfile(fname):
                    # File exists
                    print("file exists")
                    with open(fname, 'a+') as outfile:
                        outfile.seek(-1, os.SEEK_END)
                        outfile.truncate()
                        outfile.write(',')
                        json.dump(data_dict, outfile)
                        outfile.write(']')
                        print("kb updated")


    

# pp.pprint(list_par)