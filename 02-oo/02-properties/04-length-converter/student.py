class LengthConverter:
    inch_in_meter = 39.3701
    feet_in_meter = 3.28084

    def __init__(self):
        self.__distance_in_meter = 0

    @property
    def meter(self):
        return self.__distance_in_meter
    
    @meter.setter
    def meter(self,value):
        self.__distance_in_meter = value

    @property
    def feet(self):
        return self.__distance_in_meter * LengthConverter.feet_in_meter
    
    @feet.setter
    def feet(self,value):
        self.__distance_in_meter = value / LengthConverter.feet_in_meter
    
    @property
    def inch(self):
        return self.__distance_in_meter * LengthConverter.inch_in_meter
    
    @inch.setter
    def inch(self,value):
        self.__distance_in_meter = value / LengthConverter.inch_in_meter

    