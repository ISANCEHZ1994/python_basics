class NameOfClass():
    class_attribute = 'value'
    
    # __init__ : is considered Dunder Method 
    # double underscore is a special meaning for Python
    def __init__(self, param1, param2, param3):
        self.param1 = param1
        self.param2 = param2
        # _ (underscore usually means `PRIVATE`)
        # techincally there are no TRUE PRIVATE variables however
        # developers essentially mean don't touch this (_) 
        self._parm3 = param3

    def method(self):
        #code
    
    @classmethod
    def cls_method(cls, param1, param2):
        #code

    @staticmethod
    def stc_method(param1, param2):
        #code