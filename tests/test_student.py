from school_schedule.student import Student

#len of courses changes after we add class
def test_len_of_course_adds_one_after_adding_class():
    #arrange
    course = "basket weaving"
    raha = Student(
                "Raha", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ]
            )

    #act
    result = raha.add_class(course)

    #assert
    assert raha.get_num_classes() == 7
    assert result[-1] == "basket weaving"
    assert "basket weaving" in raha.courses  



#add class adds a valid class to list
def test_add_empty_class_returns_no_change():
    #arrange
    course = ""
    raha = Student(
                "Raha", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ]
            )

    result = raha.add_class(course)

    assert raha.get_num_classes() == 6

#testing that courses actually added


#does each instance have the attributes its suppose to


#valid input types


#what happens if the list of classes is empty


#being added to the correct student?


#summary returns what its suppose to


#if added a class that already exists


#if no school name is given it is ada


#case sensitivity


#Attributes of class do not change
