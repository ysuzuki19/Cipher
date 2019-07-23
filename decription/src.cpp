#include <bits/stdc++.h>
using namespace std;

#define _ << ' ' <<
#define squ(x)  ((x) * (x))
#define debug(var)  do{std::cout << #var << " : "; view(var);}while(0)
#define _max(v)  *max_element(v.begin(), v.end())
#define _min(v)  *min_element(v.begin(), v.end())
#define _sort(var)  std::sort(var.begin(), var.end());
#define _rsort(var)  std::sort(var.begin(), var.end(), std::greater<>());
using namespace std;
using ll = long long;
int gcd(int m, int n){return !n ? m : gcd(n, m%n);}
template<typename T> using V = std::vector<T>;
template<typename T> using VV = std::vector<std::vector<T>>;
template<typename T> using VVV = std::vector<std::vector<std::vector<T>>>;
template<typename T> void view(const T e){ std::cout << e << std::endl;}
template<typename T> void view(const vector<T>& v){ for(const auto& e : v) std::cout << e << " "; std::cout << std::endl; }
template<typename T> void view(const VV<T>& vv){ for(const auto& v : vv){ view(v); } }

int main(int argc, char **argv) {
//  vector<string> args(argv, argv+argc);
//  ifstream fin(args[1]);
//  string filename{""};
//  ifstream fin(filename);
//  cout << args[1] << endl;
//  int n;
//  fin >> n;
  return 0;
}
