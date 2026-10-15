# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRaySessionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_id': 'str',
        'secret_name': 'str',
        'ray_grpc_server_port': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'session_id': 'session_id',
        'secret_name': 'secret_name',
        'ray_grpc_server_port': 'ray_grpc_server_port',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, session_id=None, secret_name=None, ray_grpc_server_port=None, x_request_id=None):
        r"""CreateRaySessionResponse

        The model defined in huaweicloud sdk

        :param session_id: **参数解释**：会话ID。 **取值范围**：长度为1~36的英文、数字和中划线的组合。
        :type session_id: str
        :param secret_name: **参数解释**：pod-agency委托Secret名称，用于挂载联邦身份凭证。非AIHub联邦认证场景下返回空字符串。 **约束限制**：不涉及。 **取值范围**：长度不超过256个字符，为空时返回空字符串。 **默认取值**：空字符串。
        :type secret_name: str
        :param ray_grpc_server_port: **参数解释**：Ray集群GRPC连接端口号。 **约束限制**：不涉及。 **取值范围**：长度不超过5个字符，为空时返回空字符串。 **默认取值**：空字符串。
        :type ray_grpc_server_port: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._session_id = None
        self._secret_name = None
        self._ray_grpc_server_port = None
        self._x_request_id = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if secret_name is not None:
            self.secret_name = secret_name
        if ray_grpc_server_port is not None:
            self.ray_grpc_server_port = ray_grpc_server_port
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def session_id(self):
        r"""Gets the session_id of this CreateRaySessionResponse.

        **参数解释**：会话ID。 **取值范围**：长度为1~36的英文、数字和中划线的组合。

        :return: The session_id of this CreateRaySessionResponse.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this CreateRaySessionResponse.

        **参数解释**：会话ID。 **取值范围**：长度为1~36的英文、数字和中划线的组合。

        :param session_id: The session_id of this CreateRaySessionResponse.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def secret_name(self):
        r"""Gets the secret_name of this CreateRaySessionResponse.

        **参数解释**：pod-agency委托Secret名称，用于挂载联邦身份凭证。非AIHub联邦认证场景下返回空字符串。 **约束限制**：不涉及。 **取值范围**：长度不超过256个字符，为空时返回空字符串。 **默认取值**：空字符串。

        :return: The secret_name of this CreateRaySessionResponse.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        r"""Sets the secret_name of this CreateRaySessionResponse.

        **参数解释**：pod-agency委托Secret名称，用于挂载联邦身份凭证。非AIHub联邦认证场景下返回空字符串。 **约束限制**：不涉及。 **取值范围**：长度不超过256个字符，为空时返回空字符串。 **默认取值**：空字符串。

        :param secret_name: The secret_name of this CreateRaySessionResponse.
        :type secret_name: str
        """
        self._secret_name = secret_name

    @property
    def ray_grpc_server_port(self):
        r"""Gets the ray_grpc_server_port of this CreateRaySessionResponse.

        **参数解释**：Ray集群GRPC连接端口号。 **约束限制**：不涉及。 **取值范围**：长度不超过5个字符，为空时返回空字符串。 **默认取值**：空字符串。

        :return: The ray_grpc_server_port of this CreateRaySessionResponse.
        :rtype: str
        """
        return self._ray_grpc_server_port

    @ray_grpc_server_port.setter
    def ray_grpc_server_port(self, ray_grpc_server_port):
        r"""Sets the ray_grpc_server_port of this CreateRaySessionResponse.

        **参数解释**：Ray集群GRPC连接端口号。 **约束限制**：不涉及。 **取值范围**：长度不超过5个字符，为空时返回空字符串。 **默认取值**：空字符串。

        :param ray_grpc_server_port: The ray_grpc_server_port of this CreateRaySessionResponse.
        :type ray_grpc_server_port: str
        """
        self._ray_grpc_server_port = ray_grpc_server_port

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CreateRaySessionResponse.

        :return: The x_request_id of this CreateRaySessionResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CreateRaySessionResponse.

        :param x_request_id: The x_request_id of this CreateRaySessionResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateRaySessionResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CreateRaySessionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
