
#include <iostream>
#include <vector>
#include <queue>
#include <stack>

using namespace std;

class BFS {
public:
    vector<int> BFS_method(int v, vector<int> adj[], int goal) {
        queue<int> q;
        q.push(0);
        vector<int> vis(v, 0); 
        vis[0] = 1;
        vector<int> bsf;

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            bsf.push_back(u);

            if (u == goal){
                break;
            }

            for (int i = 0; i < adj[u].size(); i++) {
                if (!vis[adj[u][i]]) {
                    q.push(adj[u][i]);
                    vis[adj[u][i]] = 1;
                }
            }
        }

        return bsf; 
    }
};

class DFS {
public:
    vector<int> DFS_method(int v, vector<int> adj[], int goal) {
        stack<int> st;
        st.push(0);
        vector<int> vis(v, 0); 
        vis[0] = 1;
        vector<int> dfs;

        while (!st.empty()) {
            int u = st.top();
            st.pop();
            dfs.push_back(u);

            if (u == goal){
                break;
            }

            for (int i = 0; i < adj[u].size(); i++) {
                if (!vis[adj[u][i]]) {
                    st.push(adj[u][i]);
                    vis[adj[u][i]] = 1;
                }
            }
        }

        return dfs; 
    }
};


int main() {
    
    int v = 7;
    vector<int> adj[v];
    adj[0].push_back(1);
    adj[0].push_back(2);
    adj[1].push_back(3);
    adj[1].push_back(4);
    adj[2].push_back(5);
    adj[2].push_back(6);

    int goal = 3;

    BFS bfs;
    vector<int> result_bfs = bfs.BFS_method(v, adj, goal);

    cout << "BFS Traversal: ";
    for (int i = 0; i < result_bfs.size(); i++) {
        cout << result_bfs[i] << " ";
    }

    DFS dfs;
    vector<int> result_dfs = dfs.DFS_method(v, adj, goal);

    cout << "\nDFS Traversal: ";
    for (int i = 0; i < result_dfs.size(); i++) {
        cout << result_dfs[i] << " ";
    }

    return 0;
}