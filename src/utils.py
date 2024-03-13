import math
from enum import Enum


class Alignment(Enum):
    CENTER = 'CENTER'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    JUSTIFY = 'JUSTIFY'


def draw_table(table: list[list], alignment: Alignment = Alignment.CENTER) -> None:
    columns_max_width = calculate_columns(table)

    for line in table:
        line_as_str = '|'
        columns_index = 0
        for element in line:
            max_columns_length = columns_max_width[columns_index]
            buffer_length = max_columns_length - len(element)

            if alignment == Alignment.CENTER:
                right_buffer = math.ceil(buffer_length/2)
                left_buffer = buffer_length - right_buffer
                line_as_str += left_buffer * ' ' + element + right_buffer * ' ' + '|'
            elif alignment == Alignment.LEFT:
                line_as_str += element + ' ' * buffer_length + '|'
            elif alignment == Alignment.RIGHT:
                line_as_str += ' ' * buffer_length + element + '|'
            else:
                raise NotImplementedError()

            columns_index += 1
        print(line_as_str)


def calculate_columns(table):
    columns_max_width = []
    number_of_columns = len(table[0])
    for columns_index in range(number_of_columns):
        max_columns_length = 0
        for line in table:
            element = line[columns_index]
            if len(element) > max_columns_length:
                max_columns_length = len(element)

        columns_max_width.append(max_columns_length)
    print(columns_max_width)
    return columns_max_width
