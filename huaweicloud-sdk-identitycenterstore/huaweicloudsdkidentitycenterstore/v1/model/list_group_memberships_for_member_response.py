# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGroupMembershipsForMemberResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_memberships': 'list[GroupMembershipItem]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'group_memberships': 'group_memberships',
        'page_info': 'page_info'
    }

    def __init__(self, group_memberships=None, page_info=None):
        r"""ListGroupMembershipsForMemberResponse

        The model defined in huaweicloud sdk

        :param group_memberships: 满足查询条件的关联关系对象列表
        :type group_memberships: list[:class:`huaweicloudsdkidentitycenterstore.v1.GroupMembershipItem`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkidentitycenterstore.v1.PageInfoDto`
        """
        
        super(ListGroupMembershipsForMemberResponse, self).__init__()

        self._group_memberships = None
        self._page_info = None
        self.discriminator = None

        if group_memberships is not None:
            self.group_memberships = group_memberships
        if page_info is not None:
            self.page_info = page_info

    @property
    def group_memberships(self):
        r"""Gets the group_memberships of this ListGroupMembershipsForMemberResponse.

        满足查询条件的关联关系对象列表

        :return: The group_memberships of this ListGroupMembershipsForMemberResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.GroupMembershipItem`]
        """
        return self._group_memberships

    @group_memberships.setter
    def group_memberships(self, group_memberships):
        r"""Sets the group_memberships of this ListGroupMembershipsForMemberResponse.

        满足查询条件的关联关系对象列表

        :param group_memberships: The group_memberships of this ListGroupMembershipsForMemberResponse.
        :type group_memberships: list[:class:`huaweicloudsdkidentitycenterstore.v1.GroupMembershipItem`]
        """
        self._group_memberships = group_memberships

    @property
    def page_info(self):
        r"""Gets the page_info of this ListGroupMembershipsForMemberResponse.

        :return: The page_info of this ListGroupMembershipsForMemberResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListGroupMembershipsForMemberResponse.

        :param page_info: The page_info of this ListGroupMembershipsForMemberResponse.
        :type page_info: :class:`huaweicloudsdkidentitycenterstore.v1.PageInfoDto`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListGroupMembershipsForMemberResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
