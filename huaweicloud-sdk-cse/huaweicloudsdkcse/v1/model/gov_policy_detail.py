# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GovPolicyDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'match_group': 'CreateBussinessScene',
        'policies': 'list[GovPolicyDetailPolicies]'
    }

    attribute_map = {
        'match_group': 'matchGroup',
        'policies': 'policies'
    }

    def __init__(self, match_group=None, policies=None):
        r"""GovPolicyDetail

        The model defined in huaweicloud sdk

        :param match_group: 
        :type match_group: :class:`huaweicloudsdkcse.v1.CreateBussinessScene`
        :param policies: 治理策略定义。
        :type policies: list[:class:`huaweicloudsdkcse.v1.GovPolicyDetailPolicies`]
        """
        
        

        self._match_group = None
        self._policies = None
        self.discriminator = None

        if match_group is not None:
            self.match_group = match_group
        if policies is not None:
            self.policies = policies

    @property
    def match_group(self):
        r"""Gets the match_group of this GovPolicyDetail.

        :return: The match_group of this GovPolicyDetail.
        :rtype: :class:`huaweicloudsdkcse.v1.CreateBussinessScene`
        """
        return self._match_group

    @match_group.setter
    def match_group(self, match_group):
        r"""Sets the match_group of this GovPolicyDetail.

        :param match_group: The match_group of this GovPolicyDetail.
        :type match_group: :class:`huaweicloudsdkcse.v1.CreateBussinessScene`
        """
        self._match_group = match_group

    @property
    def policies(self):
        r"""Gets the policies of this GovPolicyDetail.

        治理策略定义。

        :return: The policies of this GovPolicyDetail.
        :rtype: list[:class:`huaweicloudsdkcse.v1.GovPolicyDetailPolicies`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this GovPolicyDetail.

        治理策略定义。

        :param policies: The policies of this GovPolicyDetail.
        :type policies: list[:class:`huaweicloudsdkcse.v1.GovPolicyDetailPolicies`]
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
        if not isinstance(other, GovPolicyDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
