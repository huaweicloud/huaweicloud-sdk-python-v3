# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberPolicyItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'member_id': 'str',
        'member_name': 'str',
        'member_type': 'str'
    }

    attribute_map = {
        'member_id': 'member_id',
        'member_name': 'member_name',
        'member_type': 'member_type'
    }

    def __init__(self, member_id=None, member_name=None, member_type=None):
        r"""MemberPolicyItem

        The model defined in huaweicloud sdk

        :param member_id: 成员id
        :type member_id: str
        :param member_name: 成员名称
        :type member_name: str
        :param member_type: 成员类型:USER,USER_GROUP,WORKSPACE_ROLE，分别代表空间用户、空间用户组、空间角色
        :type member_type: str
        """
        
        

        self._member_id = None
        self._member_name = None
        self._member_type = None
        self.discriminator = None

        self.member_id = member_id
        self.member_name = member_name
        if member_type is not None:
            self.member_type = member_type

    @property
    def member_id(self):
        r"""Gets the member_id of this MemberPolicyItem.

        成员id

        :return: The member_id of this MemberPolicyItem.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        r"""Sets the member_id of this MemberPolicyItem.

        成员id

        :param member_id: The member_id of this MemberPolicyItem.
        :type member_id: str
        """
        self._member_id = member_id

    @property
    def member_name(self):
        r"""Gets the member_name of this MemberPolicyItem.

        成员名称

        :return: The member_name of this MemberPolicyItem.
        :rtype: str
        """
        return self._member_name

    @member_name.setter
    def member_name(self, member_name):
        r"""Sets the member_name of this MemberPolicyItem.

        成员名称

        :param member_name: The member_name of this MemberPolicyItem.
        :type member_name: str
        """
        self._member_name = member_name

    @property
    def member_type(self):
        r"""Gets the member_type of this MemberPolicyItem.

        成员类型:USER,USER_GROUP,WORKSPACE_ROLE，分别代表空间用户、空间用户组、空间角色

        :return: The member_type of this MemberPolicyItem.
        :rtype: str
        """
        return self._member_type

    @member_type.setter
    def member_type(self, member_type):
        r"""Sets the member_type of this MemberPolicyItem.

        成员类型:USER,USER_GROUP,WORKSPACE_ROLE，分别代表空间用户、空间用户组、空间角色

        :param member_type: The member_type of this MemberPolicyItem.
        :type member_type: str
        """
        self._member_type = member_type

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
        if not isinstance(other, MemberPolicyItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
