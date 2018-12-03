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

Function genRndWord()

    

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
        ws.Rnage("D" & i).Value = genRndWord()
    Next i

End Sub



Sub test()
    Dim A As Long
    
    A = rndNum(65, 90)
    Debug.Print A
    
    Debug.Print A & " :" & Chr(A)
    
    

End Sub
