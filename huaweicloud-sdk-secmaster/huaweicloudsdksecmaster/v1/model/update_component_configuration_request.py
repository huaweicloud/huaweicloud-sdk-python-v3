# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateComponentConfigurationRequest:

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
        'component_id': 'str',
        'workspace_id': 'str',
        'body': 'ConfigurationInfoDto'
    }

    attribute_map = {
        'project_id': 'project_id',
        'component_id': 'component_id',
        'workspace_id': 'workspace_id',
        'body': 'body'
    }

    def __init__(self, project_id=None, component_id=None, workspace_id=None, body=None):
        r"""UpdateComponentConfigurationRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param component_id: 组件id
        :type component_id: str
        :param workspace_id: 工作空间id
        :type workspace_id: str
        :param body: Body of the UpdateComponentConfigurationRequest
        :type body: :class:`huaweicloudsdksecmaster.v1.ConfigurationInfoDto`
        """
        
        

        self._project_id = None
        self._component_id = None
        self._workspace_id = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.component_id = component_id
        self.workspace_id = workspace_id
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this UpdateComponentConfigurationRequest.

        项目id

        :return: The project_id of this UpdateComponentConfigurationRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this UpdateComponentConfigurationRequest.

        项目id

        :param project_id: The project_id of this UpdateComponentConfigurationRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def component_id(self):
        r"""Gets the component_id of this UpdateComponentConfigurationRequest.

        组件id

        :return: The component_id of this UpdateComponentConfigurationRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this UpdateComponentConfigurationRequest.

        组件id

        :param component_id: The component_id of this UpdateComponentConfigurationRequest.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this UpdateComponentConfigurationRequest.

        工作空间id

        :return: The workspace_id of this UpdateComponentConfigurationRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this UpdateComponentConfigurationRequest.

        工作空间id

        :param workspace_id: The workspace_id of this UpdateComponentConfigurationRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def body(self):
        r"""Gets the body of this UpdateComponentConfigurationRequest.

        :return: The body of this UpdateComponentConfigurationRequest.
        :rtype: :class:`huaweicloudsdksecmaster.v1.ConfigurationInfoDto`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateComponentConfigurationRequest.

        :param body: The body of this UpdateComponentConfigurationRequest.
        :type body: :class:`huaweicloudsdksecmaster.v1.ConfigurationInfoDto`
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
        if not isinstance(other, UpdateComponentConfigurationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
