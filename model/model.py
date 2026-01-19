from database.dao import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.teams=[]
        self.dao = DAO()
        self.grafo= nx.Graph()
        self.salary_map = {}
        self.best_path = []
        self.best_weight = 0

    def get_years(self):
        return self.dao.get_years_from_1980()

    def load_teams(self,year: int):
        self.teams=self.dao.get_teams(year)
        return self.teams

    def build_grafo(self,years):
        self.grafo.clear()
        #self.salary_map = self.dao.get_salari(years)


        teams=self.dao.get_teams(years)
        for team in teams:
            self.grafo.add_node(team.id)

        team_ids = [team.id for team in teams]
        for i in range(len(team_ids)):
            for j in range(i + 1, len(team_ids)):
                t1 = team_ids[i]
                t2 = team_ids[j]

                if t1 in self.salary_map and t2 in self.salary_map:
                    peso = self.salary_map[t1] + self.salary_map[t2]
                    self.grafo.add_edge(t1, t2, weight=peso)

    def squadre_adiacenti(self,team):
        adiacenti=[]
        for a in self.grafo.neighbors(team.id):
            w=self.grafo[team][a]['weight']
            adiacenti.append((a,w))
        return sorted(adiacenti)

    def bestPath(self,start):
        self.best_path=[]
        self.best_weight = 0
        self._ricorsione([start],0,float('inf'),k)
        return self.best_path


    def _ricorsione(self,path,peso, soglia,k):
        last = path[-1]
        if peso>self.best_weight:
            self.best_weight = peso
            self.best_path = list(path)

        vicini=[]
        for succ in self.squadre_adiacenti(last):
            if succ not in path:
                w=self.grafo[last][succ]['weight']

                if w<soglia:
                    vicini.append((succ,w))

        for succe, w in vicini[:k]:
            path.append(succe)
            self._ricorsione(path, peso + w, w, k)
            path.pop()













