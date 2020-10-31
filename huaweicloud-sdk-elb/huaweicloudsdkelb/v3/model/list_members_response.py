# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListMembersResponse(SdkResponse):


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
        """ListMembersResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

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
        """Gets the request_id of this ListMembersResponse.

        请求ID。  注：自动生成 。

        :return: The request_id of this ListMembersResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListMembersResponse.

        请求ID。  注：自动生成 。

        :param request_id: The request_id of this ListMembersResponse.
        :type: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        """Gets the page_info of this ListMembersResponse.


        :return: The page_info of this ListMembersResponse.
        :rtype: PageInfo
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListMembersResponse.


        :param page_info: The page_info of this ListMembersResponse.
        :type: PageInfo
        """
        self._page_info = page_info

    @property
    def members(self):
        """Gets the members of this ListMembersResponse.

        后端服务器对象列表。

        :return: The members of this ListMembersResponse.
        :rtype: list[Member]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this ListMembersResponse.

        后端服务器对象列表。

        :param members: The members of this ListMembersResponse.
        :type: list[Member]
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListMembersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
