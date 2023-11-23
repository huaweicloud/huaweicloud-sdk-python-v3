# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRoute:

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
        'weight': 'int',
        'tags': 'CreateRouteTags'
    }

    attribute_map = {
        'name': 'name',
        'weight': 'weight',
        'tags': 'tags'
    }

    def __init__(self, name=None, weight=None, tags=None):
        """CreateRoute

        The model defined in huaweicloud sdk

        :param name: 规则名称。
        :type name: str
        :param weight: 权重值。
        :type weight: int
        :param tags: 
        :type tags: :class:`huaweicloudsdkcse.v1.CreateRouteTags`
        """
        
        

        self._name = None
        self._weight = None
        self._tags = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if weight is not None:
            self.weight = weight
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CreateRoute.

        规则名称。

        :return: The name of this CreateRoute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRoute.

        规则名称。

        :param name: The name of this CreateRoute.
        :type name: str
        """
        self._name = name

    @property
    def weight(self):
        """Gets the weight of this CreateRoute.

        权重值。

        :return: The weight of this CreateRoute.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CreateRoute.

        权重值。

        :param weight: The weight of this CreateRoute.
        :type weight: int
        """
        self._weight = weight

    @property
    def tags(self):
        """Gets the tags of this CreateRoute.

        :return: The tags of this CreateRoute.
        :rtype: :class:`huaweicloudsdkcse.v1.CreateRouteTags`
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateRoute.

        :param tags: The tags of this CreateRoute.
        :type tags: :class:`huaweicloudsdkcse.v1.CreateRouteTags`
        """
        self._tags = tags

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
        if not isinstance(other, CreateRoute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
