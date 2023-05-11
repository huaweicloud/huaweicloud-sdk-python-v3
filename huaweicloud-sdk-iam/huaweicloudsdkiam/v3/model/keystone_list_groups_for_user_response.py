# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneListGroupsForUserResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'groups': 'list[KeystoneGroupResult]',
        'links': 'Links'
    }

    attribute_map = {
        'groups': 'groups',
        'links': 'links'
    }

    def __init__(self, groups=None, links=None):
        """KeystoneListGroupsForUserResponse

        The model defined in huaweicloud sdk

        :param groups: 用户组信息列表。
        :type groups: list[:class:`huaweicloudsdkiam.v3.KeystoneGroupResult`]
        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        """
        
        super(KeystoneListGroupsForUserResponse, self).__init__()

        self._groups = None
        self._links = None
        self.discriminator = None

        if groups is not None:
            self.groups = groups
        if links is not None:
            self.links = links

    @property
    def groups(self):
        """Gets the groups of this KeystoneListGroupsForUserResponse.

        用户组信息列表。

        :return: The groups of this KeystoneListGroupsForUserResponse.
        :rtype: list[:class:`huaweicloudsdkiam.v3.KeystoneGroupResult`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this KeystoneListGroupsForUserResponse.

        用户组信息列表。

        :param groups: The groups of this KeystoneListGroupsForUserResponse.
        :type groups: list[:class:`huaweicloudsdkiam.v3.KeystoneGroupResult`]
        """
        self._groups = groups

    @property
    def links(self):
        """Gets the links of this KeystoneListGroupsForUserResponse.

        :return: The links of this KeystoneListGroupsForUserResponse.
        :rtype: :class:`huaweicloudsdkiam.v3.Links`
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this KeystoneListGroupsForUserResponse.

        :param links: The links of this KeystoneListGroupsForUserResponse.
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        """
        self._links = links

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
        if not isinstance(other, KeystoneListGroupsForUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
