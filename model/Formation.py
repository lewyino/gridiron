
class Formation:
    __allowPositions = ('qb', 'rb', 'wr', 'te', 'ol', 'dl', 'de', 'mlb', 'olb', 'cb', 'sf', 'k')

    def __init__(self, position: str, quantity: int):
        self.position = position
        self.quantity = quantity

    def __setattr__(self, *args, **kwargs):
        try:
            if args[0] not in ('position', 'quantity'):
                raise Exception('Allow properties: position, quantity')
            if args[0] == 'position' and not self.__check_position_value(args[1]):
                raise Exception('Wrong position \'%s\', allowed positions: %s'
                                % (args[1], ', '.join(self.__allowPositions)))
            if args[0] == 'quantity' and not self.__check_quantity_position(args[1]):
                raise Exception('quantity must be a integer')
            return super().__setattr__(*args, **kwargs)
        except Exception as e:
            raise e

    @staticmethod
    def get_allow_position():
        return Formation.__allowPositions

    def __check_position_value(self, value):
        if not isinstance(value, str):
            return False
        return True if value in self.__allowPositions else False

    def __check_quantity_position(self, value):
        return True if isinstance(value, int) else False
