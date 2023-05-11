# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAllTagsTagsResp:

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
        'values': 'list[str]'
    }

    attribute_map = {
        'key': 'key',
        'values': 'values'
    }

    def __init__(self, key=None, values=None):
        """ShowAllTagsTagsResp

        The model defined in huaweicloud sdk

        :param key: 集群标签的key值。
        :type key: str
        :param values: 集群标签的value值列表。
        :type values: list[str]
        """
        
        

        self._key = None
        self._values = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if values is not None:
            self.values = values

    @property
    def key(self):
        """Gets the key of this ShowAllTagsTagsResp.

        集群标签的key值。

        :return: The key of this ShowAllTagsTagsResp.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ShowAllTagsTagsResp.

        集群标签的key值。

        :param key: The key of this ShowAllTagsTagsResp.
        :type key: str
        """
        self._key = key

    @property
    def values(self):
        """Gets the values of this ShowAllTagsTagsResp.

        集群标签的value值列表。

        :return: The values of this ShowAllTagsTagsResp.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ShowAllTagsTagsResp.

        集群标签的value值列表。

        :param values: The values of this ShowAllTagsTagsResp.
        :type values: list[str]
        """
        self._values = values

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
        if not isinstance(other, ShowAllTagsTagsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
