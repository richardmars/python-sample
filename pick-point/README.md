# pick point

## 环境搭建

### matplotlib

如果是linux环境，python3在使用matplotlib时需要依赖tkinter，而环境没有自带python3版本，自行安装

```sh
sudo apt-get install python3-tk
``` 

### xrld
    
参考

- [Rectangle to select area in plot and find maximum value](https://stackoverflow.com/questions/44274938/rectangle-to-select-area-in-plot-and-find-maximum-value)
- [PEP 289 -- Generator Expressions](https://www.python.org/dev/peps/pep-0289/)

### NEEDED FUNCTIONS
1.在xy的graph图中选择点，支持单个选择或是区域选择；

2.对选择的点可以生成原始表的子集，或者可以将选中的数据从原始的表中删除；

3.两个表的更新功能：将其中一个表的某一列更新到另一个表中，以一个单独的列作为更新的基准；