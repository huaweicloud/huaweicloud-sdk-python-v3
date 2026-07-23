# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionModelVersionMasterQueryDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'master_id': 'str',
        'version': 'str',
        'iteration': 'int',
        'decrypt': 'bool'
    }

    attribute_map = {
        'master_id': 'masterId',
        'version': 'version',
        'iteration': 'iteration',
        'decrypt': 'decrypt'
    }

    def __init__(self, master_id=None, version=None, iteration=None, decrypt=None):
        r"""VersionModelVersionMasterQueryDTO

        The model defined in huaweicloud sdk

        :param master_id: **参数解释：**  主对象ID，用于定位M-V模型实例所属的主对象。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type master_id: str
        :param version: **参数解释：**  版本号，用于指定查询的版本标识。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type version: str
        :param iteration: **参数解释：**  迭代版本号，用于精确定位某一版本下的特定迭代。如果此参数为空，则返回M-V模型实例的最新版本信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type iteration: int
        :param decrypt: **参数解释：**  是否对返回数据进行解密。当数据实体配置了加密属性时，可通过此参数控制是否返回明文数据。  **约束限制：**  不涉及。  **取值范围：**  - true：加密。 - false：不加密。  **默认取值：**  false。
        :type decrypt: bool
        """
        
        

        self._master_id = None
        self._version = None
        self._iteration = None
        self._decrypt = None
        self.discriminator = None

        self.master_id = master_id
        self.version = version
        if iteration is not None:
            self.iteration = iteration
        if decrypt is not None:
            self.decrypt = decrypt

    @property
    def master_id(self):
        r"""Gets the master_id of this VersionModelVersionMasterQueryDTO.

        **参数解释：**  主对象ID，用于定位M-V模型实例所属的主对象。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The master_id of this VersionModelVersionMasterQueryDTO.
        :rtype: str
        """
        return self._master_id

    @master_id.setter
    def master_id(self, master_id):
        r"""Sets the master_id of this VersionModelVersionMasterQueryDTO.

        **参数解释：**  主对象ID，用于定位M-V模型实例所属的主对象。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param master_id: The master_id of this VersionModelVersionMasterQueryDTO.
        :type master_id: str
        """
        self._master_id = master_id

    @property
    def version(self):
        r"""Gets the version of this VersionModelVersionMasterQueryDTO.

        **参数解释：**  版本号，用于指定查询的版本标识。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The version of this VersionModelVersionMasterQueryDTO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this VersionModelVersionMasterQueryDTO.

        **参数解释：**  版本号，用于指定查询的版本标识。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param version: The version of this VersionModelVersionMasterQueryDTO.
        :type version: str
        """
        self._version = version

    @property
    def iteration(self):
        r"""Gets the iteration of this VersionModelVersionMasterQueryDTO.

        **参数解释：**  迭代版本号，用于精确定位某一版本下的特定迭代。如果此参数为空，则返回M-V模型实例的最新版本信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The iteration of this VersionModelVersionMasterQueryDTO.
        :rtype: int
        """
        return self._iteration

    @iteration.setter
    def iteration(self, iteration):
        r"""Sets the iteration of this VersionModelVersionMasterQueryDTO.

        **参数解释：**  迭代版本号，用于精确定位某一版本下的特定迭代。如果此参数为空，则返回M-V模型实例的最新版本信息。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param iteration: The iteration of this VersionModelVersionMasterQueryDTO.
        :type iteration: int
        """
        self._iteration = iteration

    @property
    def decrypt(self):
        r"""Gets the decrypt of this VersionModelVersionMasterQueryDTO.

        **参数解释：**  是否对返回数据进行解密。当数据实体配置了加密属性时，可通过此参数控制是否返回明文数据。  **约束限制：**  不涉及。  **取值范围：**  - true：加密。 - false：不加密。  **默认取值：**  false。

        :return: The decrypt of this VersionModelVersionMasterQueryDTO.
        :rtype: bool
        """
        return self._decrypt

    @decrypt.setter
    def decrypt(self, decrypt):
        r"""Sets the decrypt of this VersionModelVersionMasterQueryDTO.

        **参数解释：**  是否对返回数据进行解密。当数据实体配置了加密属性时，可通过此参数控制是否返回明文数据。  **约束限制：**  不涉及。  **取值范围：**  - true：加密。 - false：不加密。  **默认取值：**  false。

        :param decrypt: The decrypt of this VersionModelVersionMasterQueryDTO.
        :type decrypt: bool
        """
        self._decrypt = decrypt

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
        if not isinstance(other, VersionModelVersionMasterQueryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
