# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""

import os
import anybadge
from i18n_counter import translate_score
from config import Config


def generate_badge(project, svg_path, score):
    svg_path = svg_path + project + '.svg'
    thresholds = {30: 'red',
                  50: 'orange',
                  70: 'yellow',
                  90: 'green'
                  }
    percentage = score

    badge = anybadge.Badge('Translate Rate', percentage, thresholds=thresholds, value_suffix='%')
    badge.write_badge(svg_path, overwrite=True)


if __name__ == '__main__':
    svg_path = Config.svg_path
    modules_path = Config.modules_path

    projects = os.listdir(modules_path)

    for project in projects:
        print(project)
        source_lang = 'zh-CN'
        target_lang = 'en-US'
        in_project = modules_path + project + '/src/locales'
        source_counter, source_files, target_counter, target_files = translate_score(in_project, source_lang,
                                                                                     target_lang)

        generate_badge(project=project, svg_path=svg_path, score=round(target_counter / source_counter * 100, 2))
