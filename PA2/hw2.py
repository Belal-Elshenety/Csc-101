import data

def create_rectangle(point1,point2):
    top_left = data.Point(point1.x,point2.y)
    bottom_right = data.Point(point2.x,point1.y)
    return data.Rectangle(top_left,bottom_right)

def shorter_duration_than(duration1, duration2):
    duration1 = duration1.minutes * 60 + duration1.seconds
    duration2 = duration2.minutes * 60 + duration2.seconds
    return duration1 < duration2

def song_shorter_than(song_list:list[data.Song],duration):
    new_list = []
    for song in song_list:
        if shorter_duration_than(song.duration,duration):
            new_list.append(song)
    return new_list

def running_time(song_list:list[data.Song],playlist:list):
    songs = []
    total_seconds = 0
    total_minutes = 0
    for idx in playlist:
        songs.append(song_list[idx])
    for song in songs:
        total_seconds += song.duration.seconds
        total_minutes += song.duration.minutes + total_seconds // 60
        total_seconds %= 60
    return data.Duration(total_minutes,total_seconds)

def validate_route(city_links, route):
    # An empty route or a route with a single city is valid
    if len(route) <= 1:
        return True
    # Check if there is a link between consecutive cities in the route
    for i in range(len(route) - 1):
        current_city = route[i]
        next_city = route[i + 1]
        if [current_city, next_city] not in city_links and [next_city, current_city] not in city_links:
            return False

    return True

def longest_repetition(lst):
        if not lst:
            return None

        longest_idx, current_idx = 0, 0
        current_count, longest_count = 1, 1

        for i in range(1, len(lst)):
            if lst[i] == lst[i - 1]:
                current_count += 1
                if current_count > longest_count:
                    longest_count = current_count
                    longest_idx = current_idx
            else:
                current_idx = i
                current_count = 1

        return longest_idx

