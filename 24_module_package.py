from pack import *
from test_module import *
import pack.test_module_2
# 说明：
# 以 import pack.test_module_2 这种方式导入模块时，
# 包内模块的 __all__ 属性不会影响导入的内容。
# __all__ 只在使用 from ... import * 语法时才会生效，用于限制“*”能导入哪些成员。
# 直接 import pack.test_module_2 后，依然可以通过 pack.test_module_2.成员名 访问模块内所有公开成员（不以下划线开头的）。
# 例如：pack.test_module_2.test_module_2() 依然可以正常调用。


# 模块
# 模块是Python中用于组织代码的单位
# 模块可以包含变量、函数、类等
# 模块可以被其他模块导入
# 模块可以被其他模块导入
# 基本语法： [from 模块名] import (函数名|变量名|类名|*) [as 别名]
# 例子：
# 下面这行代码是“导入math模块中的所有函数、变量和类”
from math import *
# 这样可以直接使用math模块中的所有公开成员（不需要加math.前缀），例如：sqrt(16)
# 但是不推荐这样做，因为可能会导致命名冲突，建议只导入需要的函数
from math import sqrt as s
from math import sqrt
# 这不是导入math中的所有函数，而是只导入了math模块本身，需要通过math.函数名来调用
import math
print(math.sqrt(16))
print(sqrt(16))
print(s(16))
print(sqrt(16))


# 自定义模块
# 使用__name__获取模块名，可以避免模块中测试代码的执行
print(__name__)

# test_module.test_module()
# test_module.test_module2()
test_module()
# test_module2()

# 使用__all__限制模块的公开成员，当导入方式为from 模块名 import * 时，只能导入__all__中的成员。
# 但是import 模块名 的方式不受影响


# 包
# 包是Python中用于组织模块的单位
# 包可以包含模块、子包、__init__.py文件等
# 包可以被其他包导入
# 包可以被其他包导入
# 基本语法： [from 包名] import (模块名|子包名|*) [as 别名]
# 或者 import 包名.模块名
# 再或者 from 包名 import 模块名
# 再或者 from 包名.模块名 import 成员名
# 再或者 from 包名.模块名 import *
# 再或者 from 包名.模块名 import 成员名 as 别名
# 例子：
pack.test_module_2.test_module_2()
pack.test_module_2.test_module2_2()

# __init__.py 中 通过 __all__ = ["模块名"] 限制包内模块的公开成员，
# 当导入方式为from 包名 import * 时，只能导入__all__中的成员。
# 但是import 包名 的方式不受影响


# 包可以有多个层级
# 使用方式一：import 包名.子包名.模块名
# 使用方式二：from 包名.子包名 import 模块名
# 使用方式三：from 包名.子包名.模块名 import 成员名
# 使用方式四：from 包名.子包名.模块名 import *
# 使用方式五：from 包名.子包名.模块名 import 成员名 as 别名
# 例子：


# 快捷键：alt + enter / alt + shift + enter 可以提示选择/快速导入模块
# 快捷键：ctrl + alt + o 可以快速删除未使用的导入
