Implementation of polynomial caculations
===

terms: each component in expression
coefficient: the scalar of terms
degree: the exponenet of the x part

1. addition
2. muliplication
3. evaluation


===
	Define: Polynomial ADT

Polynomial(): Creates a new polynomial initialized to be empty and thus
containing no terms.

Polynomial( degree, coefficient ): Creates a new polynomial initialized
with a single term constructed from the degree and coefficient arguments.

degree(): Returns the degree of the polynomial. If the polynomial contains
no terms, a value of −1 is returned.

getitem ( degree ): Returns the coefficient for the term of the provided de-
gree. Thus, if the expression of this polynomial is x 3 + 4x + 2 and a degree of
1 is provided, this operation returns 4. The coefficient cannot be returned for
an empty polynomial.

evaluate( scalar ): Evaluates the polynomial at the given scalar value and
returns the result. An empty polynomial cannot be evaluated.

add ( rhsPolynomial ): Creates and returns a new Polynomial that is the
result of adding this polynomial and the rhsPoly. This operation is not
defined if either polynomial is empty.

subtract ( rhsPoly ): Creates and returns a new Polynomial that is the re-
sult of subtracting this polynomial and the rhsPoly. This operation is not
defined if either polynomial is empty.

multiply ( rhsPoly ): Creates and returns a new Polynomial that is the re-
sult of multiplying this polynomial and the rhsPoly. This operation is not
defined if either polynomial is empty.
