class Television:
    """
    These are the default values for the Tv
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        '''
        Here we are initializing the variables for the new object
        '''
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self):
        '''
        Method to turn on the Tv
        :return:
        '''
        if not self.__status:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        '''
        Method to mute the Tv
        :return:
        '''
        if self.__status:
            if not self.__muted:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self):
        '''
        Method to turn up the channel number
        :return:
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        '''
        Method to turn down the channel number
        :return:
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        '''
        Method to turn up the volume of the Tv
        :return:
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        '''
        Method to turn down the volume of the Tv
        :return:
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        '''
        Method to show the television status
        :return:
        '''
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'