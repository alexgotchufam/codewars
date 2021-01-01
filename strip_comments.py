from typing import List


def solution(string: str, markers: List[str]) -> str:
    lines = string.split("\n")
    for i, line in enumerate(lines):
        comment_index = len(line)
        for marker in markers:
            tmp_index = line.find(marker)
            if tmp_index != -1:
                comment_index = min(comment_index, tmp_index)

        lines[i] = line[:comment_index].strip()
    return "\n".join(lines)


assert (
    solution(
        "strawberries cherries\noranges - @ avocados\nstrawberries strawberries\n, apples watermelons cherries oranges watermelons",
        [".", "=", "-", "!", "@", ",", "'", "#", "^"],
    )
    == "strawberries cherries\noranges\nstrawberries strawberries\n"
)
