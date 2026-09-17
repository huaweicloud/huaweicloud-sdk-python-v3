# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTenantIssueListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'issue_type': 'str',
        'body': 'QueryVO'
    }

    attribute_map = {
        'project_id': 'project_id',
        'issue_type': 'issue_type',
        'body': 'body'
    }

    def __init__(self, project_id=None, issue_type=None, body=None):
        r"""ShowTenantIssueListRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目32位UUID
        :type project_id: str
        :param issue_type: 工作项类型
        :type issue_type: str
        :param body: Body of the ShowTenantIssueListRequest
        :type body: :class:`huaweicloudsdkprojectman.v4.QueryVO`
        """
        
        

        self._project_id = None
        self._issue_type = None
        self._body = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if issue_type is not None:
            self.issue_type = issue_type
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowTenantIssueListRequest.

        项目32位UUID

        :return: The project_id of this ShowTenantIssueListRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowTenantIssueListRequest.

        项目32位UUID

        :param project_id: The project_id of this ShowTenantIssueListRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def issue_type(self):
        r"""Gets the issue_type of this ShowTenantIssueListRequest.

        工作项类型

        :return: The issue_type of this ShowTenantIssueListRequest.
        :rtype: str
        """
        return self._issue_type

    @issue_type.setter
    def issue_type(self, issue_type):
        r"""Sets the issue_type of this ShowTenantIssueListRequest.

        工作项类型

        :param issue_type: The issue_type of this ShowTenantIssueListRequest.
        :type issue_type: str
        """
        self._issue_type = issue_type

    @property
    def body(self):
        r"""Gets the body of this ShowTenantIssueListRequest.

        :return: The body of this ShowTenantIssueListRequest.
        :rtype: :class:`huaweicloudsdkprojectman.v4.QueryVO`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ShowTenantIssueListRequest.

        :param body: The body of this ShowTenantIssueListRequest.
        :type body: :class:`huaweicloudsdkprojectman.v4.QueryVO`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowTenantIssueListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
