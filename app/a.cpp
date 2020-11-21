#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
const ll INF = (ll) 10000000;
const ll MAXN = 300*300+2;
ll n, source, sink;
ll d[MAXN], y[MAXN], pq[MAXN];

struct edge {
	ll a, b, capacity, flow;
};

vector<edge> edges;
vector<ll> gr[MAXN];

void newEdge(ll a, ll b, ll capacity) {
	edge e1 = { a, b, capacity, 0 };
	edge e2 = { b, a, 0, 0 };
	gr[a].push_back((ll) edges.size());
    gr[b].push_back((ll) edges.size());
	edges.push_back(e1);
	edges.push_back(e2);
}

bool bfs() {
	pq[0] = source;
    ll a = 0, b = 1;
	memset(d, -1, n * sizeof d[0]);
	d[source] = 0;
	while(a < b && d[sink] == -1) {
		ll v = pq[a++];
		for(size_t i=0; i<gr[v].size(); ++i) {
			ll id = gr[v][i], to = edges[id].b;
			if(d[to] == -1 && edges[id].flow < edges[id].capacity) {
				pq[b++] = to;
				d[to] = d[v] + 1;
			}
		}
	}
	if(d[sink] != -1)
        return true;
    return false;
}

ll dfs(ll v, ll flow) {
	if(!flow)  return 0;
	if(v == sink)  return flow;
	for(; y[v]<(ll)gr[v].size(); ++y[v]) {
		ll id = gr[v][y[v]];
        ll to = edges[id].b;
		if(d[to] != d[v] + 1)
            continue;
		ll pushed = dfs(to, min(flow, edges[id].capacity - edges[id].flow));
		if(pushed) {
			edges[id].flow += pushed;
			edges[id ^ 1].flow -= pushed;
			return pushed;
		}
	}
	return 0;
}

ll dinic() {
	ll flow = 0;
	while(bfs()) {
		memset(y, 0, n * sizeof y[0]);
		while(ll pushed = dfs(source,INF))
			flow += pushed;
	}
	return flow;
}

int main() {
    ll sn, k, m;
    cin >> sn >> k >> m;

    n = sn*k + 2;

    source = n-1;
    sink = n-2;

    for(ll i = 0; i < sn; i++) {
        if(i < k) {
            ll time = i*sn;
            newEdge(source,i+time,1);
        }
        if(i == sn-1) {
            for(ll j = 0; j < k; j++) {
                ll time = j*sn;
                newEdge(i+time,sink,INF);
            }
        }
    }

    for(ll i = 0; i < m; i++) {
        ll u, v;
        cin >> u >> v;
        for(ll j = 0; j < k; j++) {
            ll t = ((j+1)%k)*sn;
            newEdge(u-1+j*sn,v-1+t,1);
        }
    }
    cout << dinic() << endl;
}