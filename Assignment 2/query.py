class Query():
    #Check user exists or not in the database
    def checkAuth(self, connection, credentials):
        cursor = connection.cursor()
        cred = self.splitParams(credentials)
        
        cursor.execute("SELECT username, password FROM staff " +
                "WHERE username=? AND password=?", (cred[1], cred[2]))
        auth = cursor.fetchone()

        if (auth != None):
            return True
        return False
    
    #Retrives the staff id using username
    def getStaffId(self, connection, username):
        cursor = connection.cursor()
        cursor.execute("SELECT staffid FROM staff WHERE username=?", (username, ))

        id = cursor.fetchone()

        if (id != None):
            return id
        return ""

    #Retrives historical place code using staff id
    def getHistoricalPlace(self, connection, username):
        cursor = connection.cursor()
        id = self.getStaffId(connection, username)
        
        if id != "":
            cursor.execute("SELECT hpcode FROM historical_place WHERE staffid=?", id)
            hpcode = cursor.fetchone()

            if (hpcode != None):
                return hpcode
            return ""
        return ""
    
    #Inserts the data coming from Historical Place Manager
    def insertStatistics(self, connection, params):
        cursor = connection.cursor()

        params = self.splitParams(params)

        hpcode = self.getHistoricalPlace(connection, params[1])
        
        if hpcode != "":
            if (int(params[2]) == int(params[5]) + int(params[6])):
                if (int(params[2]) == int(params[4]) + int(params[7])):
                    data = (params[3], hpcode[0], params[4], params[5], params[6], params[7])
                    cursor.execute('INSERT INTO visitor VALUES(?,?,?,?,?,?)', data)
                    connection.commit()
                    
                    return True
        return False

    #Retrives the maximum visitor of the historical places
    #(Option A)
    def getMaxVisitorOfHistoricalPlace(self, connection):
        cursor = connection.cursor()

        cursor.execute('SELECT historical_place.hpname, '+
                       'MAX(visitor.numberofMaleVisitor + visitor.numberofFemaleVisitor) '+
                       'FROM visitor, historical_place WHERE visitor.hpcode = historical_place.hpcode ' +
                       'GROUP BY historical_place.hpcode')
        result = cursor.fetchall()
        
        if (result != None):
            return result
        return ""
    
    #Retrives the Maximum visitor of the cities
    #(Option B)
    def getMaxVisitorOfCity(self, connection):
        cursor = connection.cursor()

        cursor.execute('SELECT city.cityname, ' +
                       'MAX(visitor.numberofMaleVisitor + visitor.numberofFemaleVisitor)' +
                       'FROM visitor, historical_place, city WHERE visitor.hpcode = historical_place.hpcode ' +
                       'AND city.citycode = historical_place.citycode GROUP BY city.cityname')
        result = cursor.fetchall()

        return result

    #Retrives total visitor of the cities
    #(Option C)
    def totalVisitorOfCities(self, connection):
        cursor = connection.cursor()

        cursor.execute('SELECT city.cityname, SUM(visitor.numberofMaleVisitor + visitor.numberofFemaleVisitor) as "Total Visitors", '
                       'SUM(numberofMaleVisitor), SUM(numberofFemaleVisitor), ' +
                       'SUM(visitor.numberofLocalVisitor), SUM(visitor.numberofTourists) ' +
                       'FROM historical_place, visitor, city WHERE visitor.hpcode = historical_place.hpcode ' +
                       'AND city.citycode = historical_place.citycode GROUP BY city.cityname')
        result = cursor.fetchall()

        return result

    #Retrives the city code according to city name 
    def getCity(self, connection, cityName):
        cursor = connection.cursor()
        cursor.execute('SELECT citycode FROM city WHERE cityname=?', (cityName, ))
        result = cursor.fetchone()
        
        if (result != None):
            return result
        return ""
    
    #Retrives data according to city code (Option D)
    def totalVisitorOfGivenCity(self, connection, params):
        cursor = connection.cursor()
        data = self.splitParams(params)
        citycode = self.getCity(connection, data[1])

        if citycode != "":
            cursor.execute('SELECT historical_place.hpname, SUM(numberofMaleVisitor + numberofFemaleVisitor) as "Total Visitors", ' +
                           'SUM(numberofMaleVisitor), SUM(numberofFemaleVisitor), '
                           'SUM(numberofLocalVisitor), SUM(numberofTourists) ' +
                           'FROM historical_place, visitor ' +
                           'WHERE visitor.hpcode = historical_place.hpcode ' +
                           'AND historical_place.citycode=? GROUP BY visitor.hpcode', citycode)
            result = cursor.fetchall()
            if len(result) > 0:
                return result
            return ""
        else:
            return ""

    #Retrives data according to given date and historical place name
    #(Option E)
    def totalVisitorOfGivenHp(self, connection, params):
        cursor = connection.cursor()
        param = self.splitParams(params)
        param[1] = self.splitHp(param[1])
       
        data = (param[1], param[2])
        cursor.execute('SELECT historical_place.hpName, SUM(visitor.numberofMaleVisitor + visitor.numberofFemaleVisitor) as "Total Visitors", ' +
                        'visitor.numberofMaleVisitor, visitor.numberofFemaleVisitor, '
                        'visitor.numberofLocalVisitor, visitor.numberofTourists ' +
                        'FROM historical_place, visitor WHERE visitor.hpcode = historical_place.hpcode ' +
                        'AND historical_place.hpName=? AND visitor.date=?', data)
        result = cursor.fetchone()
        
        if None not in result:
            return result
        return ""

    #Splits the coming parameters according to space delimeter
    def splitParams(self, params):
        paramList = params.split()
        return paramList
    
    #Replace dash with space on Historical Place Name 
    def splitHp(self, params):
        hp = params.replace("-", " ")
        return hp