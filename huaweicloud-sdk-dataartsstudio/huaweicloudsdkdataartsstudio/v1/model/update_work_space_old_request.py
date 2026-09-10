# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWorkSpaceOldRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'workspace_id': 'str',
        'body': 'WorkspaceDto'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'workspace_id': 'workspace_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, workspace_id=None, body=None):
        r"""UpdateWorkSpaceOldRequest

        The model defined in huaweicloud sdk

        :param instance_id: DataArts Studio实例ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type instance_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param body: Body of the UpdateWorkSpaceOldRequest
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.WorkspaceDto`
        """
        
        

        self._instance_id = None
        self._workspace_id = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.workspace_id = workspace_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateWorkSpaceOldRequest.

        DataArts Studio实例ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The instance_id of this UpdateWorkSpaceOldRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateWorkSpaceOldRequest.

        DataArts Studio实例ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param instance_id: The instance_id of this UpdateWorkSpaceOldRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this UpdateWorkSpaceOldRequest.

        工作空间ID

        :return: The workspace_id of this UpdateWorkSpaceOldRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this UpdateWorkSpaceOldRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this UpdateWorkSpaceOldRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def body(self):
        r"""Gets the body of this UpdateWorkSpaceOldRequest.

        :return: The body of this UpdateWorkSpaceOldRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.WorkspaceDto`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateWorkSpaceOldRequest.

        :param body: The body of this UpdateWorkSpaceOldRequest.
        :type body: :class:`huaweicloudsdkdataartsstudio.v1.WorkspaceDto`
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
        if not isinstance(other, UpdateWorkSpaceOldRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
