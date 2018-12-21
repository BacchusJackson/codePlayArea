Attribute VB_Name = "stressTesting"
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
    Dim data() As Variant
    Set ws = Sheets("Sheet1")
    
    ReDim data(2 To 2000, 1 To 7)
    
    For i = 2 To UBound(data, 1)
        
        'generate a random date and time at some point in the past year
        data(i, 1) = DateAdd("d", rndNum(0, 365) * -1, Now())
        data(i, 2) = Format(DateAdd("n", rndNum(0, 86400) * -1, Now()), "h:nn AM/PM")
        data(i, 3) = rndBENum()
        data(i, 4) = Hex(rndNum(20000000, 10010100))
        data(i, 5) = Hex(rndNum(20000000, 10010100)) & Hex(rndNum(20000000, 10010100))
        data(i, 6) = Hex(rndNum(20000000, 10010100)) & Hex(rndNum(20000000, 10010100))
        data(i, 7) = Hex(rndNum(20000000, 10010100)) & Hex(rndNum(20000000, 10010100))
    Next i
    
    'paste array to sheet
    ws.Range(Cells(2, 1), Cells(UBound(data, 1), UBound(data, 2))).Value = data()
    
End Sub

Sub testDriveOnWorksheets2D()
    Dim i As Long, ws As Worksheet, data() As Variant
    
'    'start Timer
'    startTime = Timer
    
    Set ws = Sheets("Sheet1")
    'find the number of columns
    Do
        colCount = colCount + 1
    Loop Until ws.Range("A1").Offset(0, colCount).Value = ""

    'find the number of rows
    rowsCount = ws.Range("A" & Rows.Count).End(xlUp).Row
    
    'put the data into an array
    data() = ws.Range(Cells(2, 1), Cells(rowsCount, colCount)).Value
   
    'start Timer
    startTime = Timer
    
    'sort the data
    Call quickSort2DArray(data(), 1)
    
    endTime = Timer - startTime
    Debug.Print "Seconds Elapsed: " & endTime
    
    'Paste data
    'ws.Range(Cells(2, 9), Cells(rowsCount, colCount + 8)).Value = data()
    
'    'end Timer
'    endTime = Timer - startTime
'    Debug.Print "Seconds Elapsed: " & endTime
    
End Sub

Sub testDrive1D()
    Dim data() As Variant
    
    ReDim data(1 To 1000000)
    
    For i = 1 To UBound(data)
        
        data(i) = DateAdd("d", rndNum(0, 365) * -1, Now())
    
    Next i
    
    'start Timer
    startTime = Timer
    
    Call quickSort1DArray(data())
    
    'end Timer
    endTime = Timer - startTime
    Debug.Print "Seconds Elapsed: " & endTime

End Sub

Sub test()

    A = Timer
    
    Debug.Print A
    
    
    

End Sub
