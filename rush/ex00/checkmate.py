DIAGONALS = ((-1, -1), (-1, 1), (1, -1), (1, 1))
STRAIGHTS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def parse_board(board):
    """Return the list of rows if the board is valid, otherwise None."""
    if not isinstance(board, str):
        return None
    rows = board.splitlines()
    size = len(rows)
    if size == 0:
        return None
    for row in rows:
        if len(row) != size:
            return None
    if sum(row.count("K") for row in rows) != 1:
        return None
    return rows


def find_king(rows):
    for y, row in enumerate(rows):
        x = row.find("K")
        if x != -1:
            return y, x
    return None


def is_attacked_by_pawn(rows, ky, kx):
    # An enemy pawn captures one square diagonally "up" (towards row 0),
    # so it must stand one row below the King, on a neighbouring column.
    y = ky + 1
    for x in (kx - 1, kx + 1):
        if 0 <= y < len(rows) and 0 <= x < len(rows) and rows[y][x] == "P":
            return True
    return False


def is_attacked_along(rows, ky, kx, directions, attackers):
    # Walk away from the King: only the first piece met can capture it.
    size = len(rows)
    for dy, dx in directions:
        y, x = ky + dy, kx + dx
        while 0 <= y < size and 0 <= x < size:
            cell = rows[y][x]
            if cell in "PBRQK":
                if cell in attackers:
                    return True
                break
            y += dy
            x += dx
    return False


def checkmate(board):
    rows = parse_board(board)
    if rows is None:
        print("Error")
        return
    ky, kx = find_king(rows)
    in_check = (
        is_attacked_by_pawn(rows, ky, kx)
        or is_attacked_along(rows, ky, kx, DIAGONALS, "BQ")
        or is_attacked_along(rows, ky, kx, STRAIGHTS, "RQ")
    )
    print("Success" if in_check else "Fail")
