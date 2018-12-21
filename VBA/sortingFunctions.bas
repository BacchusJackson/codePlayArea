Attribute VB_Name = "sortingFunctions"
'Attribute VB_Name = "addRandData"
Sub quickSort1DArray(arr() As Variant)

    Dim stack() As Variant
    
    hi = UBound(arr)
    lo = LBound(arr)
    Top = 0
    
    ReDim stack(1 To UBound(arr))
    
    Top = Top + 1
    stack(Top) = lo
    Top = Top + 1
    stack(Top) = hi
    
    Do While Top >= 1
        
        'get subarray hi
        hi = stack(Top)
        Top = Top - 1
        'get subarray lo
        lo = stack(Top)
        Top = Top - 1
        
        pivot = partition(arr(), lo, hi)
        
        'If there are elements on the left side of pivot
        If pivot - 1 > lo Then
            'set sub array lo
            Top = Top + 1
            stack(Top) = lo
            
            'set sub array hi based on pivot - 1
            Top = Top + 1
            stack(Top) = pivot - 1
            
        End If
        
        'If there are elements on the right side of pivot
        If pivot + 1 < hi Then
            'set sub array lo
            Top = Top + 1
            stack(Top) = pivot + 1
            'set sub array hi
            Top = Top + 1
            stack(Top) = hi
        End If
    Loop

End Sub

Function partition(ByRef data() As Variant, lo, hi)
        
'---Partition Data---
    'find the value that you have to compare in the array. Should be right most in the array
    
    'Do do the compare if there is only one element
    If lo = hi Then
        partition = hi
        Exit Function
    End If
    rightMostCompareValue = data(hi)
    
    i = lo - 1
    'loop from low index to high index
    
    For j = lo To hi - 1
        If data(j) <= rightMostCompareValue Then
            i = i + 1
            If i <> j Then
                temp = data(i)
                data(i) = data(j)
                data(j) = temp
            End If
        End If
    Next j
    
    'swap i with the rightmost value to put the pivot in the right spot
    If data(i + 1) <> data(hi) Then
        temp = data(hi)
        data(hi) = data(i + 1)
        data(i + 1) = temp
    End If
    
    partition = i + 1
    
End Function

Sub quickSort2DArray(arr() As Variant, sortByColumn As Integer)
    Dim stack() As Variant
    
    'initialize variables
    hi = UBound(arr)
    lo = 1
    Top = 0
    
    ReDim stack(1 To UBound(arr))
    
    'set initial lo on stack
    Top = Top + 1
    stack(Top) = lo
    'set initial hi on stack
    Top = Top + 1
    stack(Top) = hi
    
    'iterate until Top hits zero
    Do While Top >= 1
        
        'get subarray hi
        hi = stack(Top)
        Top = Top - 1
        'get subarray lo
        lo = stack(Top)
        Top = Top - 1
        
        pivot = partition2(arr(), lo, hi, sortByColumn)
        
        'If there are elements on the left side of pivot
        If pivot - 1 > lo Then
            'set sub array lo
            Top = Top + 1
            stack(Top) = lo
            
            'set sub array hi based on pivot - 1
            Top = Top + 1
            stack(Top) = pivot - 1
            
        End If
        
        'If there are elements on the right side of pivot
        If pivot + 1 < hi Then
            'set sub array lo
            Top = Top + 1
            stack(Top) = pivot + 1
            'set sub array hi
            Top = Top + 1
            stack(Top) = hi
        End If
    Loop

End Sub

Function partition2(ByRef data() As Variant, lo, hi, sortByColumn)
    'find the value that you have to compare in the array. Should be right most in the array
    
    'Do do the compare if there is only one element
    If lo = hi Then
        partition2 = hi
        Exit Function
    End If
    rightMostCompareValue = data(hi, sortByColumn)
    
    i = lo - 1
    'loop from low index to high index
    
    For j = lo To hi - 1
        If data(j, sortByColumn) <= rightMostCompareValue Then
            i = i + 1
            If i <> j Then
                arraySwap data(), i, j
            End If
        End If
    Next j
    
    'swap i with the rightmost value to put the pivot in the right spot
    If data(i + 1, sortByColumn) <> data(hi, sortByColumn) Then
        
        'swap elements
        arraySwap data(), i + 1, j
    End If
    
    'return pivot point plus 1
    partition2 = i + 1
    
End Function

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
