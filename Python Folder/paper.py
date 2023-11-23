
class bp():
    def __init__(self,size):
        self.size=size#folds on one side
        self.num_corners= (size+1)**2
        self.folds={}
        for i in range(self.size+1):#add edges of the paper in at this step
            for j in range(self.size+1):
                self.folds[(i*4)+j]={}

        
    def update_fold(self,node_1,node_2,type):#no input sanitation
        self.folds[node_1][node_2]=type
        self.folds[node_2][node_1]=type

    def MJ_satisfied(self):# may be incorrect for edges
        for i in range(1,self.size-1):#no edge corners
            for j in range(1,self.size-1):
                node=(i*(self.size+1))+j
                mj_value=0
                for k in self.folds[node].values():
                    if k==1:
                        mj_value+=1
                    elif k==2:
                        mj_value-=1
                if not(mj_value==2 or mj_value==-2):
                    return False
        return True
    
    def KJ_satisfied(self):#edge corners need more consideration
        for i in range(1,self.size-1):
            for j in range(1,self.size-1):
                node=(i*(self.size+1))+j
                start=0
                rot=0
                for i in [-4,-3,1,5,4,3,-1,-5]:
                    if node+i in self.folds[node]:
                        
