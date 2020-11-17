import sys

for line in sys.stdin.readlines():

obs = ('noun/verb', 'pr', 'det/prn', 'noun/verb')
obs = ('noun/verb', 'pr', 'det/prn/verb', 'noun/verb', 'adj', 'sent')
states = ('verb', 'noun', 'det', 'prn', 'pr', 'adj', 'sent')
start_p = {'verb':0.75, 'noun':0.0, 'det':0.25, 'prn':0.0, 'pr':0.0, 'adj':0.0, 'sent':0.0}
trans_p = {
	'verb': {'verb':0.0, 'noun':0.2, 'det':0.2, 'prn':0.0, 'pr':0.4, 'adj':0.2, 'sent':0.0},
	'noun': {'verb':0.16, 'noun':0.0, 'det':0.0, 'prn':0.0, 'pr':0.16, 'adj':0.16, 'sent':0.5},
	'det':  {'verb':0.0, 'noun':1.0, 'det':0.0, 'prn':0.0, 'pr':0.0, 'adj':0.0, 'sent':0.0},
	'prn':  {'verb':0.0, 'noun':0.0, 'det':0.0, 'prn':0.0, 'pr':0.0, 'adj':0.0, 'sent':0.0},
	'pr':   {'verb':0.0, 'noun':0.33, 'det':0.66, 'prn':0.0, 'pr':0.0, 'adj':0.0, 'sent':0.0},
	'adj':  {'verb':0.0, 'noun':0.0, 'det':0.0, 'prn':0.0, 'pr':0.0, 'adj':0.0, 'sent':1.0},
	'sent':  {'verb':0.75, 'noun':0.0, 'det':0.25, 'prn':0.0, 'pr':0.0, 'adj':0.0, 'sent':0.0}
}

emit_p = {
	'verb' : {'det/prn/verb':0.0, 'det/prn':0.0, 'noun/verb':0.2, 'verb':0.8, 'noun':0.0, 'det':0.0, 'prn':0.0, 'pr':0.0, 'adj':0.0, 'sent':0.0},
	'noun' : {'det/prn/verb':0.0, 'det/prn':0.0, 'noun/verb':0.67, 'verb':0.0, 'noun':0.33, 'det':0.0, 'prn':0.0, 'pr':0.0, 'adj':0.0, 'sent':0.0},
	'det' : {'det/prn/verb':0.25, 'det/prn':0.75, 'noun/verb':0.0, 'verb':0.0, 'noun':0.0, 'det':0.0, 'prn':0.0, 'pr':0.0, 'adj':0.0, 'sent':0.0},
	'prn' : {'det/prn/verb':0.0, 'det/prn':0.0, 'noun/verb':0.0, 'verb':0.0, 'noun':0.0, 'det':0.0, 'prn':0.0, 'pr':0.0, 'adj':0.0, 'sent':0.0},
	'pr' : {'det/prn/verb':0.0, 'det/prn':0.0, 'noun/verb':0.0, 'verb':0.0, 'noun':0.0, 'det':0.0, 'prn':0.0, 'pr':1.0, 'adj':0.0, 'sent':0.0},
	'adj' : {'det/prn/verb':0.0, 'det/prn':0.0, 'noun/verb':0.0, 'verb':0.0, 'noun':0.0, 'det':0.0, 'prn':0.0, 'pr':0.0, 'adj':1.0, 'sent':0.0},
	'sent' : {'det/prn/verb':0.0, 'det/prn':0.0, 'noun/verb':0.0, 'verb':0.0, 'noun':0.0, 'det':0.0, 'prn':0.0, 'pr':0.0, 'adj':0.0, 'sent':1.0},
}

def dptable(V):

print("\t".join(("%12d" % i) for i in range(len(V))))
	for state in V[0]:
		print("%.7s:\t" % state + "\t".join("%.7s" % ("%f" % v[state]["prob"]) for v in V))

def viterbi(obs, states, start_p, trans_p, emit_p):
	V = [{}] 
for state in states:
		V[0][state] = {"prob": start_p[state] * emit_p[state][obs[0]], "prev": None}
for t in range(1, len(obs)):
		V.append({})
		for state in states:
			max_tr_prob = max(V[t-1][prev_state]["prob"] * trans_p[prev_state][state] for prev_state in states)
			for prev_state in states:
				if V[t-1][prev_state]["prob"] * trans_p[prev_state][state] == max_tr_prob:
					max_prob = max_tr_prob * emit_p[state][obs[t]]
					V[t][state] = {"prob": max_prob, "prev": prev_state}
					break
dptable(V);
best_path = []

max_prob = max(value["prob"] for value in V[-1].values())
previous = None

for st, data in V[-1].items():
		if data["prob"] == max_prob:
			best_path.append(st)
			previous = st
			break

for t in range(len(V) - 2, -1, -1):
		best_path.insert(0, V[t + 1][previous]["prev"])
		previous = V[t + 1][previous]["prev"]
	print('--\nBest path: %.8f\t%s' % (max_prob, ' '.join(best_path)));

viterbi(obs, states, start_p, trans_p, emit_p);



