
class HashTable:

    def __init__(self, capacity=10):
        """hash table is a list of lists(buckets)"""
        self.hash_table = []
        for i in range(capacity):
            self.hash_table.append([])

    def hash_calculation(self, key):
        key = key % 10
        return key


    def insert(self, package):
        """compute key using package_id, append entire package to bucket"""
        key = self.hash_calculation(package.package_id)
        self.hash_table[key].append(package)


    def lookup(self, package_id):
        """compute key given package_id, iterate over bucket, return package if found else None"""
        key = self.hash_calculation(package_id)
        for pkg in self.hash_table[key]:
            if pkg.package_id == package_id:
                return pkg
        return None


    def remove(self, package_id):
        """"
        compute key given package_id
        iterate over bucket, return True if package found and deleted else False
        unrequired, but it felt like something that I should add
        """
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