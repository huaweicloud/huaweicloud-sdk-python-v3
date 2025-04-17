# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceGroupTagRelation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'operator': 'str',
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'operator': 'operator',
        'value': 'value'
    }

    def __init__(self, key=None, operator=None, value=None):
        r"""ResourceGroupTagRelation

        The model defined in huaweicloud sdk

        :param key: TMS标签键规范。
        :type key: str
        :param operator: tag操作符，含义是标签key与value的关系。   include表示包含   prefix表示前缀   suffix表示后缀   notInclude表示不包含   equal表示相等   当operator为equal，value为空字符串时表示为全部   all表示全部 
        :type operator: str
        :param value: TMS标签值规范。
        :type value: str
        """
        
        

        self._key = None
        self._operator = None
        self._value = None
        self.discriminator = None

        self.key = key
        if operator is not None:
            self.operator = operator
        if value is not None:
            self.value = value

    @property
    def key(self):
        r"""Gets the key of this ResourceGroupTagRelation.

        TMS标签键规范。

        :return: The key of this ResourceGroupTagRelation.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ResourceGroupTagRelation.

        TMS标签键规范。

        :param key: The key of this ResourceGroupTagRelation.
        :type key: str
        """
        self._key = key

    @property
    def operator(self):
        r"""Gets the operator of this ResourceGroupTagRelation.

        tag操作符，含义是标签key与value的关系。   include表示包含   prefix表示前缀   suffix表示后缀   notInclude表示不包含   equal表示相等   当operator为equal，value为空字符串时表示为全部   all表示全部 

        :return: The operator of this ResourceGroupTagRelation.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this ResourceGroupTagRelation.

        tag操作符，含义是标签key与value的关系。   include表示包含   prefix表示前缀   suffix表示后缀   notInclude表示不包含   equal表示相等   当operator为equal，value为空字符串时表示为全部   all表示全部 

        :param operator: The operator of this ResourceGroupTagRelation.
        :type operator: str
        """
        self._operator = operator

    @property
    def value(self):
        r"""Gets the value of this ResourceGroupTagRelation.

        TMS标签值规范。

        :return: The value of this ResourceGroupTagRelation.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ResourceGroupTagRelation.

        TMS标签值规范。

        :param value: The value of this ResourceGroupTagRelation.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, ResourceGroupTagRelation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
