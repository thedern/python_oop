from intro.dog_class import Dog


class Aussie(Dog):

    """
    inherits from Dog class, no need to redefine __init__
    """
    # override description from dog class
    description = "Override Aussie!!!"

    def aussie_bite(self):
        # skip looking in current class for bite and go directly to parent class via super()
        bt = super().bite()
        print(f'aussies, {bt}')

    # add a new method
    def speak(self) -> None:
        print("rufff!!")


