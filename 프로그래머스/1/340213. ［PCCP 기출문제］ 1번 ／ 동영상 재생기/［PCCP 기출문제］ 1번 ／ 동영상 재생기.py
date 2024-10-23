def solution(video_len, pos, op_start, op_end, commands):
    
    video_m, video_s = map(int, video_len.split(':'))
    video = 60 * video_m + video_s
    
    pos_m, pos_s = map(int, pos.split(':'))
    pos = pos_m * 60 + pos_s
    
    op_start_m, op_start_s = map(int, op_start.split(':'))
    op_start = op_start_m * 60 + op_start_s
    
    op_end_m, op_end_s = map(int, op_end.split(':'))
    op_end = op_end_m * 60 + op_end_s
    
    for command in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        if command == 'prev':
            pos -= 10
            if pos <= 0:
                pos = 0
            elif op_start <= pos <= op_end:
                pos = op_end
        if command == 'next':
            pos += 10
            if pos >= video:
                pos = video
            elif op_start <= pos <= op_end:
                pos = op_end
    
    answer = str(pos // 60).zfill(2)+':'+str(pos % 60).zfill(2)
    
    return answer