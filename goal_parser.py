def goal_parser(command):
    command = command.replace('()', 'o')
    command = command.replace('(al)', 'al')
    return command 
