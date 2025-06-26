# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceReplicationPoliciesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policies': 'list[ReplicationPolicy]',
        'total': 'int'
    }

    attribute_map = {
        'policies': 'policies',
        'total': 'total'
    }

    def __init__(self, policies=None, total=None):
        r"""ListInstanceReplicationPoliciesResponse

        The model defined in huaweicloud sdk

        :param policies: 同步策略列表
        :type policies: list[:class:`huaweicloudsdkswr.v2.ReplicationPolicy`]
        :param total: 同步策略总数
        :type total: int
        """
        
        super(ListInstanceReplicationPoliciesResponse, self).__init__()

        self._policies = None
        self._total = None
        self.discriminator = None

        if policies is not None:
            self.policies = policies
        if total is not None:
            self.total = total

    @property
    def policies(self):
        r"""Gets the policies of this ListInstanceReplicationPoliciesResponse.

        同步策略列表

        :return: The policies of this ListInstanceReplicationPoliciesResponse.
        :rtype: list[:class:`huaweicloudsdkswr.v2.ReplicationPolicy`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this ListInstanceReplicationPoliciesResponse.

        同步策略列表

        :param policies: The policies of this ListInstanceReplicationPoliciesResponse.
        :type policies: list[:class:`huaweicloudsdkswr.v2.ReplicationPolicy`]
        """
        self._policies = policies

    @property
    def total(self):
        r"""Gets the total of this ListInstanceReplicationPoliciesResponse.

        同步策略总数

        :return: The total of this ListInstanceReplicationPoliciesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceReplicationPoliciesResponse.

        同步策略总数

        :param total: The total of this ListInstanceReplicationPoliciesResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListInstanceReplicationPoliciesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
