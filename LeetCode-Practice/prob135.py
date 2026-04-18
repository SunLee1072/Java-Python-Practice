class Solution:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)
        Rcandies = [1] * len(ratings)
        Lcandies = [1] * len(ratings)
        answer = [1] * len(ratings)

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                Rcandies[i] = Rcandies[i-1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                Lcandies[i] = Lcandies[i + 1] + 1

        for i in range(len(answer)):
            answer.append(max(Rcandies[i], Lcandies[i]))

        return sum(answer)
