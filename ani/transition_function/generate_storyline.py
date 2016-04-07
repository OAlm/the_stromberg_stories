from transition_initial_midpoint_end import get_transition_with_start
import itertools


# def build_story(story_lines):
#     for story_line in story_lines:
#         for story



story_lines=get_transition_with_start('work_for', no_of_sentences=1)

story_lines=list(itertools.product(*story_lines))



for x in story_lines:
    print(x)








