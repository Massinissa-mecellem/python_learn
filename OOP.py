import statistics as stat
from collections import Counter

class statistic:
    def __init__(self, data):
        self.data = data
        
    def count(self):
        return len(self.data)
    def somme(self):
        return sum(self.data)
    def minimum(self):
        return min(self.data)
    def maximum(self):
        return max(self.data)
    def Etendu(self):
        valeur_max = self.maximum()
        valeur_min = self.minimum()
        return valeur_max - valeur_min
    def moy(self):
        return stat.mean(self.data)
    def mediane(self):
        return stat.median(self.data)
    def Mode(self):
        counts = Counter(self.data)
        mode_val, frequence = counts.most_common(1)[0]
        return {'mode': mode_val, 'count': frequence}
        
    def std(self):
        return stat.stdev(self.data)
    def var(self):
        return stat.variance(self.data)
    def freq_dist(self):
        cpt = Counter(self.data)
        return [(cp * 4.0, n) for n, cp in cpt.most_common()]


    
    def describe(self):
        return f'le Nombre {self.count} \n la somme {self.somme()} \n le maximum {self.maximum()} \n le minimum {self.minimum()} \n le minimum {self.minimum()} \n letendu {self.Etendu()} \n la Moyenne {self.moy()} \n le mediane {self.mediane()} \n le mode {self.Mode()} \n la variance  {self.var()} \n frequence de distribution {self.freq_dist()}'

    
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

s1 = statistic(ages)
print(s1.describe())


class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def add_income(self, revenu, amount):
        self.incomes[revenu] = amount
    def add_expense(self, depense, amount):
        self.expenses[depense] = amount

    
    def total_income(self):
        return sum(self.incomes.values())
    
    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()



    def affiche_info(self):
        return (
            f'Client {self.firstname} {self.lastname}\n' 
            f'Ces revenus: {self.incomes} et dépenses: {self.expenses}\n'
            f'le total des revenues: {self.total_income()}\n'
            f'le totale des depenses: {self.total_expense()}\n'
            f'le reste est: {self.account_balance()}'
            )

acc = PersonAccount('massinissa', 'mecellem')
acc.add_income('freelance', 4900)
acc.add_income('teletravail', 2900)
acc.add_income('entreprise', 900)

acc.add_expense('loyer', 500)
acc.add_expense('cours', 300)
acc.add_expense('activité', 200)





    


class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError


class SuperQueue(Queue):
    def __init__(self):
        super().__init__()

    def isempty(self):
        return len(self.queue) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
    
    