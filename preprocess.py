import re
import pandas as pd
import pprint as pp

min_length=200
include_line_breaks=False
image_name='m.png'
text="""
  Grid-connected solar-PV systems

In order to supply electricity into a mains electricity system, the de output from
the module smst te converted to ac at the correct voltage and frequency. “n
electronic inverter is used to do this. Generally a number of PV modules ar
connected in series to provide a higher de voltage to the inverter input, and
sometimes several of these ‘series strings’ are connected in parallel, so that a single
inverter can be used for 50 or more modules. Modern inverters are very efficient
(typically 97%), and use electronic control systems to ensure that the PV array keeps
working at its optimum voltage. They also incorporate safety systems as required in
the country of use.

Many grid connected PV systems are installed on frames which are mounted
on the roof or walls of a building. Used in this way the PV does not take up land that
could be used for other purposes. Ideally the PV faces towards the equator (i.e. South
in the northern hemisphere) but the exact direction is not critical. However, it is
important to make sure that there is minimal shading of the PV. The inverter is
housed inside the building and connected to the mains electrical supply, usually with
a meter to measure the kWh generated. If the PV electricity production exceeds
building demand then the excess can be exported to the grid, and vice versa.

a) Net Metering

Grid Tied Net Metered systems involve connecting your system to the power
grid but you use the power, and it offsets your electric bill. If you don’t produce as
much electricity as you use then the grid just supplies the difference and you get
billed for that difference, if you produce more than you use, the excess just goes 10
the grid. Whether you get paid for that difference that you supply to the grid depentis

"""
df = pd.DataFrame(columns=["title", "paragraphs"])
df.loc[1] = [image_name.replace(".png",''), None]
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
df.loc[1, "paragraphs"] = list_par
pp.pprint(list_par[2])