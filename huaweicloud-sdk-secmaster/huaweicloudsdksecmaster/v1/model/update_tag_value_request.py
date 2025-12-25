# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTagValueRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'project_id': 'str',
        'resource_id': 'str',
        'key': 'str',
        'body': 'UpdateTagValueRequestBody'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'project_id': 'project_id',
        'resource_id': 'resource_id',
        'key': 'key',
        'body': 'body'
    }

    def __init__(self, resource_type=None, project_id=None, resource_id=None, key=None, body=None):
        r"""UpdateTagValueRequest

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型
        :type resource_type: str
        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param key: 标签键
        :type key: str
        :param body: Body of the UpdateTagValueRequest
        :type body: :class:`huaweicloudsdksecmaster.v1.UpdateTagValueRequestBody`
        """
        
        

        self._resource_type = None
        self._project_id = None
        self._resource_id = None
        self._key = None
        self._body = None
        self.discriminator = None

        self.resource_type = resource_type
        self.project_id = project_id
        self.resource_id = resource_id
        self.key = key
        if body is not None:
            self.body = body

    @property
    def resource_type(self):
        r"""Gets the resource_type of this UpdateTagValueRequest.

        资源类型

        :return: The resource_type of this UpdateTagValueRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this UpdateTagValueRequest.

        资源类型

        :param resource_type: The resource_type of this UpdateTagValueRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def project_id(self):
        r"""Gets the project_id of this UpdateTagValueRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this UpdateTagValueRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this UpdateTagValueRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this UpdateTagValueRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this UpdateTagValueRequest.

        资源ID

        :return: The resource_id of this UpdateTagValueRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this UpdateTagValueRequest.

        资源ID

        :param resource_id: The resource_id of this UpdateTagValueRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def key(self):
        r"""Gets the key of this UpdateTagValueRequest.

        标签键

        :return: The key of this UpdateTagValueRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this UpdateTagValueRequest.

        标签键

        :param key: The key of this UpdateTagValueRequest.
        :type key: str
        """
        self._key = key

    @property
    def body(self):
        r"""Gets the body of this UpdateTagValueRequest.

        :return: The body of this UpdateTagValueRequest.
        :rtype: :class:`huaweicloudsdksecmaster.v1.UpdateTagValueRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateTagValueRequest.

        :param body: The body of this UpdateTagValueRequest.
        :type body: :class:`huaweicloudsdksecmaster.v1.UpdateTagValueRequestBody`
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
        if not isinstance(other, UpdateTagValueRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
