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
    
    n = UBound(data)
    Call quickSort(data(), 1, n, 1)
    
    Debug.Print ("complete")
    'Call sortArray(data())
    'arraySwap data(), 1, 4
    
End Sub

Function dataPartition(ByRef data() As Variant, lo, hi, sortByCol)
    Dim i As Long
    
    i = lo - 1
    rightMostCompareValue = data(hi, sortByCol)
    
    For j = lo To hi
        If data(j, sortByCol) <= rightMostCompareValue Then
            i = i + 1
            If i <> j Then
                arraySwap data(), i, j
            End If
        End If
    Next j
    
    arraySwap data(), i, hi
    dataPartition = i + 1
    
End Function

Sub quickSort(ByRef data() As Variant, lo, hi, sortByCol)
    
    If lo < hi Then
        
        'take the higher values and put them on the right
        'take the lower values and put them on the left
        'figure out where that split is
        pivotPoint = dataPartition(data(), lo, hi, sortByCol)
        
        'call this function again with a new hi of -1 from the split to order the lower values
        Call quickSort(data(), lo, pivotPoint - 1, 1)
        'call this fucntion again with a new high of +1 from the split to order the other higher values
        Call quickSort(data(), pivotPoint + 1, hi, 1)
    End If

End Sub

Function arraySwap(ByRef data() As Variant, index1, index2)
    Dim temp1() As Variant
    
    'Don't want to waste compute time if the numbers are equal
    If index1 = index2 Then
        arraySwap = True
        Exit Function
    End If
    
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
