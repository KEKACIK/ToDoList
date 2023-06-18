from openpyxl.styles import Font, Alignment
from openpyxl.utils import get_column_letter


def reform(ws):
    font_style = Font(size=12)
    for column_cells in ws.columns:
        length = 0
        for cell in column_cells:
            curr_length = len("" if cell.value is None else str(cell.value))
            if curr_length > length:
                length = curr_length

            cell.alignment = Alignment(horizontal='center', wrap_text=True, vertical="center")
            cell.font = font_style

        ws.column_dimensions[get_column_letter(column_cells[0].column)].width = length + 7
    return ws
