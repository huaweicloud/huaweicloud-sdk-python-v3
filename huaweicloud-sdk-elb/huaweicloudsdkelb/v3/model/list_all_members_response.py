# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllMembersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'page_info': 'PageInfo',
        'members': 'list[Member]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'page_info': 'page_info',
        'members': 'members'
    }

    def __init__(self, request_id=None, page_info=None, members=None):
        """ListAllMembersResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID。  注：自动生成 。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkelb.v3.PageInfo`
        :param members: 后端服务器对象列表。
        :type members: list[:class:`huaweicloudsdkelb.v3.Member`]
        """
        
        super(ListAllMembersResponse, self).__init__()

        self._request_id = None
        self._page_info = None
        self._members = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info
        if members is not None:
            self.members = members

    @property
    def request_id(self):
        """Gets the request_id of this ListAllMembersResponse.

        请求ID。  注：自动生成 。

        :return: The request_id of this ListAllMembersResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListAllMembersResponse.

        请求ID。  注：自动生成 。

        :param request_id: The request_id of this ListAllMembersResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        """Gets the page_info of this ListAllMembersResponse.

        :return: The page_info of this ListAllMembersResponse.
        :rtype: :class:`huaweicloudsdkelb.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListAllMembersResponse.

        :param page_info: The page_info of this ListAllMembersResponse.
        :type page_info: :class:`huaweicloudsdkelb.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def members(self):
        """Gets the members of this ListAllMembersResponse.

        后端服务器对象列表。

        :return: The members of this ListAllMembersResponse.
        :rtype: list[:class:`huaweicloudsdkelb.v3.Member`]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this ListAllMembersResponse.

        后端服务器对象列表。

        :param members: The members of this ListAllMembersResponse.
        :type members: list[:class:`huaweicloudsdkelb.v3.Member`]
        """
        self._members = members

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
        if not isinstance(other, ListAllMembersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
