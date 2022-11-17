# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronListSecurityGroupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'security_groups': 'list[NeutronSecurityGroup]',
        'security_groups_links': 'list[NeutronPageLink]'
    }

    attribute_map = {
        'security_groups': 'security_groups',
        'security_groups_links': 'security_groups_links'
    }

    def __init__(self, security_groups=None, security_groups_links=None):
        """NeutronListSecurityGroupsResponse

        The model defined in huaweicloud sdk

        :param security_groups: 安全组对象列表
        :type security_groups: list[:class:`huaweicloudsdkvpc.v2.NeutronSecurityGroup`]
        :param security_groups_links: 分页信息
        :type security_groups_links: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        
        super(NeutronListSecurityGroupsResponse, self).__init__()

        self._security_groups = None
        self._security_groups_links = None
        self.discriminator = None

        if security_groups is not None:
            self.security_groups = security_groups
        if security_groups_links is not None:
            self.security_groups_links = security_groups_links

    @property
    def security_groups(self):
        """Gets the security_groups of this NeutronListSecurityGroupsResponse.

        安全组对象列表

        :return: The security_groups of this NeutronListSecurityGroupsResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.NeutronSecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this NeutronListSecurityGroupsResponse.

        安全组对象列表

        :param security_groups: The security_groups of this NeutronListSecurityGroupsResponse.
        :type security_groups: list[:class:`huaweicloudsdkvpc.v2.NeutronSecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def security_groups_links(self):
        """Gets the security_groups_links of this NeutronListSecurityGroupsResponse.

        分页信息

        :return: The security_groups_links of this NeutronListSecurityGroupsResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        return self._security_groups_links

    @security_groups_links.setter
    def security_groups_links(self, security_groups_links):
        """Sets the security_groups_links of this NeutronListSecurityGroupsResponse.

        分页信息

        :param security_groups_links: The security_groups_links of this NeutronListSecurityGroupsResponse.
        :type security_groups_links: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        self._security_groups_links = security_groups_links

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
        if not isinstance(other, NeutronListSecurityGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
