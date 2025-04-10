# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlertRequest:

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
        'alert_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'alert_id': 'alert_id'
    }

    def __init__(self, project_id=None, workspace_id=None, alert_id=None):
        r"""ShowAlertRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param workspace_id: 工作空间id
        :type workspace_id: str
        :param alert_id: 告警ID
        :type alert_id: str
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._alert_id = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        self.alert_id = alert_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowAlertRequest.

        项目id

        :return: The project_id of this ShowAlertRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowAlertRequest.

        项目id

        :param project_id: The project_id of this ShowAlertRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ShowAlertRequest.

        工作空间id

        :return: The workspace_id of this ShowAlertRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ShowAlertRequest.

        工作空间id

        :param workspace_id: The workspace_id of this ShowAlertRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def alert_id(self):
        r"""Gets the alert_id of this ShowAlertRequest.

        告警ID

        :return: The alert_id of this ShowAlertRequest.
        :rtype: str
        """
        return self._alert_id

    @alert_id.setter
    def alert_id(self, alert_id):
        r"""Sets the alert_id of this ShowAlertRequest.

        告警ID

        :param alert_id: The alert_id of this ShowAlertRequest.
        :type alert_id: str
        """
        self._alert_id = alert_id

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
        if not isinstance(other, ShowAlertRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
