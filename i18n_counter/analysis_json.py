# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

function: count the number of translated strings in i18n files

- count need translate files
- count need translate strings


"""

import json
import os


def test_translate(text, i=0):
    for k, v in text.items():
        if isinstance(v, dict):
            i = test_translate(v, i)
        else:
            if v != "":
                i += 1

    return i


def project_translate_score(project_name, source_lang, target_lang):
    project_path = '/Users/samzonglu/Git/daocloud/frontend/{}/src/locales/{}/'.format(project_name, source_lang)

    os.chdir(project_path)

    source_count = source_files = target_count = target_files = 0

    for root, path, files in os.walk(project_path):
        for file in files:
            if file.endswith('.json'):
                source_path = os.path.join(root, file)
                target_path = source_path.replace(source_lang, target_lang)

                if os.path.exists(source_path):
                    with open(source_path, 'r') as f:
                        source_data = json.load(f)
                    source_count += test_translate(source_data)
                    source_files += 1

                if os.path.exists(target_path):
                    with open(target_path, 'r') as f:
                        target_data = json.load(f)
                    target_count += test_translate(target_data)
                    target_files += 1

    return source_count, source_files, target_count, target_files


if __name__ == '__main__':
    projects = [
        'amamba-ui',
        'insight-ui',
        'kairship-ui',
        'kpanda-ui',
        'mspider-ui',
        'skoala-ui'
        ]

    for project in projects:
        source_lang = 'zh-CN'
        target_lang = 'en-US'
        zh_counter, zh_files, en_counter, en_files = project_translate_score(project, source_lang,
                                                                             target_lang)
        print('------------------------------')
        print('项目名称: ', project)
        print(source_lang, '文件数: ', zh_files)
        print(source_lang, '字符串数: ', zh_counter)
        print('')
        print(target_lang, '文件数: ', en_files)
        print(target_lang, '字符串数: ', en_counter)
        print('')
        print(target_lang, '->', source_lang, '文件翻译率: ', str('%.2f' % (en_files / zh_files * 100)) + '%')
        print(target_lang, '->', source_lang, '字符串翻译率: ', str('%.2f' % (en_counter / zh_counter * 100)) + '%')
        print('')
