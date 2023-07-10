class Card:
    OICHO_KABU_RANKS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def __init__(self, rank):
        if rank not in self.OICHO_KABU_RANKS:
            raise ValueError(f"Invalid rank. Correct ranks: {self.OICHO_KABU_RANKS}")
        self.rank = rank

    def __str__(self):
        return f"{self.rank}"

    def __repr__(self):
        return f"Card('{self.rank}')"

    def __eq__(self, other_card):
        return self.rank == other_card.rank

    def __lt__(self, other_card):
        return self.rank < other_card.rank

    def __gt__(self, other_card):
        return self.rank > other_card.rank

    @classmethod
    def create_oicho_kabu_set(cls):
        return [cls(rank) for _ in range(4) for rank in cls.OICHO_KABU_RANKS]
