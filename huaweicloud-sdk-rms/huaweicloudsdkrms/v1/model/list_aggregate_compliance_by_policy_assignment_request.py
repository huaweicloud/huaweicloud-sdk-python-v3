# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAggregateComplianceByPolicyAssignmentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'body': 'AggregatePolicyAssignmentsRequest'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'body': 'body'
    }

    def __init__(self, limit=None, marker=None, body=None):
        r"""ListAggregateComplianceByPolicyAssignmentRequest

        The model defined in huaweicloud sdk

        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        :param body: Body of the ListAggregateComplianceByPolicyAssignmentRequest
        :type body: :class:`huaweicloudsdkrms.v1.AggregatePolicyAssignmentsRequest`
        """
        
        

        self._limit = None
        self._marker = None
        self._body = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if body is not None:
            self.body = body

    @property
    def limit(self):
        r"""Gets the limit of this ListAggregateComplianceByPolicyAssignmentRequest.

        最大的返回数量

        :return: The limit of this ListAggregateComplianceByPolicyAssignmentRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAggregateComplianceByPolicyAssignmentRequest.

        最大的返回数量

        :param limit: The limit of this ListAggregateComplianceByPolicyAssignmentRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListAggregateComplianceByPolicyAssignmentRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ListAggregateComplianceByPolicyAssignmentRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListAggregateComplianceByPolicyAssignmentRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ListAggregateComplianceByPolicyAssignmentRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def body(self):
        r"""Gets the body of this ListAggregateComplianceByPolicyAssignmentRequest.

        :return: The body of this ListAggregateComplianceByPolicyAssignmentRequest.
        :rtype: :class:`huaweicloudsdkrms.v1.AggregatePolicyAssignmentsRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListAggregateComplianceByPolicyAssignmentRequest.

        :param body: The body of this ListAggregateComplianceByPolicyAssignmentRequest.
        :type body: :class:`huaweicloudsdkrms.v1.AggregatePolicyAssignmentsRequest`
        """
        self._body = body

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
        if not isinstance(other, ListAggregateComplianceByPolicyAssignmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
