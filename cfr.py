import random

tree = {
    'JQ': {
        'info_set': 'J',
        'p': {
            'info_set': 'Qp',
            'p': -1,
            'b': {
                'info_set': 'Jpb',
                'p': -1,
                'b': -2
            }
        },
        'b': {
            'info_set': 'Qb',
            'p': 1,
            'b': -2
        }
    },
'KQ': {
        'info_set': 'K',
        'p': {
            'info_set': 'Qp',
            'p': 1,
            'b': {
                'info_set': 'Kpb',
                'p': -1,
                'b': 2
            }
        },
        'b': {
            'info_set': 'Qb',
            'p': 1,
            'b': 2
        }
    },
'JK': {
        'info_set': 'J',
        'p': {
            'info_set': 'Kp',
            'p': -1,
            'b': {
                'info_set': 'Jpb',
                'p': -1,
                'b': -2
            }
        },
        'b': {
            'info_set': 'Kb',
            'p': 1,
            'b': -2
        }
    },
'QJ': {
        'info_set': 'Q',
        'p': {
            'info_set': 'Jp',
            'p': 1,
            'b': {
                'info_set': 'Qpb',
                'p': -1,
                'b': 2
            }
        },
        'b': {
            'info_set': 'Jb',
            'p': 1,
            'b': 2
        }
    },
'QK': {
        'info_set': 'Q',
        'p': {
            'info_set': 'Kp',
            'p': -1,
            'b': {
                'info_set': 'Qpb',
                'p': -1,
                'b': -2
            }
        },
        'b': {
            'info_set': 'Kb',
            'p': 1,
            'b': -2
        }
    },
'KJ': {
        'info_set': 'K',
        'p': {
            'info_set': 'Jp',
            'p': 1,
            'b': {
                'info_set': 'Kpb',
                'p': -1,
                'b': 2
            }
        },
        'b': {
            'info_set': 'Jb',
            'p': 1,
            'b': 2
        }
    }

}

cards = ['JQ','KQ','JK','QJ','QK','KJ']
info_sets = {'J':{'p':.5,'b':.5},'Qp':{'p':.5,'b':.5},'Qb':{'p':.5,'b':.5},'Jpb':{'p':.5,'b':.5},
             'K':{'p':.5,'b':.5},'Kpb':{'p':.5,'b':.5},'Q':{'p':.5,'b':.5},'Jp':{'p':.5,'b':.5},
             'Jb':{'p':.5,'b':.5},'Kp':{'p':.5,'b':.5},'Kb':{'p':.5,'b':.5},'Qpb':{'p':.5,'b':.5},
             'Kpb':{'p':.5,'b':.5},'Qbp':{'p':.5,'b':.5}
             }
strategy_sum = {'J':{'p':0,'b':0},'Qp':{'p':0,'b':0},'Qb':{'p':0,'b':0},'Jpb':{'p':0,'b':0},
             'K':{'p':0,'b':0},'Kpb':{'p':0,'b':0},'Q':{'p':0,'b':0},'Jp':{'p':0,'b':0},
             'Jb':{'p':0,'b':0},'Kp':{'p':0,'b':0},'Kb':{'p':0,'b':0},'Qpb':{'p':0,'b':0},
             'Kpb':{'p':0,'b':0},'Qbp':{'p':0,'b':0}
             }
reach_sum = {'J':{'p':0,'b':0},'Qp':{'p':0,'b':0},'Qb':{'p':0,'b':0},'Jpb':{'p':0,'b':0},
             'K':{'p':0,'b':0},'Kpb':{'p':0,'b':0},'Q':{'p':0,'b':0},'Jp':{'p':0,'b':0},
             'Jb':{'p':0,'b':0},'Kp':{'p':0,'b':0},'Kb':{'p':0,'b':0},'Qpb':{'p':0,'b':0},
             'Kpb':{'p':0,'b':0},'Qbp':{'p':0,'b':0}
             }

average_strategy = {'J':{'p':0,'b':0},'Qp':{'p':0,'b':0},'Qb':{'p':0,'b':0},'Jpb':{'p':0,'b':0},
             'K':{'p':0,'b':0},'Kpb':{'p':0,'b':0},'Q':{'p':0,'b':0},'Jp':{'p':0,'b':0},
             'Jb':{'p':0,'b':0},'Kp':{'p':0,'b':0},'Kb':{'p':0,'b':0},'Qpb':{'p':0,'b':0},
             'Kpb':{'p':0,'b':0},'Qbp':{'p':0,'b':0}}


actions = ['p','pp','pb','pbp','pbb','b','bp','bb']

regrets={'J':{'p':[],'b':[]},'Qp':{'p':[],'b':[]},'Qb':{'p':[],'b':[]},'Jpb':{'p':[],'b':[]}\
    ,'K':{'p':[],'b':[]},'Kpb':{'p':[],'b':[]},'Q':{'p':[],'b':[]},'Jp':{'p':[],'b':[]},'Jb':{'p':[],'b':[]}
         ,'Kp':{'p':[],'b':[]}, 'Kb':{'p':[],'b':[]},'Kpb':{'p':[],'b':[]},
         'Qpb':{'p':[],'b':[]}}


