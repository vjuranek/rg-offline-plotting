class RgVar:
    @classmethod
    def title(cls):
        return cls.rg_name.replace(".", " ")

class MRT(RgVar):
    '''Mean response time'''
    ylabel = 'Mean response time [ms]' # in RG in nano seconds, but RgReport converts it to miliseconds
    rg_name = ""
    @classmethod
    def title(cls):
        return cls.rg_name.replace(".", " ") + " Mean response time" # TODO super(MRT).title() ?? failss with TypeError

class GET(MRT):
    '''Mean response time of GET operation'''
    rg_name = 'BasicOperations.Get'

class GET_NULL(MRT):
    #TODO what exactly this variable standas for?
    rg_name = 'BasicOperations.Get.Null'

class PUT(MRT):
    '''Mean response time of PUT operation'''
    rg_name = 'BasicOperations.Put'

class REMOVE(MRT):
    '''Mean response time of REMOVE operation'''
    rg_name = 'BasicOperations.Remove'



class AT(RgVar):
    '''Actual throughtput'''
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
