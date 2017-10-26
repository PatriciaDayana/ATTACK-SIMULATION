#!/usr/bin/python

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.link import Link,TCLink,Intf
from mininet.log import setLogLevel

def main():
# net = Mininet(link=TCLink,controller='192.168.0.104')
 net = Mininet(controller=RemoteController, link=TCLink, switch=OVSKernelSwitch)
 h1 = net.addHost('h1', mac ="00:00:00:00:00:01")
 h2 = net.addHost('h2', mac ="00:00:00:00:00:02")
 h3 = net.addHost('h3', mac ="00:00:00:00:00:03")
 br1 = net.addSwitch('br1', protocols=["OpenFlow13"])
 c0 = net.addController( 'c0', controller=RemoteController, ip='192.168.56.104', port=6633 )
 net.addLink(h1,br1)
 net.addLink(h2,br1)
 net.addLink(h3,br1)
 
 net.build()
 c0.start()
 br1.start([c0])
 
 h1.cmd("ifconfig h1-eth0 0")
 h2.cmd("ifconfig h2-eth0 0")
 h3.cmd("ifconfig h3-eth0 0")
 
 br1.cmd("ifconfig br1-eth0 0")
 br1.cmd("ifconfig br1-eth1 0")
 br1.cmd("ifconfig br1-eth2 0")
 
 br1.cmd("brctl addbr mybr")
 br1.cmd("brctl addif mybr br1-eth0")
 br1.cmd("brctl addif mybr br1-eth1")
 br1.cmd("brctl addif mybr br1-eth2")
 
 br1.cmd("ifconfig mybr up")
 
 h1.cmd("ip address add 192.168.10.1/24 dev h1-eth0")
 h2.cmd("ip address add 192.168.10.2/24 dev h2-eth0")
 h3.cmd("ip address add 192.168.10.3/24 dev h3-eth0")
 
 CLI(net)
 net.stop()
 

if '__main__' == __name__:
 setLogLevel('info')
 main()
