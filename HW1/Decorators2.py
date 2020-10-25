def person_lister(f):
    def inner(people):
        # complete the function
        # 1:order by age by sorted function
        ordered_age=sorted(people,key=lambda x:int(x[2]))
        return map(f,ordered_age)
    return inner