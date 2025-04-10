# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityResourcePermissionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'policies': 'list[PermissionResourcePolicy]'
    }

    attribute_map = {
        'total': 'total',
        'policies': 'policies'
    }

    def __init__(self, total=None, policies=None):
        r"""ListSecurityResourcePermissionsResponse

        The model defined in huaweicloud sdk

        :param total: 空间资源权限策略总条数
        :type total: int
        :param policies: 空间资源权限策略列表
        :type policies: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionResourcePolicy`]
        """
        
        super(ListSecurityResourcePermissionsResponse, self).__init__()

        self._total = None
        self._policies = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if policies is not None:
            self.policies = policies

    @property
    def total(self):
        r"""Gets the total of this ListSecurityResourcePermissionsResponse.

        空间资源权限策略总条数

        :return: The total of this ListSecurityResourcePermissionsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSecurityResourcePermissionsResponse.

        空间资源权限策略总条数

        :param total: The total of this ListSecurityResourcePermissionsResponse.
        :type total: int
        """
        self._total = total

    @property
    def policies(self):
        r"""Gets the policies of this ListSecurityResourcePermissionsResponse.

        空间资源权限策略列表

        :return: The policies of this ListSecurityResourcePermissionsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionResourcePolicy`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this ListSecurityResourcePermissionsResponse.

        空间资源权限策略列表

        :param policies: The policies of this ListSecurityResourcePermissionsResponse.
        :type policies: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionResourcePolicy`]
        """
        self._policies = policies

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
        if not isinstance(other, ListSecurityResourcePermissionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
