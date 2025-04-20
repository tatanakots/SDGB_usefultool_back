# 舞萌DX科技专页

本项目是舞萌DX科技专页的简易后端。

## 开发环境

本项目使用 [Flask](https://flask.palletsprojects.com/) 作为服务器框架，使用 [Python](https://python.org/) 作为基础语言。

请使用下面的命令运行项目：

```bash
python3 main.py
```

## 关于 `sdgb.py` 与 `authlite.py`

> 本仓库 **不** 附带这两个模块，请自行准备。

### sdgb.py

- **函数：** `sdgb_api(data: str, useApi: str, userId: int) → str`  
  向官方服务器发送请求并返回原始响应。  
  - `data`：JSON 格式的请求体  
  - `useApi`：接口端点名称（字符串，不含服务器后缀，如 `MaimaiChn`）  
  - `userId`：用户 ID（整数）  

- **函数：** `qr_api(qr_code: str) → dict`  
  向官方 AimeDB 解析二维码并返回已序列化的 JSON 对象。  
  - `qr_code`：二维码内容（以 `MAID` 或 `SGWCMAID` 开头的字符串）  

### authlite.py

- **函数：** `authlite() → dict`  
  调用官方配信接口，返回已序列化的 JSON 字典。

## 备注

项目仍在积极开发中，因此可能存在一些问题。