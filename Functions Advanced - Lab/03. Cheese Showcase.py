import os


def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(
        kwargs.items(),
        key=lambda x: (-len(x[1]), x[0]),

    )
    result = []
    for name, pieces_counts in sorted_cheeses:
        result.append(name)
        # for piece_counts in pieces_counts:
        #     result.append(piece_counts)
        result.extend(
            sorted(pieces_counts, reverse=True)
        )
    return '\n'.join([str(x) for x in result])

