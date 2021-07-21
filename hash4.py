def solution(genres, plays):
    genre = {}
    play = {}
    answer = []

    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        play[g] = play.get(g,  0) + p
        genre[g] = genre.get(g, []) + [(p, i)]

    genreSort = sorted(play.items(), key=lambda x: x[1], reverse=True)
    
    for (g, total) in genreSort:
        genre[g] = sorted(genre[g], key=lambda x: (-x[0], x[1]))
        answer += [idx for (p, idx) in genre[g][:2]]

    return answer

"""
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
"""