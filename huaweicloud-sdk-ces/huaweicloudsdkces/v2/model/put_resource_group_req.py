# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutResourceGroupReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'tags': 'list[ResourceGroupTagRelation]'
    }

    attribute_map = {
        'group_name': 'group_name',
        'tags': 'tags'
    }

    def __init__(self, group_name=None, tags=None):
        """PutResourceGroupReq

        The model defined in huaweicloud sdk

        :param group_name: 资源分组名称，只能为字母、数字、汉字、-、_，最大长度为128
        :type group_name: str
        :param tags: 标签动态匹配时的关联标签,type为TAG时必传
        :type tags: list[:class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`]
        """
        
        

        self._group_name = None
        self._tags = None
        self.discriminator = None

        self.group_name = group_name
        if tags is not None:
            self.tags = tags

    @property
    def group_name(self):
        """Gets the group_name of this PutResourceGroupReq.

        资源分组名称，只能为字母、数字、汉字、-、_，最大长度为128

        :return: The group_name of this PutResourceGroupReq.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this PutResourceGroupReq.

        资源分组名称，只能为字母、数字、汉字、-、_，最大长度为128

        :param group_name: The group_name of this PutResourceGroupReq.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def tags(self):
        """Gets the tags of this PutResourceGroupReq.

        标签动态匹配时的关联标签,type为TAG时必传

        :return: The tags of this PutResourceGroupReq.
        :rtype: list[:class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PutResourceGroupReq.

        标签动态匹配时的关联标签,type为TAG时必传

        :param tags: The tags of this PutResourceGroupReq.
        :type tags: list[:class:`huaweicloudsdkces.v2.ResourceGroupTagRelation`]
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
        if not isinstance(other, PutResourceGroupReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
