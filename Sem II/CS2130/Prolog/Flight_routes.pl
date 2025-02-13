% Saurav Pokharel
% CS2130
% Prolog program to determine airline routes between cities, 

%--- FACTS ---
% Direct flights between cities
flight(dgz, qyy).
flight(dgz, azi).
flight(qyy, csi).
flight(azi, tva).
flight(csi, ppg).
flight(tva, brw).
flight(brw, csi).

%--- RULES ---
% Direct flight with 0 stops
route(Origin, Destination, 0):- flight(Origin, Destination).

% Add one stop to route
route(Origin, Destination, Stops) :-
    flight(Origin, Intermediate), route(Intermediate, Destination, Stops1), Stops is Stops1 + 1.

% route cities list
route_cities(Origin, Destination, Stops, [Origin|Cities]) :-  
    flight(Origin, Destination), 
    Stops is 0, 
    Cities = [Destination].
route_cities(Origin, Destination, Stops, [Origin|Cities]) :- 
    flight(Origin, Intermediate), 
    route_with_cities(Intermediate, Destination, Stops1, Cities1), 
    Stops is Stops1 + 1, 
    Cities = [Intermediate|Cities1].

