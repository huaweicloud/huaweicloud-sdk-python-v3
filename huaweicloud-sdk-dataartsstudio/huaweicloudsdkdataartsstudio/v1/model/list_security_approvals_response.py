# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityApprovalsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'approvals': 'list[PermissionApprovalOpenapiDTO]',
        'total': 'int'
    }

    attribute_map = {
        'approvals': 'approvals',
        'total': 'total'
    }

    def __init__(self, approvals=None, total=None):
        r"""ListSecurityApprovalsResponse

        The model defined in huaweicloud sdk

        :param approvals: 工单列表
        :type approvals: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionApprovalOpenapiDTO`]
        :param total: 规则组总数
        :type total: int
        """
        
        super(ListSecurityApprovalsResponse, self).__init__()

        self._approvals = None
        self._total = None
        self.discriminator = None

        if approvals is not None:
            self.approvals = approvals
        if total is not None:
            self.total = total

    @property
    def approvals(self):
        r"""Gets the approvals of this ListSecurityApprovalsResponse.

        工单列表

        :return: The approvals of this ListSecurityApprovalsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionApprovalOpenapiDTO`]
        """
        return self._approvals

    @approvals.setter
    def approvals(self, approvals):
        r"""Sets the approvals of this ListSecurityApprovalsResponse.

        工单列表

        :param approvals: The approvals of this ListSecurityApprovalsResponse.
        :type approvals: list[:class:`huaweicloudsdkdataartsstudio.v1.PermissionApprovalOpenapiDTO`]
        """
        self._approvals = approvals

    @property
    def total(self):
        r"""Gets the total of this ListSecurityApprovalsResponse.

        规则组总数

        :return: The total of this ListSecurityApprovalsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSecurityApprovalsResponse.

        规则组总数

        :param total: The total of this ListSecurityApprovalsResponse.
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
        if not isinstance(other, ListSecurityApprovalsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
