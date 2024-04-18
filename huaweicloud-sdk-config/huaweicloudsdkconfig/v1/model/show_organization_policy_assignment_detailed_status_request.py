# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOrganizationPolicyAssignmentDetailedStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'organization_id': 'str',
        'organization_policy_assignment_name': 'str',
        'organization_policy_assignment_id': 'str',
        'status': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'organization_id': 'organization_id',
        'organization_policy_assignment_name': 'organization_policy_assignment_name',
        'organization_policy_assignment_id': 'organization_policy_assignment_id',
        'status': 'status',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, organization_id=None, organization_policy_assignment_name=None, organization_policy_assignment_id=None, status=None, limit=None, marker=None):
        """ShowOrganizationPolicyAssignmentDetailedStatusRequest

        The model defined in huaweicloud sdk

        :param organization_id: 组织ID。
        :type organization_id: str
        :param organization_policy_assignment_name: 组织合规规则名称。
        :type organization_policy_assignment_name: str
        :param organization_policy_assignment_id: 组织合规规则ID
        :type organization_policy_assignment_id: str
        :param status: 成员帐号规则部署状态，区分大小写。
        :type status: str
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        """
        
        

        self._organization_id = None
        self._organization_policy_assignment_name = None
        self._organization_policy_assignment_id = None
        self._status = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.organization_id = organization_id
        if organization_policy_assignment_name is not None:
            self.organization_policy_assignment_name = organization_policy_assignment_name
        if organization_policy_assignment_id is not None:
            self.organization_policy_assignment_id = organization_policy_assignment_id
        if status is not None:
            self.status = status
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def organization_id(self):
        """Gets the organization_id of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.

        组织ID。

        :return: The organization_id of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.

        组织ID。

        :param organization_id: The organization_id of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def organization_policy_assignment_name(self):
        """Gets the organization_policy_assignment_name of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.

        组织合规规则名称。

        :return: The organization_policy_assignment_name of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.
        :rtype: str
        """
        return self._organization_policy_assignment_name

    @organization_policy_assignment_name.setter
    def organization_policy_assignment_name(self, organization_policy_assignment_name):
        """Sets the organization_policy_assignment_name of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.

        组织合规规则名称。

        :param organization_policy_assignment_name: The organization_policy_assignment_name of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.
        :type organization_policy_assignment_name: str
        """
        self._organization_policy_assignment_name = organization_policy_assignment_name

    @property
    def organization_policy_assignment_id(self):
        """Gets the organization_policy_assignment_id of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.

        组织合规规则ID

        :return: The organization_policy_assignment_id of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.
        :rtype: str
        """
        return self._organization_policy_assignment_id

    @organization_policy_assignment_id.setter
    def organization_policy_assignment_id(self, organization_policy_assignment_id):
        """Sets the organization_policy_assignment_id of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.

        组织合规规则ID

        :param organization_policy_assignment_id: The organization_policy_assignment_id of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.
        :type organization_policy_assignment_id: str
        """
        self._organization_policy_assignment_id = organization_policy_assignment_id

    @property
    def status(self):
        """Gets the status of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.

        成员帐号规则部署状态，区分大小写。

        :return: The status of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.

        成员帐号规则部署状态，区分大小写。

        :param status: The status of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.
        :type status: str
        """
        self._status = status

    @property
    def limit(self):
        """Gets the limit of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.

        最大的返回数量

        :return: The limit of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.

        最大的返回数量

        :param limit: The limit of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ShowOrganizationPolicyAssignmentDetailedStatusRequest.
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
        if not isinstance(other, ShowOrganizationPolicyAssignmentDetailedStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
