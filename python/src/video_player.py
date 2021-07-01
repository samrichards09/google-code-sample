"""A video player class."""

from .video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        global video_playing
        video_playing = [None, False]

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        sorted_list = sorted(self._video_library.get_all_videos(), key=lambda x: x.title)
        print("Here's a list of all available videos:")
        for x in range(len(sorted_list)):
            print(f"{sorted_list[x].title} ({sorted_list[x].video_id}) [{' '.join(sorted_list[x].tags)}]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        global video_playing
        try:
            title = self._video_library.get_video(video_id).title
            if video_playing[0] != None:
                print(f"Stopping video: {video_playing[0]}")
            video_playing = [title, False]
            print(f"Playing video: {video_playing[0]}")
        except AttributeError:
            print(f"Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        global video_playing
        if video_playing[0] != None:
            print(f"Stopping video: {video_playing[0]}")
            video_playing = [None, False]
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        self.play_video(random.choice(self._video_library.get_all_videos()).video_id)

    def pause_video(self):
        """Pauses the current video."""
        global video_playing
        if video_playing[1] == True:
            print(f"Video already paused: {video_playing[0]}")
        elif video_playing[0] != None:
            print(f"Pausing video: {video_playing[0]}")
            video_playing[1] = True
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        global video_playing
        if video_playing[0] == None:
            print("Cannot continue video: No video is currently playing")
        elif video_playing[1] == False:
            print("Cannot continue video: Video is not paused")
        else:
            print(f"Continuing video: {video_playing[0]}")
            video_playing[1] = True

    def show_playing(self):
        """Displays video currently playing."""
        global video_playing
        if video_playing[0] == None:
            output = "No video is currently playing"
        else:
            list = self._video_library.get_all_videos()
            for x in range(len(list)):
                if list[x].title == video_playing:
                    print(list[x].title)
                    output = f"{list[x].title} ({list[x].video_id}) [{' '.join(list[x].tags)}]"
            if video_playing[1] == True:
                output += " - PAUSED"
        print(output)

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
