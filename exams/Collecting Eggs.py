from collections import deque

eggs = deque(int(x) for x in input().split(', '))
papers = [int(x) for x in input().split(', ')]
box_size = 50
filled_boxes = 0

while eggs and papers:
    current_egg = eggs.popleft()
    current_paper = papers.pop()
    if current_egg <= 0:
        papers.append(current_paper)
    else:
        if current_paper + current_egg <= 50:
            if current_egg == 13:
                papers.append(current_paper)
                papers[0], papers[-1] = papers[-1], papers[0]
            else:
                filled_boxes += 1


if filled_boxes:
    print(f'Great! You filled {filled_boxes} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")
