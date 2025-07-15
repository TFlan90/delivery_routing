
class HashTable:

    def __init__(self, capacity=10):
        self.hash_table = []
        for i in range(capacity):
            self.hash_table.append([])

    def hash_calculation(self, key):
        key = key % 10
        return key

    def insert(self, package):
        key = self.hash_calculation(package.package_id)
        self.hash_table[key].append(package)

    def lookup(self, package_id):
        key = self.hash_calculation(package_id)
        for pkg in self.hash_table[key]:
            if pkg.package_id == package_id:
                return pkg
        return None

    def remove(self, package_id):
        key = self.hash_calculation(package_id)
        for i, p in enumerate(self.hash_table[key]):
            if p.package_id == package_id:
                self.hash_table[key].pop(i)
                return True

        return False


    def __str__(self):
        return str(self.hash_table)

    def __repr__(self):
      return str(self.hash_table)













