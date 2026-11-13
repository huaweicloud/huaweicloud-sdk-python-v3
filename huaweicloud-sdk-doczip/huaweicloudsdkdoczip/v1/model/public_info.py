# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kid': 'str',
        'public_key': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'kid': 'kid',
        'public_key': 'public_key',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, kid=None, public_key=None, created_at=None, updated_at=None):
        r"""PublicInfo

        The model defined in huaweicloud sdk

        :param kid: **参数解释**： Key ID。 **约束限制**： 不涉及。 **取值范围**： [1-128]个字符。 **默认取值**： 不涉及。
        :type kid: str
        :param public_key: **参数解释**： PEM 格式公钥。 **约束限制**： 不涉及。 **取值范围**： [1-2048]的字符串。 **默认取值**： 不涉及。
        :type public_key: str
        :param created_at: **参数解释**： [创建时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:his) [创建时间。UTC时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:hws) **取值范围**： 不涉及。
        :type created_at: datetime
        :param updated_at: **参数解释**： [创建时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:his) [创建时间。UTC时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:hws) **取值范围**： 不涉及。
        :type updated_at: datetime
        """
        
        

        self._kid = None
        self._public_key = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if kid is not None:
            self.kid = kid
        if public_key is not None:
            self.public_key = public_key
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def kid(self):
        r"""Gets the kid of this PublicInfo.

        **参数解释**： Key ID。 **约束限制**： 不涉及。 **取值范围**： [1-128]个字符。 **默认取值**： 不涉及。

        :return: The kid of this PublicInfo.
        :rtype: str
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        r"""Sets the kid of this PublicInfo.

        **参数解释**： Key ID。 **约束限制**： 不涉及。 **取值范围**： [1-128]个字符。 **默认取值**： 不涉及。

        :param kid: The kid of this PublicInfo.
        :type kid: str
        """
        self._kid = kid

    @property
    def public_key(self):
        r"""Gets the public_key of this PublicInfo.

        **参数解释**： PEM 格式公钥。 **约束限制**： 不涉及。 **取值范围**： [1-2048]的字符串。 **默认取值**： 不涉及。

        :return: The public_key of this PublicInfo.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        r"""Sets the public_key of this PublicInfo.

        **参数解释**： PEM 格式公钥。 **约束限制**： 不涉及。 **取值范围**： [1-2048]的字符串。 **默认取值**： 不涉及。

        :param public_key: The public_key of this PublicInfo.
        :type public_key: str
        """
        self._public_key = public_key

    @property
    def created_at(self):
        r"""Gets the created_at of this PublicInfo.

        **参数解释**： [创建时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:his) [创建时间。UTC时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:hws) **取值范围**： 不涉及。

        :return: The created_at of this PublicInfo.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this PublicInfo.

        **参数解释**： [创建时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:his) [创建时间。UTC时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:hws) **取值范围**： 不涉及。

        :param created_at: The created_at of this PublicInfo.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this PublicInfo.

        **参数解释**： [创建时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:his) [创建时间。UTC时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:hws) **取值范围**： 不涉及。

        :return: The updated_at of this PublicInfo.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this PublicInfo.

        **参数解释**： [创建时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:his) [创建时间。UTC时间。格式为YYYY-MM-DD HH:mm:ss。例如：2023-11-24 17:35:25。](tag:hws) **取值范围**： 不涉及。

        :param updated_at: The updated_at of this PublicInfo.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, PublicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
