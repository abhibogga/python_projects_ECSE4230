def dateTimeFunction(compare): 
    global timeStart
    global programStart
    global queue
    global wordQueue
    global wordQueueCounter
    global bCounter
    global loadValue
    global loadWord
    now = datetime.now()
    now = str(now)
    
    if bCounter == 3:
        print("hit 3")
        loadZero(CLK1)
        loadZero(CLK2)
        loadZero(CLK3)
        loadZero(CLK4)
        bCounter = 0
        queue = [0,0,0,0]
        wordQueue = [0,0,0,0]
        wordQueueCounter = 0
        loadValue = False
        loadWord = True
        return
    
    #If we need to compare: 
    if compare: 
        cmp = [char for char in str(now)]
        cmp = cmp[11:16:1]
    

        #Now lets compare values: 
    
        if cmp != timeStart or programStart:
            bCounter = 0
            #this is what updates the thing 
            fourStageLoad(now, queue, True)
            timeStart = cmp
            programStart = False
    else: 
        #UPdates the clocks
        fourStageLoad(now, queue, True)





def dateTimeFunction(compare): 
    global timeStart
    global programStart
    global queue
    global wordQueue
    global wordQueueCounter
    global bCounter
    global loadValue
    global loadWord
    now = datetime.now()
    now = str(now)
    

    while True: 
        counter+=1
        readKeypad(rows[counter%4], hash[counter%4], False, False)
        
        if bCounter == 3:
            print("hit 3")
            loadZero(CLK1)
            loadZero(CLK2)
            loadZero(CLK3)
            loadZero(CLK4)
            bCounter = 0
            queue = [0,0,0,0]
            wordQueue = [0,0,0,0]
            wordQueueCounter = 0
            loadValue = False
            loadWord = True
            break 
        
        #If we need to compare: 
        if compare: 
            cmp = [char for char in str(now)]
            cmp = cmp[11:16:1]
        

            #Now lets compare values: 
        
            if cmp != timeStart or programStart:
                bCounter = 0
                #this is what updates the thing 
                fourStageLoad(now, queue, True)
                timeStart = cmp
                programStart = False
        else: 
            #UPdates the clocks
            fourStageLoad(now, queue, True) 
    print("done")