def main():
    command = 'Hello, World'
    match command:
        case 'Hello, World':
            print('Hello, World')
        case 'Goodbye, World':
            print('Goodbye, World')
        case other:
            print('No natch found')

main()