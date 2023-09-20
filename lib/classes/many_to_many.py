from datetime import datetime

class NationalPark:

    def __init__(self, name):
        self.name = name

    @property 
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            print("This park already has a name")
        elif isinstance(name, str) and len(name)>=3:
            self._name=name
        else:
            print("Try again- invalid format.")

    #all trips at this park, should be of class trip    
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park ==self]

    #unique list of all visitors to this park, should be of class visitor
    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))

    #how many times this park has been visited, 0 if none
    def total_visits(self):
        if len(self.trips()) > 0:
            return len(self.trips())
        else:
            return 0
    
    #visitor instance that's visited the park the most, 0 if none
    def best_visitor(self):      
        # most_visits = 0
        # most_visitor= None
        #look at each visitor in self.visitors
        #get total_number_of_trips to self
        # for visitor in self.visitors():
        #     visitors_visits= visitor.total_visits_at_park(self)
        #     if most_visits < visitors_visits:
        #         #print("entered if") 
        #         most_visits=visitors_visits
        #         most_visitors=visitor
        # return most_visitor
        visitors = [trip.visitor for trip in self.trips()]
        return max(visitors, key= visitors.count)
        

class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self,start_date):
        if isinstance(start_date, str) and len(start_date)>=7:
            self._start_date= start_date
        else:
            print("Start date must be in format Month Day")

    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date)>=7:
            self._end_date= end_date
        else:
            print("End date must be in format Month Day")

    @property
    def visitor(self):
        return self._visitor
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            print("Visitor must be in class Visitor")

    @property
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            print("National park must be in class NationalPark")


class Visitor:

    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    @ name.setter
    def name(self, name):
        if isinstance (name, str) and 1<=len(name)<=15:
            self._name = name

    #connecting visitors to trips to national parks
    #returns a list of all trips for this visitor, must be class Trips
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    #unique list of all parks the visitor has visited, must be type NationalPark
    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))

    #tests don't work on this one says Rachel
    #recieves natl park object as argument, returns total number of visits per visitor, 0 if none
    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park == park])
        #count the number of visits for the park with array length
        # visits = 0
        # #iterate over self.trips (all current visitors trips)
        # for trip in self.trips():
        #     #if current trip matches park argument, increment visits
        #     if (trip.national_park == park):
        #         visits += 1
        # return visits