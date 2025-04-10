# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IsMemberInGroupsReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_ids': 'list[str]',
        'member_id': 'MemberIdDto'
    }

    attribute_map = {
        'group_ids': 'group_ids',
        'member_id': 'member_id'
    }

    def __init__(self, group_ids=None, member_id=None):
        r"""IsMemberInGroupsReqBody

        The model defined in huaweicloud sdk

        :param group_ids: 用户组标识符列表
        :type group_ids: list[str]
        :param member_id: 
        :type member_id: :class:`huaweicloudsdkidentitycenterstore.v1.MemberIdDto`
        """
        
        

        self._group_ids = None
        self._member_id = None
        self.discriminator = None

        self.group_ids = group_ids
        self.member_id = member_id

    @property
    def group_ids(self):
        r"""Gets the group_ids of this IsMemberInGroupsReqBody.

        用户组标识符列表

        :return: The group_ids of this IsMemberInGroupsReqBody.
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        r"""Sets the group_ids of this IsMemberInGroupsReqBody.

        用户组标识符列表

        :param group_ids: The group_ids of this IsMemberInGroupsReqBody.
        :type group_ids: list[str]
        """
        self._group_ids = group_ids

    @property
    def member_id(self):
        r"""Gets the member_id of this IsMemberInGroupsReqBody.

        :return: The member_id of this IsMemberInGroupsReqBody.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.MemberIdDto`
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        r"""Sets the member_id of this IsMemberInGroupsReqBody.

        :param member_id: The member_id of this IsMemberInGroupsReqBody.
        :type member_id: :class:`huaweicloudsdkidentitycenterstore.v1.MemberIdDto`
        """
        self._member_id = member_id

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
        if not isinstance(other, IsMemberInGroupsReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
