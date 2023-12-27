# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttentionDO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attention': 'str',
        'ids': 'list[str]',
        'format': 'str'
    }

    attribute_map = {
        'attention': 'attention',
        'ids': 'ids',
        'format': 'format'
    }

    def __init__(self, attention=None, ids=None, format=None):
        """AttentionDO

        The model defined in huaweicloud sdk

        :param attention: 关注/取消关注
        :type attention: str
        :param ids: 组件id列表
        :type ids: list[str]
        :param format: 格式
        :type format: str
        """
        
        

        self._attention = None
        self._ids = None
        self._format = None
        self.discriminator = None

        self.attention = attention
        self.ids = ids
        if format is not None:
            self.format = format

    @property
    def attention(self):
        """Gets the attention of this AttentionDO.

        关注/取消关注

        :return: The attention of this AttentionDO.
        :rtype: str
        """
        return self._attention

    @attention.setter
    def attention(self, attention):
        """Sets the attention of this AttentionDO.

        关注/取消关注

        :param attention: The attention of this AttentionDO.
        :type attention: str
        """
        self._attention = attention

    @property
    def ids(self):
        """Gets the ids of this AttentionDO.

        组件id列表

        :return: The ids of this AttentionDO.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this AttentionDO.

        组件id列表

        :param ids: The ids of this AttentionDO.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def format(self):
        """Gets the format of this AttentionDO.

        格式

        :return: The format of this AttentionDO.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this AttentionDO.

        格式

        :param format: The format of this AttentionDO.
        :type format: str
        """
        self._format = format

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
        if not isinstance(other, AttentionDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
