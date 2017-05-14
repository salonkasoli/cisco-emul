import re,os

HELLO_CHAR = '$ '


ROUTE = "route"
SUDO = "sudo "
IFCONFIG = "ifconfig"
IF_ROUTING = "sudo sysctl -w net.ipv4.ip_forward=1"


SHOW_INTERFACE = re.compile('( )*show( )+interface( )+(.)+( )*[0-9]*')
ADD_ROUTE = re.compile('ip( )+route( )+' + IP_REGEX + '( )+' + IP_REGEX + '( )+' +  IP_REGEX + '( )*')
IP_REGEX = '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'


def print_error(cmd):
    print 'wrong number of arguments! see "man ' + cmd[0] + '"\n';










#########################################################################
# SHOW COMMANDS
#########################################################################

def show_interfaces(cmd):
    if len(cmd) == 2:
        os.system(IFCONFIG)
    else:
        print_error(cmd)
        
        
def show_ip_route(cmd):
    if len(cmd) == 3:
        os.system(ROUTE + ' -n')
    else:
        print_error(cmd)
    
def show_ip(cmd):
    if len(cmd) == 2:
        print_error(cmd)
    else:
        if cmd[2] == 'route':
            show_ip_route(cmd)
        else:
            print_error(cmd)
            
def show_interface(cmd):
    if len(cmd) == 2:
        print_error(cmd)
    else:
        show_interface_iname(cmd)

def show_interface_iname(cmd):
    if len(cmd) == 3:
        execute = IFCONFIG
        execute += ' ' + cmd[2]
        os.system(execute)
    else:
        show_interface_iname_num(cmd)
        
def show_interface_iname_num(cmd):
    if len(cmd) == 4:
        execute = IFCONFIG
        execute += ' ' + cmd[2]
        execute += ':' + cmd[3]
        os.system(execute)
    else:
        print_error(cmd)


def show(cmd):
    if len(cmd) == 1:
        print_error(cmd)
    else:
        if cmd[1] == 'interfaces':
            show_interfaces(cmd)
        elif cmd[1] == 'ip':
            show_ip(cmd)
        elif cmd[1] == 'interface':
            show_interface(cmd)
        else:
            print_error(cmd)
            


#########################################################################
# IP COMMANDS
#########################################################################
        
        
def ip(cmd):
    if len(cmd) == 1:
        print_error(cmd)
    else:
        if cmd[1] == 'route':
            ip_route(cmd)
        elif cmd[1] == 'routing':
            ip_routing(cmd)
        elif cmd[1] == 'name':
            ip_name(cmd)
        else:
            print_error(cmd)
    
        
def ip_route(cmd):
    if len(cmd) == 2:
        print_error(cmd)
    else:
        ip_route_prefix(cmd)
        
def ip_route_prefix(cmd):
    if len(cmd) == 3:
        print_error(cmd)
    else:
        ip_route_prefix_mask(cmd)

def ip_route_prefix_mask(cmd):
    if len(cmd) == 4:
        print_error(cmd)
    else:
        ip_route_prefix_mask_ip(cmd)
        
def ip_route_prefix_mask_ip(cmd):
    if len(cmd) == 5:
        execute = SUDO + ROUTE
        execute += " add"
        execute += " -net " + cmd[2]
        execute += " netmask " + cmd[3]
        execute += " gw " + cmd[4]
        os.system(execute)
    else:
        print_error(cmd)
        
def ip_routing(cmd):
    if len(cmd) == 2:
        os.system(IP_ROUTING)
    else:
        print_error(cmd)

def ip_name(cmd):
    if len(cmd) == 2:
        print_error(cmd)
    else:
        ip_name_addr(cmd)

def ip_name_addr(cmd):
    if len(cmd) == 3:
        #TODO
    else:
        ip_name_addr_addr2(cmd)
        
def ip_name_addr_addr2(cmd):
    if len(cmd) == 4:
        #TODO
    else:
        print_error(cmd)
        


#########################################################################
# INTERFACE MANAGER COMMANDS
#########################################################################



iface_error(cmd):
    print 'meh\n'


def interface(cmd):
    if len(cmd) == 1:
        print_error(cmd)
    else:
        interface_iname(cmd)
        
def interface_iname(cmd):
    if len(cmd) == 2:
        manage_interface(cmd[1])
    else:
        interface_iname_num(cmd)


def interface_iname_num:
    if len(cmd) == 3:
        manage_interface(cmd[1] + ':' + cmd[2])
    else:
        print_error(cmd)
        

def manage_interface(iface):
    cmd = raw_input('manage ' + cmd[1] + ' : ')
    if len(cmd) > 0:
        analyze_iface(iface, cmd)
    else:
        manage_interface(iface)
        
        
def analyze_iface(iface, cmd):
    if cmd[0] == 'ip':
        iface_ip(iface, cmd)
    elif cmd[0] == 'no':
        iface_no(iface,cmd)
    elif cmd[0] == 'shutdown'
        iface_shutdown(iface, cmd)
    else:
        iface_error(cmd)

def iface_ip(iface, cmd):
    if len(cmd) == 1:
        iface_error(cmd)
    else:
        if cmd[1] == 'address':
            iface_ip_address(iface, cmd)
        else:
            iface_error(cmd)


def iface_ip_address(iface, cmd):
    if len(cmd) == 2:
        iface_error(cmd)
    else:
        iface_ip_address_ip(iface, cmd)

def iface_ip_address_ip(iface, cmd):
    if len(cmd) == 3:
        iface_error(cmd)
    else:
        iface_ip_address_ip_mask(iface, cmd)
        
        
def iface_ip_address_ip_mask(iface, cmd):
    if len(cmd) == 4:
        execute = SUDO + IFCONFIG
        execute += " " + iface
        execute += " " + cmd[2]
        execute += " " + cmd[3]
        os.system(execute)
    else:
        iface_error(cmd)
                
        
###########################
#TODO NO IP ADDRESS


def iface_no(iface,cmd):
    if len(cmd) == 1:
        iface_error(cmd)
    else:
        if cmd[1] == 'shutdown':
            iface_no_shutdonw(iface, cmd)
        elif cmd[1] == 'ip':
            iface_no_ip(iface,cmd)
        else:
            iface_error(cmd)

def iface_no_shutdown(iface, cmd):
    if len(cmd) == 2:
        execute = SUDO + IFCONFIG
        execute += " " + iface
        execute += " up"
        os.system(execute)
    else:
        iface_error(cmd)


def iface_shutdown(iface, cmd):
    if len(cmd) == 1:
        execute = SUDO + IFCONFIG
        execute += " " + iface
        execute += " down"
        os.system(execute)
    else:
        iface_error(cmd)
    


            




    


def analyze(cmd):
    if cmd[0] == 'show'
        show(cmd)
    elif cmd[0] == 'ip'
        ip(cmd)
    elif cmd[0] == 'interface'
        interface(cmd)
        



def request_another():
    command = raw_input(HELLO_CHAR)
    cmd = command.split()
    if len(cmd) > 0 :
        analyze(cmd)
    request_another():



print "Welcome to CISCO cmd"
request_another()
