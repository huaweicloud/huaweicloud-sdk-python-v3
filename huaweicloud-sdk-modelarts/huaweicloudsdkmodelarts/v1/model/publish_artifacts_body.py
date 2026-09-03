# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublishArtifactsBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'publish_artifacts': 'list[ArtifactsPublish]'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'publish_artifacts': 'publish_artifacts'
    }

    def __init__(self, workspace_id=None, publish_artifacts=None):
        r"""PublishArtifactsBody

        The model defined in huaweicloud sdk

        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param publish_artifacts: 产物发布请求列表
        :type publish_artifacts: list[:class:`huaweicloudsdkmodelarts.v1.ArtifactsPublish`]
        """
        
        

        self._workspace_id = None
        self._publish_artifacts = None
        self.discriminator = None

        if workspace_id is not None:
            self.workspace_id = workspace_id
        if publish_artifacts is not None:
            self.publish_artifacts = publish_artifacts

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this PublishArtifactsBody.

        工作空间ID

        :return: The workspace_id of this PublishArtifactsBody.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this PublishArtifactsBody.

        工作空间ID

        :param workspace_id: The workspace_id of this PublishArtifactsBody.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def publish_artifacts(self):
        r"""Gets the publish_artifacts of this PublishArtifactsBody.

        产物发布请求列表

        :return: The publish_artifacts of this PublishArtifactsBody.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ArtifactsPublish`]
        """
        return self._publish_artifacts

    @publish_artifacts.setter
    def publish_artifacts(self, publish_artifacts):
        r"""Sets the publish_artifacts of this PublishArtifactsBody.

        产物发布请求列表

        :param publish_artifacts: The publish_artifacts of this PublishArtifactsBody.
        :type publish_artifacts: list[:class:`huaweicloudsdkmodelarts.v1.ArtifactsPublish`]
        """
        self._publish_artifacts = publish_artifacts

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
        if not isinstance(other, PublishArtifactsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
