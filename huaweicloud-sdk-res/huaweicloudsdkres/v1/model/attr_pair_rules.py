# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttrPairRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'attr_pairs': 'list[AttrPair]'
    }

    attribute_map = {
        'attr_pairs': 'attr_pairs'
    }

    def __init__(self, attr_pairs=None):
        """AttrPairRules

        The model defined in huaweicloud sdk

        :param attr_pairs: 属性对。
        :type attr_pairs: list[:class:`huaweicloudsdkres.v1.AttrPair`]
        """
        
        

        self._attr_pairs = None
        self.discriminator = None

        if attr_pairs is not None:
            self.attr_pairs = attr_pairs

    @property
    def attr_pairs(self):
        """Gets the attr_pairs of this AttrPairRules.

        属性对。

        :return: The attr_pairs of this AttrPairRules.
        :rtype: list[:class:`huaweicloudsdkres.v1.AttrPair`]
        """
        return self._attr_pairs

    @attr_pairs.setter
    def attr_pairs(self, attr_pairs):
        """Sets the attr_pairs of this AttrPairRules.

        属性对。

        :param attr_pairs: The attr_pairs of this AttrPairRules.
        :type attr_pairs: list[:class:`huaweicloudsdkres.v1.AttrPair`]
        """
        self._attr_pairs = attr_pairs

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
        if not isinstance(other, AttrPairRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
