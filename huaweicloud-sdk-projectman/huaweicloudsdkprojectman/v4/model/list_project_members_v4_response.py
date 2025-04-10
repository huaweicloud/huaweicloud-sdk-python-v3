# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectMembersV4Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'members': 'list[MemberListV4Members]',
        'total': 'int'
    }

    attribute_map = {
        'members': 'members',
        'total': 'total'
    }

    def __init__(self, members=None, total=None):
        r"""ListProjectMembersV4Response

        The model defined in huaweicloud sdk

        :param members: 项目成员列表
        :type members: list[:class:`huaweicloudsdkprojectman.v4.MemberListV4Members`]
        :param total: 总数
        :type total: int
        """
        
        super(ListProjectMembersV4Response, self).__init__()

        self._members = None
        self._total = None
        self.discriminator = None

        if members is not None:
            self.members = members
        if total is not None:
            self.total = total

    @property
    def members(self):
        r"""Gets the members of this ListProjectMembersV4Response.

        项目成员列表

        :return: The members of this ListProjectMembersV4Response.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.MemberListV4Members`]
        """
        return self._members

    @members.setter
    def members(self, members):
        r"""Sets the members of this ListProjectMembersV4Response.

        项目成员列表

        :param members: The members of this ListProjectMembersV4Response.
        :type members: list[:class:`huaweicloudsdkprojectman.v4.MemberListV4Members`]
        """
        self._members = members

    @property
    def total(self):
        r"""Gets the total of this ListProjectMembersV4Response.

        总数

        :return: The total of this ListProjectMembersV4Response.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListProjectMembersV4Response.

        总数

        :param total: The total of this ListProjectMembersV4Response.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListProjectMembersV4Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
