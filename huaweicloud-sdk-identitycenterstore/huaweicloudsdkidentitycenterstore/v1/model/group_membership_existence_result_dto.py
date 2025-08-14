# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupMembershipExistenceResultDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'member_id': 'MemberIdDto',
        'membership_exists': 'bool'
    }

    attribute_map = {
        'group_id': 'group_id',
        'member_id': 'member_id',
        'membership_exists': 'membership_exists'
    }

    def __init__(self, group_id=None, member_id=None, membership_exists=None):
        r"""GroupMembershipExistenceResultDto

        The model defined in huaweicloud sdk

        :param group_id: 身份源中IdentityCenter用户组的全局唯一标识符（ID）
        :type group_id: str
        :param member_id: 
        :type member_id: :class:`huaweicloudsdkidentitycenterstore.v1.MemberIdDto`
        :param membership_exists: 一个布尔值，表示用户是否在组中
        :type membership_exists: bool
        """
        
        

        self._group_id = None
        self._member_id = None
        self._membership_exists = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if member_id is not None:
            self.member_id = member_id
        if membership_exists is not None:
            self.membership_exists = membership_exists

    @property
    def group_id(self):
        r"""Gets the group_id of this GroupMembershipExistenceResultDto.

        身份源中IdentityCenter用户组的全局唯一标识符（ID）

        :return: The group_id of this GroupMembershipExistenceResultDto.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this GroupMembershipExistenceResultDto.

        身份源中IdentityCenter用户组的全局唯一标识符（ID）

        :param group_id: The group_id of this GroupMembershipExistenceResultDto.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def member_id(self):
        r"""Gets the member_id of this GroupMembershipExistenceResultDto.

        :return: The member_id of this GroupMembershipExistenceResultDto.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.MemberIdDto`
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        r"""Sets the member_id of this GroupMembershipExistenceResultDto.

        :param member_id: The member_id of this GroupMembershipExistenceResultDto.
        :type member_id: :class:`huaweicloudsdkidentitycenterstore.v1.MemberIdDto`
        """
        self._member_id = member_id

    @property
    def membership_exists(self):
        r"""Gets the membership_exists of this GroupMembershipExistenceResultDto.

        一个布尔值，表示用户是否在组中

        :return: The membership_exists of this GroupMembershipExistenceResultDto.
        :rtype: bool
        """
        return self._membership_exists

    @membership_exists.setter
    def membership_exists(self, membership_exists):
        r"""Sets the membership_exists of this GroupMembershipExistenceResultDto.

        一个布尔值，表示用户是否在组中

        :param membership_exists: The membership_exists of this GroupMembershipExistenceResultDto.
        :type membership_exists: bool
        """
        self._membership_exists = membership_exists

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
        if not isinstance(other, GroupMembershipExistenceResultDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
