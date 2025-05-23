# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOrganizationPolicyDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policies': 'list[OrganizationPolicyStatus]',
        'count': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'policies': 'policies',
        'count': 'count',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, policies=None, count=None, limit=None, offset=None):
        r"""ListOrganizationPolicyDetailResponse

        The model defined in huaweicloud sdk

        :param policies: 组织策略部署状态列表
        :type policies: list[:class:`huaweicloudsdkcbr.v1.OrganizationPolicyStatus`]
        :param count: 组织策略状态成员数量
        :type count: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询
        :type offset: int
        """
        
        super(ListOrganizationPolicyDetailResponse, self).__init__()

        self._policies = None
        self._count = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if policies is not None:
            self.policies = policies
        if count is not None:
            self.count = count
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def policies(self):
        r"""Gets the policies of this ListOrganizationPolicyDetailResponse.

        组织策略部署状态列表

        :return: The policies of this ListOrganizationPolicyDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.OrganizationPolicyStatus`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this ListOrganizationPolicyDetailResponse.

        组织策略部署状态列表

        :param policies: The policies of this ListOrganizationPolicyDetailResponse.
        :type policies: list[:class:`huaweicloudsdkcbr.v1.OrganizationPolicyStatus`]
        """
        self._policies = policies

    @property
    def count(self):
        r"""Gets the count of this ListOrganizationPolicyDetailResponse.

        组织策略状态成员数量

        :return: The count of this ListOrganizationPolicyDetailResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListOrganizationPolicyDetailResponse.

        组织策略状态成员数量

        :param count: The count of this ListOrganizationPolicyDetailResponse.
        :type count: int
        """
        self._count = count

    @property
    def limit(self):
        r"""Gets the limit of this ListOrganizationPolicyDetailResponse.

        每页显示的条目数量

        :return: The limit of this ListOrganizationPolicyDetailResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOrganizationPolicyDetailResponse.

        每页显示的条目数量

        :param limit: The limit of this ListOrganizationPolicyDetailResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListOrganizationPolicyDetailResponse.

        偏移量，表示从此偏移量开始查询

        :return: The offset of this ListOrganizationPolicyDetailResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOrganizationPolicyDetailResponse.

        偏移量，表示从此偏移量开始查询

        :param offset: The offset of this ListOrganizationPolicyDetailResponse.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListOrganizationPolicyDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
