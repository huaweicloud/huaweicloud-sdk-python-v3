# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTenantRepoEncryptionSettingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'encryption_type': 'str',
        'default_encryption_enabled': 'bool',
        'cmk_key_name': 'str',
        'cmk_key_id': 'str',
        'id': 'int',
        'key_state': 'str',
        'region': 'str',
        'region_type': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'encryption_type': 'encryption_type',
        'default_encryption_enabled': 'default_encryption_enabled',
        'cmk_key_name': 'cmk_key_name',
        'cmk_key_id': 'cmk_key_id',
        'id': 'id',
        'key_state': 'key_state',
        'region': 'region',
        'region_type': 'region_type'
    }

    def __init__(self, tenant_id=None, encryption_type=None, default_encryption_enabled=None, cmk_key_name=None, cmk_key_id=None, id=None, key_state=None, region=None, region_type=None):
        r"""ShowTenantRepoEncryptionSettingResponse

        The model defined in huaweicloud sdk

        :param tenant_id: **参数解释：** 租户id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type tenant_id: str
        :param encryption_type: **参数解释：** 加密类型。 **取值范围：** KMS表示开启KMS加密，normal或者null表示未开启KMS加密。
        :type encryption_type: str
        :param default_encryption_enabled: **参数解释：** 是否开启租户下默认加密设置。
        :type default_encryption_enabled: bool
        :param cmk_key_name: **参数解释：** 加密主密钥的名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type cmk_key_name: str
        :param cmk_key_id: **参数解释：** 加密主密钥的id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type cmk_key_id: str
        :param id: **参数解释：** 记录id。
        :type id: int
        :param key_state: **参数解释：** 加密主密钥key的状态。 **取值范围：** 1表示待激活状态,2 表示启用状态,3 表示禁用状态,4 表示计划删除状态,5 表示等待导入状态。
        :type key_state: str
        :param region: **参数解释：** 当前region 。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type region: str
        :param region_type: **参数解释：** region类型。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type region_type: str
        """
        
        super().__init__()

        self._tenant_id = None
        self._encryption_type = None
        self._default_encryption_enabled = None
        self._cmk_key_name = None
        self._cmk_key_id = None
        self._id = None
        self._key_state = None
        self._region = None
        self._region_type = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if encryption_type is not None:
            self.encryption_type = encryption_type
        if default_encryption_enabled is not None:
            self.default_encryption_enabled = default_encryption_enabled
        if cmk_key_name is not None:
            self.cmk_key_name = cmk_key_name
        if cmk_key_id is not None:
            self.cmk_key_id = cmk_key_id
        if id is not None:
            self.id = id
        if key_state is not None:
            self.key_state = key_state
        if region is not None:
            self.region = region
        if region_type is not None:
            self.region_type = region_type

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ShowTenantRepoEncryptionSettingResponse.

        **参数解释：** 租户id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The tenant_id of this ShowTenantRepoEncryptionSettingResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ShowTenantRepoEncryptionSettingResponse.

        **参数解释：** 租户id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param tenant_id: The tenant_id of this ShowTenantRepoEncryptionSettingResponse.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def encryption_type(self):
        r"""Gets the encryption_type of this ShowTenantRepoEncryptionSettingResponse.

        **参数解释：** 加密类型。 **取值范围：** KMS表示开启KMS加密，normal或者null表示未开启KMS加密。

        :return: The encryption_type of this ShowTenantRepoEncryptionSettingResponse.
        :rtype: str
        """
        return self._encryption_type

    @encryption_type.setter
    def encryption_type(self, encryption_type):
        r"""Sets the encryption_type of this ShowTenantRepoEncryptionSettingResponse.

        **参数解释：** 加密类型。 **取值范围：** KMS表示开启KMS加密，normal或者null表示未开启KMS加密。

        :param encryption_type: The encryption_type of this ShowTenantRepoEncryptionSettingResponse.
        :type encryption_type: str
        """
        self._encryption_type = encryption_type

    @property
    def default_encryption_enabled(self):
        r"""Gets the default_encryption_enabled of this ShowTenantRepoEncryptionSettingResponse.

        **参数解释：** 是否开启租户下默认加密设置。

        :return: The default_encryption_enabled of this ShowTenantRepoEncryptionSettingResponse.
        :rtype: bool
        """
        return self._default_encryption_enabled

    @default_encryption_enabled.setter
    def default_encryption_enabled(self, default_encryption_enabled):
        r"""Sets the default_encryption_enabled of this ShowTenantRepoEncryptionSettingResponse.

        **参数解释：** 是否开启租户下默认加密设置。

        :param default_encryption_enabled: The default_encryption_enabled of this ShowTenantRepoEncryptionSettingResponse.
        :type default_encryption_enabled: bool
        """
        self._default_encryption_enabled = default_encryption_enabled

    @property
    def cmk_key_name(self):
        r"""Gets the cmk_key_name of this ShowTenantRepoEncryptionSettingResponse.

        **参数解释：** 加密主密钥的名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The cmk_key_name of this ShowTenantRepoEncryptionSettingResponse.
        :rtype: str
        """
        return self._cmk_key_name

    @cmk_key_name.setter
    def cmk_key_name(self, cmk_key_name):
        r"""Sets the cmk_key_name of this ShowTenantRepoEncryptionSettingResponse.

        **参数解释：** 加密主密钥的名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param cmk_key_name: The cmk_key_name of this ShowTenantRepoEncryptionSettingResponse.
        :type cmk_key_name: str
        """
        self._cmk_key_name = cmk_key_name

    @property
    def cmk_key_id(self):
        r"""Gets the cmk_key_id of this ShowTenantRepoEncryptionSettingResponse.

        **参数解释：** 加密主密钥的id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The cmk_key_id of this ShowTenantRepoEncryptionSettingResponse.
        :rtype: str
        """
        return self._cmk_key_id

    @cmk_key_id.setter
    def cmk_key_id(self, cmk_key_id):
        r"""Sets the cmk_key_id of this ShowTenantRepoEncryptionSettingResponse.

        **参数解释：** 加密主密钥的id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param cmk_key_id: The cmk_key_id of this ShowTenantRepoEncryptionSettingResponse.
        :type cmk_key_id: str
        """
        self._cmk_key_id = cmk_key_id

    @property
    def id(self):
        r"""Gets the id of this ShowTenantRepoEncryptionSettingResponse.

        **参数解释：** 记录id。

        :return: The id of this ShowTenantRepoEncryptionSettingResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowTenantRepoEncryptionSettingResponse.

        **参数解释：** 记录id。

        :param id: The id of this ShowTenantRepoEncryptionSettingResponse.
        :type id: int
        """
        self._id = id

    @property
    def key_state(self):
        r"""Gets the key_state of this ShowTenantRepoEncryptionSettingResponse.

        **参数解释：** 加密主密钥key的状态。 **取值范围：** 1表示待激活状态,2 表示启用状态,3 表示禁用状态,4 表示计划删除状态,5 表示等待导入状态。

        :return: The key_state of this ShowTenantRepoEncryptionSettingResponse.
        :rtype: str
        """
        return self._key_state

    @key_state.setter
    def key_state(self, key_state):
        r"""Sets the key_state of this ShowTenantRepoEncryptionSettingResponse.

        **参数解释：** 加密主密钥key的状态。 **取值范围：** 1表示待激活状态,2 表示启用状态,3 表示禁用状态,4 表示计划删除状态,5 表示等待导入状态。

        :param key_state: The key_state of this ShowTenantRepoEncryptionSettingResponse.
        :type key_state: str
        """
        self._key_state = key_state

    @property
    def region(self):
        r"""Gets the region of this ShowTenantRepoEncryptionSettingResponse.

        **参数解释：** 当前region 。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The region of this ShowTenantRepoEncryptionSettingResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowTenantRepoEncryptionSettingResponse.

        **参数解释：** 当前region 。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param region: The region of this ShowTenantRepoEncryptionSettingResponse.
        :type region: str
        """
        self._region = region

    @property
    def region_type(self):
        r"""Gets the region_type of this ShowTenantRepoEncryptionSettingResponse.

        **参数解释：** region类型。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The region_type of this ShowTenantRepoEncryptionSettingResponse.
        :rtype: str
        """
        return self._region_type

    @region_type.setter
    def region_type(self, region_type):
        r"""Sets the region_type of this ShowTenantRepoEncryptionSettingResponse.

        **参数解释：** region类型。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param region_type: The region_type of this ShowTenantRepoEncryptionSettingResponse.
        :type region_type: str
        """
        self._region_type = region_type

    def to_dict(self):
        import warnings
        warnings.warn("ShowTenantRepoEncryptionSettingResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowTenantRepoEncryptionSettingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
