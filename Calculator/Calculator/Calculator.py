class Calculator() :
    def add(self, addend1, addend2) :
        if not isinstance(addend1, int) or not isinstance(addend2, int) :
            raise TypeError(f'arguments must be int.  types are {type(addend1)} and {type(addend2)}')
        return addend1 + addend2