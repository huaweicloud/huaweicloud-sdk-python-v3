# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TenantCMKDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cmk_key_name': 'str',
        'cmk_key_id': 'str',
        'key_state': 'str'
    }

    attribute_map = {
        'cmk_key_name': 'cmk_key_name',
        'cmk_key_id': 'cmk_key_id',
        'key_state': 'key_state'
    }

    def __init__(self, cmk_key_name=None, cmk_key_id=None, key_state=None):
        r"""TenantCMKDto

        The model defined in huaweicloud sdk

        :param cmk_key_name: **参数解释：** 加密主密钥的名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type cmk_key_name: str
        :param cmk_key_id: **参数解释：** 加密主密钥的id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type cmk_key_id: str
        :param key_state: **参数解释：** 加密主密钥key的状态。 **取值范围：** 1表示待激活状态,2 表示启用状态,3 表示禁用状态,4 表示计划删除状态,5 表示等待导入状态。
        :type key_state: str
        """
        
        

        self._cmk_key_name = None
        self._cmk_key_id = None
        self._key_state = None
        self.discriminator = None

        if cmk_key_name is not None:
            self.cmk_key_name = cmk_key_name
        if cmk_key_id is not None:
            self.cmk_key_id = cmk_key_id
        if key_state is not None:
            self.key_state = key_state

    @property
    def cmk_key_name(self):
        r"""Gets the cmk_key_name of this TenantCMKDto.

        **参数解释：** 加密主密钥的名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The cmk_key_name of this TenantCMKDto.
        :rtype: str
        """
        return self._cmk_key_name

    @cmk_key_name.setter
    def cmk_key_name(self, cmk_key_name):
        r"""Sets the cmk_key_name of this TenantCMKDto.

        **参数解释：** 加密主密钥的名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param cmk_key_name: The cmk_key_name of this TenantCMKDto.
        :type cmk_key_name: str
        """
        self._cmk_key_name = cmk_key_name

    @property
    def cmk_key_id(self):
        r"""Gets the cmk_key_id of this TenantCMKDto.

        **参数解释：** 加密主密钥的id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The cmk_key_id of this TenantCMKDto.
        :rtype: str
        """
        return self._cmk_key_id

    @cmk_key_id.setter
    def cmk_key_id(self, cmk_key_id):
        r"""Sets the cmk_key_id of this TenantCMKDto.

        **参数解释：** 加密主密钥的id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param cmk_key_id: The cmk_key_id of this TenantCMKDto.
        :type cmk_key_id: str
        """
        self._cmk_key_id = cmk_key_id

    @property
    def key_state(self):
        r"""Gets the key_state of this TenantCMKDto.

        **参数解释：** 加密主密钥key的状态。 **取值范围：** 1表示待激活状态,2 表示启用状态,3 表示禁用状态,4 表示计划删除状态,5 表示等待导入状态。

        :return: The key_state of this TenantCMKDto.
        :rtype: str
        """
        return self._key_state

    @key_state.setter
    def key_state(self, key_state):
        r"""Sets the key_state of this TenantCMKDto.

        **参数解释：** 加密主密钥key的状态。 **取值范围：** 1表示待激活状态,2 表示启用状态,3 表示禁用状态,4 表示计划删除状态,5 表示等待导入状态。

        :param key_state: The key_state of this TenantCMKDto.
        :type key_state: str
        """
        self._key_state = key_state

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
        if not isinstance(other, TenantCMKDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
