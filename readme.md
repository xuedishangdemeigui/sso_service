- 实现简易的 SCM 编译，将程序生成为镜像。编译并生成可以运行的镜像文件
- 实现简易的 TCE 部署流程，将镜像部署到 K8s 集群

## K8s 集群搭建
参考：
- https://juejin.cn/post/7042907905741291533
- https://k8s.easydoc.net/docs/dRiQjyTY/28366845/6GiNOzyZ/nd7yOvdY
- 重新生成 Token： https://blog.csdn.net/YouMing_Li/article/details/117553658

```
sudo kubeadm join 10.0.2.15:6443 --token wk1coa.oqirfyc04dlhj9yd \
        --discovery-token-ca-cert-hash sha256:4012a00026df5e98364482a79208d8eed7692d222b39a1c75f91ce9fd4e72c81
```