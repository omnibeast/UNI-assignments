% Saurav Pokharel
% Homework 01
% file: hw1.pl
% Family tree prolog program

% Defining the male and famales in the Family
female(ann).
female(beth).
female(liz).
female(sue).
female(jill).
female(mary).
female(carol).

male(bob).
male(ted).
male(bill).
male(sam).
male(harry).
male(john).
male(matt).

% parental relationship
parentof(beth, bill).
parentof(bill, jill).
parentof(bill, liz).
parentof(ann, jill).
parentof(ann, liz).
parentof(ann, ted).
parentof(liz, matt).
parentof(matt, john).
parentof(mary, john).
parentof(sue, mary).
parentof(harry, sue).
parentof(harry, sam).
parentof(carol, sue).
parentof(carol, sam).
parentof(bob, carol).

% relation rule
% Sibling Rule
siblings(Sib1, Sib2) :- 
    parentof(Parent, Sib1), parentof(Parent, Sib2).

% sister rule
sisterof(Sis, Sib) :- 
    siblings(Sis, Sib), female(Sis).

% brother rule
brotherof(Bro, Sib) :- 
    siblings(Bro, Sib), male(Bro).

% rule to determine if an individual is an ancestor of another
ancestor_of(A,B) :- 
    parentof(A,B).
ancestor_of(A,B) :- 
    parentof(A,C), ancestor_of(C,B).

% rule to determine the generation between ancestors
ancestor_gen(A,B,G) :- 
    parentof(A,B), G is 1.

ancestor_gen(A,B,G) :- 
    parentof(A,C), ancestor_gen(C,B,F), G is F + 1.
