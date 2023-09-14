import json
import sys
import os
result_path = sys.argv[1]

_result = {'model_name':result_path, 'arc_challenge':-99, 'hellaswag':-99, 'mmlu':-99, 'truthfulqa_mc':-99}

try:
    with open(os.path.join(result_path, 'arc_result.json'), 'r', encoding='utf-8-sig') as file:
        _result['arc_challenge'] = round(json.load(file)['results']['arc_challenge']['acc_norm']*100,2)
except:
    _result['arc_challenge']=None

try:
    with open(os.path.join(result_path, 'hellaswag_result.json'), 'r', encoding='utf-8-sig') as file:
        _result['hellaswag'] = round(json.load(file)['results']['hellaswag']['acc_norm']*100,2)
except:
    _result['hellaswag']=None

try:
    with open(os.path.join(result_path, 'mmlu_result.json'), 'r', encoding='utf-8-sig') as file:
        res_mmlu = json.load(file)
    acc_norm_values = [category_data['acc_norm'] for category_data in res_mmlu['results'].values()]
    _result['mmlu'] = round(sum(acc_norm_values) / len(acc_norm_values)*100,2)
except:
    _result['mmlu'] =None

try:
    with open(os.path.join(result_path, 'truthfulQA_result.json'), 'r', encoding='utf-8-sig') as file:
        _result['truthfulqa_mc'] = round(json.load(file)['results']['truthfulqa_mc']['mc2']*100,2)
except:
    _result['truthfulqa_mc'] =None

print(_result)