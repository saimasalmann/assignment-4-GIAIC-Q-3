MAX_TERM_VALUE : int = 10000

def main():
    print()
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term ,end='   ')
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next
    print()  # Print a newline at the end of the output


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()