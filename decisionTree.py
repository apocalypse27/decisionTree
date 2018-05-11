# -*- coding: utf-8 -*-

class node:
        def __init__(self,data,branchName,parentNode=None,isLeaf=False,height=0):
            self.left=None;
            self.right=None;
            self.height=height;
            self.data=data;
            self.dataframe=None;
            self.numLabel=0;
            self.parentNode=parentNode;
            self.isLeaf=isLeaf;            
            self.branchName=branchName;
            
class decisionTree:
    
    def __init__(self,feature):
        rootNode=node(feature,None,None);
        self.root=rootNode;
        self.numOfNonLeafNodes=0;
    
    def addNonLeafNode(self,parentNode,childData,bName,df):
        if(self.hasLeftChild(parentNode)):
            newNode=self.addRightChild(parentNode,childData,bName);
        else:
            newNode=self.addLeftChild(parentNode,childData,bName);
        newNode.dataframe=df;
        self.numOfNonLeafNodes=self.numOfNonLeafNodes+1;
        return newNode;
        
        
    def hasLeftChild(self,n):
        if(n.left!=None):
            return True;
        else:
            return False;
        
    def addLeafNode(self,parentNode,branchName,leafLabel):
        if(self.hasLeftChild(parentNode)):
            newLeafNode=self.addRightChild(parentNode,leafLabel,branchName);
        else:
            newLeafNode=self.addLeftChild(parentNode,leafLabel,branchName);
        newLeafNode.isLeaf=True;
        return(newLeafNode);
        
    # A function to do inorder tree traversal
    def printInorder(self,root):
        if root:           
            for item in range(0,root.height):
                print("|  ", end=" ")
            if(root.parentNode is not None):
                print(root.parentNode.data,"=",root.branchName,":",end=" ");
            if(root.isLeaf is True):
                print(root.data);
            else:
                print("");
            self.printInorder(root.left)
            self.printInorder(root.right);
           
           
           
    def __findNumberedNode(self,num,node):
        if(node!=None):
            if(node.numLabel==num):
                return node;  
            else:
                foundNode=self.__findNumberedNode(num,node.left);
                if(foundNode==None):
                    foundNode=self.__findNumberedNode(num,node.right);
                return foundNode;
        
    def addLeftChild(self,parentNode,childData,bName):
        newNode=node(childData,bName,parentNode);
        newNode.height=parentNode.height+1;
        parentNode.left=newNode;
        return newNode;
        
    def addRightChild(self,parentNode,childData,bName):
       newNode=node(childData,bName,parentNode);
       newNode.height=parentNode.height+1;
       parentNode.right=newNode;
       return newNode;
   
    def replaceSubtreeWithLeaf(self,n,fileObj):
        node=self.__findNumberedNode(n,self.root);
        if(node == self.root):
            node.left=None;
            node.right=None;
            node.isLeaf=True;
            return;
        majorityCount=0;
        #find the majority of target class
        for classVal in fileObj.uniqueValDictionary[fileObj.targetFeature]:
            df=node.dataframe.loc[node.dataframe[fileObj.targetFeature]==classVal];
            if(df.shape[0]>majorityCount):
                majorityCount=df.shape[0];
                majorityClassVal=classVal;       
        #Create a leafnode with data as the majorityClassVal
        newLeafNode=self.addLeafNode(node.parentNode,node.branchName,majorityClassVal);
        #replace the current node with the new leafNode created
        if(node.parentNode.left==node):
            node.parentNode.left=newLeafNode;
        else:
            node.parentNode.right=newLeafNode;
        return;
   
    def copyTree(self):
        newTree=decisionTree(self.root.data);
        newTree.root=self.__copyTree(self.root);
        return newTree;
        
        
    def __copyTree(self,oldNode):
        if(oldNode!=None):
            newNode=node(oldNode.data,oldNode.branchName,None,oldNode.isLeaf,oldNode.height);            
            newNode.left=self.__copyTree(oldNode.left);
            newNode.right=self.__copyTree(oldNode.right); 
            newNode.dataframe=oldNode.dataframe;
            if(newNode.isLeaf==False):
                newNode.left.parentNode=newNode;
                newNode.right.parentNode=newNode;
            return newNode;
        else:
            return None;
        
        
    def numberNodesOfTree(self):
        n=(self.__numberNodesPrivate(self.root,0));
        #print("num of nodes",n)
        return n;
    
    def __numberNodesPrivate(self,node,num):
        if(node!=None):
            if(node.isLeaf==False):
                newNum=num;
                if(node.left!=None):
                    newNum=self.__numberNodesPrivate(node.left,num);
                if(node.right!=None):
                    newNum=self.__numberNodesPrivate(node.right,newNum);
                if(newNum>num):
                    newNum=newNum+1;
                else:
                    newNum=num+1;
                node.numLabel=newNum;
                return newNum;
            else:
                return(num);
            
                
    def validate(self,validatingDataObj):
        df=validatingDataObj.masterCopy;
        #print("masterCopy of vSet",df);
        total=df.shape[0];
        correct=0;
        for index,row in df.iterrows():
            retValue=self.validateRow(row,self.root);
            if(retValue==True):
                correct=correct+1;        
        return((correct/total)*100);
        
        
        
    def validateRow(self,row,node):
        if(node.isLeaf):
            if(node.data==row[-1]):
                return True;
            else:
                return False;   
        nextVal=row.loc[node.data];
        if(nextVal==node.left.branchName):
            return(self.validateRow(row,node.left));
        else:
            return(self.validateRow(row,node.right));
        
            
            
        
        
        
        
        
        
        
        
        
