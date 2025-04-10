# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityTableApproversResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'approvers': 'list[TableApprover]',
        'has_table_rule': 'bool'
    }

    attribute_map = {
        'approvers': 'approvers',
        'has_table_rule': 'has_table_rule'
    }

    def __init__(self, approvers=None, has_table_rule=None):
        r"""ListSecurityTableApproversResponse

        The model defined in huaweicloud sdk

        :param approvers: 审批人列表
        :type approvers: list[:class:`huaweicloudsdkdataartsstudio.v1.TableApprover`]
        :param has_table_rule: 是否已经有权限
        :type has_table_rule: bool
        """
        
        super(ListSecurityTableApproversResponse, self).__init__()

        self._approvers = None
        self._has_table_rule = None
        self.discriminator = None

        if approvers is not None:
            self.approvers = approvers
        if has_table_rule is not None:
            self.has_table_rule = has_table_rule

    @property
    def approvers(self):
        r"""Gets the approvers of this ListSecurityTableApproversResponse.

        审批人列表

        :return: The approvers of this ListSecurityTableApproversResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TableApprover`]
        """
        return self._approvers

    @approvers.setter
    def approvers(self, approvers):
        r"""Sets the approvers of this ListSecurityTableApproversResponse.

        审批人列表

        :param approvers: The approvers of this ListSecurityTableApproversResponse.
        :type approvers: list[:class:`huaweicloudsdkdataartsstudio.v1.TableApprover`]
        """
        self._approvers = approvers

    @property
    def has_table_rule(self):
        r"""Gets the has_table_rule of this ListSecurityTableApproversResponse.

        是否已经有权限

        :return: The has_table_rule of this ListSecurityTableApproversResponse.
        :rtype: bool
        """
        return self._has_table_rule

    @has_table_rule.setter
    def has_table_rule(self, has_table_rule):
        r"""Sets the has_table_rule of this ListSecurityTableApproversResponse.

        是否已经有权限

        :param has_table_rule: The has_table_rule of this ListSecurityTableApproversResponse.
        :type has_table_rule: bool
        """
        self._has_table_rule = has_table_rule

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
        if not isinstance(other, ListSecurityTableApproversResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
