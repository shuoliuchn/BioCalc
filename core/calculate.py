#!/usr/bin/python
# coding=utf-8

#__author__ = "Shuo Liu"
#__date__ = 2018-02-18 23:04
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)
sys.path.append(base_dir)

from conf import settings

def uv_calc(sequence):
    '''
    To calculate the UV absorbance of a specific DNA sequence. RNA and Protein absorbance shall be added in the future.
    :param sequence:
    :return:
    '''
    uv_ab = 0
    for unit in sequence:
        uv_ab += settings.deoxynucleotide_uv[unit]
    return uv_ab


def mw_calc(mf):
    '''
    To calculate the molecular weight of a specific molecule which molecular format is already known.
    :param mf:
    :return: mw
    '''
    mw = 0
    for a in mf:
        mw = settings.atom_weight[a] * mf[a] + mw
    return mw

def dna_mf(sequence):
    '''
    To calculate the DNA molecular format with the DNA sequence.
    :param sequence:
    :return: atoms
    '''
    atoms = {'C': 0, 'H': 0, 'O': 0, 'N': 0, 'P': 0}
    for nucleotide in sequence:
        for each in atoms:
            atoms[each] += settings.deoxynucleotide_mf[nucleotide][each]
        atoms['H'] -= 2
        atoms['O'] -= 1
    atoms['H'] += 1
    atoms['P'] -= 1
    atoms['O'] -= 2
    return atoms

if __name__ == '__main__':
    mf = {'C': 80, 'H': 93, 'O': 37, 'N': 22, 'P': 5}
    print(mw_calc(mf))
