# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCoreSpaceNetworkRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'space_id': 'str',
        'body': 'UpdateCoreSpaceNetworkRequestBody'
    }

    attribute_map = {
        'space_id': 'space_id',
        'body': 'body'
    }

    def __init__(self, space_id=None, body=None):
        r"""UpdateCoreSpaceNetworkRequest

        The model defined in huaweicloud sdk

        :param space_id: **参数解释：**  记忆库 ID，唯一标识一个记忆库，可以通过AgentArts智能体记忆库控制台或者记忆库查询接口获取。 **约束限制：** 仅支持字母、数字和中划线。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 
        :type space_id: str
        :param body: Body of the UpdateCoreSpaceNetworkRequest
        :type body: :class:`huaweicloudsdkagentarts.v1.UpdateCoreSpaceNetworkRequestBody`
        """
        
        

        self._space_id = None
        self._body = None
        self.discriminator = None

        self.space_id = space_id
        if body is not None:
            self.body = body

    @property
    def space_id(self):
        r"""Gets the space_id of this UpdateCoreSpaceNetworkRequest.

        **参数解释：**  记忆库 ID，唯一标识一个记忆库，可以通过AgentArts智能体记忆库控制台或者记忆库查询接口获取。 **约束限制：** 仅支持字母、数字和中划线。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :return: The space_id of this UpdateCoreSpaceNetworkRequest.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        r"""Sets the space_id of this UpdateCoreSpaceNetworkRequest.

        **参数解释：**  记忆库 ID，唯一标识一个记忆库，可以通过AgentArts智能体记忆库控制台或者记忆库查询接口获取。 **约束限制：** 仅支持字母、数字和中划线。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :param space_id: The space_id of this UpdateCoreSpaceNetworkRequest.
        :type space_id: str
        """
        self._space_id = space_id

    @property
    def body(self):
        r"""Gets the body of this UpdateCoreSpaceNetworkRequest.

        :return: The body of this UpdateCoreSpaceNetworkRequest.
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateCoreSpaceNetworkRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateCoreSpaceNetworkRequest.

        :param body: The body of this UpdateCoreSpaceNetworkRequest.
        :type body: :class:`huaweicloudsdkagentarts.v1.UpdateCoreSpaceNetworkRequestBody`
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
        if not isinstance(other, UpdateCoreSpaceNetworkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
