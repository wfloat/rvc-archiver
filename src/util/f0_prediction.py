from pytube import YouTube, Search
from dataclasses import dataclass
from typing import Optional, List, Dict, Any

VIDEO_LENGTH_MINIMUM = 240

@dataclass
class VideoSearchResult:
    id: str
    url: str
    title: str
    duration: int # seconds
    # upload_date: datetime
    # age_restricted: bool
    author: str

def duration_str_to_seconds(duration_str: str) -> int:
    """
    Converts a length string in the format "HH:MM:SS" or "MM:SS" to the total number of seconds.
    
    Args:
    duration_str (str): A string representing a time duration in the format "HH:MM:SS" or "MM:SS".
    
    Returns:
    int: Total number of seconds represented by the input string.
    """
    # Split the string into its components
    parts = duration_str.split(":")
    
    # Check the number of parts and calculate the total seconds accordingly
    if len(parts) == 3:
        hours, minutes, seconds = map(int, parts)
        total_seconds = hours * 3600 + minutes * 60 + seconds
    elif len(parts) == 2:
        minutes, seconds = map(int, parts)
        total_seconds = minutes * 60 + seconds
    else:
        raise ValueError("Invalid time duration format. Expected 'HH:MM:SS' or 'MM:SS'.")

    return total_seconds

# Based off of the Pytube Search.fetch_and_parse function
def parse_innertube_search(raw_results) -> List[VideoSearchResult]:
    """Parse the search results from the innertube API.
    """
    # Begin by executing the query and identifying the relevant sections
    #  of the results
    # raw_results = self.fetch_query(continuation)

    # Initial result is handled by try block, continuations by except block
    try:
        sections = raw_results['contents']['twoColumnSearchResultsRenderer'][
            'primaryContents']['sectionListRenderer']['contents']
    except KeyError:
        sections = raw_results['onResponseReceivedCommands'][0][
            'appendContinuationItemsAction']['continuationItems']
    item_renderer = None
    continuation_renderer = None
    for s in sections:
        if 'itemSectionRenderer' in s:
            item_renderer = s['itemSectionRenderer']

    # If the itemSectionRenderer doesn't exist, assume no results.
    if item_renderer:
        videos: List[VideoSearchResult] = []
        raw_video_list = item_renderer['contents']
        for video_details in raw_video_list:
            # Skip over ads
            if video_details.get('searchPyvRenderer', {}).get('ads', None):
                continue

            # Skip "recommended" type videos e.g. "people also watched" and "popular X"
            #  that break up the search results
            if 'shelfRenderer' in video_details:
                continue

            # Skip auto-generated "mix" playlist results
            if 'radioRenderer' in video_details:
                continue
            # Skip playlist results
            if 'playlistRenderer' in video_details:
                continue

            # Skip channel results
            if 'channelRenderer' in video_details:
                continue

            # Skip 'people also searched for' results
            if 'horizontalCardListRenderer' in video_details:
                continue

            # Can't seem to reproduce, probably related to typo fix suggestions
            if 'didYouMeanRenderer' in video_details:
                continue

            # Seems to be the renderer used for the image shown on a no results page
            if 'backgroundPromoRenderer' in video_details:
                continue

            if 'videoRenderer' not in video_details:
                # logger.warn('Unexpected renderer encountered.')
                # logger.warn(f'Renderer name: {video_details.keys()}')
                # logger.warn(f'Search term: {self.query}')
                # logger.warn(
                #     'Please open an issue at '
                #     'https://github.com/pytube/pytube/issues '
                #     'and provide this log output.'
                # )
                continue

            # Extract relevant video information from the details.
            # Some of this can be used to pre-populate attributes of the
            #  YouTube object.
            vid_renderer = video_details['videoRenderer']
            vid_id = vid_renderer['videoId']
            vid_url = f'https://www.youtube.com/watch?v={vid_id}'
            vid_title = vid_renderer['title']['runs'][0]['text']
            vid_channel_name = vid_renderer['ownerText']['runs'][0]['text']
            vid_channel_uri = vid_renderer['ownerText']['runs'][0][
                'navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
            # Livestreams have "runs", non-livestreams have "simpleText",
            #  and scheduled releases do not have 'viewCountText'
            if 'viewCountText' in vid_renderer:
                if 'runs' in vid_renderer['viewCountText']:
                    vid_view_count_text = vid_renderer['viewCountText']['runs'][0]['text']
                else:
                    vid_view_count_text = vid_renderer['viewCountText']['simpleText']
                # Strip ' views' text, then remove commas
                stripped_text = vid_view_count_text.split()[0].replace(',','')
                if stripped_text == 'No':
                    vid_view_count = 0
                else:
                    vid_view_count = int(stripped_text)
            else:
                vid_view_count = 0
            if 'lengthText' in vid_renderer:
                vid_length = vid_renderer['lengthText']['simpleText']
            else:
                vid_length = None

            # vid_metadata = {
            #     'id': vid_id,
            #     'url': vid_url,
            #     'title': vid_title,
            #     'channel_name': vid_channel_name,
            #     # 'channel_url': vid_channel_uri,
            #     'view_count': vid_view_count,
            #     'length': vid_length
            # }

            # Construct YouTube object from metadata and append to results
            videos.append(VideoSearchResult(
                id=vid_id,
                url=vid_url,
                title=vid_title,
                author=vid_channel_name,
                duration=duration_str_to_seconds(vid_length)
            ))
    else:
        videos = None

    return videos

search_results_raw = Search('Invasions Season 3 Trailer').fetch_query()
results: List[VideoSearchResult] = parse_innertube_search(search_results_raw)

print(results)