def node_value(node, value, counter_reach_prob):
    if type(node) == int:
        return value * node * counter_reach_prob
    else:
        return node_value(node['p'], value * info_sets[node['info_set']]['p'],counter_reach_prob) + \
               node_value(node['b'], value * info_sets[node['info_set']]['b'],counter_reach_prob)


def update_regret(action):
    if len(action) == 1:

        info_set = current_tree['info_set']
        ##print('info_set1',info_set)
        counter_reach_prob = 1
        #reach prob of each leaf * leaf value

        action_value = node_value(current_tree[action], 1, counter_reach_prob)
        base_value = node_value(current_tree, 1, counter_reach_prob)
        ##print('action_value', action_value)
        ##print('base_value',base_value)
        regret = action_value - base_value
        ##print('regret', regret)

        regrets[info_set][action].append(regret)
        return [info_set,counter_reach_prob]

    elif len(action) == 2:
        #current_tree[action[0]][action[1]]
        info_set = current_tree[action[0]]['info_set']
        #print('info_set2',info_set)
        opponent_info_set = current_tree['info_set']
        ##print('opponent_info_set',opponent_info_set)
        ###print(opponent_info_set)
        counter_reach_prob = info_sets[opponent_info_set][action[0]]
        #print('counter_reach_prob', counter_reach_prob)
        ##print('counter_reach_prob',counter_reach_prob)
        action_value = node_value(current_tree[action[0]][action[1]], 1, counter_reach_prob)*-1
        base_value = node_value(current_tree[action[0]], 1, counter_reach_prob)*-1
        # if action in ['pp','bp','bb']:
        #     ###print(action)
        #     action_value*=-1
        #     base_value*=-1
        ##print('action_value', action_value)
        ##print('base_value', base_value)
        regret = action_value - base_value
        ##print('regret',regret)

        regrets[info_set][action[1]].append(regret)
        return [info_set,counter_reach_prob]


    elif len(action) == 3:
        current_tree[action[0]][action[1]][action[2]]
        info_set = current_tree[action[0]][action[1]]['info_set']
        #print('info_set3',info_set)
        opponent_info_set = current_tree[action[0]]['info_set']
        ##print('opponent_info_set3',opponent_info_set)
        counter_reach_prob = info_sets[opponent_info_set][action[1]]
        #print('counter_reach_prob',counter_reach_prob)
        action_value = node_value(current_tree[action[0]][action[1]][action[2]], 1, counter_reach_prob)
        base_value = node_value(current_tree[action[0]][action[1]], 1, counter_reach_prob)
        ##print('action_value', action_value)
        ##print('base_value', base_value)
        regret = action_value - base_value
        ##print('regret', regret)

        regrets[info_set][action[2]].append(regret)
        return [info_set,counter_reach_prob]


for x in range(10000):

    ##print('_____________')
    random_num = random.randrange(0, 6, 1)
    current_tree = tree[cards[random_num]]
    random_num = random.randrange(0,8,1)
    act = actions[random_num]
    return_set = update_regret(act)
    i_set = return_set[0]
    reach_prob = return_set[1]
    ##print(regrets)
    ##print('i_set',i_set)
    ##print('action',act)
    #update strategy
    RT = 0
    for element in regrets[i_set][act[-1]]:
        RT += element
    if RT <=0:
        RT=0

    RT = RT/len(regrets[i_set][act[-1]])


    #get other regret

    if act[-1] == 'p':
        action_o = act[:-1]+'b'
    else:
        action_o = act[:-1]+'p'

    return_set = update_regret(action_o)
    i_set= return_set[0]
    reach_prob=return_set[1]
    ##print(regrets)
    ##print('i_set', i_set)
    ##print('action', action_o)

    RTo = 0
    for element in regrets[i_set][action_o[-1]]:
        RTo += element
    if RTo <=0:
        RTo=0

    RTo = RTo/len(regrets[i_set][action_o[-1]])

    strategy = 0
    ###print('RT',RT)
    ###print('RTo',RTo)
    if RT+RTo > 0:
        strategy = RT / (RT+RTo)
    else:
        strategy = 1/2

    strategy_sum[i_set][act[-1]]+=strategy*reach_prob
    reach_sum[i_set][act[-1]]+=reach_prob
    try:
        #print('average_strategy',strategy_sum[i_set][act[-1]]/reach_sum[i_set][act[-1]])
        average_strategy[i_set][act[-1]] = strategy_sum[i_set][act[-1]]/reach_sum[i_set][act[-1]]
    except:
        pass


    ###print(actions[random_num])
    ###print(i_set)
    ###print(act[-1])
    ###print('strategy', strategy)

    info_sets[i_set][act[-1]] = strategy
    info_sets[i_set][action_o[-1]] = 1-strategy
    ##print(info_sets)

print(average_strategy)
#print(regrets)



'''
1. pick cards randomly from list
2. calculate new strategy for the action:
    a. calculate the reach probability of the info set with Pi always taking actions that led to it
        - get info set
        - get P-i actions leading to the info set and their current probability
        
    


'''
