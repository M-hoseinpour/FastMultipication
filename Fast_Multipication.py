class Fast_Multipication():

    def integer_Multipication(self, x, y):

        if len(str(x)) == 1 or len(str(y)) == 1 : return x * y

        n = max(len(str(x)), len(str(y)))
        n_half = n / 2

        a = int(int(x) / 10**(n_half))
        b = int(int(x) % 10**(n_half))
        c = int(int(y) / 10**(n_half))
        d = int(int(y) % 10**(n_half))
        
        ac = self.integer_Multipication(int(a), int(c))
        bd = self.integer_Multipication(int(b),int(d))
        ad_plus_bc = self.integer_Multipication(a+b,c+d) - ac - bd
            
        prod = ac * 10**(2*n_half) + (ad_plus_bc * 10**n_half) + bd
        return prod

    def filter(slef, x, y):
        m, n = len(str(x)), len(str(y))
        if (m < n):
            x = '0' * (n - m) + str(x)
        else:
            y = '0' * (m - n) + str(y)
        return str(x), str(y)

    def add_binary(self, x, y):
        integer_sum = int(x, 2) + int(y, 2)
        binSum = bin(integer_sum)
        return str(binSum[2:])

    def binary_Multipication(self, x, y):
        x, y = self.filter(x, y)
        n = len(str(x))
        if n == 0:
         return 0
        if n == 1:
         return int(x) & int(y)

        a, b = x[:n // 2], x[n // 2:]
        c, d = y[:n // 2], y[n // 2:]

        ac = self.binary_Multipication(a, c)
        bd = self.binary_Multipication(b, d)
        ad_plus_bc = self.binary_Multipication(self.add_binary(a, b), self.add_binary(c, d))
        result = ac * (1 << 2 * (n - n // 2)) + (ad_plus_bc - ac - bd) * (1 << (n - n // 2)) + bd
        return result



multiply = Fast_Multipication()

integer_multiplied = multiply.integer_Multipication(26842, 274782)
print("Result: " + str(integer_multiplied))

binary_multiplied = multiply.binary_Multipication('100101010', '1101010')
print("Integer: "+ str(binary_multiplied) + " Binary: " + str(bin(binary_multiplied))[2:])