class Department:
    def __init__(self, name, email, schedule):
        """
        :param str name: department's name
        :param str email: department's email
        :param dict[list[list[datetime]]] schedule: The public schedule. A dict, mapping day names
            to lists of hours between which the department is open for business publicly
            Example: {"monday": [["08:00", "12:30"], ["13:30", "20:00"]], ..., "friday": ["08:00", "14:00"]}
        """
        self.name = name
        self.email = email
        self.schedule = schedule

class Employee:
    def __init__(self, name, level, birth_date, address, phone, department):
        """
        :param str name: employee's name
        :param str level: either "manager" or "basic"
        :param datetime.datetime birth_date: employee's birth date
        :param str address: their address
        :param str phone: the employee's phone number
        :param Department department: the employee's department
        """
        self.name = name
        self.level = level
        self.birth_date = birth_date
        self.address = address
        self.phone = phone
        self.department = department
