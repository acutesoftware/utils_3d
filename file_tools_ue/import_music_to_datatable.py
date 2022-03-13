#!/usr/bin/python3
# coding: utf-8
# import_music_to_datatable.py
# searches an Unreal Project folder for sound cues and creates
# sanct format data tables ready to import (or append) to your
# datatable of master sounds.

import os 
import sys 

pth = r'E:\UE4_proj'

search_file = 'files_ue4_sanct.txt'  # you need to run "create_ue4_filelist.py" to refresh this
op_csv_to_append = 'sounds_append.csv'
srch_terms = ['Minimal_Orchestral', 'Cues']
package_prefix = 'Min_'  # prefix all sounds for this import for easier grouping

sound_cue_string_old = 'E:/UE4_proj/sanct_427_TEST/sanct_427_TEST/Content'
sound_cue_string_new = 'SoundCue\'/Game'

#excluded = []

def main():

    raw_results = find_strings(srch_terms)
    with open(op_csv_to_append, 'w') as fop:
        for raw_result in raw_results:
            #print(get_short_name(raw_result))
            fop.write(generate_csv_line(raw_result) + '\n')

    print('found ' + str(len(raw_results)) + ' results for ' + str(srch_terms))

def find_strings(srch_terms):
    raw = []

    num_terms = len(srch_terms)

    with open(search_file, 'r') as fip:
        for line in fip:
            found = 0
            for srch_term in srch_terms:
                if srch_term in line:
                    found += 1


            if found == num_terms:
                raw.append(line)
    return raw

def generate_csv_line(raw_result):
    cols = raw_result.replace('\\', r'/').split('","')
    short_fname = cols[1].replace('.uasset', '')
    short_name = package_prefix + short_fname.replace('_Cue', '')
    desc = short_name.replace('_', ' ').capitalize() + ' (' + str(cols[3] + ')')
    cue = cols[2].replace(sound_cue_string_old, sound_cue_string_new ) + '/' + short_fname + '.' + short_fname + '\''
    #csv_line = 'row_id,Name,Description,category,isLoop,Cue,fadeInRate,fadeOutRate'
    csv_line = short_name + ','
    csv_line += '"' + short_name + '",'
    csv_line += '"' + desc + '",'
    csv_line += '"music",'  # category
    csv_line += '"True",'  # loop this music
    csv_line += '"' + cue + '","0.000000","0.000000"'
    
 
    return csv_line


def get_short_name(raw_result):
    """
    parses a CSV line from search file to get a nice UE4 friendly name
    """
    cols = raw_result.split(',')
    res = cols[1][1:][:-1] + ' (' + cols[3][1:][:-1] + ') in folder ' + cols[2][1:][:-1]
    return res


if __name__ == '__main__':  
    main()            