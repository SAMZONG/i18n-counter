# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""

import sys
from analysis_json import translate_score


def show_tips():
    return {"tips": 'Usage: python3 foo.py locales_path source_language target_language'}


def foo() -> dict:
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
            print('------------------------------')
            print('项目名称: ', locales_path)
            print(source_lang, '文件数: ', source_files)
            print(source_lang, '字符串数: ', source_counter)
            print('')
            print(target_lang, '文件数: ', target_files)
            print(target_lang, '字符串数: ', target_counter)
            print('')
            print(target_lang, '->', source_lang, '文件翻译率: ',
                  str('%.2f' % (target_files / source_files * 100)) + '%')
            print(target_lang, '->', source_lang, '字符串翻译率: ',
                  str('%.2f' % (target_counter / source_counter * 100)) + '%')
            print('')

            return {
                "source_counter": source_counter,
                "source_files": source_files,
                "target_counter": target_counter,
                "target_files": target_files
                }
        else:
            return show_tips()
    else:
        return show_tips()


if __name__ == "__main__":
    result = foo()
    print(type(result), result)
