from flask import Flask, request, redirect, render_template
from flask.ext.bootstrap import Bootstrap
from math import log

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def home_form():
    return render_template('home.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(400)
def internal_server_error(e):
    return render_template('400.html'), 400
 
@app.route("/categorise", methods = ["GET", "POST"] )
def process_form():
    lst = request.form
    number = lst['number']
    n = number[1:]
    if len(n) == 0:
        return render_template('nonumber.html')
    else:
        n = int(number)
        n = abs(n)
    prime1 = None
    mersenne_prime1 = None
    divisors1 = 'None'
    prime_factorisation1 = 'None'
    fibonacci1 = None
    happy1 = None
    narcissistic1 = None
    perfect1 = None
    triangle1 = None
    binary1 = 'None'
    if 'pr' in lst:
        i = 2
        while i * i <= n:
            if n % i == 0:
                prime1 = False
                break
            i += 1
        if i * i >= n:
            prime1 = True
    elif 'm' in lst:
        p = log(n + 1) / log(2)
        if 2 ** int(p) - 1 == n:
            i = 2
            while i * i <= n:
                if n % i == 0:
                    mersenne_prime1 = False
                    break
                i += 1
            mersenne_prime1 = True
        else:
            mersenne_prime1 = False
    elif 'd' in lst:
        i = 1
        divisors = []
        while i * i <= n:
            if n % i == 0:
                divisors.append(i)
                divisors.append(int(n / i))
            i += 1
        divisors = str(divisors)
        divisors = divisors[1:-1]
        divisors1 = ''
        divisors1 += divisors
    elif 'prf' in lst:
        x = n
        i = 2
        prime_factorisation = []
        while i * i <= x:
            while x % i == 0:
                x = x / i
                prime_factorisation.append(i)
            i += 1
        if x == 1:
            prime_factorisation = str(prime_factorisation)
            prime_factorisation = prime_factorisation[1:-1]
            prime_factorisation1 = ''
            prime_factorisation1 += prime_factorisation
        else:
            prime_factorisation.append(int(x))
            prime_factorisation = str(prime_factorisation)
            prime_factorisation = prime_factorisation[1:-1]
            prime_factorisation1 = ''
            prime_factorisation1 += prime_factorisation
    elif 'f' in lst:
        a = 0
        b = 1
        count = 0
        while a < n:
            a, b = b, b+a
            count += 1
        if a == n:
            fibonacci1 = True
        else:
            fibonacci1 = False
    elif 'h' in lst:
        next_iter = []
        repeat_check = []
        for i in str(n):
            next_iter.append(int(i))
        while sum(e ** 2 for e in next_iter) != 1:
            sum_squares = sum(e ** 2 for e in next_iter)
            next_iter = []
            for E in str(sum_squares):
                next_iter.append(int(E))
            try:
                repeat_check.index(sum_squares)
                if repeat_check.index(sum_squares):
                    happy1 = False
            except ValueError:
                repeat_check.append(sum_squares)
        happy1 = True
    elif 'n' in lst:
        sum_ = 0
        for e in str(n):
            sum_ += int(e) ** len(str(n))
        if sum_ == n:
            narcissistic1 = True
        else:
            narcissistic1 = False
    elif 'p' in lst:
        sum_ = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                sum_ += i
                sum_ += n / i
            i += 1
        if int(sum_) == 2 * n:
            perfect1 = True
        else:
            perfect1 = False
    elif 't' in lst:
        if (int((1 + 8*n) ** 0.5)) ** 2 == 1 + 8*n:
            triangle1 = True
        else:
            triangle1 = False
    elif 'b' in lst:
        x = bin(n)[2:]
        binary1 = ''
        binary1 += x
    return render_template('return.html', category='check', prime=prime1, mersenne_prime=mersenne_prime1, divisors=divisors1, prime_factorisation=prime_factorisation1, happy=happy1, narcissistic=narcissistic1, triangle=triangle1, fibonacci=fibonacci1, binary=binary1, perfect=perfect1, number = n)
    
     
if __name__ == "__main__":
    app.run(debug=True)
