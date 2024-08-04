<!-- markdownlint-disable -->

<a href="https://github.com/khulnasoft/fastnode/blob/main/src/fastnode/api/readyapi_utils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `fastnode.api.readyapi_utils`
Collection of utilities for ReadyAPI apps. 


---

<a href="https://github.com/khulnasoft/fastnode/blob/main/src/fastnode/api/readyapi_utils.py#L10"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `as_form`

```python
as_form(cls: Type[BaseModel]) → Any
```

Adds an as_form class method to decorated models. 

The as_form class method can be used with ReadyAPI endpoints 


---

<a href="https://github.com/khulnasoft/fastnode/blob/main/src/fastnode/api/readyapi_utils.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `patch_readyapi`

```python
patch_readyapi(app: ReadyAPI) → None
```

Patch function to allow relative url resolution. 

This patch is required to make readyapi fully functional with a relative url path. This code snippet can be copy-pasted to any Readyapi application. 




---

_This file was automatically generated via [docsai](https://github.com/khulnasoft/docsai)._
