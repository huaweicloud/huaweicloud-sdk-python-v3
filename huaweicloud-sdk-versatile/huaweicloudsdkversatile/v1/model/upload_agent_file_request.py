# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadAgentFileRequest:

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
        'expires': 'int',
        'is_image': 'bool',
        'body': 'UploadAgentFileRequestBody'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'expires': 'expires',
        'is_image': 'is_image',
        'body': 'body'
    }

    def __init__(self, workspace_id=None, expires=None, is_image=None, body=None):
        r"""UploadAgentFileRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**： 空间ID，当前资源所属工作空间  **取值范围**： 由英文，数字，“-”，“_”组成，不超过64位字符
        :type workspace_id: str
        :param expires: 访问授权过期时间（天）
        :type expires: int
        :param is_image: 是否是图片上传
        :type is_image: bool
        :param body: Body of the UploadAgentFileRequest
        :type body: :class:`huaweicloudsdkversatile.v1.UploadAgentFileRequestBody`
        """
        
        

        self._workspace_id = None
        self._expires = None
        self._is_image = None
        self._body = None
        self.discriminator = None

        self.workspace_id = workspace_id
        if expires is not None:
            self.expires = expires
        if is_image is not None:
            self.is_image = is_image
        if body is not None:
            self.body = body

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this UploadAgentFileRequest.

        **参数解释**： 空间ID，当前资源所属工作空间  **取值范围**： 由英文，数字，“-”，“_”组成，不超过64位字符

        :return: The workspace_id of this UploadAgentFileRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this UploadAgentFileRequest.

        **参数解释**： 空间ID，当前资源所属工作空间  **取值范围**： 由英文，数字，“-”，“_”组成，不超过64位字符

        :param workspace_id: The workspace_id of this UploadAgentFileRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def expires(self):
        r"""Gets the expires of this UploadAgentFileRequest.

        访问授权过期时间（天）

        :return: The expires of this UploadAgentFileRequest.
        :rtype: int
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        r"""Sets the expires of this UploadAgentFileRequest.

        访问授权过期时间（天）

        :param expires: The expires of this UploadAgentFileRequest.
        :type expires: int
        """
        self._expires = expires

    @property
    def is_image(self):
        r"""Gets the is_image of this UploadAgentFileRequest.

        是否是图片上传

        :return: The is_image of this UploadAgentFileRequest.
        :rtype: bool
        """
        return self._is_image

    @is_image.setter
    def is_image(self, is_image):
        r"""Sets the is_image of this UploadAgentFileRequest.

        是否是图片上传

        :param is_image: The is_image of this UploadAgentFileRequest.
        :type is_image: bool
        """
        self._is_image = is_image

    @property
    def body(self):
        r"""Gets the body of this UploadAgentFileRequest.

        :return: The body of this UploadAgentFileRequest.
        :rtype: :class:`huaweicloudsdkversatile.v1.UploadAgentFileRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UploadAgentFileRequest.

        :param body: The body of this UploadAgentFileRequest.
        :type body: :class:`huaweicloudsdkversatile.v1.UploadAgentFileRequestBody`
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
        if not isinstance(other, UploadAgentFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
