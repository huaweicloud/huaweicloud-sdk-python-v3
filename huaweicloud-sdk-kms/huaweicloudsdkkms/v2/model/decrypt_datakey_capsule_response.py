# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DecryptDatakeyCapsuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'instance_id': 'str',
        'datakey': 'str',
        'datakey_cipher': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'instance_id': 'instance_id',
        'datakey': 'datakey',
        'datakey_cipher': 'datakey_cipher'
    }

    def __init__(self, key_id=None, instance_id=None, datakey=None, datakey_cipher=None):
        r"""DecryptDatakeyCapsuleResponse

        The model defined in huaweicloud sdk

        :param key_id: **参数解释：** 密钥ID **取值范围：** 不涉及
        :type key_id: str
        :param instance_id: **参数解释：** 解密胶囊所在的实例ID **取值范围：** ECS ID，CCE的集群ID或者通用场景的access_point_id
        :type instance_id: str
        :param datakey: **参数解释：** datakey和datakey_cipher响应二选一，如果请求参数中没传递public_key，则返回datakey **取值范围：** 不涉及
        :type datakey: str
        :param datakey_cipher: **参数解释：** datakey和datakey_cipher响应二选一，如果请求参数中传递了public_key，使用public_key加密datakey后返回datakey_cipher **取值范围：** 不涉及
        :type datakey_cipher: str
        """
        
        super().__init__()

        self._key_id = None
        self._instance_id = None
        self._datakey = None
        self._datakey_cipher = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if instance_id is not None:
            self.instance_id = instance_id
        if datakey is not None:
            self.datakey = datakey
        if datakey_cipher is not None:
            self.datakey_cipher = datakey_cipher

    @property
    def key_id(self):
        r"""Gets the key_id of this DecryptDatakeyCapsuleResponse.

        **参数解释：** 密钥ID **取值范围：** 不涉及

        :return: The key_id of this DecryptDatakeyCapsuleResponse.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this DecryptDatakeyCapsuleResponse.

        **参数解释：** 密钥ID **取值范围：** 不涉及

        :param key_id: The key_id of this DecryptDatakeyCapsuleResponse.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DecryptDatakeyCapsuleResponse.

        **参数解释：** 解密胶囊所在的实例ID **取值范围：** ECS ID，CCE的集群ID或者通用场景的access_point_id

        :return: The instance_id of this DecryptDatakeyCapsuleResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DecryptDatakeyCapsuleResponse.

        **参数解释：** 解密胶囊所在的实例ID **取值范围：** ECS ID，CCE的集群ID或者通用场景的access_point_id

        :param instance_id: The instance_id of this DecryptDatakeyCapsuleResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def datakey(self):
        r"""Gets the datakey of this DecryptDatakeyCapsuleResponse.

        **参数解释：** datakey和datakey_cipher响应二选一，如果请求参数中没传递public_key，则返回datakey **取值范围：** 不涉及

        :return: The datakey of this DecryptDatakeyCapsuleResponse.
        :rtype: str
        """
        return self._datakey

    @datakey.setter
    def datakey(self, datakey):
        r"""Sets the datakey of this DecryptDatakeyCapsuleResponse.

        **参数解释：** datakey和datakey_cipher响应二选一，如果请求参数中没传递public_key，则返回datakey **取值范围：** 不涉及

        :param datakey: The datakey of this DecryptDatakeyCapsuleResponse.
        :type datakey: str
        """
        self._datakey = datakey

    @property
    def datakey_cipher(self):
        r"""Gets the datakey_cipher of this DecryptDatakeyCapsuleResponse.

        **参数解释：** datakey和datakey_cipher响应二选一，如果请求参数中传递了public_key，使用public_key加密datakey后返回datakey_cipher **取值范围：** 不涉及

        :return: The datakey_cipher of this DecryptDatakeyCapsuleResponse.
        :rtype: str
        """
        return self._datakey_cipher

    @datakey_cipher.setter
    def datakey_cipher(self, datakey_cipher):
        r"""Sets the datakey_cipher of this DecryptDatakeyCapsuleResponse.

        **参数解释：** datakey和datakey_cipher响应二选一，如果请求参数中传递了public_key，使用public_key加密datakey后返回datakey_cipher **取值范围：** 不涉及

        :param datakey_cipher: The datakey_cipher of this DecryptDatakeyCapsuleResponse.
        :type datakey_cipher: str
        """
        self._datakey_cipher = datakey_cipher

    def to_dict(self):
        import warnings
        warnings.warn("DecryptDatakeyCapsuleResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DecryptDatakeyCapsuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
