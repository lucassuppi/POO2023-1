class Trade:
    def __init__(self, biddername, required_sticker, available_sticker):
        self.__biddername = biddername
        self.__required_sticker = required_sticker
        self.__available_sticker = available_sticker
        self.__status = 0  # 0 = Pending, 1 = Accepted, -1 = Rejected

    def swap(self, biddername, required_sticker, available_sticker):
        #need to do swap part
        pass

    def accept(self, accepted):
        #need to do accept part
        pass