import json
import pathlib
from Assistant_API import assistant_api
from rapidfuzz import fuzz, process

def powered_sensitive_scan(ocr_json_path:str)->list:
    filename = pathlib.Path(ocr_json_path).stem
    # ocrtext 存放的地方是 ./tempFiles/stem/ScanText
    ocrtext_path = pathlib.Path(ocr_json_path).parent.parent
    ocrtext_path = ocrtext_path / 'ScanText'
    output_filepath = ocrtext_path / (filename + '.txt')

    # 串接json檔案的文字到ocrtext
    with open(ocr_json_path, 'r', encoding='utf-8') as json_file:
        ocrjson = json.load(json_file)
    
    # 將ocrjson中的文字串接到ocrtext
    ocrtext = ""
    for item in ocrjson:
        for line in item:
            ocrtext += line[1][0] + "\n"
    
    # print (ocrtext)

    # 將ocrtext寫入檔案
    with open(output_filepath, 'w', encoding='utf-8') as output_file:
        output_file.write(ocrtext)

    # 將檔案上傳到assistant api
    result = assistant_api(output_filepath)
    result = json.loads(result)
    # print("result: ", result)
    # #print result type
    # print(type(result))
    list_config = {"names": True, "address": True, "phone": True, "email": True}

    # 將assistant api的結果轉成list
    sensitive_list = []
    for item in result:
        if item in list_config:
            if list_config[item] is True:
                for i in result[item]:
                    sensitive_list.append(i)
    print("sensitive list:")
    print(sensitive_list)

    blackout_list = []
    for index in range(len(ocrjson)):
        ocr_result = ocrjson[index]
        for line in ocr_result:
            string = line[1][0]
            for sensitive_word in sensitive_list:
                    has_alphabet = any('a' <= char <= 'z' or 'A' <= char <= 'Z' for char in string)
                    has_chinese = any('\u4e00' <= char <= '\u9fff' for char in string)

                    if has_chinese:
                        # count alphabet in string
                        alphabet_count = 0
                        for char in string:
                            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                                alphabet_count += 1
                        if alphabet_count >= 3:
                            has_alphabet = True

                    if sensitive_word in string:
                        startIndex = string.find(sensitive_word)
                        endIndex = startIndex + len(sensitive_word) 
                        # 計算左上左下右上右下的座標
                        leftTop = line[0][0]
                        leftBottom = line[0][3]
                        rightTop = (line[0][1][0], line[0][0][1])
                        rightBottom = (line[0][2][0], line[0][3][1])
                        # 將座標的橫軸切成len(sensitive)等分，並計算出起始點和結束點的座標
                        # 計算左上和右上的座標
                        leftTopStart = (leftTop[0] + (rightTop[0] - leftTop[0]) * startIndex / len(string), leftTop[1])
                        leftTopEnd = (leftTop[0] + (rightTop[0] - leftTop[0]) * endIndex / len(string), leftTop[1])
                        # 計算左下和右下的座標
                        leftBottomStart = (leftBottom[0] + (rightBottom[0] - leftBottom[0]) * startIndex / len(string), leftBottom[1])
                        leftBottomEnd = (leftBottom[0] + (rightBottom[0] - leftBottom[0]) * endIndex / len(string), leftBottom[1])

                        word_pos = [leftTopStart, leftTopEnd, leftBottomEnd, leftBottomStart]
                        blackout_list.append(word_pos)
                    
                    # 如果有英文，對英文做模糊比對
                    if has_alphabet:
                        result = process.extractOne(string, sensitive_list, scorer=fuzz.WRatio, score_cutoff=75)
                        if result:
                            # 將有相關的文字的textbox加入blackout_list
                            blackout_list.append(line[0])
                        else:
                            pass
    
    return blackout_list



if __name__ == '__main__':
    # jsonpath = './tempFiles/udgra_01/ScanJson/images_5.json'
    jsonpath = './tempFiles/Associative_memory_based_fuzzy_inference/ScanJson/images_0.json'
    powered_sensitive_scan(jsonpath)
    exit(0)