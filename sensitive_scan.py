from rapidfuzz import fuzz, process
import json
from power_sensitive_scan import powered_sensitive_scan

def sensitive_scan(jsonPath:str)->list:
    with open(jsonPath, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # 學號 研究生 指導教授 簽章
    privacy_words = ["學號", "研究生", "指導教授", "簽章","計畫參與人員","計畫参與人員","e-mail","主持人","指導老師","號：M", "系（學程）主任", "申請人", "發明人", "代理人", "審查人員", "地址", "專利附件","單位職稱","生日","TEL","Address","email","委員"]

    # blackout list
    blackout_list = []

    # 對json中的每一行進行處理
    for idx in range(len(data)):
        res = data[idx]
        for line in res:
            # print(line[1][0])
            # 對每一行進行模糊比對
            result = process.extractOne(line[1][0], privacy_words, scorer=fuzz.WRatio, score_cutoff=80)
            if result:
                # print("有相關")
                print(result)
                # 將有相關的文字的textbox加入blackout_list
                blackout_list.append(line[0])
            else:
                #print("沒有相關")
                pass

    # 如果為致謝頁面，進行特殊處理
    contain_specific_word = False
    for idx in range(len(data)):
        res = data[idx]
        for line in res:
            # a utf-8 string
            appreciate_title = ["致謝", "感謝", "謝謝", "致谢", "感激"]
            string = line[1][0]
            if any(appreciate in string for appreciate in appreciate_title):
                contain_specific_word = True
                break

    # 強化檢測
    if contain_specific_word or True:
        powered_blackout_list = powered_sensitive_scan(jsonPath)

    # 將強化檢測的結果加入blackout_list
    for item in powered_blackout_list:
        blackout_list.append(item)

    return blackout_list


if __name__ == '__main__':
    jsonPath = './tempFiles/udgra_02/ScanJson/images_0.json'
    blackout_list = sensitive_scan(jsonPath)
    print(blackout_list)
    exit(0)