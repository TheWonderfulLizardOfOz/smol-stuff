class Check_date():
    def __init__(self, date):
        self.date = date
        self.valid_d = False
        self.valid_m = False
        self.valid_y = False
        self.valid_f = False
        self.valid = False
        self.date_list = []
        self.day = None
        self.month = None
        self.year = None

    def check_format(self):
        try:
            self.date_list = self.date.split("/")
            self.day = self.date_list[0]
            self.month = self.date_list[1]
            self.year = self.date_list[2]
            if len(self.year) == 4:
                self.valid_f = True
        except:
            self.day = "a"
            self.month = "b"
            self.year = "c"
            
        return self.valid_f

    def check_day(self):
        try:
            self.day = int(self.day)
        except:
            return self.valid_d

        if self.day <= 31 and self.day >= 1:
            self.valid_d = True

        return self.valid_d

    def check_month(self):
        try:
            self.month = int(self.month)
        except:
            return self.valid_m

        if self.month <= 12 and self.month >= 1:
            self.valid_m = True

        return self.valid_m

    def check_year(self):
        try:
            self.year = int(self.year)
        except:
            return self.valid_y

        if self.year <= 9999 and self.year >= 0:
            self.valid_y = True

        return self.valid_y

    def check_valid(self):
        total = self.valid_f + self.valid_d + self.valid_m + self.valid_y
        if total == 4:
            self.valid = True

        return self.valid
