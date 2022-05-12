class ClassService:

    def AddClass(connection, classObj):
        """
        Create a new Class into the class table
        :param connection:
        :param classObj:
        :return: none
        """

        """
        try:
            sql = ''' INSERT INTO class(name,schoolId,teacherId)
              VALUES(?,?,?,?,?,?) '''
            cur = connection.cursor()
            cur.execute(sql, classObj)
            connection.commit()

        except Error as e:
            print(e) 

        finally:
        
        """
    
    def GetClass(connection, classId):
        pass

    def GetStudentsOfClass(connection, classId):
        pass

    
    