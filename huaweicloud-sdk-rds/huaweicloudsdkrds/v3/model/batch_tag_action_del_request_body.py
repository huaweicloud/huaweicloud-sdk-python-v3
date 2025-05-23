# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchTagActionDelRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'tags': 'list[TagDelWithKeyValue]'
    }

    attribute_map = {
        'action': 'action',
        'tags': 'tags'
    }

    def __init__(self, action=None, tags=None):
        r"""BatchTagActionDelRequestBody

        The model defined in huaweicloud sdk

        :param action: 操作标识（区分大小写）：删除时为“delete”。
        :type action: str
        :param tags: 标签列表。单个实例总标签数上限20个。
        :type tags: list[:class:`huaweicloudsdkrds.v3.TagDelWithKeyValue`]
        """
        
        

        self._action = None
        self._tags = None
        self.discriminator = None

        self.action = action
        self.tags = tags

    @property
    def action(self):
        r"""Gets the action of this BatchTagActionDelRequestBody.

        操作标识（区分大小写）：删除时为“delete”。

        :return: The action of this BatchTagActionDelRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BatchTagActionDelRequestBody.

        操作标识（区分大小写）：删除时为“delete”。

        :param action: The action of this BatchTagActionDelRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def tags(self):
        r"""Gets the tags of this BatchTagActionDelRequestBody.

        标签列表。单个实例总标签数上限20个。

        :return: The tags of this BatchTagActionDelRequestBody.
        :rtype: list[:class:`huaweicloudsdkrds.v3.TagDelWithKeyValue`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this BatchTagActionDelRequestBody.

        标签列表。单个实例总标签数上限20个。

        :param tags: The tags of this BatchTagActionDelRequestBody.
        :type tags: list[:class:`huaweicloudsdkrds.v3.TagDelWithKeyValue`]
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
        if not isinstance(other, BatchTagActionDelRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
