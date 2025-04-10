# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchHandTags:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[Tag]',
        'action': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'action': 'action'
    }

    def __init__(self, tags=None, action=None):
        r"""BatchHandTags

        The model defined in huaweicloud sdk

        :param tags: 标签列表。删除时tags结构体不能缺失。
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        :param action: 操作标识（区分大小写）：create（创建）、delete（删除）。
        :type action: str
        """
        
        

        self._tags = None
        self._action = None
        self.discriminator = None

        self.tags = tags
        self.action = action

    @property
    def tags(self):
        r"""Gets the tags of this BatchHandTags.

        标签列表。删除时tags结构体不能缺失。

        :return: The tags of this BatchHandTags.
        :rtype: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this BatchHandTags.

        标签列表。删除时tags结构体不能缺失。

        :param tags: The tags of this BatchHandTags.
        :type tags: list[:class:`huaweicloudsdkdns.v2.Tag`]
        """
        self._tags = tags

    @property
    def action(self):
        r"""Gets the action of this BatchHandTags.

        操作标识（区分大小写）：create（创建）、delete（删除）。

        :return: The action of this BatchHandTags.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BatchHandTags.

        操作标识（区分大小写）：create（创建）、delete（删除）。

        :param action: The action of this BatchHandTags.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, BatchHandTags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
