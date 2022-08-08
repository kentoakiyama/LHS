# ラテン超方格サンプリングの実装

# 使い方
```python
lhs_result = lhs(n_dim, n_sample, init_array)
```

引数
- n_dim: 次元数（2次元空間からサンプリングしたい場合は2を指定）
- n_sample: サンプル数
- init_array: すでにあるサンプリングから追加でサンプリングしたい場合に指定

返り値
lhs_result -> np.array([n_sample, n_dim])のサイズになっています。
全て、0から1で正規化されているので、適宜範囲を修正してください。

# 参考文献
- [ラテン超方格サンプリング(LHS)の実装(Python)](https://qiita.com/Zoo1234/items/634f567983a7240353a0)
- [An Example of Augmenting a Latin Hypercube](https://cran.r-project.org/web/packages/lhs/vignettes/augment_lhs.html)
