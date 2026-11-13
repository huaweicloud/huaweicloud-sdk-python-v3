# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicUpdateInfo:

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
        'op_type': 'str'
    }

    attribute_map = {
        'kid': 'kid',
        'public_key': 'public_key',
        'op_type': 'op_type'
    }

    def __init__(self, kid=None, public_key=None, op_type=None):
        r"""PublicUpdateInfo

        The model defined in huaweicloud sdk

        :param kid: **参数解释**： Key ID。 **约束限制**： 不涉及。 **取值范围**： [1-128]个字符。 **默认取值**： 不涉及。
        :type kid: str
        :param public_key: **参数解释**： PEM 格式公钥。 **约束限制**： 不涉及。 **取值范围**： [1-2048]的字符串。 **默认取值**： 不涉及。
        :type public_key: str
        :param op_type: **参数解释**： 操作类型。 **约束限制**： 不涉及。 **取值范围**： - add：新增。 - update：更新。 - delete：删除 **默认取值**： 不涉及。
        :type op_type: str
        """
        
        

        self._kid = None
        self._public_key = None
        self._op_type = None
        self.discriminator = None

        if kid is not None:
            self.kid = kid
        if public_key is not None:
            self.public_key = public_key
        if op_type is not None:
            self.op_type = op_type

    @property
    def kid(self):
        r"""Gets the kid of this PublicUpdateInfo.

        **参数解释**： Key ID。 **约束限制**： 不涉及。 **取值范围**： [1-128]个字符。 **默认取值**： 不涉及。

        :return: The kid of this PublicUpdateInfo.
        :rtype: str
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        r"""Sets the kid of this PublicUpdateInfo.

        **参数解释**： Key ID。 **约束限制**： 不涉及。 **取值范围**： [1-128]个字符。 **默认取值**： 不涉及。

        :param kid: The kid of this PublicUpdateInfo.
        :type kid: str
        """
        self._kid = kid

    @property
    def public_key(self):
        r"""Gets the public_key of this PublicUpdateInfo.

        **参数解释**： PEM 格式公钥。 **约束限制**： 不涉及。 **取值范围**： [1-2048]的字符串。 **默认取值**： 不涉及。

        :return: The public_key of this PublicUpdateInfo.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        r"""Sets the public_key of this PublicUpdateInfo.

        **参数解释**： PEM 格式公钥。 **约束限制**： 不涉及。 **取值范围**： [1-2048]的字符串。 **默认取值**： 不涉及。

        :param public_key: The public_key of this PublicUpdateInfo.
        :type public_key: str
        """
        self._public_key = public_key

    @property
    def op_type(self):
        r"""Gets the op_type of this PublicUpdateInfo.

        **参数解释**： 操作类型。 **约束限制**： 不涉及。 **取值范围**： - add：新增。 - update：更新。 - delete：删除 **默认取值**： 不涉及。

        :return: The op_type of this PublicUpdateInfo.
        :rtype: str
        """
        return self._op_type

    @op_type.setter
    def op_type(self, op_type):
        r"""Sets the op_type of this PublicUpdateInfo.

        **参数解释**： 操作类型。 **约束限制**： 不涉及。 **取值范围**： - add：新增。 - update：更新。 - delete：删除 **默认取值**： 不涉及。

        :param op_type: The op_type of this PublicUpdateInfo.
        :type op_type: str
        """
        self._op_type = op_type

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
        if not isinstance(other, PublicUpdateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
