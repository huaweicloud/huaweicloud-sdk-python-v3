# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StacksTags:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stack_list': 'list[StackInfo]',
        'tags': 'list[str]'
    }

    attribute_map = {
        'stack_list': 'stack_list',
        'tags': 'tags'
    }

    def __init__(self, stack_list=None, tags=None):
        r"""StacksTags

        The model defined in huaweicloud sdk

        :param stack_list: 技术栈列表
        :type stack_list: list[:class:`huaweicloudsdkcloudide.v2.StackInfo`]
        :param tags: 技术栈tag集合
        :type tags: list[str]
        """
        
        

        self._stack_list = None
        self._tags = None
        self.discriminator = None

        if stack_list is not None:
            self.stack_list = stack_list
        if tags is not None:
            self.tags = tags

    @property
    def stack_list(self):
        r"""Gets the stack_list of this StacksTags.

        技术栈列表

        :return: The stack_list of this StacksTags.
        :rtype: list[:class:`huaweicloudsdkcloudide.v2.StackInfo`]
        """
        return self._stack_list

    @stack_list.setter
    def stack_list(self, stack_list):
        r"""Sets the stack_list of this StacksTags.

        技术栈列表

        :param stack_list: The stack_list of this StacksTags.
        :type stack_list: list[:class:`huaweicloudsdkcloudide.v2.StackInfo`]
        """
        self._stack_list = stack_list

    @property
    def tags(self):
        r"""Gets the tags of this StacksTags.

        技术栈tag集合

        :return: The tags of this StacksTags.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this StacksTags.

        技术栈tag集合

        :param tags: The tags of this StacksTags.
        :type tags: list[str]
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
        if not isinstance(other, StacksTags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
