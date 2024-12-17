These are the basic ML project resources. If you can do better, you are allowed to push changes.


SOURCE CODE:
% Family relationships
parent('Pratik', 'Megh').
parent('Pratik', 'Manoj').
parent('Manoj', 'Subodh').
male('Pratik'). male('Megh'). male('Subodh').
female('Manoj').
% Rules
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).




