import networkx as nx
print('nodes,n,m,diameter,average shortest path length,ratio')
for n in range(1,10):
	for m in range(1,10):
		kn = nx.complete_graph(n)
		kn.add_edge('H1',0)
		kn.add_edge('T1',n-1)
		for tail_length in range(2,m+1):
			kn.add_edge('H'+str(tail_length),'H'+str(tail_length-1))
			kn.add_edge('T'+str(tail_length),'T'+str(tail_length-1))
		diameter=nx.diameter(kn)
		avg_path_length=nx.average_shortest_path_length(kn)
		ratio=diameter/avg_path_length
		if(ratio>=3.0):
			print(str(n+2*m)+","+str(n)+","+str(m)+","+str(diameter)+","+str(avg_path_length)+","+str(ratio))
			nx.write_graphml(kn,'/home/arif/iit/assignments/SNA/1a.graphml')
			exit()