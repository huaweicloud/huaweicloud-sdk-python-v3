# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectEncryptionStatusBriefDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'status': 'str',
        'last_encryption_at': 'str',
        'last_decryption_at': 'str',
        'is_consistent': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'last_encryption_at': 'last_encryption_at',
        'last_decryption_at': 'last_decryption_at',
        'is_consistent': 'is_consistent'
    }

    def __init__(self, id=None, status=None, last_encryption_at=None, last_decryption_at=None, is_consistent=None):
        r"""ProjectEncryptionStatusBriefDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 仓库加密状态ID。 **取值范围：** 不涉及。
        :type id: int
        :param status: **参数解释：** 仓库加密状态 **取值范围：** - encrypting，加密中。 - encrypted，已加密。 - decrypting，解密中。 - decrypted，已解密。 **默认取值：** 不涉及。
        :type status: str
        :param last_encryption_at: **参数解释：** 最近加密时间。 **取值范围：** 不涉及。
        :type last_encryption_at: str
        :param last_decryption_at: **参数解释：** 最近解密时间。 **取值范围：** 不涉及。
        :type last_decryption_at: str
        :param is_consistent: **参数解释：** 是否开启仓库加密。 **约束限制：** 不涉及。 **取值范围：** - true，开启仓库加密。 - false，关闭仓库加密。
        :type is_consistent: bool
        """
        
        

        self._id = None
        self._status = None
        self._last_encryption_at = None
        self._last_decryption_at = None
        self._is_consistent = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if last_encryption_at is not None:
            self.last_encryption_at = last_encryption_at
        if last_decryption_at is not None:
            self.last_decryption_at = last_decryption_at
        if is_consistent is not None:
            self.is_consistent = is_consistent

    @property
    def id(self):
        r"""Gets the id of this ProjectEncryptionStatusBriefDto.

        **参数解释：** 仓库加密状态ID。 **取值范围：** 不涉及。

        :return: The id of this ProjectEncryptionStatusBriefDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProjectEncryptionStatusBriefDto.

        **参数解释：** 仓库加密状态ID。 **取值范围：** 不涉及。

        :param id: The id of this ProjectEncryptionStatusBriefDto.
        :type id: int
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this ProjectEncryptionStatusBriefDto.

        **参数解释：** 仓库加密状态 **取值范围：** - encrypting，加密中。 - encrypted，已加密。 - decrypting，解密中。 - decrypted，已解密。 **默认取值：** 不涉及。

        :return: The status of this ProjectEncryptionStatusBriefDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ProjectEncryptionStatusBriefDto.

        **参数解释：** 仓库加密状态 **取值范围：** - encrypting，加密中。 - encrypted，已加密。 - decrypting，解密中。 - decrypted，已解密。 **默认取值：** 不涉及。

        :param status: The status of this ProjectEncryptionStatusBriefDto.
        :type status: str
        """
        self._status = status

    @property
    def last_encryption_at(self):
        r"""Gets the last_encryption_at of this ProjectEncryptionStatusBriefDto.

        **参数解释：** 最近加密时间。 **取值范围：** 不涉及。

        :return: The last_encryption_at of this ProjectEncryptionStatusBriefDto.
        :rtype: str
        """
        return self._last_encryption_at

    @last_encryption_at.setter
    def last_encryption_at(self, last_encryption_at):
        r"""Sets the last_encryption_at of this ProjectEncryptionStatusBriefDto.

        **参数解释：** 最近加密时间。 **取值范围：** 不涉及。

        :param last_encryption_at: The last_encryption_at of this ProjectEncryptionStatusBriefDto.
        :type last_encryption_at: str
        """
        self._last_encryption_at = last_encryption_at

    @property
    def last_decryption_at(self):
        r"""Gets the last_decryption_at of this ProjectEncryptionStatusBriefDto.

        **参数解释：** 最近解密时间。 **取值范围：** 不涉及。

        :return: The last_decryption_at of this ProjectEncryptionStatusBriefDto.
        :rtype: str
        """
        return self._last_decryption_at

    @last_decryption_at.setter
    def last_decryption_at(self, last_decryption_at):
        r"""Sets the last_decryption_at of this ProjectEncryptionStatusBriefDto.

        **参数解释：** 最近解密时间。 **取值范围：** 不涉及。

        :param last_decryption_at: The last_decryption_at of this ProjectEncryptionStatusBriefDto.
        :type last_decryption_at: str
        """
        self._last_decryption_at = last_decryption_at

    @property
    def is_consistent(self):
        r"""Gets the is_consistent of this ProjectEncryptionStatusBriefDto.

        **参数解释：** 是否开启仓库加密。 **约束限制：** 不涉及。 **取值范围：** - true，开启仓库加密。 - false，关闭仓库加密。

        :return: The is_consistent of this ProjectEncryptionStatusBriefDto.
        :rtype: bool
        """
        return self._is_consistent

    @is_consistent.setter
    def is_consistent(self, is_consistent):
        r"""Sets the is_consistent of this ProjectEncryptionStatusBriefDto.

        **参数解释：** 是否开启仓库加密。 **约束限制：** 不涉及。 **取值范围：** - true，开启仓库加密。 - false，关闭仓库加密。

        :param is_consistent: The is_consistent of this ProjectEncryptionStatusBriefDto.
        :type is_consistent: bool
        """
        self._is_consistent = is_consistent

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
        if not isinstance(other, ProjectEncryptionStatusBriefDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
