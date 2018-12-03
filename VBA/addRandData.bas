Attribute VB_Name = "addRandData"
Function rndNum(lo As Long, hi As Long)

    rndNum = CLng((hi - lo + 1) * Rnd + lo)

End Function

Function rndBENum()

'####X
rndBENum = CStr(rndNum(0, 9) & rndNum(0, 9) & rndNum(0, 9) & rndNum(0, 9) & Chr(rndNum(65, 89)))

'####XX####
rndBENum = rndBENum + CStr(Chr(rndNum(65, 90)) & rndNum(0, 9) & rndNum(0, 9) & rndNum(0, 9) & rndNum(0, 9))


End Function

Sub addData()
    Dim ws As Worksheet
    
    Set ws = Sheets("Sheet1")
    
    For i = 2 To 20
        
        'generate a random date and time at some point in the past
        ws.Range("A" & i).Value = DateAdd("d", rndNum(0, 365) * -1, Now())
        ws.Range("B" & i).Value = Format(DateAdd("n", rndNum(0, 86400) * -1, Now()), "h:nn AM/PM")
        ws.Range("C" & i).Value = rndBENum()
        ws.Range("D" & i).Value = Hex(rndNum(20000000, 10010100))
        ws.Range("E" & i).Value = Hex(rndNum(20000000, 10010100)) & Hex(rndNum(20000000, 10010100))
        ws.Range("F" & i).Value = Hex(rndNum(20000000, 10010100)) & Hex(rndNum(20000000, 10010100))
        ws.Range("G" & i).Value = Hex(rndNum(20000000, 10010100)) & Hex(rndNum(20000000, 10010100))
    Next i

End Sub

Sub addToArray()
    Dim i As Long, ws As Worksheet, data() As Variant
    
    Set ws = Sheets("Sheet1")
    'find the number of columns
    Do
        colCount = colCount + 1
    Loop Until ws.Range("A1").Offset(0, colCount).Value = ""

    'find the number of rows
    RowsCount = ws.Range("A" & Rows.Count).End(xlUp).Row
    
    'put the data into an array
    data() = ws.Range(Cells(2, 1), Cells(RowsCount, colCount)).Value
    
    Call sortArray(data())
    'arraySwap data(), 1, 4
    
End Sub

Sub sortArray(data() As Variant)
    'Dim temp() As Variant
    Dim hiRight As New Collection
    Dim loLeft As New Collection
    
    'ReDim temp(1 To UBound(data), 1 To UBound(data, 2))
    
    pivot = data(1, 1)
    
    'split the data into two collections
    For i = 1 To UBound(data)
        
        If data(i, 1) >= pivot Then
            hiRight.Add i
        Else
            loLeft.Add i
        End If
        
    Next i
    
    'We know where the pivot should go becuase everything else was sorted around it
    'there are x in the lower half (left) collection so the pivot must be one after that
    arraySwap data(), 1, loLeft.Count + 1
    
    'Loop through the loLeft part and follow the same principle
    sIndex = 1
    Do Until loLeft.Count = 1
        sIndex = 1
        pivot = data(loLeft(1), 1)
        
        If data(loLeft(sIndex), 1) >= pivot Then
            
            arraySwap data(), sIndex, loLeft(1)
            loLeft.Remove (1)
        Else
            sIndex = sIndex + 1
            
        End If
        
    Loop
    
    'loop through the hiRight
    sIndex = 1
    Do Until hiRight.Count = 1
        sIndex = 1
        pivot = data(hiRight(1), 1)
        
        If data(hiRight(sIndex), 1) >= pivot Then
            
            arraySwap data(), sIndex, hiRight(1)
            hiRight.Remove (1)
        Else
            sIndex = sIndex + 1
            
        End If
        
        
    Loop
    
    Debug.Print data(1, 1)
    
End Sub

Function arraySwap(ByRef data() As Variant, index1, index2)
    Dim temp1() As Variant
    
    ReDim temp(1 To UBound(data), 1 To UBound(data, 2))
    
    For e = 1 To UBound(data, 2)
        temp(index1, e) = data(index2, e)
        temp(index2, e) = data(index1, e)
    Next e
    
    
    For i = 1 To UBound(data)
        If i = index1 Or i = index2 Then GoTo Skip
        
        For e = 1 To UBound(data, 2)
            temp(i, e) = data(i, e)
        Next e
        
Skip:
    Next i
    
    data() = temp()
    
arraySwap = True
    
End Function
