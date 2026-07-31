from fastapi import FastAPI,Query

app=FastAPI()

@app.get('/items')
def getList(itemId:int=Query(0)):
    return {
        'itemId' : itemId
    }

@app.get('/items2')
def getList2(itemId:int=Query(...)):
    #必须传递
    return {
        'itemId' : itemId
    }

@app.get('/items3')
def getList3(itemId:int=Query(...,min_length=2,max_length=6)):
    #必须传递
    #最小长度为2
    #最大长度为6
    return {
        'itemId' : itemId
    }


@app.get('/items4')
def getList4(itemId:int=Query(...,gt=0,lt=5)):
    #必须传递
    #大于0小于5，同 0<X<5
    # 关键字	含义	                           运算符
    # gt	  大于 (Greater Than)	                >
    # ge	  大于等于 (Greater than or Equal to)	>=
    # lt	  小于 (Less Than)	                    <
    # le	  小于等于 (Less than or Equal to)	    <=
    return {
        'itemId' : itemId
    }

@app.get('/items5')
def getList5(itemId:int=Query(0, alais='id')):
    #别名，前端传id
    return {
        'itemId' : itemId
    }

@app.get('/items6')
def getList6(itemId:int=Query(0, description='这是一个参数描述')):
    return {
        'itemId' : itemId
    }

@app.get('/items7')
def getList7(itemId:int=Query(0, deprecated=True)):
    #其实也是一个描述，抛弃这个参数
    return {
        'itemId' : itemId
    }
    