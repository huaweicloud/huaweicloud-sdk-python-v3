# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateResourceOwner:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'new_owner': 'str',
        'group_name': 'str',
        'resource_name': 'str'
    }

    attribute_map = {
        'new_owner': 'new_owner',
        'group_name': 'group_name',
        'resource_name': 'resource_name'
    }

    def __init__(self, new_owner=None, group_name=None, resource_name=None):
        """UpdateResourceOwner

        The model defined in huaweicloud sdk

        :param new_owner: 新用户名,只能包含数字、英文字母、下划线和中划线且不能以数字开头,长度在5-32字符之间
        :type new_owner: str
        :param group_name: 组名,名称只能包含数字、英文字母、点、下划线和中划线,长度不能超过64字符
        :type group_name: str
        :param resource_name: 包名,包名,长度（包含文件后缀）不能超过128个字符
        :type resource_name: str
        """
        
        

        self._new_owner = None
        self._group_name = None
        self._resource_name = None
        self.discriminator = None

        self.new_owner = new_owner
        self.group_name = group_name
        if resource_name is not None:
            self.resource_name = resource_name

    @property
    def new_owner(self):
        """Gets the new_owner of this UpdateResourceOwner.

        新用户名,只能包含数字、英文字母、下划线和中划线且不能以数字开头,长度在5-32字符之间

        :return: The new_owner of this UpdateResourceOwner.
        :rtype: str
        """
        return self._new_owner

    @new_owner.setter
    def new_owner(self, new_owner):
        """Sets the new_owner of this UpdateResourceOwner.

        新用户名,只能包含数字、英文字母、下划线和中划线且不能以数字开头,长度在5-32字符之间

        :param new_owner: The new_owner of this UpdateResourceOwner.
        :type new_owner: str
        """
        self._new_owner = new_owner

    @property
    def group_name(self):
        """Gets the group_name of this UpdateResourceOwner.

        组名,名称只能包含数字、英文字母、点、下划线和中划线,长度不能超过64字符

        :return: The group_name of this UpdateResourceOwner.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this UpdateResourceOwner.

        组名,名称只能包含数字、英文字母、点、下划线和中划线,长度不能超过64字符

        :param group_name: The group_name of this UpdateResourceOwner.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def resource_name(self):
        """Gets the resource_name of this UpdateResourceOwner.

        包名,包名,长度（包含文件后缀）不能超过128个字符

        :return: The resource_name of this UpdateResourceOwner.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this UpdateResourceOwner.

        包名,包名,长度（包含文件后缀）不能超过128个字符

        :param resource_name: The resource_name of this UpdateResourceOwner.
        :type resource_name: str
        """
        self._resource_name = resource_name

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
        if not isinstance(other, UpdateResourceOwner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
