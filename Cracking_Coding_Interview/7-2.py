class Call:
    rank = 0
    def reply(self,message):
        pass
    def disconnect(self):
        pass

class CallHandler:
    levels = 3
    num_fresher = 5
    employeeLevels = list(list(Employee))
    callQueues = [[]]*levels
    def __init__(self):
        pass
    def getCallHandler(self,call):
        for rank in range(call.rank,levels-1):
            for employee in employeeLevels[rank]:
                if employee.free:
                    return employee
        return None
    def dispatchCall(self,call):
        emp = self.getCallHandler(call)
        if emp:
            emp.ReceiveCall(call)
        else:
            self.callQueue[call.rank].append(call)
    def getNextCall(emp):
        pass

class Employee:
    def __init__(self,rank):
        self.rank=rank
    def ReceiveCall(self,call):
        pass
    def CallHandled(self,call):
        pass
    def CannotHandle(self,call,callHandler):
        call.rank=self.rank+1
        callHandler.dispatchCall(call)
        self.free=True
        callHandler.getNextCall(self)

class Fresher(Employee):
    def __init__(self):
        Employee.__init__(self,0)

class TechLead(Employee):
    def __init__(self):
        Employee.__init__(self,1)

class ProductManager(Employee):
    def __init__(self):
        EMpoyee.__init__(self,2)
