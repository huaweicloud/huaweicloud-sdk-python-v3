# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FunctionRef:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ref_name': 'str',
        'invoke_mode': 'str',
        'arguments': 'object'
    }

    attribute_map = {
        'ref_name': 'ref_name',
        'invoke_mode': 'invoke_mode',
        'arguments': 'arguments'
    }

    def __init__(self, ref_name=None, invoke_mode=None, arguments=None):
        """FunctionRef

        The model defined in huaweicloud sdk

        :param ref_name: 函数引用名称，需要和外层functions中的name对应
        :type ref_name: str
        :param invoke_mode: 函数调用模式，目前只支持同步调用
        :type invoke_mode: str
        :param arguments: 函数执行时的入参，支持引用constants中的常量 定义方式：参数路径 | 常量值/常量路径 参数路径指输入参数的JsonPath路径，如$.a.b[0].c 常量值可以为数字类型，字符串类型(需要用单引号括起来)，布尔类型 常量路径为常量的JsonPath路径，但是根节点需要用$CONST表示，示例：$CONST.a.b
        :type arguments: object
        """
        
        

        self._ref_name = None
        self._invoke_mode = None
        self._arguments = None
        self.discriminator = None

        self.ref_name = ref_name
        if invoke_mode is not None:
            self.invoke_mode = invoke_mode
        self.arguments = arguments

    @property
    def ref_name(self):
        """Gets the ref_name of this FunctionRef.

        函数引用名称，需要和外层functions中的name对应

        :return: The ref_name of this FunctionRef.
        :rtype: str
        """
        return self._ref_name

    @ref_name.setter
    def ref_name(self, ref_name):
        """Sets the ref_name of this FunctionRef.

        函数引用名称，需要和外层functions中的name对应

        :param ref_name: The ref_name of this FunctionRef.
        :type ref_name: str
        """
        self._ref_name = ref_name

    @property
    def invoke_mode(self):
        """Gets the invoke_mode of this FunctionRef.

        函数调用模式，目前只支持同步调用

        :return: The invoke_mode of this FunctionRef.
        :rtype: str
        """
        return self._invoke_mode

    @invoke_mode.setter
    def invoke_mode(self, invoke_mode):
        """Sets the invoke_mode of this FunctionRef.

        函数调用模式，目前只支持同步调用

        :param invoke_mode: The invoke_mode of this FunctionRef.
        :type invoke_mode: str
        """
        self._invoke_mode = invoke_mode

    @property
    def arguments(self):
        """Gets the arguments of this FunctionRef.

        函数执行时的入参，支持引用constants中的常量 定义方式：参数路径 | 常量值/常量路径 参数路径指输入参数的JsonPath路径，如$.a.b[0].c 常量值可以为数字类型，字符串类型(需要用单引号括起来)，布尔类型 常量路径为常量的JsonPath路径，但是根节点需要用$CONST表示，示例：$CONST.a.b

        :return: The arguments of this FunctionRef.
        :rtype: object
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """Sets the arguments of this FunctionRef.

        函数执行时的入参，支持引用constants中的常量 定义方式：参数路径 | 常量值/常量路径 参数路径指输入参数的JsonPath路径，如$.a.b[0].c 常量值可以为数字类型，字符串类型(需要用单引号括起来)，布尔类型 常量路径为常量的JsonPath路径，但是根节点需要用$CONST表示，示例：$CONST.a.b

        :param arguments: The arguments of this FunctionRef.
        :type arguments: object
        """
        self._arguments = arguments

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FunctionRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
