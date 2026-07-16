# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInferServiceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_auth_token_provider')

    openapi_types = {
        'x_auth_token_provider': 'str',
        'body': 'ServiceCreateRequest'
    }

    attribute_map = {
        'x_auth_token_provider': 'X-Auth-Token-Provider',
        'body': 'body'
    }

    def __init__(self, x_auth_token_provider=None, body=None):
        r"""CreateInferServiceRequest

        The model defined in huaweicloud sdk

        :param x_auth_token_provider: **参数解释：** 服务提供者的domain级或project级Token，创建服务携带该请求头时，系统将解析该token并将账号id保存为服务的提供者即provider，该服务将被系统保护，仅携带该提供者的domain级或project级Token的更新操作允许执行。[通过调用IAM服务获取用户Token接口获取响应消息头中X-Subject-Token的值。](tag:hws,hws_hk)获取方法请参见[[获取IAM用户Token（使用密码）](modelarts_03_0004.xml)](tag:hws,hws_hk)[[获取Token](modelarts_03_0015.xml)](tag:hcs,hcs_sm)。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type x_auth_token_provider: str
        :param body: Body of the CreateInferServiceRequest
        :type body: :class:`huaweicloudsdkmodelarts.v1.ServiceCreateRequest`
        """
        
        

        self._x_auth_token_provider = None
        self._body = None
        self.discriminator = None

        if x_auth_token_provider is not None:
            self.x_auth_token_provider = x_auth_token_provider
        if body is not None:
            self.body = body

    @property
    def x_auth_token_provider(self):
        r"""Gets the x_auth_token_provider of this CreateInferServiceRequest.

        **参数解释：** 服务提供者的domain级或project级Token，创建服务携带该请求头时，系统将解析该token并将账号id保存为服务的提供者即provider，该服务将被系统保护，仅携带该提供者的domain级或project级Token的更新操作允许执行。[通过调用IAM服务获取用户Token接口获取响应消息头中X-Subject-Token的值。](tag:hws,hws_hk)获取方法请参见[[获取IAM用户Token（使用密码）](modelarts_03_0004.xml)](tag:hws,hws_hk)[[获取Token](modelarts_03_0015.xml)](tag:hcs,hcs_sm)。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The x_auth_token_provider of this CreateInferServiceRequest.
        :rtype: str
        """
        return self._x_auth_token_provider

    @x_auth_token_provider.setter
    def x_auth_token_provider(self, x_auth_token_provider):
        r"""Sets the x_auth_token_provider of this CreateInferServiceRequest.

        **参数解释：** 服务提供者的domain级或project级Token，创建服务携带该请求头时，系统将解析该token并将账号id保存为服务的提供者即provider，该服务将被系统保护，仅携带该提供者的domain级或project级Token的更新操作允许执行。[通过调用IAM服务获取用户Token接口获取响应消息头中X-Subject-Token的值。](tag:hws,hws_hk)获取方法请参见[[获取IAM用户Token（使用密码）](modelarts_03_0004.xml)](tag:hws,hws_hk)[[获取Token](modelarts_03_0015.xml)](tag:hcs,hcs_sm)。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param x_auth_token_provider: The x_auth_token_provider of this CreateInferServiceRequest.
        :type x_auth_token_provider: str
        """
        self._x_auth_token_provider = x_auth_token_provider

    @property
    def body(self):
        r"""Gets the body of this CreateInferServiceRequest.

        :return: The body of this CreateInferServiceRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ServiceCreateRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateInferServiceRequest.

        :param body: The body of this CreateInferServiceRequest.
        :type body: :class:`huaweicloudsdkmodelarts.v1.ServiceCreateRequest`
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
        if not isinstance(other, CreateInferServiceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
