class RgVar:
    @classmethod
    def title(cls):
        return cls.rg_name.replace(".", " ")

class MRT(RgVar):
    ylabel = 'Mean response time [ms]'
    rg_name = ""
    @classmethod
    def title(cls):
        return cls.rg_name.replace(".", " ") + " Mean response time" # TODO super(MRT).title() ?? failss with TypeError

class GET(MRT):
    rg_name = 'BasicOperations.Get'

class GET_NULL(MRT):
    rg_name = 'BasicOperations.Get.Null'

class PUT(MRT):
    rg_name = 'BasicOperations.Put'

class REMOVE(MRT):
    rg_name = 'BasicOperations.Remove'



class AT(RgVar):
    ylabel = 'Operations per second'
    @classmethod
    def title(cls):
        return cls.rg_name.replace(".", " ") + " Actual Throughput" # TODO super(MRT).title()

class GET_AT(AT, GET):
    pass

class GET_NULL_AT(AT, GET_NULL):
    pass

class PUT_AT(AT, PUT):
    pass

class REMOVE_AT(AT, REMOVE):
    pass
