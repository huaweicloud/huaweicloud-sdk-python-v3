# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrganizationPolicyAssignmentStatusResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'organization_policy_assignment_id': 'str',
        'organization_policy_assignment_name': 'str',
        'organization_policy_assignment_status': 'str',
        'error_code': 'str',
        'error_message': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'organization_policy_assignment_id': 'organization_policy_assignment_id',
        'organization_policy_assignment_name': 'organization_policy_assignment_name',
        'organization_policy_assignment_status': 'organization_policy_assignment_status',
        'error_code': 'error_code',
        'error_message': 'error_message',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, organization_policy_assignment_id=None, organization_policy_assignment_name=None, organization_policy_assignment_status=None, error_code=None, error_message=None, created_at=None, updated_at=None):
        r"""OrganizationPolicyAssignmentStatusResponse

        The model defined in huaweicloud sdk

        :param organization_policy_assignment_id: 组织合规规则ID。
        :type organization_policy_assignment_id: str
        :param organization_policy_assignment_name: 组织合规规则名称。
        :type organization_policy_assignment_name: str
        :param organization_policy_assignment_status: 组织合规规则部署状态。
        :type organization_policy_assignment_status: str
        :param error_code: 当创建或更新组织合规规则失败时错误码。
        :type error_code: str
        :param error_message: 当创建或更新组织合规规则失败时错误信息。
        :type error_message: str
        :param created_at: 创建时间。
        :type created_at: str
        :param updated_at: 更新时间。
        :type updated_at: str
        """
        
        

        self._organization_policy_assignment_id = None
        self._organization_policy_assignment_name = None
        self._organization_policy_assignment_status = None
        self._error_code = None
        self._error_message = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if organization_policy_assignment_id is not None:
            self.organization_policy_assignment_id = organization_policy_assignment_id
        if organization_policy_assignment_name is not None:
            self.organization_policy_assignment_name = organization_policy_assignment_name
        if organization_policy_assignment_status is not None:
            self.organization_policy_assignment_status = organization_policy_assignment_status
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def organization_policy_assignment_id(self):
        r"""Gets the organization_policy_assignment_id of this OrganizationPolicyAssignmentStatusResponse.

        组织合规规则ID。

        :return: The organization_policy_assignment_id of this OrganizationPolicyAssignmentStatusResponse.
        :rtype: str
        """
        return self._organization_policy_assignment_id

    @organization_policy_assignment_id.setter
    def organization_policy_assignment_id(self, organization_policy_assignment_id):
        r"""Sets the organization_policy_assignment_id of this OrganizationPolicyAssignmentStatusResponse.

        组织合规规则ID。

        :param organization_policy_assignment_id: The organization_policy_assignment_id of this OrganizationPolicyAssignmentStatusResponse.
        :type organization_policy_assignment_id: str
        """
        self._organization_policy_assignment_id = organization_policy_assignment_id

    @property
    def organization_policy_assignment_name(self):
        r"""Gets the organization_policy_assignment_name of this OrganizationPolicyAssignmentStatusResponse.

        组织合规规则名称。

        :return: The organization_policy_assignment_name of this OrganizationPolicyAssignmentStatusResponse.
        :rtype: str
        """
        return self._organization_policy_assignment_name

    @organization_policy_assignment_name.setter
    def organization_policy_assignment_name(self, organization_policy_assignment_name):
        r"""Sets the organization_policy_assignment_name of this OrganizationPolicyAssignmentStatusResponse.

        组织合规规则名称。

        :param organization_policy_assignment_name: The organization_policy_assignment_name of this OrganizationPolicyAssignmentStatusResponse.
        :type organization_policy_assignment_name: str
        """
        self._organization_policy_assignment_name = organization_policy_assignment_name

    @property
    def organization_policy_assignment_status(self):
        r"""Gets the organization_policy_assignment_status of this OrganizationPolicyAssignmentStatusResponse.

        组织合规规则部署状态。

        :return: The organization_policy_assignment_status of this OrganizationPolicyAssignmentStatusResponse.
        :rtype: str
        """
        return self._organization_policy_assignment_status

    @organization_policy_assignment_status.setter
    def organization_policy_assignment_status(self, organization_policy_assignment_status):
        r"""Sets the organization_policy_assignment_status of this OrganizationPolicyAssignmentStatusResponse.

        组织合规规则部署状态。

        :param organization_policy_assignment_status: The organization_policy_assignment_status of this OrganizationPolicyAssignmentStatusResponse.
        :type organization_policy_assignment_status: str
        """
        self._organization_policy_assignment_status = organization_policy_assignment_status

    @property
    def error_code(self):
        r"""Gets the error_code of this OrganizationPolicyAssignmentStatusResponse.

        当创建或更新组织合规规则失败时错误码。

        :return: The error_code of this OrganizationPolicyAssignmentStatusResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this OrganizationPolicyAssignmentStatusResponse.

        当创建或更新组织合规规则失败时错误码。

        :param error_code: The error_code of this OrganizationPolicyAssignmentStatusResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        r"""Gets the error_message of this OrganizationPolicyAssignmentStatusResponse.

        当创建或更新组织合规规则失败时错误信息。

        :return: The error_message of this OrganizationPolicyAssignmentStatusResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this OrganizationPolicyAssignmentStatusResponse.

        当创建或更新组织合规规则失败时错误信息。

        :param error_message: The error_message of this OrganizationPolicyAssignmentStatusResponse.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def created_at(self):
        r"""Gets the created_at of this OrganizationPolicyAssignmentStatusResponse.

        创建时间。

        :return: The created_at of this OrganizationPolicyAssignmentStatusResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this OrganizationPolicyAssignmentStatusResponse.

        创建时间。

        :param created_at: The created_at of this OrganizationPolicyAssignmentStatusResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this OrganizationPolicyAssignmentStatusResponse.

        更新时间。

        :return: The updated_at of this OrganizationPolicyAssignmentStatusResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this OrganizationPolicyAssignmentStatusResponse.

        更新时间。

        :param updated_at: The updated_at of this OrganizationPolicyAssignmentStatusResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, OrganizationPolicyAssignmentStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
