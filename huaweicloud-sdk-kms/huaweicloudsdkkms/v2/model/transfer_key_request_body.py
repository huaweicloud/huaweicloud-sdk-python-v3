# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransferKeyRequestBody:

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
        'target_keyspace_id': 'str',
        'transfer_mode': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'target_keyspace_id': 'target_keyspace_id',
        'transfer_mode': 'transfer_mode'
    }

    def __init__(self, key_id=None, target_keyspace_id=None, transfer_mode=None):
        r"""TransferKeyRequestBody

        The model defined in huaweicloud sdk

        :param key_id: **参数解释：** 待转移的密钥ID **约束限制：** 满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及
        :type key_id: str
        :param target_keyspace_id: **参数解释：** 目标密钥空间ID **约束限制：** 满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及
        :type target_keyspace_id: str
        :param transfer_mode: **参数解释：** 转移模式 **约束限制：** ASSIGN模式仅支持对称密钥，且密钥必须未属于任何密钥空间，目标密钥空间类型需与密钥所属keystore类型匹配； **取值范围：** - ASSIGN：将密钥分配给目标密钥空间 **默认取值：** ASSIGN
        :type transfer_mode: str
        """
        
        

        self._key_id = None
        self._target_keyspace_id = None
        self._transfer_mode = None
        self.discriminator = None

        self.key_id = key_id
        self.target_keyspace_id = target_keyspace_id
        if transfer_mode is not None:
            self.transfer_mode = transfer_mode

    @property
    def key_id(self):
        r"""Gets the key_id of this TransferKeyRequestBody.

        **参数解释：** 待转移的密钥ID **约束限制：** 满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The key_id of this TransferKeyRequestBody.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this TransferKeyRequestBody.

        **参数解释：** 待转移的密钥ID **约束限制：** 满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及

        :param key_id: The key_id of this TransferKeyRequestBody.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def target_keyspace_id(self):
        r"""Gets the target_keyspace_id of this TransferKeyRequestBody.

        **参数解释：** 目标密钥空间ID **约束限制：** 满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The target_keyspace_id of this TransferKeyRequestBody.
        :rtype: str
        """
        return self._target_keyspace_id

    @target_keyspace_id.setter
    def target_keyspace_id(self, target_keyspace_id):
        r"""Sets the target_keyspace_id of this TransferKeyRequestBody.

        **参数解释：** 目标密钥空间ID **约束限制：** 满足正则表达式^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ **取值范围：** 不涉及 **默认取值：** 不涉及

        :param target_keyspace_id: The target_keyspace_id of this TransferKeyRequestBody.
        :type target_keyspace_id: str
        """
        self._target_keyspace_id = target_keyspace_id

    @property
    def transfer_mode(self):
        r"""Gets the transfer_mode of this TransferKeyRequestBody.

        **参数解释：** 转移模式 **约束限制：** ASSIGN模式仅支持对称密钥，且密钥必须未属于任何密钥空间，目标密钥空间类型需与密钥所属keystore类型匹配； **取值范围：** - ASSIGN：将密钥分配给目标密钥空间 **默认取值：** ASSIGN

        :return: The transfer_mode of this TransferKeyRequestBody.
        :rtype: str
        """
        return self._transfer_mode

    @transfer_mode.setter
    def transfer_mode(self, transfer_mode):
        r"""Sets the transfer_mode of this TransferKeyRequestBody.

        **参数解释：** 转移模式 **约束限制：** ASSIGN模式仅支持对称密钥，且密钥必须未属于任何密钥空间，目标密钥空间类型需与密钥所属keystore类型匹配； **取值范围：** - ASSIGN：将密钥分配给目标密钥空间 **默认取值：** ASSIGN

        :param transfer_mode: The transfer_mode of this TransferKeyRequestBody.
        :type transfer_mode: str
        """
        self._transfer_mode = transfer_mode

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
        if not isinstance(other, TransferKeyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
