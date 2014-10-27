#!/usr/bin/env python
"""Remote Console"""
import sys
import socket
try:
    import readline
except:
    pass

PACKING_STRING = '\xFF\xFF\xFF\xFF'
BUFFER_SIZE = 10240
SOCKET_TIMEOUT = 4

def usage():
    print 'Quake Remote Console (part of AGRIP AudioQuake)'
    print 'Usage:', sys.argv[0], '[host [port]]'
    print '   or:', sys.argv[0], '--ask'


def _log_command():
    return _command_core('log\n')  # leaving out the \n or having \x00 works too


def _command(command, password):
    return _command_core('rcon ' + password + ' ' + command + '\x00')


def _command_core(processed):
    return PACKING_STRING + processed


def _filter_response(received):
    if received.startswith(PACKING_STRING):
        return received[5:].rstrip()  # an 'n' follows the padding
    else:
        return received.rstrip()


if __name__ == '__main__':
    if len(sys.argv) is 2 and sys.argv[1] == '--ask':
        # Ask user for host and port (used when run from launcher)
        host = raw_input('Server hostname or IP [default: localhost]: ') \
            or 'localhost'
        port = raw_input('Server port [default: 27500]: ') or '27500'
        port = int(port)
    else:
        # Standard command-line use
        if len(sys.argv) < 2:
            usage()
        elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
            usage()
            sys.exit(0)
        host = sys.argv[1] if len(sys.argv) > 1 else 'localhost'
        port = int(sys.argv[2]) if len(sys.argv) > 2 else 27500
    print 'Will connect to:', host, port
    address = (host, port)

    # Ask for password
    password = raw_input('Server rcon password [default: rconpasswd]: ') \
            or 'rconpasswd'

    # Create and bind to socket (but we are not really connecting yet)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(SOCKET_TIMEOUT)
    except Exception, e:
        print 'There was an error making the socket:', str(e)
        sys.exit(1)

    # Main loop
    print "Ready to talk: 'quit' shuts down the server; 'exit' leaves rcon."
    while True:
        try:
            user_input = raw_input('] ')
            if not user_input:
                continue
            elif user_input == 'exit':
                print 'Leaving rcon...'
                break
            elif user_input == 'log':
                sock.sendto(_log_command(), address)
            else:
                sock.sendto(_command(user_input, password), address)

            if user_input == 'quit':
                print 'Sent server shutdown command; leaving rcon...'
                break
            else:
                response = _filter_response(sock.recv(BUFFER_SIZE))
                if response:
                    print response
        except socket.timeout:
            print 'Socket timed out; maybe the server is down?'
        except KeyboardInterrupt:
            print 'Keyboard interrupt; leaving rcon.'
            break
        except Exception, e:
            print 'There was an unanticipated error:', str(e)
            sys.exit(1)

    sock.close()
