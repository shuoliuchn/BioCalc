#!/usr/bin/python
# coding=utf-8

#__author__ = "Shuo Liu"
#__date__ = 2018-02-16 12:32:07

from conf import settings
from core import calculate

sequence_info = {
    'sequence_type': None, #DNA, RNA or protein
    'init_modi': None, #initial modification
    'term_modi': None, #terminal modification
    'modi_type': None, #modification type
}


def format(sequence):
    '''
    To remove the spaces.
    :param sequence:
    :return:
    '''
    formation = sequence.strip().upper()
    return formation



def run():
    '''
    This is the first function which will be run once the biocalc process is run.
    :return:
    '''
    # print('i am in main.run()')
    '''The code listed below is used for future optimization.'''
    # print(settings.sequence_type)
    # sequence_info['sequence_type'] = settings.sequence_type[input('请输入需要查询的分子对应的序号：')]
    while True:
        sequence = input('Please input DNA sequence(type q to exit): ')
        so_uv_ab = input('Please input the UV absorbance of the DNA solution(type q to exit or type p to pass):')
        if sequence == 'q' or so_uv_ab == 'q':
            break
        sequence = format(sequence)
        sequence_mf = calculate.dna_mf(sequence)
        uv_ab = calculate.uv_calc(sequence)
        print(sequence_mf)
        print(calculate.mw_calc(sequence_mf))
        print("1 ml of a sol'n with an Absorbance of 1 at 260 nm is %f microMolar" % (1 / uv_ab))
        if so_uv_ab != 'p':
            volume = float(so_uv_ab) / uv_ab
            print('You need to add %f ul of water to make the solution be 1 mM' % volume)