# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecretVolumeResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'secret_name': 'str',
        'secret_key': 'str',
        'secret_value': 'str',
        'mount_path': 'str'
    }

    attribute_map = {
        'secret_name': 'secret_name',
        'secret_key': 'secret_key',
        'secret_value': 'secret_value',
        'mount_path': 'mount_path'
    }

    def __init__(self, secret_name=None, secret_key=None, secret_value=None, mount_path=None):
        r"""SecretVolumeResponse

        The model defined in huaweicloud sdk

        :param secret_name: **参数解释：** 密钥名称。 **取值范围：** 不涉及。
        :type secret_name: str
        :param secret_key: **参数解释：** 密钥key。 **取值范围：** 长度不大于63。
        :type secret_key: str
        :param secret_value: **参数解释：** 密钥值。 **取值范围：** 长度不大于32768。
        :type secret_value: str
        :param mount_path: **参数解释：** 挂载路径。 **取值范围：** 不涉及。
        :type mount_path: str
        """
        
        

        self._secret_name = None
        self._secret_key = None
        self._secret_value = None
        self._mount_path = None
        self.discriminator = None

        if secret_name is not None:
            self.secret_name = secret_name
        if secret_key is not None:
            self.secret_key = secret_key
        if secret_value is not None:
            self.secret_value = secret_value
        self.mount_path = mount_path

    @property
    def secret_name(self):
        r"""Gets the secret_name of this SecretVolumeResponse.

        **参数解释：** 密钥名称。 **取值范围：** 不涉及。

        :return: The secret_name of this SecretVolumeResponse.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        r"""Sets the secret_name of this SecretVolumeResponse.

        **参数解释：** 密钥名称。 **取值范围：** 不涉及。

        :param secret_name: The secret_name of this SecretVolumeResponse.
        :type secret_name: str
        """
        self._secret_name = secret_name

    @property
    def secret_key(self):
        r"""Gets the secret_key of this SecretVolumeResponse.

        **参数解释：** 密钥key。 **取值范围：** 长度不大于63。

        :return: The secret_key of this SecretVolumeResponse.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        r"""Sets the secret_key of this SecretVolumeResponse.

        **参数解释：** 密钥key。 **取值范围：** 长度不大于63。

        :param secret_key: The secret_key of this SecretVolumeResponse.
        :type secret_key: str
        """
        self._secret_key = secret_key

    @property
    def secret_value(self):
        r"""Gets the secret_value of this SecretVolumeResponse.

        **参数解释：** 密钥值。 **取值范围：** 长度不大于32768。

        :return: The secret_value of this SecretVolumeResponse.
        :rtype: str
        """
        return self._secret_value

    @secret_value.setter
    def secret_value(self, secret_value):
        r"""Sets the secret_value of this SecretVolumeResponse.

        **参数解释：** 密钥值。 **取值范围：** 长度不大于32768。

        :param secret_value: The secret_value of this SecretVolumeResponse.
        :type secret_value: str
        """
        self._secret_value = secret_value

    @property
    def mount_path(self):
        r"""Gets the mount_path of this SecretVolumeResponse.

        **参数解释：** 挂载路径。 **取值范围：** 不涉及。

        :return: The mount_path of this SecretVolumeResponse.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        r"""Sets the mount_path of this SecretVolumeResponse.

        **参数解释：** 挂载路径。 **取值范围：** 不涉及。

        :param mount_path: The mount_path of this SecretVolumeResponse.
        :type mount_path: str
        """
        self._mount_path = mount_path

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
        if not isinstance(other, SecretVolumeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
