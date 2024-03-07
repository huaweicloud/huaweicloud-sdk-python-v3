# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPolicyAssignmentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_assignment_name': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'policy_assignment_name': 'policy_assignment_name',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, policy_assignment_name=None, limit=None, marker=None):
        """ListPolicyAssignmentsRequest

        The model defined in huaweicloud sdk

        :param policy_assignment_name: 合规规则名称
        :type policy_assignment_name: str
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        """
        
        

        self._policy_assignment_name = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if policy_assignment_name is not None:
            self.policy_assignment_name = policy_assignment_name
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def policy_assignment_name(self):
        """Gets the policy_assignment_name of this ListPolicyAssignmentsRequest.

        合规规则名称

        :return: The policy_assignment_name of this ListPolicyAssignmentsRequest.
        :rtype: str
        """
        return self._policy_assignment_name

    @policy_assignment_name.setter
    def policy_assignment_name(self, policy_assignment_name):
        """Sets the policy_assignment_name of this ListPolicyAssignmentsRequest.

        合规规则名称

        :param policy_assignment_name: The policy_assignment_name of this ListPolicyAssignmentsRequest.
        :type policy_assignment_name: str
        """
        self._policy_assignment_name = policy_assignment_name

    @property
    def limit(self):
        """Gets the limit of this ListPolicyAssignmentsRequest.

        最大的返回数量

        :return: The limit of this ListPolicyAssignmentsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPolicyAssignmentsRequest.

        最大的返回数量

        :param limit: The limit of this ListPolicyAssignmentsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListPolicyAssignmentsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ListPolicyAssignmentsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPolicyAssignmentsRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ListPolicyAssignmentsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListPolicyAssignmentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
