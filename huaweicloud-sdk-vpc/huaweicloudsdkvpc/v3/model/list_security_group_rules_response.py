# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListSecurityGroupRulesResponse(SdkResponse):


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
        'security_group_rules': 'list[SecurityGroupRule]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'request_id': 'request_id',
        'security_group_rules': 'security_group_rules',
        'page_info': 'page_info'
    }

    def __init__(self, request_id=None, security_group_rules=None, page_info=None):
        """ListSecurityGroupRulesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._request_id = None
        self._security_group_rules = None
        self._page_info = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if security_group_rules is not None:
            self.security_group_rules = security_group_rules
        if page_info is not None:
            self.page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListSecurityGroupRulesResponse.

        请求ID

        :return: The request_id of this ListSecurityGroupRulesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListSecurityGroupRulesResponse.

        请求ID

        :param request_id: The request_id of this ListSecurityGroupRulesResponse.
        :type: str
        """
        self._request_id = request_id

    @property
    def security_group_rules(self):
        """Gets the security_group_rules of this ListSecurityGroupRulesResponse.

        安全组规则列表响应体

        :return: The security_group_rules of this ListSecurityGroupRulesResponse.
        :rtype: list[SecurityGroupRule]
        """
        return self._security_group_rules

    @security_group_rules.setter
    def security_group_rules(self, security_group_rules):
        """Sets the security_group_rules of this ListSecurityGroupRulesResponse.

        安全组规则列表响应体

        :param security_group_rules: The security_group_rules of this ListSecurityGroupRulesResponse.
        :type: list[SecurityGroupRule]
        """
        self._security_group_rules = security_group_rules

    @property
    def page_info(self):
        """Gets the page_info of this ListSecurityGroupRulesResponse.


        :return: The page_info of this ListSecurityGroupRulesResponse.
        :rtype: PageInfo
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListSecurityGroupRulesResponse.


        :param page_info: The page_info of this ListSecurityGroupRulesResponse.
        :type: PageInfo
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
        if not isinstance(other, ListSecurityGroupRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
