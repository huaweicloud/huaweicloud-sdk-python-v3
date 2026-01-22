# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIpsWhitelistsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fw_instance_id': 'str',
        'source_address': 'str',
        'dest_address': 'str',
        'name': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'source_address': 'source_address',
        'dest_address': 'dest_address',
        'name': 'name',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, fw_instance_id=None, source_address=None, dest_address=None, name=None, limit=None, offset=None):
        r"""ListIpsWhitelistsRequest

        The model defined in huaweicloud sdk

        :param fw_instance_id: **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及
        :type fw_instance_id: str
        :param source_address: **参数解释**： 白名单源地址 **约束限制**： 不涉及  **取值范围**： 不涉及  **默认取值**： 不涉及
        :type source_address: str
        :param dest_address: **参数解释**：  目的地址  **约束限制**：  不涉及  **取值范围**：  不涉及  **默认取值**：  不涉及
        :type dest_address: str
        :param name: **参数解释**：  白名单名称  **约束限制**：  不涉及  **取值范围**： 不涉及  **默认取值**：  不涉及
        :type name: str
        :param limit: **参数解释**：  每页大小  **约束限制**：  不涉及  **取值范围**：  不涉及  **默认取值**：  不涉及
        :type limit: int
        :param offset: **参数解释**：  偏移量  **约束限制**：  不涉及  **取值范围**：  不涉及  **默认取值**：  不涉及
        :type offset: int
        """
        
        

        self._fw_instance_id = None
        self._source_address = None
        self._dest_address = None
        self._name = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.fw_instance_id = fw_instance_id
        if source_address is not None:
            self.source_address = source_address
        if dest_address is not None:
            self.dest_address = dest_address
        if name is not None:
            self.name = name
        self.limit = limit
        self.offset = offset

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ListIpsWhitelistsRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :return: The fw_instance_id of this ListIpsWhitelistsRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ListIpsWhitelistsRequest.

        **参数解释**： 防火墙ID，用户创建防火墙实例后产生的唯一ID，配置后可区分不同防火墙，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取 **约束限制**： 不涉及 **取值范围**： 32位UUID **默认取值**： 不涉及

        :param fw_instance_id: The fw_instance_id of this ListIpsWhitelistsRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def source_address(self):
        r"""Gets the source_address of this ListIpsWhitelistsRequest.

        **参数解释**： 白名单源地址 **约束限制**： 不涉及  **取值范围**： 不涉及  **默认取值**： 不涉及

        :return: The source_address of this ListIpsWhitelistsRequest.
        :rtype: str
        """
        return self._source_address

    @source_address.setter
    def source_address(self, source_address):
        r"""Sets the source_address of this ListIpsWhitelistsRequest.

        **参数解释**： 白名单源地址 **约束限制**： 不涉及  **取值范围**： 不涉及  **默认取值**： 不涉及

        :param source_address: The source_address of this ListIpsWhitelistsRequest.
        :type source_address: str
        """
        self._source_address = source_address

    @property
    def dest_address(self):
        r"""Gets the dest_address of this ListIpsWhitelistsRequest.

        **参数解释**：  目的地址  **约束限制**：  不涉及  **取值范围**：  不涉及  **默认取值**：  不涉及

        :return: The dest_address of this ListIpsWhitelistsRequest.
        :rtype: str
        """
        return self._dest_address

    @dest_address.setter
    def dest_address(self, dest_address):
        r"""Sets the dest_address of this ListIpsWhitelistsRequest.

        **参数解释**：  目的地址  **约束限制**：  不涉及  **取值范围**：  不涉及  **默认取值**：  不涉及

        :param dest_address: The dest_address of this ListIpsWhitelistsRequest.
        :type dest_address: str
        """
        self._dest_address = dest_address

    @property
    def name(self):
        r"""Gets the name of this ListIpsWhitelistsRequest.

        **参数解释**：  白名单名称  **约束限制**：  不涉及  **取值范围**： 不涉及  **默认取值**：  不涉及

        :return: The name of this ListIpsWhitelistsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListIpsWhitelistsRequest.

        **参数解释**：  白名单名称  **约束限制**：  不涉及  **取值范围**： 不涉及  **默认取值**：  不涉及

        :param name: The name of this ListIpsWhitelistsRequest.
        :type name: str
        """
        self._name = name

    @property
    def limit(self):
        r"""Gets the limit of this ListIpsWhitelistsRequest.

        **参数解释**：  每页大小  **约束限制**：  不涉及  **取值范围**：  不涉及  **默认取值**：  不涉及

        :return: The limit of this ListIpsWhitelistsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListIpsWhitelistsRequest.

        **参数解释**：  每页大小  **约束限制**：  不涉及  **取值范围**：  不涉及  **默认取值**：  不涉及

        :param limit: The limit of this ListIpsWhitelistsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListIpsWhitelistsRequest.

        **参数解释**：  偏移量  **约束限制**：  不涉及  **取值范围**：  不涉及  **默认取值**：  不涉及

        :return: The offset of this ListIpsWhitelistsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListIpsWhitelistsRequest.

        **参数解释**：  偏移量  **约束限制**：  不涉及  **取值范围**：  不涉及  **默认取值**：  不涉及

        :param offset: The offset of this ListIpsWhitelistsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListIpsWhitelistsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
