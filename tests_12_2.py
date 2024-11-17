import runner
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        set = {'Усэйн': 10, 'Андрей': 9, 'Ник': 3}
        self.runners = {n: runner.Runner(name=n, speed=v) for n, v in set.items()}

    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            print(f'{k}: {v}')

    def test_tournament(self):
        tournament = runner.Tournament(90, self.runners['Усэйн'], self.runners['Ник'])
        all_results = tournament.start()
        self.assertTrue(all_results[2], self.runners['Ник'])

    def test_tournament_2(self):
        tournament = runner.Tournament(90, self.runners['Андрей'], self.runners['Ник'])
        all_results = tournament.start()
        self.assertTrue(all_results[2], self.runners['Ник'])

    def test_tournament_3(self):
        tournament = runner.Tournament(90, self.runners['Усэйн'], self.runners['Андрей'], self.runners['Ник'])
        all_results = tournament.start()
        self.assertTrue(all_results[3], self.runners['Ник'])

if __name__ == '__main__':
    unittest.main()
