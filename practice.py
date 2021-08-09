def solution(genres, plays):
    genre = {}
    play = {}
    answer = []

    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        play[g] = play.get(g,  0) + p
        genre[g] = genre.get(g, []) + [(p, i)]

        print(play)
        print(genre)
        print()

    genreSort = sorted(play.items(), key=lambda x: x[1], reverse=True)

    print(genreSort)
    print()

    for (g, total) in genreSort:
        genre[g] = sorted(genre[g], key=lambda x: (-x[0], x[1]))
        print(genre[g])
        answer += [idx for (p, idx) in genre[g][:2]]

    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))
