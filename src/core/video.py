from src.utils import load_data, filter_by_options

class VideoCore:

    def get_video(by, value):
        if not by or not value:
            raise Exception('you need to inform a filter')
        video_data = load_data('videos')
        return list(filter(lambda video: video.get(by) == value, video_data))

    def get_tops_videos():
        videos_data = load_data('videos')
        return sorted(videos_data, key= lambda video: video.get('likes'), reverse=True)

    def get_recommendations(by, value, category, top):
        recommendation_data = load_data('recommendations')
        recomendations = list(filter(lambda recommendation: recommendation.get(by) == value, recommendation_data))
        return filter_by_options(category=category, top=top, content=recomendations)

    def get_videos():
        return load_data('videos')
