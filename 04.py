aiMark = 'O'
humanMark = 'X'

def printBoard(curr_state):
  for i in range(3):
    for j in range(3):
      index = i * 3 + j
      print(curr_state[index], end=" ")
    print()
  print()
      

def getAllEmptyCellIndex(curr_state):
    empty_cell_array = []
    for cell in curr_state:
        if (cell != 'X' and cell!= 'O' ):
            empty_cell_array.append(cell)

    return empty_cell_array

def checkWinnerFound(curr_state, curr_mark):
    if (  

      (curr_state[0] == curr_mark and
        curr_state[1] == curr_mark and
        curr_state[2] == curr_mark) or

      (curr_state[3] == curr_mark and
        curr_state[4] == curr_mark and
        curr_state[5] == curr_mark) or

      (curr_state[6] == curr_mark and
        curr_state[7] == curr_mark and
        curr_state[8] == curr_mark) or

      (curr_state[0] == curr_mark and
        curr_state[3] == curr_mark and
        curr_state[6] == curr_mark) or

      (curr_state[1] == curr_mark and
        curr_state[4] == curr_mark and
        curr_state[7] == curr_mark) or

      (curr_state[2] == curr_mark and
        curr_state[5] == curr_mark and
        curr_state[8] == curr_mark) or

      (curr_state[0] == curr_mark and
        curr_state[4] == curr_mark and
        curr_state[8] == curr_mark) or

      (curr_state[2] == curr_mark and
        curr_state[4] == curr_mark and
        curr_state[6] == curr_mark)
        ):
        return True
    
    else: 
      return False

def minimax(curr_state,curr_mark):
    available_cell_index = getAllEmptyCellIndex(curr_state)

    if(checkWinnerFound(curr_state,humanMark)):
        return {"score":-1}
    
    elif(checkWinnerFound(curr_state,aiMark)):
        return {"score": 1}
    
    elif ( len(available_cell_index)== 0):
        return {"score":0}
    

    all_tests_info = []

    for i in range(0,len(available_cell_index)):
      curr_test_info = {}
      curr_test_info["index"] = curr_state[available_cell_index[i]]
      curr_state[available_cell_index[i]] = curr_mark

      if ( curr_mark == aiMark):
          result = minimax(curr_state,humanMark)
          if result["score"] == -1:
            curr_test_info["score"] = result["score"]  - 1
          elif result["score"] == 1:
            curr_test_info["score"] = result["score"]  + 1 
          else:
            curr_test_info["score"] = result["score"]   

      else:
          result = minimax(curr_state,aiMark)
          if result["score"] == -1:
            curr_test_info["score"] = result["score"]  - 1
          elif result["score"] == 1:
            curr_test_info["score"] = result["score"]  + 1 
          else:
            curr_test_info["score"] = result["score"] 

      curr_state[available_cell_index[i]] = curr_test_info["index"]
      all_tests_info.append(curr_test_info)

    best_test_play = None
    if ( curr_mark == aiMark):
      best_score = float('-inf')
      for i in range(0,len(all_tests_info)):
        if (all_tests_info[i]["score"] > best_score):
          best_score = all_tests_info[i]["score"]
          best_test_play = i
    else:
      best_score = float('inf')
      for i in range(0,len(all_tests_info)):
         if (all_tests_info[i]["score"] < best_score):
            best_score = all_tests_info[i]["score"]
            best_test_play = i

    return all_tests_info[best_test_play]

start_board_state =[0, 1, 2, 3, 4, 5, 6, 7, 8]

# 1 for AI  0 for human
first_move = input("Who do you want to go first (0)AI or (1)You: ")
printBoard(start_board_state)

while len(getAllEmptyCellIndex(start_board_state))!= 0:
   
  if ( first_move == 0):
    best_play_info = minimax(start_board_state,aiMark)
    index_to_play = best_play_info["index"]
    start_board_state[index_to_play] = aiMark
    printBoard(start_board_state)

    if(checkWinnerFound(start_board_state,aiMark)):
      print("Sorry AI won again!!")
      break

  
  first_move = 0
  human_input = int(input("Enter the Value of empty index tile to play your move: "))
  start_board_state[human_input] = humanMark

  if(checkWinnerFound(start_board_state,humanMark)):
    print("Yay you win!!")
    break
   
print("\nThe Game Ended in a Tie!")
