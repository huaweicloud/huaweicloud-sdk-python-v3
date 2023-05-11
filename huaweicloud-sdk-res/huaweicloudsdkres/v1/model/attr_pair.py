# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttrPair:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'party_a': 'str',
        'party_b': 'str'
    }

    attribute_map = {
        'party_a': 'party_a',
        'party_b': 'party_b'
    }

    def __init__(self, party_a=None, party_b=None):
        """AttrPair

        The model defined in huaweicloud sdk

        :param party_a: 被推荐对象的属性名。
        :type party_a: str
        :param party_b: 被推荐对象的属性名。
        :type party_b: str
        """
        
        

        self._party_a = None
        self._party_b = None
        self.discriminator = None

        if party_a is not None:
            self.party_a = party_a
        if party_b is not None:
            self.party_b = party_b

    @property
    def party_a(self):
        """Gets the party_a of this AttrPair.

        被推荐对象的属性名。

        :return: The party_a of this AttrPair.
        :rtype: str
        """
        return self._party_a

    @party_a.setter
    def party_a(self, party_a):
        """Sets the party_a of this AttrPair.

        被推荐对象的属性名。

        :param party_a: The party_a of this AttrPair.
        :type party_a: str
        """
        self._party_a = party_a

    @property
    def party_b(self):
        """Gets the party_b of this AttrPair.

        被推荐对象的属性名。

        :return: The party_b of this AttrPair.
        :rtype: str
        """
        return self._party_b

    @party_b.setter
    def party_b(self, party_b):
        """Sets the party_b of this AttrPair.

        被推荐对象的属性名。

        :param party_b: The party_b of this AttrPair.
        :type party_b: str
        """
        self._party_b = party_b

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
        if not isinstance(other, AttrPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
