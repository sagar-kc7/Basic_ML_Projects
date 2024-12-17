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




Objective: Write a prolog program to find the solution of Tower of Hanoi problem.
Source code:
% Move a single disk
moveone_disk(1, Source, Destination) :-
 write('Move top disk from '), 
 write(Source), write(' to '), write(Destination), nl.
% Move N disks
movedisks(N, Source, Destination, Auxiliary) :-
 N =:= 1, % Base case: if there's only one disk, just move it
 moveone_disk(1, Source, Destination);
 N > 1, % Recursive case: move N-1 disks to the auxiliary, move the Nth disk, then 
move the N-1 disks to the destination
 N1 is N - 1, 
 movedisks(N1, Source, Auxiliary, Destination), 
 moveone_disk(1, Source, Destination), 
 movedisks(N1, Auxiliary, Destination, Source).
% Base case for 1 disk (to avoid infinite loop)
move_disks(1, Source, Destination) :-
 moveone_disk(1, Source, Destination).
%Prakriti Pokhare



Objective: Write a prolog program to find the family relation.
Source code:
% Family relationships
parent('Punam', 'Prakriti').
parent('Punam', 'Sita').
parent('Sita', 'Ram').
female('Punam').
female('Prakriti').
female('Sita').
male('Ram').
% Rules
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
% Prakriti Pokharel
Output:


