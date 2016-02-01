import networkx as nx

def get_avg_path_length_formula(m,n):
	return (((n*(n-1))/2)+(((m*(m+1)*(m+2))/3)+((n-1)*m*(m+3)))+(m*m*(m+2)))/((((n+(2*m))*(n+(2*m)-1))/2));

def get_avg_path_length_nx(m,n):
	#Constructs graph like:   (H4)--(H3)--(H2)--(H1)--(Kn)--(T1)--(T2)--(T3)--(T4)
	kn = nx.complete_graph(n)
	kn.add_edge('H1',0)
	kn.add_edge('T1',n-1)
	for tail_index in range(2,m+1):
		kn.add_edge('H'+str(tail_index),'H'+str(tail_index-1))
		kn.add_edge('T'+str(tail_index),'T'+str(tail_index-1))
	return nx.average_shortest_path_length(kn)


for n in range(3,50):
	for m in range(1,50):
		nx_avg_path_length=get_avg_path_length_nx(m,n)
		derived_avg_path_length=get_avg_path_length_formula(m,n)
		assert(nx_avg_path_length==derived_avg_path_length),'Failed for n='+str(n)+' m='+str(m)