# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DecryptDatakeyCapsuleRequestBodyAttestationDocument:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ecs_signature': 'str',
        'custom_signature': 'str',
        'custom_public_key': 'str',
        'expire_time': 'str',
        'service_token': 'str'
    }

    attribute_map = {
        'ecs_signature': 'ecs_signature',
        'custom_signature': 'custom_signature',
        'custom_public_key': 'custom_public_key',
        'expire_time': 'expire_time',
        'service_token': 'service_token'
    }

    def __init__(self, ecs_signature=None, custom_signature=None, custom_public_key=None, expire_time=None, service_token=None):
        r"""DecryptDatakeyCapsuleRequestBodyAttestationDocument

        The model defined in huaweicloud sdk

        :param ecs_signature: **参数解释：** ECS证明文档 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type ecs_signature: str
        :param custom_signature: **参数解释：** 通用类型接入点的签名信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type custom_signature: str
        :param custom_public_key: **参数解释：** 通用类型接入点公钥信息 **约束限制：** 格式是X509公钥格式中的Base64字符串 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type custom_public_key: str
        :param expire_time: **参数解释：** 通用类型签名信息过期时间 **约束限制：** 时间格式是ISO 8601格式，yyyy-mm-ddTHH:MM:SSZ **取值范围：** 不涉及 **默认取值：** 不涉及
        :type expire_time: str
        :param service_token: **参数解释：** CCE类型访问凭证 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type service_token: str
        """
        
        

        self._ecs_signature = None
        self._custom_signature = None
        self._custom_public_key = None
        self._expire_time = None
        self._service_token = None
        self.discriminator = None

        if ecs_signature is not None:
            self.ecs_signature = ecs_signature
        if custom_signature is not None:
            self.custom_signature = custom_signature
        if custom_public_key is not None:
            self.custom_public_key = custom_public_key
        if expire_time is not None:
            self.expire_time = expire_time
        if service_token is not None:
            self.service_token = service_token

    @property
    def ecs_signature(self):
        r"""Gets the ecs_signature of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.

        **参数解释：** ECS证明文档 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The ecs_signature of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.
        :rtype: str
        """
        return self._ecs_signature

    @ecs_signature.setter
    def ecs_signature(self, ecs_signature):
        r"""Sets the ecs_signature of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.

        **参数解释：** ECS证明文档 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param ecs_signature: The ecs_signature of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.
        :type ecs_signature: str
        """
        self._ecs_signature = ecs_signature

    @property
    def custom_signature(self):
        r"""Gets the custom_signature of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.

        **参数解释：** 通用类型接入点的签名信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The custom_signature of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.
        :rtype: str
        """
        return self._custom_signature

    @custom_signature.setter
    def custom_signature(self, custom_signature):
        r"""Sets the custom_signature of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.

        **参数解释：** 通用类型接入点的签名信息 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param custom_signature: The custom_signature of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.
        :type custom_signature: str
        """
        self._custom_signature = custom_signature

    @property
    def custom_public_key(self):
        r"""Gets the custom_public_key of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.

        **参数解释：** 通用类型接入点公钥信息 **约束限制：** 格式是X509公钥格式中的Base64字符串 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The custom_public_key of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.
        :rtype: str
        """
        return self._custom_public_key

    @custom_public_key.setter
    def custom_public_key(self, custom_public_key):
        r"""Sets the custom_public_key of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.

        **参数解释：** 通用类型接入点公钥信息 **约束限制：** 格式是X509公钥格式中的Base64字符串 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param custom_public_key: The custom_public_key of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.
        :type custom_public_key: str
        """
        self._custom_public_key = custom_public_key

    @property
    def expire_time(self):
        r"""Gets the expire_time of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.

        **参数解释：** 通用类型签名信息过期时间 **约束限制：** 时间格式是ISO 8601格式，yyyy-mm-ddTHH:MM:SSZ **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The expire_time of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.

        **参数解释：** 通用类型签名信息过期时间 **约束限制：** 时间格式是ISO 8601格式，yyyy-mm-ddTHH:MM:SSZ **取值范围：** 不涉及 **默认取值：** 不涉及

        :param expire_time: The expire_time of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def service_token(self):
        r"""Gets the service_token of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.

        **参数解释：** CCE类型访问凭证 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The service_token of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.
        :rtype: str
        """
        return self._service_token

    @service_token.setter
    def service_token(self, service_token):
        r"""Sets the service_token of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.

        **参数解释：** CCE类型访问凭证 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param service_token: The service_token of this DecryptDatakeyCapsuleRequestBodyAttestationDocument.
        :type service_token: str
        """
        self._service_token = service_token

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
        if not isinstance(other, DecryptDatakeyCapsuleRequestBodyAttestationDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
