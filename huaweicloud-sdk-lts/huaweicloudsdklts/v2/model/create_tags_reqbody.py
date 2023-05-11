# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTagsReqbody:

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
        'is_open': 'bool',
        'tags': 'list[TagsBody]'
    }

    attribute_map = {
        'action': 'action',
        'is_open': 'is_open',
        'tags': 'tags'
    }

    def __init__(self, action=None, is_open=None, tags=None):
        """CreateTagsReqbody

        The model defined in huaweicloud sdk

        :param action: 添加标签方式
        :type action: str
        :param is_open: 是否对外接口调用
        :type is_open: bool
        :param tags: 标签字段信息
        :type tags: list[:class:`huaweicloudsdklts.v2.TagsBody`]
        """
        
        

        self._action = None
        self._is_open = None
        self._tags = None
        self.discriminator = None

        self.action = action
        self.is_open = is_open
        self.tags = tags

    @property
    def action(self):
        """Gets the action of this CreateTagsReqbody.

        添加标签方式

        :return: The action of this CreateTagsReqbody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CreateTagsReqbody.

        添加标签方式

        :param action: The action of this CreateTagsReqbody.
        :type action: str
        """
        self._action = action

    @property
    def is_open(self):
        """Gets the is_open of this CreateTagsReqbody.

        是否对外接口调用

        :return: The is_open of this CreateTagsReqbody.
        :rtype: bool
        """
        return self._is_open

    @is_open.setter
    def is_open(self, is_open):
        """Sets the is_open of this CreateTagsReqbody.

        是否对外接口调用

        :param is_open: The is_open of this CreateTagsReqbody.
        :type is_open: bool
        """
        self._is_open = is_open

    @property
    def tags(self):
        """Gets the tags of this CreateTagsReqbody.

        标签字段信息

        :return: The tags of this CreateTagsReqbody.
        :rtype: list[:class:`huaweicloudsdklts.v2.TagsBody`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateTagsReqbody.

        标签字段信息

        :param tags: The tags of this CreateTagsReqbody.
        :type tags: list[:class:`huaweicloudsdklts.v2.TagsBody`]
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
        if not isinstance(other, CreateTagsReqbody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
