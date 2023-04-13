# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StyleExtraMetaEditColorItems:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min_value': 'list[float]',
        'max_value': 'list[float]',
        'label': 'dict(str, str)'
    }

    attribute_map = {
        'min_value': 'min_value',
        'max_value': 'max_value',
        'label': 'label'
    }

    def __init__(self, min_value=None, max_value=None, label=None):
        """StyleExtraMetaEditColorItems

        The model defined in huaweicloud sdk

        :param min_value: 最小值
        :type min_value: list[float]
        :param max_value: 最大值
        :type max_value: list[float]
        :param label: 展示标签 {\&quot;cn\&quot;: \&quot;xxxxx\&quot;,\&quot;en\&quot;:\&quot;xxxxx\&quot;}
        :type label: dict(str, str)
        """
        
        

        self._min_value = None
        self._max_value = None
        self._label = None
        self.discriminator = None

        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value
        if label is not None:
            self.label = label

    @property
    def min_value(self):
        """Gets the min_value of this StyleExtraMetaEditColorItems.

        最小值

        :return: The min_value of this StyleExtraMetaEditColorItems.
        :rtype: list[float]
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this StyleExtraMetaEditColorItems.

        最小值

        :param min_value: The min_value of this StyleExtraMetaEditColorItems.
        :type min_value: list[float]
        """
        self._min_value = min_value

    @property
    def max_value(self):
        """Gets the max_value of this StyleExtraMetaEditColorItems.

        最大值

        :return: The max_value of this StyleExtraMetaEditColorItems.
        :rtype: list[float]
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this StyleExtraMetaEditColorItems.

        最大值

        :param max_value: The max_value of this StyleExtraMetaEditColorItems.
        :type max_value: list[float]
        """
        self._max_value = max_value

    @property
    def label(self):
        """Gets the label of this StyleExtraMetaEditColorItems.

        展示标签 {\"cn\": \"xxxxx\",\"en\":\"xxxxx\"}

        :return: The label of this StyleExtraMetaEditColorItems.
        :rtype: dict(str, str)
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this StyleExtraMetaEditColorItems.

        展示标签 {\"cn\": \"xxxxx\",\"en\":\"xxxxx\"}

        :param label: The label of this StyleExtraMetaEditColorItems.
        :type label: dict(str, str)
        """
        self._label = label

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
        if not isinstance(other, StyleExtraMetaEditColorItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
