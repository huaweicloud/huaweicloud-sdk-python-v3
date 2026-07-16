# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecretVolume:

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
        r"""SecretVolume

        The model defined in huaweicloud sdk

        :param secret_name: **参数解释：** 密钥名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type secret_name: str
        :param secret_key: **参数解释：** 密钥key。 **约束限制：** 匹配一个长度在1到63之间的字符串，只能包含字母、数字、点、下划线和连字符，并且不能以两个连续的点（..）开头。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type secret_key: str
        :param secret_value: **参数解释：** 密钥值。 **约束限制：** 长度在1~32768，Base64编码后的密钥值。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type secret_value: str
        :param mount_path: **参数解释：** 挂载路径。 **约束限制：** 不涉及。 **取值范围：** 以(/)开头和结尾，可包含字母、数字、中划线、下划线，整个挂载路径长度不能超过255位。 **默认取值：** 不涉及。
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
        r"""Gets the secret_name of this SecretVolume.

        **参数解释：** 密钥名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The secret_name of this SecretVolume.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        r"""Sets the secret_name of this SecretVolume.

        **参数解释：** 密钥名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param secret_name: The secret_name of this SecretVolume.
        :type secret_name: str
        """
        self._secret_name = secret_name

    @property
    def secret_key(self):
        r"""Gets the secret_key of this SecretVolume.

        **参数解释：** 密钥key。 **约束限制：** 匹配一个长度在1到63之间的字符串，只能包含字母、数字、点、下划线和连字符，并且不能以两个连续的点（..）开头。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The secret_key of this SecretVolume.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        r"""Sets the secret_key of this SecretVolume.

        **参数解释：** 密钥key。 **约束限制：** 匹配一个长度在1到63之间的字符串，只能包含字母、数字、点、下划线和连字符，并且不能以两个连续的点（..）开头。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param secret_key: The secret_key of this SecretVolume.
        :type secret_key: str
        """
        self._secret_key = secret_key

    @property
    def secret_value(self):
        r"""Gets the secret_value of this SecretVolume.

        **参数解释：** 密钥值。 **约束限制：** 长度在1~32768，Base64编码后的密钥值。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The secret_value of this SecretVolume.
        :rtype: str
        """
        return self._secret_value

    @secret_value.setter
    def secret_value(self, secret_value):
        r"""Sets the secret_value of this SecretVolume.

        **参数解释：** 密钥值。 **约束限制：** 长度在1~32768，Base64编码后的密钥值。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param secret_value: The secret_value of this SecretVolume.
        :type secret_value: str
        """
        self._secret_value = secret_value

    @property
    def mount_path(self):
        r"""Gets the mount_path of this SecretVolume.

        **参数解释：** 挂载路径。 **约束限制：** 不涉及。 **取值范围：** 以(/)开头和结尾，可包含字母、数字、中划线、下划线，整个挂载路径长度不能超过255位。 **默认取值：** 不涉及。

        :return: The mount_path of this SecretVolume.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        r"""Sets the mount_path of this SecretVolume.

        **参数解释：** 挂载路径。 **约束限制：** 不涉及。 **取值范围：** 以(/)开头和结尾，可包含字母、数字、中划线、下划线，整个挂载路径长度不能超过255位。 **默认取值：** 不涉及。

        :param mount_path: The mount_path of this SecretVolume.
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
        if not isinstance(other, SecretVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
