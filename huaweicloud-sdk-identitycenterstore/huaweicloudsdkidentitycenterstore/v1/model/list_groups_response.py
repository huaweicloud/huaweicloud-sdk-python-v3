# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGroupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'groups': 'list[GroupDto]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'groups': 'groups',
        'page_info': 'page_info'
    }

    def __init__(self, groups=None, page_info=None):
        r"""ListGroupsResponse

        The model defined in huaweicloud sdk

        :param groups: 满足查询条件的用户组对象列表
        :type groups: list[:class:`huaweicloudsdkidentitycenterstore.v1.GroupDto`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkidentitycenterstore.v1.PageInfoDto`
        """
        
        super(ListGroupsResponse, self).__init__()

        self._groups = None
        self._page_info = None
        self.discriminator = None

        if groups is not None:
            self.groups = groups
        if page_info is not None:
            self.page_info = page_info

    @property
    def groups(self):
        r"""Gets the groups of this ListGroupsResponse.

        满足查询条件的用户组对象列表

        :return: The groups of this ListGroupsResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.GroupDto`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this ListGroupsResponse.

        满足查询条件的用户组对象列表

        :param groups: The groups of this ListGroupsResponse.
        :type groups: list[:class:`huaweicloudsdkidentitycenterstore.v1.GroupDto`]
        """
        self._groups = groups

    @property
    def page_info(self):
        r"""Gets the page_info of this ListGroupsResponse.

        :return: The page_info of this ListGroupsResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListGroupsResponse.

        :param page_info: The page_info of this ListGroupsResponse.
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
        if not isinstance(other, ListGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
