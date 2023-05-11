# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetHostGroupListTag:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag_type': 'str',
        'tag_list': 'list[HostGroupTag]'
    }

    attribute_map = {
        'tag_type': 'tag_type',
        'tag_list': 'tag_list'
    }

    def __init__(self, tag_type=None, tag_list=None):
        """GetHostGroupListTag

        The model defined in huaweicloud sdk

        :param tag_type: 标签类型。AND：标签过滤的逻辑为与，OR：标签过滤的逻辑为或
        :type tag_type: str
        :param tag_list: 主机组标签
        :type tag_list: list[:class:`huaweicloudsdklts.v2.HostGroupTag`]
        """
        
        

        self._tag_type = None
        self._tag_list = None
        self.discriminator = None

        if tag_type is not None:
            self.tag_type = tag_type
        if tag_list is not None:
            self.tag_list = tag_list

    @property
    def tag_type(self):
        """Gets the tag_type of this GetHostGroupListTag.

        标签类型。AND：标签过滤的逻辑为与，OR：标签过滤的逻辑为或

        :return: The tag_type of this GetHostGroupListTag.
        :rtype: str
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        """Sets the tag_type of this GetHostGroupListTag.

        标签类型。AND：标签过滤的逻辑为与，OR：标签过滤的逻辑为或

        :param tag_type: The tag_type of this GetHostGroupListTag.
        :type tag_type: str
        """
        self._tag_type = tag_type

    @property
    def tag_list(self):
        """Gets the tag_list of this GetHostGroupListTag.

        主机组标签

        :return: The tag_list of this GetHostGroupListTag.
        :rtype: list[:class:`huaweicloudsdklts.v2.HostGroupTag`]
        """
        return self._tag_list

    @tag_list.setter
    def tag_list(self, tag_list):
        """Sets the tag_list of this GetHostGroupListTag.

        主机组标签

        :param tag_list: The tag_list of this GetHostGroupListTag.
        :type tag_list: list[:class:`huaweicloudsdklts.v2.HostGroupTag`]
        """
        self._tag_list = tag_list

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
        if not isinstance(other, GetHostGroupListTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
