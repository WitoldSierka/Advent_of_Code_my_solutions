import pytest
import main

def test_parse_input():
    #expected output from example
    #00...111...2...333.44.5555.6666.777.888899
    temp = main.parse_input('example.txt')
    result = ''.join(temp)
    assert result == '00...111...2...333.44.5555.6666.777.888899'

def test_parse_input2():
    result = main.parse_input2('example.txt')
    expected = [ '0', '0', '.', '.', '.', '1', '1', '1', '.', '.', '.', '2', '.', '.', '.', '3', '3', '3', '.', '4', '4', '.', '5', '5', '5', '5', '.', '6', '6', '6', '6', '.', '7', '7', '7', '.', '8', '8', '8', '8', '9', '9' ]
    assert result == expected

def test_parse_input_2digits():
    #233313312141413140211
    result = main.parse_input('example2.txt')
    assert result == [
        '0', '0', '.', '.', '.', '1', '1', '1', '.', '.', '.', '2', '.', '.', '.', '3', '3', '3', '.', '4', '4', '.',
        '5', '5', '5', '5', '.', '6', '6', '6', '6', '.', '7', '7', '7', '.', '8', '8', '8', '8', '9', '9', '.', '10'
    ]

def test_file_compacter():
    #expected final form
    #0099811188827773336446555566..............
    test_string = '00...111...2...333.44.5555.6666.777.888899'
    temp = main.file_compacter(list(test_string))
    result = ''.join(temp)
    assert result == '0099811188827773336446555566'

def test_file_compacter_2digits():
    #test_string = '00...111...2...333.44.5555.6666.777.888899.10'
    test_map = [
        '0', '0', '.', '.', '.', '1', '1', '1', '.', '.', '.', '2', '.', '.', '.', '3', '3', '3', '.', '4', '4', '.',
        '5', '5', '5', '5', '.', '6', '6', '6', '6', '.', '7', '7', '7', '.', '8', '8', '8', '8', '9', '9', '.', '10']
    result = main.file_compacter(test_map)
    expected = [
        '0', '0', '10', '9', '9', '1', '1', '1', '8', '8',
        '8', '2', '8', '7', '7', '3', '3', '3', '7', '4',
        '4', '6', '5', '5', '5', '5', '6', '6', '6'
    ]
    assert result == expected

def test_cont_compacter():
    temp = main.cont_compacter([ '0', '0', '.','.','.', '1','1','1', '.','.','.', '2', '.','.','.', '3','3','3', '.', '4','4', '.', '5','5','5','5', '.', '6','6','6','6', '.', '7','7','7', '.', '8','8','8','8', '9','9' ])
    result = ''.join(temp)
    expected = '00992111777.44.333....5555.6666.....8888'
    assert result == expected

def test_filesystem_checksum():
    #expected checksum 1928
    test_diskmap = ['0', '0', '9', '9', '8', '1', '1', '1', '8', '8', '8', '2', '7', '7', '7', '3', '3', '3', '6', '4', '4', '6', '5', '5', '5', '5', '6', '6', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    result = main.filesystem_checksum(test_diskmap)
    assert result == 1928


def test_filesystem_checksum_2digits():
    test_diskmap = [
        '0', '0', '10', '9', '9', '1', '1', '1', '8', '8',
        '8', '2', '8', '7', '7', '3', '3', '3', '7', '4',
        '4', '6', '5', '5', '5', '5', '6', '6', '6', '.',
        '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
        '.', '.', '.', '.'
        ]
    result = main.filesystem_checksum(test_diskmap)
    assert result == 2132