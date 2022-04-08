from src.utils import load_data

class CommentsCore:

    def get_comment(by, value):
        if not by or not value:
            raise Exception('you need to inform a filter')
        comments_data = load_data('comments')
        return list(filter(lambda comments: comments.get(by) == value, comments_data))


