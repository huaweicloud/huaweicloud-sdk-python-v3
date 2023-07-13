# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiRequestPara:

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
        'mapping': 'str',
        'condition': 'str'
    }

    attribute_map = {
        'name': 'name',
        'mapping': 'mapping',
        'condition': 'condition'
    }

    def __init__(self, name=None, mapping=None, condition=None):
        """ApiRequestPara

        The model defined in huaweicloud sdk

        :param name: 参数名称
        :type name: str
        :param mapping: 映射字段
        :type mapping: str
        :param condition: 操作符
        :type condition: str
        """
        
        

        self._name = None
        self._mapping = None
        self._condition = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if mapping is not None:
            self.mapping = mapping
        if condition is not None:
            self.condition = condition

    @property
    def name(self):
        """Gets the name of this ApiRequestPara.

        参数名称

        :return: The name of this ApiRequestPara.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiRequestPara.

        参数名称

        :param name: The name of this ApiRequestPara.
        :type name: str
        """
        self._name = name

    @property
    def mapping(self):
        """Gets the mapping of this ApiRequestPara.

        映射字段

        :return: The mapping of this ApiRequestPara.
        :rtype: str
        """
        return self._mapping

    @mapping.setter
    def mapping(self, mapping):
        """Sets the mapping of this ApiRequestPara.

        映射字段

        :param mapping: The mapping of this ApiRequestPara.
        :type mapping: str
        """
        self._mapping = mapping

    @property
    def condition(self):
        """Gets the condition of this ApiRequestPara.

        操作符

        :return: The condition of this ApiRequestPara.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this ApiRequestPara.

        操作符

        :param condition: The condition of this ApiRequestPara.
        :type condition: str
        """
        self._condition = condition

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
        if not isinstance(other, ApiRequestPara):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
