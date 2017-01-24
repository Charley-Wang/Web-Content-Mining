import re

def get_data_file_index():
    fileName = "C:/Users/li/Desktop/jobs_20151111_last_used.txt"
    f = open(fileName, "r")
    lines = f.readlines()

    search =  r"\bdata\b|\bbi\b|\bmachine learning\b|\bbusiness intelligence\b"
    search += r"|\bbusiness .*?analyst\b|\bsap\b.*?analyst\b|\bmarketing .*?analyst\b"
    search += r"|\binformatics .*?analyst\b|\bstatistical\b"
    search += r"|\bsecurity .*?analyst\b|\bproduct .*?analyst\b|\bservices .*?analyst\b|\brisk .*?analyst\b|\bsas\b"
    p1 = re.compile(search)

    num = 0
    nums = []
    for line in lines:
        line = line.lower()
        if len(p1.findall(line)) > 0:
            num += 1
            txts = line.split(",")
            nums.append(int(txts[0]))

    print("number of data: ", num)
    return nums

# state analysis
def state_stat():
    dict_state = {}

    fileName = "C:/Users/li/Desktop/jobs_20151111_last_used.txt"
    f = open(fileName, "r")
    lines = f.readlines()

    index = []
    state = []
    for ii in range(len(lines)):
        txts = lines[ii].split(",")
        index1 = int(txts[0])
        state1 = txts[2].strip()
        index.append(index1)
        state.append(state1)

    for ii in range(1, len(lines)-1):
        if len(state[ii]) != 2 and state[ii - 1] == state[ii + 1]:
            state[ii] = state[ii-1]

    for ii in range(len(lines)):
        state1 = state[ii]
        if state1 in dict_state.keys():
            dict_state[state1] += 1
        else:
            dict_state[state1] = 1

    dict_state2 = {}
    data_index = get_data_file_index()
    for ii in range(len(lines)):
        if index[ii] not in data_index:
            continue
        state1 = state[ii]
        if state1 in dict_state2.keys():
            dict_state2[state1] += 1
        else:
            dict_state2[state1] = 1

    print(dict_state)
    print(dict_state2)

    for key in dict_state2:
        print(key, dict_state2[key])

    dict_state3 = {}
    for key in dict_state.keys():
        if key not in dict_state2.keys():
            dict_state3[key] = 0
        else:
            dict_state3[key] = dict_state2[key] / dict_state[key]

print(get_data_file_index())
state_stat()


