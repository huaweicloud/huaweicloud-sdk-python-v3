# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListSecurityGroupsResponse(SdkResponse):


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
        'security_group': 'list[SecurityGroup]',
        'page_info': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'security_group': 'security_group',
        'page_info': 'page_info'
    }

    def __init__(self, request_id=None, security_group=None, page_info=None):
        """ListSecurityGroupsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._request_id = None
        self._security_group = None
        self._page_info = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if security_group is not None:
            self.security_group = security_group
        if page_info is not None:
            self.page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListSecurityGroupsResponse.

        请求ID

        :return: The request_id of this ListSecurityGroupsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListSecurityGroupsResponse.

        请求ID

        :param request_id: The request_id of this ListSecurityGroupsResponse.
        :type: str
        """
        self._request_id = request_id

    @property
    def security_group(self):
        """Gets the security_group of this ListSecurityGroupsResponse.

        安全组列表响应体

        :return: The security_group of this ListSecurityGroupsResponse.
        :rtype: list[SecurityGroup]
        """
        return self._security_group

    @security_group.setter
    def security_group(self, security_group):
        """Sets the security_group of this ListSecurityGroupsResponse.

        安全组列表响应体

        :param security_group: The security_group of this ListSecurityGroupsResponse.
        :type: list[SecurityGroup]
        """
        self._security_group = security_group

    @property
    def page_info(self):
        """Gets the page_info of this ListSecurityGroupsResponse.

        分页信息

        :return: The page_info of this ListSecurityGroupsResponse.
        :rtype: str
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListSecurityGroupsResponse.

        分页信息

        :param page_info: The page_info of this ListSecurityGroupsResponse.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSecurityGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
