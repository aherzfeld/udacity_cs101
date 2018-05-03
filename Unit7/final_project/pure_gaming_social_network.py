#code to create a simple social network for gamers


#raw data input
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

#creating the data structure

#data value input to get_name should start at space before name
def extract_name(data):
	end_name = data.find(' ')
	name = data[ : end_name]
	return name

#returns a list of connections
def extract_connections(data):
	start = data.find('connected to ') + 13
	end = data.find('.')
	raw_string = data[start : end]
	connections = raw_string.split(',')
	connections = [c.lstrip() for c in connections]# bug fix attempt
	return connections
	
#returns a list of games liked and and end location
def extract_games(data):
	start = data.find('to play ') + 8
	end = data.find('.', start)
	raw_string = data[start : end]
	games = raw_string.split(',')
	games = [g.lstrip() for g in games]
	return games, end

#takes an input string and returns a dictionary (network) containing names as keys
#with a list of connections and a list of games liked as values
def create_data_structure(data):
	network = {}	
	while True:
		name = extract_name(data)
		if name:
			connections = extract_connections(data)
			games, endpos = extract_games(data)
			network[name] = [connections, games]
			data = data[endpos +1 : ]
		else:
			break
	return network

#querying the data

def get_connections(network, user):
	return network[user][0]


def get_games_liked(network,user):
    return network[user][1]

def get_secondary_connections(network, user):
	secondary_connections = []
	if user in network:
		if network[user][0] == []:
			return []
		else:
			for e in network[user][0]:#for each of the users connections
				for e2 in network[e][0]:#for	each of the secondary connections
					if e2 not in secondary_connections:#checking for duplicates
						secondary_connections.append(e2)
			return secondary_connections
	else:
		return None	
	return []


def count_common_connections(network, user_A, user_B):
	if user_A in network and user_B in network:
		common_list = set(network[user_A][0]).intersection(network[user_B][0])
		return len(common_list)
	return False


def find_path_to_friend(network, user_A, user_B):
	if user_A in network and user_B in network:
		if user_B in network[user_A][0]:
			return [user_A] + [user_B]
		else:
			for e in network[user_A][0]:
				return [user_A] + find_path_to_friend(network, e, user_B)
	return None


#modifying the data

def add_connection(network, user_A, user_B):
	if user_A in network and user_B in network:
		if user_B not in network[user_A][0]:
			network[user_A][0].append(user_B)
	else:
		return False	
	return network


def add_new_user(network, user, games):
	if user not in network:
		network[user] = [[], games]
	return network
