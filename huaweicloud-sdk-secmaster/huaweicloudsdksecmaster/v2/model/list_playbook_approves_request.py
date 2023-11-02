# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPlaybookApprovesRequest:

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
        'workspace_id': 'str',
        'resource_id': 'str',
        'approve_type': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'resource_id': 'resource_id',
        'approve_type': 'approve_type'
    }

    def __init__(self, project_id=None, workspace_id=None, resource_id=None, approve_type=None):
        """ListPlaybookApprovesRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param approve_type: 审核类型。（PLAYBOOK-剧本, AOP_WORKFLOW--流程)
        :type approve_type: str
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._resource_id = None
        self._approve_type = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if resource_id is not None:
            self.resource_id = resource_id
        if approve_type is not None:
            self.approve_type = approve_type

    @property
    def project_id(self):
        """Gets the project_id of this ListPlaybookApprovesRequest.

        项目ID

        :return: The project_id of this ListPlaybookApprovesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListPlaybookApprovesRequest.

        项目ID

        :param project_id: The project_id of this ListPlaybookApprovesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ListPlaybookApprovesRequest.

        工作空间ID

        :return: The workspace_id of this ListPlaybookApprovesRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ListPlaybookApprovesRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this ListPlaybookApprovesRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def resource_id(self):
        """Gets the resource_id of this ListPlaybookApprovesRequest.

        资源ID

        :return: The resource_id of this ListPlaybookApprovesRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListPlaybookApprovesRequest.

        资源ID

        :param resource_id: The resource_id of this ListPlaybookApprovesRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def approve_type(self):
        """Gets the approve_type of this ListPlaybookApprovesRequest.

        审核类型。（PLAYBOOK-剧本, AOP_WORKFLOW--流程)

        :return: The approve_type of this ListPlaybookApprovesRequest.
        :rtype: str
        """
        return self._approve_type

    @approve_type.setter
    def approve_type(self, approve_type):
        """Sets the approve_type of this ListPlaybookApprovesRequest.

        审核类型。（PLAYBOOK-剧本, AOP_WORKFLOW--流程)

        :param approve_type: The approve_type of this ListPlaybookApprovesRequest.
        :type approve_type: str
        """
        self._approve_type = approve_type

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
        if not isinstance(other, ListPlaybookApprovesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
