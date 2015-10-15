#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# multi_diff.py
# 2015-10-15
# 

import os
import traceback
import codecs
import difflib


# 是否是C++源代码
def is_source(filename):
    source_exts = ('.c', '.cpp', '.cc', '.cxx', '.h', '.hxx', '.hpp')
    for ext in source_exts:
        if filename.lower().endswith(ext):
            return True
    return False


def main():
    cd = os.path.abspath('.')
    print(cd)

    threshold = 0.8

    file_list = []
    for root, dir, files in os.walk("."):
        for file in files:
            file_path = os.path.join(root, file)
            if is_source(file_path):
                file_list.append(file_path)

    bad_list = []
    for i in range(0, len(file_list)):
        for j in range(i + 1, len(file_list)):
            try:
                fp = open(file_list[i], errors='ignore')
                lines1 = '\n'.join(fp.readlines())
                fp.close()
                fp = open(file_list[j], errors='ignore')
                lines2 = '\n'.join(fp.readlines())
                fp.close()

                simi = difflib.SequenceMatcher(None, lines1, lines2).ratio()
                if simi >= threshold:
                    bad_list.append((simi, file_list[i], file_list[j]))
            except Exception as e:
                traceback.print_exc()
                print(e)

    bad_list.sort(key=lambda x:x[0], reverse=True)
    for pair in bad_list:
        print('%7.4f%% %s' % (pair[0] * 100, pair[1]))
        print(' ' * 9 + pair[2])
        print()
    print('nice!')


if __name__ == '__main__':
    main()
    os.system('pause')

