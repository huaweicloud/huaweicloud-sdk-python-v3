# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceTags:

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
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'action': 'action',
        'tags': 'tags'
    }

    def __init__(self, action=None, tags=None):
        """ResourceTags

        The model defined in huaweicloud sdk

        :param action: 动作。|- create：创建。 delete：删除。
        :type action: str
        :param tags: 批量添加/删除资源标签
        :type tags: list[:class:`huaweicloudsdkcc.v2.Tag`]
        """
        
        

        self._action = None
        self._tags = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if tags is not None:
            self.tags = tags

    @property
    def action(self):
        """Gets the action of this ResourceTags.

        动作。|- create：创建。 delete：删除。

        :return: The action of this ResourceTags.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ResourceTags.

        动作。|- create：创建。 delete：删除。

        :param action: The action of this ResourceTags.
        :type action: str
        """
        self._action = action

    @property
    def tags(self):
        """Gets the tags of this ResourceTags.

        批量添加/删除资源标签

        :return: The tags of this ResourceTags.
        :rtype: list[:class:`huaweicloudsdkcc.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ResourceTags.

        批量添加/删除资源标签

        :param tags: The tags of this ResourceTags.
        :type tags: list[:class:`huaweicloudsdkcc.v2.Tag`]
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
        if not isinstance(other, ResourceTags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
