
def get_str_length(data:str,length:int=70):
    if len(data)>length:
        re=data[0:length]
        for e in data[length:len(data)]:
            if len(e.strip())==0:
                break
            else:
                re+=e
        return re
    return data