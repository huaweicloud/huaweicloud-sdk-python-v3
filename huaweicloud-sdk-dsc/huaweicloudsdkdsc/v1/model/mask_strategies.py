# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MaskStrategies:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'algorithm': 'str',
        'parameters': 'dict(str, object)'
    }

    attribute_map = {
        'name': 'name',
        'algorithm': 'algorithm',
        'parameters': 'parameters'
    }

    def __init__(self, name=None, algorithm=None, parameters=None):
        """MaskStrategies

        The model defined in huaweicloud sdk

        :param name: 需要脱敏的字段名称，最大支持长度256。
        :type name: str
        :param algorithm: 脱敏算法名称，详情见附录\&quot;动态脱敏策略配置\&quot;。
        :type algorithm: str
        :param parameters: 脱敏算法参数，详情见附录\&quot;动态脱敏策略配置\&quot;。
        :type parameters: dict(str, object)
        """
        
        

        self._name = None
        self._algorithm = None
        self._parameters = None
        self.discriminator = None

        self.name = name
        self.algorithm = algorithm
        if parameters is not None:
            self.parameters = parameters

    @property
    def name(self):
        """Gets the name of this MaskStrategies.

        需要脱敏的字段名称，最大支持长度256。

        :return: The name of this MaskStrategies.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MaskStrategies.

        需要脱敏的字段名称，最大支持长度256。

        :param name: The name of this MaskStrategies.
        :type name: str
        """
        self._name = name

    @property
    def algorithm(self):
        """Gets the algorithm of this MaskStrategies.

        脱敏算法名称，详情见附录\"动态脱敏策略配置\"。

        :return: The algorithm of this MaskStrategies.
        :rtype: str
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        """Sets the algorithm of this MaskStrategies.

        脱敏算法名称，详情见附录\"动态脱敏策略配置\"。

        :param algorithm: The algorithm of this MaskStrategies.
        :type algorithm: str
        """
        self._algorithm = algorithm

    @property
    def parameters(self):
        """Gets the parameters of this MaskStrategies.

        脱敏算法参数，详情见附录\"动态脱敏策略配置\"。

        :return: The parameters of this MaskStrategies.
        :rtype: dict(str, object)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this MaskStrategies.

        脱敏算法参数，详情见附录\"动态脱敏策略配置\"。

        :param parameters: The parameters of this MaskStrategies.
        :type parameters: dict(str, object)
        """
        self._parameters = parameters

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
        if not isinstance(other, MaskStrategies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
