# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabaseUserAuthoritiesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authority_list': 'list[GrantAuthority]',
        'count': 'int'
    }

    attribute_map = {
        'authority_list': 'authority_list',
        'count': 'count'
    }

    def __init__(self, authority_list=None, count=None):
        r"""ListDatabaseUserAuthoritiesResponse

        The model defined in huaweicloud sdk

        :param authority_list: **参数解释**： 权限详情列表。 **取值范围**： 不涉及。
        :type authority_list: list[:class:`huaweicloudsdkdws.v2.GrantAuthority`]
        :param count: **参数解释**： 权限总条数。 **取值范围**： 不涉及。
        :type count: int
        """
        
        super(ListDatabaseUserAuthoritiesResponse, self).__init__()

        self._authority_list = None
        self._count = None
        self.discriminator = None

        if authority_list is not None:
            self.authority_list = authority_list
        if count is not None:
            self.count = count

    @property
    def authority_list(self):
        r"""Gets the authority_list of this ListDatabaseUserAuthoritiesResponse.

        **参数解释**： 权限详情列表。 **取值范围**： 不涉及。

        :return: The authority_list of this ListDatabaseUserAuthoritiesResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.GrantAuthority`]
        """
        return self._authority_list

    @authority_list.setter
    def authority_list(self, authority_list):
        r"""Sets the authority_list of this ListDatabaseUserAuthoritiesResponse.

        **参数解释**： 权限详情列表。 **取值范围**： 不涉及。

        :param authority_list: The authority_list of this ListDatabaseUserAuthoritiesResponse.
        :type authority_list: list[:class:`huaweicloudsdkdws.v2.GrantAuthority`]
        """
        self._authority_list = authority_list

    @property
    def count(self):
        r"""Gets the count of this ListDatabaseUserAuthoritiesResponse.

        **参数解释**： 权限总条数。 **取值范围**： 不涉及。

        :return: The count of this ListDatabaseUserAuthoritiesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListDatabaseUserAuthoritiesResponse.

        **参数解释**： 权限总条数。 **取值范围**： 不涉及。

        :param count: The count of this ListDatabaseUserAuthoritiesResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListDatabaseUserAuthoritiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
