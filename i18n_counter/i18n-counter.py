# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

introduce: i18n-counter_mac_arm64 is a tool to count the number of translated strings in a project.

Usage: i18n-counter_mac_arm64 locales_path source_language target_language

Example: `i18n-counter_mac_arm64 locales zh-CN en-US`

please make sure that the language has exists before using this tool.

"""

import sys
import json
import os


def do_trans_count(text, i=0):
    for k, v in text.items():
        if isinstance(v, dict):
            i = do_trans_count(v, i)
        else:
            if v != "":
                i += 1

    return i


def translate_score(source_folder, source_lang, target_lang):
    project_path = '{}/{}/'.format(source_folder, source_lang)

    try:
        os.chdir(project_path)

        source_counter = source_files = target_counter = target_files = 0

        for root, path, files in os.walk(project_path):
            for file in files:
                if file.endswith('.json'):
                    source_path = os.path.join(root, file)
                    target_path = source_path.replace(source_lang, target_lang)

                    if os.path.exists(source_path):
                        with open(source_path, 'r') as f:
                            source_data = json.load(f)
                        source_counter += do_trans_count(source_data)
                        source_files += 1

                    if os.path.exists(target_path):
                        with open(target_path, 'r') as f:
                            target_data = json.load(f)
                        target_counter += do_trans_count(target_data)
                        target_files += 1

        return source_counter, source_files, target_counter, target_files
    except Exception as e:
        print(e)
        return 0, 0, 0, 0


def show_tips():
    return {"tips": 'Usage: i18n-counter_mac_arm64 locales_path source_language target_language'}


def i18n_counter() -> dict:
    if len(sys.argv) > 1:
        if sys.argv[1] == '-h':
            return show_tips()
        elif len(sys.argv) == 4:
            locales_path = sys.argv[1]
            source_lang = sys.argv[2]
            target_lang = sys.argv[3]

            source_counter, source_files, target_counter, target_files = translate_score(locales_path,
                                                                                         source_lang,
                                                                                         target_lang)
            if source_files == 0 or source_counter == 0:
                return {"tips": 'No translation files found.'}
            else:
                print('project: ', locales_path)
                print(source_lang, 'files: ', source_files)
                print(source_lang, 'strings: ', source_counter)
                print('')
                print(target_lang, 'files: ', target_files)
                print(target_lang, 'strings: ', target_counter)
                print('')
                print(target_lang, '->', source_lang, 'file translation rate: ',
                      str('%.2f' % (target_files / source_files * 100)) + '%')
                print(target_lang, '->', source_lang, 'string translation rate: ',
                      str('%.2f' % (target_counter / source_counter * 100)) + '%')
                print('')

                return {
                    "source_files": source_files,
                    "source_counter": source_counter,
                    "target_files": target_files,
                    "target_counter": target_counter
                    }
        else:
            return show_tips()
    else:
        return show_tips()


if __name__ == "__main__":
    print(i18n_counter())
