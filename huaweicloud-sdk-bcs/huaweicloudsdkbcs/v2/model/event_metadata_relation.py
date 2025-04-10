# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventMetadataRelation:

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
        'value': 'list[str]',
        'relation': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'relation': 'relation'
    }

    def __init__(self, key=None, value=None, relation=None):
        r"""EventMetadataRelation

        The model defined in huaweicloud sdk

        :param key: 指定查询字段的key，对应metadata里面的key
        :type key: str
        :param value: 查询条件中指定key的值
        :type value: list[str]
        :param relation: 该条件与其他条件的组合方式
        :type relation: str
        """
        
        

        self._key = None
        self._value = None
        self._relation = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if relation is not None:
            self.relation = relation

    @property
    def key(self):
        r"""Gets the key of this EventMetadataRelation.

        指定查询字段的key，对应metadata里面的key

        :return: The key of this EventMetadataRelation.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this EventMetadataRelation.

        指定查询字段的key，对应metadata里面的key

        :param key: The key of this EventMetadataRelation.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this EventMetadataRelation.

        查询条件中指定key的值

        :return: The value of this EventMetadataRelation.
        :rtype: list[str]
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this EventMetadataRelation.

        查询条件中指定key的值

        :param value: The value of this EventMetadataRelation.
        :type value: list[str]
        """
        self._value = value

    @property
    def relation(self):
        r"""Gets the relation of this EventMetadataRelation.

        该条件与其他条件的组合方式

        :return: The relation of this EventMetadataRelation.
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        r"""Sets the relation of this EventMetadataRelation.

        该条件与其他条件的组合方式

        :param relation: The relation of this EventMetadataRelation.
        :type relation: str
        """
        self._relation = relation

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
        if not isinstance(other, EventMetadataRelation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
