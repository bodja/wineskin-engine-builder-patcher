class EnvProperty(object):
    def __init__(self, value):
        self.value = value

    def __set__(self, instance, value):
        self.value = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.transform(self.value)

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError('Instances are not the same type.')

        return self.__class__(self.value + other.value)

    def transform(self, value):
        return value


class ListOption(EnvProperty):
    def __get__(self, instance, owner):
        if not instance:
            return self
        return self.transform(self.value)

    def transform(self, value):
        return ' '.join(value)


class CFlagArchListOption(ListOption):
    def __get__(self, instance, owner):
        if instance:
            if instance.universal_bin:
                return self.transform(instance.arch_universal + self.value)
            return self.transform(self.value)
        return self
