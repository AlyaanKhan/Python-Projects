def cricket_scoring_app():
    format_cric = input("Enter the format (T20, ODI, Test): ").strip().upper()
    if format_cric == 'T20':
        total_overs = 20
    elif format_cric == 'ODI':
        total_overs = 50
    elif format_cric == 'TEST':
        total_overs = 90 
    else:
        print("Invalid format!")
        return
    
    total_balls = total_overs * 6
    total_score = 0
    balls = 0
    
    while total_balls > 0:
        score = int(input("Enter the score for ball {}: ".format(balls + 1)))
        total_score += score
        balls += 1
        total_balls -= 1
        
        if balls % 6 == 0:
            over = balls // 6
            print("Score after over", over, "is:", total_score)
    
    print("Total score after the match is:", total_score)

cricket_scoring_app()
