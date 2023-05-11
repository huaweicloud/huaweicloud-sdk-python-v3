# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchOperateResourceTagsRequestBody:

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
        'tags': 'list[Tag]',
        'sys_tags': 'list[Tag]'
    }

    attribute_map = {
        'action': 'action',
        'tags': 'tags',
        'sys_tags': 'sys_tags'
    }

    def __init__(self, action=None, tags=None, sys_tags=None):
        """BatchOperateResourceTagsRequestBody

        The model defined in huaweicloud sdk

        :param action: 功能说明：操作标识。 取值范围： create（创建） delete（删除）
        :type action: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkdc.v3.Tag`]
        :param sys_tags: 标签列表。
        :type sys_tags: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        
        

        self._action = None
        self._tags = None
        self._sys_tags = None
        self.discriminator = None

        self.action = action
        if tags is not None:
            self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags

    @property
    def action(self):
        """Gets the action of this BatchOperateResourceTagsRequestBody.

        功能说明：操作标识。 取值范围： create（创建） delete（删除）

        :return: The action of this BatchOperateResourceTagsRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this BatchOperateResourceTagsRequestBody.

        功能说明：操作标识。 取值范围： create（创建） delete（删除）

        :param action: The action of this BatchOperateResourceTagsRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def tags(self):
        """Gets the tags of this BatchOperateResourceTagsRequestBody.

        标签列表。

        :return: The tags of this BatchOperateResourceTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BatchOperateResourceTagsRequestBody.

        标签列表。

        :param tags: The tags of this BatchOperateResourceTagsRequestBody.
        :type tags: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        """Gets the sys_tags of this BatchOperateResourceTagsRequestBody.

        标签列表。

        :return: The sys_tags of this BatchOperateResourceTagsRequestBody.
        :rtype: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this BatchOperateResourceTagsRequestBody.

        标签列表。

        :param sys_tags: The sys_tags of this BatchOperateResourceTagsRequestBody.
        :type sys_tags: list[:class:`huaweicloudsdkdc.v3.Tag`]
        """
        self._sys_tags = sys_tags

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
        if not isinstance(other, BatchOperateResourceTagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
