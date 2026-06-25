# TechWorld, a technology training center, wants to allocate courses to instructors. 
# An instructor is described by their name, their technology skills,
#  their years of experience, and their average feedback score. 
# An instructor may only be given a course if BOTH of the following conditions are true:
# •	If their experience is more than 3 years, their average feedback must be 
# 4.5 or higher. If their experience is 3 years or less, their average feedback must be 4 or higher.
# •	They must already possess the technology skill that the course requires.
# Design a class to represent an instructor, and build it with these rules in mind:
# 1.	Keep every instance variable private, and make every method public.
# 2.	An instructor can know more than one technology, so technology_skill should be a list.
# 3.	check_eligibility() — returns True if the instructor meets the eligibility
#  rule above, otherwise False.
# 4.	allocate_course(technology) — returns True if the instructor can be given 
# a course that needs the given technology, otherwise False.
# 5.	Create a few instructor objects, set their details using setter methods, 
# and test that your methods work correctly.

class Instructor:
    def __init__(self):
        self.__name 
        self.__skills
        self.__experience
        self.__feedback

    def check_eligibility(self,experience,feedback):
        self.__feedback = feedback
        self.__experience = experience
        if self.__experience > 3 and self.__feedback >=4.5:
            print("the course can be given to the instructor!")
            return True
        elif self.__experience <=3 and self.__feedback >=4:
            if self.__skills == True :
                print("the instructor is eligible for the course !")
                return True
        else: 
            print("the instructor is not eligible for the course !")
            return False

    def allocate_course(self,technology):
        if self.check_eligibility is True:
            return True
        else: return False
    

    
