# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePlaybookVersionRequest:

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
        'version_id': 'str',
        'body': 'ModifyPlaybookVersionInfo'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'version_id': 'version_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, workspace_id=None, version_id=None, body=None):
        """UpdatePlaybookVersionRequest

        The model defined in huaweicloud sdk

        :param project_id: ID of project
        :type project_id: str
        :param workspace_id: ID of workspace
        :type workspace_id: str
        :param version_id: version Id value
        :type version_id: str
        :param body: Body of the UpdatePlaybookVersionRequest
        :type body: :class:`huaweicloudsdksa.v2.ModifyPlaybookVersionInfo`
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._version_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.version_id = version_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        """Gets the project_id of this UpdatePlaybookVersionRequest.

        ID of project

        :return: The project_id of this UpdatePlaybookVersionRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UpdatePlaybookVersionRequest.

        ID of project

        :param project_id: The project_id of this UpdatePlaybookVersionRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this UpdatePlaybookVersionRequest.

        ID of workspace

        :return: The workspace_id of this UpdatePlaybookVersionRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this UpdatePlaybookVersionRequest.

        ID of workspace

        :param workspace_id: The workspace_id of this UpdatePlaybookVersionRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def version_id(self):
        """Gets the version_id of this UpdatePlaybookVersionRequest.

        version Id value

        :return: The version_id of this UpdatePlaybookVersionRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this UpdatePlaybookVersionRequest.

        version Id value

        :param version_id: The version_id of this UpdatePlaybookVersionRequest.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def body(self):
        """Gets the body of this UpdatePlaybookVersionRequest.

        :return: The body of this UpdatePlaybookVersionRequest.
        :rtype: :class:`huaweicloudsdksa.v2.ModifyPlaybookVersionInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdatePlaybookVersionRequest.

        :param body: The body of this UpdatePlaybookVersionRequest.
        :type body: :class:`huaweicloudsdksa.v2.ModifyPlaybookVersionInfo`
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
        if not isinstance(other, UpdatePlaybookVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
