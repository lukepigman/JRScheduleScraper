
def chopString(input):
    thestr = input
    if(thestr[0] == "R"):
         that = thestr.lstrip("R - ")
         if("(" not in thestr):
             return thestr
         this = that.index("(")
         final = that[:this]
         return final
    else:
        return thestr

   


