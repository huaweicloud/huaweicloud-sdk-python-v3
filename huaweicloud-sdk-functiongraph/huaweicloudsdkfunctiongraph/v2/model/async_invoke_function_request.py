# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AsyncInvokeFunctionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'function_urn': 'str',
        'x_cff_instance_memory': 'str',
        'body': 'dict(str, object)'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'x_cff_instance_memory': 'X-Cff-Instance-Memory',
        'body': 'body'
    }

    def __init__(self, function_urn=None, x_cff_instance_memory=None, body=None):
        r"""AsyncInvokeFunctionRequest

        The model defined in huaweicloud sdk

        :param function_urn: 函数的URN，详细解释见FunctionGraph函数模型的描述。
        :type function_urn: str
        :param x_cff_instance_memory: 设置本次执行函数使用的内存规格,取值： 128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096、8192、10240
        :type x_cff_instance_memory: str
        :param body: 执行函数请求体，为json格式。
        :type body: dict(str, object)
        """
        
        

        self._function_urn = None
        self._x_cff_instance_memory = None
        self._body = None
        self.discriminator = None

        self.function_urn = function_urn
        if x_cff_instance_memory is not None:
            self.x_cff_instance_memory = x_cff_instance_memory
        if body is not None:
            self.body = body

    @property
    def function_urn(self):
        r"""Gets the function_urn of this AsyncInvokeFunctionRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :return: The function_urn of this AsyncInvokeFunctionRequest.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        r"""Sets the function_urn of this AsyncInvokeFunctionRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :param function_urn: The function_urn of this AsyncInvokeFunctionRequest.
        :type function_urn: str
        """
        self._function_urn = function_urn

    @property
    def x_cff_instance_memory(self):
        r"""Gets the x_cff_instance_memory of this AsyncInvokeFunctionRequest.

        设置本次执行函数使用的内存规格,取值： 128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096、8192、10240

        :return: The x_cff_instance_memory of this AsyncInvokeFunctionRequest.
        :rtype: str
        """
        return self._x_cff_instance_memory

    @x_cff_instance_memory.setter
    def x_cff_instance_memory(self, x_cff_instance_memory):
        r"""Sets the x_cff_instance_memory of this AsyncInvokeFunctionRequest.

        设置本次执行函数使用的内存规格,取值： 128、256、512、768、1024、1280、1536、1792、2048、2560、3072、3584、4096、8192、10240

        :param x_cff_instance_memory: The x_cff_instance_memory of this AsyncInvokeFunctionRequest.
        :type x_cff_instance_memory: str
        """
        self._x_cff_instance_memory = x_cff_instance_memory

    @property
    def body(self):
        r"""Gets the body of this AsyncInvokeFunctionRequest.

        执行函数请求体，为json格式。

        :return: The body of this AsyncInvokeFunctionRequest.
        :rtype: dict(str, object)
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this AsyncInvokeFunctionRequest.

        执行函数请求体，为json格式。

        :param body: The body of this AsyncInvokeFunctionRequest.
        :type body: dict(str, object)
        """
        self._body = body

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
        if not isinstance(other, AsyncInvokeFunctionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
