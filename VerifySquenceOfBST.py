def VerifySquenceOfBST(sequence):
    length = len(sequence)

    #空结点返回False
    #但是如果计算过程中遇到了空结点应该为True，这里加了两个判断保证计算时不会以空数组作为输入
    if not length: return False
    if length == 1: return True
    else:
        #根结点应为最后一个
        sep = sequence[-1]
        for i in range(length):
            #如果找到了和根结点值相等的结点
            # 当它不是根节点时说明此时二叉树中存在重复值，树的结构有问题
            # 是根节点，表示只有左子树，且此左子树保证了所有值小于根节点，故只验证左子树
            if sequence[i] == sep: 
                if i != length - 1: 
                    return False
                else:
                    return VerifySquenceOfBST(sequence[:i])
            if sequence[i] > sep:
                break
        
        #保证右子树中不存在小于根的结点
        for j in range(i,length-1):
            if sequence[j] <= sep:return False

        #如果首个结点就发现了比根结点大的结点，则只验证右子树，上面的循环，保证到这一步的右子树是合法的
        if i == 0:return VerifySquenceOfBST(sequence[0:-1])
        return VerifySquenceOfBST(sequence[:i]) and VerifySquenceOfBST(sequence[i:-1])


print(VerifySquenceOfBST([5,4,3,2,1]))
