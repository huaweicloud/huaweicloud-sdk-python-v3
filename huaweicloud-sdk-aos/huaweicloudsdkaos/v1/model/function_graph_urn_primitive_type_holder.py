# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FunctionGraphUrnPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'function_graph_urn': 'str'
    }

    attribute_map = {
        'function_graph_urn': 'function_graph_urn'
    }

    def __init__(self, function_graph_urn=None):
        """FunctionGraphUrnPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param function_graph_urn: FunctionGraph方法的统一资源标识，用于唯一标识的FunctionGraph方法。当前只支持和RFS同region的function_graph_urn，如果给予了关于其他region的，会报错400。  关于该参数的详细解释，请参考官方文档：https://support.huaweicloud.com/api-functiongraph/functiongraph_06_0102.html
        :type function_graph_urn: str
        """
        
        

        self._function_graph_urn = None
        self.discriminator = None

        if function_graph_urn is not None:
            self.function_graph_urn = function_graph_urn

    @property
    def function_graph_urn(self):
        """Gets the function_graph_urn of this FunctionGraphUrnPrimitiveTypeHolder.

        FunctionGraph方法的统一资源标识，用于唯一标识的FunctionGraph方法。当前只支持和RFS同region的function_graph_urn，如果给予了关于其他region的，会报错400。  关于该参数的详细解释，请参考官方文档：https://support.huaweicloud.com/api-functiongraph/functiongraph_06_0102.html

        :return: The function_graph_urn of this FunctionGraphUrnPrimitiveTypeHolder.
        :rtype: str
        """
        return self._function_graph_urn

    @function_graph_urn.setter
    def function_graph_urn(self, function_graph_urn):
        """Sets the function_graph_urn of this FunctionGraphUrnPrimitiveTypeHolder.

        FunctionGraph方法的统一资源标识，用于唯一标识的FunctionGraph方法。当前只支持和RFS同region的function_graph_urn，如果给予了关于其他region的，会报错400。  关于该参数的详细解释，请参考官方文档：https://support.huaweicloud.com/api-functiongraph/functiongraph_06_0102.html

        :param function_graph_urn: The function_graph_urn of this FunctionGraphUrnPrimitiveTypeHolder.
        :type function_graph_urn: str
        """
        self._function_graph_urn = function_graph_urn

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
        if not isinstance(other, FunctionGraphUrnPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
