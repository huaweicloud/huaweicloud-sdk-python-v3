# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicIp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'public_bind_type': 'str',
        'eip_id': 'str',
        'ip_type': 'str',
        'eip_address': 'str',
        'band_width': 'int',
        'status': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'public_bind_type': 'public_bind_type',
        'eip_id': 'eip_id',
        'ip_type': 'ip_type',
        'eip_address': 'eip_address',
        'band_width': 'band_width',
        'status': 'status',
        'error_message': 'error_message'
    }

    def __init__(self, public_bind_type=None, eip_id=None, ip_type=None, eip_address=None, band_width=None, status=None, error_message=None):
        r"""PublicIp

        The model defined in huaweicloud sdk

        :param public_bind_type: **参数解释**： 弹性IP绑定类型。 **约束限制**： 不涉及。 **取值范围**： - auto_assign：自动绑定。 - not_use：暂未使用。 - bind_existing ：使用已有。  **默认取值**： null
        :type public_bind_type: str
        :param eip_id: **参数解释**： 弹性公网IP的id。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null
        :type eip_id: str
        :param ip_type: **参数解释**： 弹性公网IP的类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null
        :type ip_type: str
        :param eip_address: **参数解释**： 弹性公网IP的地址。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null
        :type eip_address: str
        :param band_width: **参数解释**： 弹性公网IP的带宽。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null
        :type band_width: int
        :param status: **参数解释**： 弹性公网IP的状态。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null
        :type status: str
        :param error_message: **参数解释**： 弹性公网IP的错误码。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null
        :type error_message: str
        """
        
        

        self._public_bind_type = None
        self._eip_id = None
        self._ip_type = None
        self._eip_address = None
        self._band_width = None
        self._status = None
        self._error_message = None
        self.discriminator = None

        if public_bind_type is not None:
            self.public_bind_type = public_bind_type
        if eip_id is not None:
            self.eip_id = eip_id
        if ip_type is not None:
            self.ip_type = ip_type
        if eip_address is not None:
            self.eip_address = eip_address
        if band_width is not None:
            self.band_width = band_width
        if status is not None:
            self.status = status
        if error_message is not None:
            self.error_message = error_message

    @property
    def public_bind_type(self):
        r"""Gets the public_bind_type of this PublicIp.

        **参数解释**： 弹性IP绑定类型。 **约束限制**： 不涉及。 **取值范围**： - auto_assign：自动绑定。 - not_use：暂未使用。 - bind_existing ：使用已有。  **默认取值**： null

        :return: The public_bind_type of this PublicIp.
        :rtype: str
        """
        return self._public_bind_type

    @public_bind_type.setter
    def public_bind_type(self, public_bind_type):
        r"""Sets the public_bind_type of this PublicIp.

        **参数解释**： 弹性IP绑定类型。 **约束限制**： 不涉及。 **取值范围**： - auto_assign：自动绑定。 - not_use：暂未使用。 - bind_existing ：使用已有。  **默认取值**： null

        :param public_bind_type: The public_bind_type of this PublicIp.
        :type public_bind_type: str
        """
        self._public_bind_type = public_bind_type

    @property
    def eip_id(self):
        r"""Gets the eip_id of this PublicIp.

        **参数解释**： 弹性公网IP的id。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :return: The eip_id of this PublicIp.
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        r"""Sets the eip_id of this PublicIp.

        **参数解释**： 弹性公网IP的id。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :param eip_id: The eip_id of this PublicIp.
        :type eip_id: str
        """
        self._eip_id = eip_id

    @property
    def ip_type(self):
        r"""Gets the ip_type of this PublicIp.

        **参数解释**： 弹性公网IP的类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :return: The ip_type of this PublicIp.
        :rtype: str
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, ip_type):
        r"""Sets the ip_type of this PublicIp.

        **参数解释**： 弹性公网IP的类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :param ip_type: The ip_type of this PublicIp.
        :type ip_type: str
        """
        self._ip_type = ip_type

    @property
    def eip_address(self):
        r"""Gets the eip_address of this PublicIp.

        **参数解释**： 弹性公网IP的地址。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :return: The eip_address of this PublicIp.
        :rtype: str
        """
        return self._eip_address

    @eip_address.setter
    def eip_address(self, eip_address):
        r"""Sets the eip_address of this PublicIp.

        **参数解释**： 弹性公网IP的地址。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :param eip_address: The eip_address of this PublicIp.
        :type eip_address: str
        """
        self._eip_address = eip_address

    @property
    def band_width(self):
        r"""Gets the band_width of this PublicIp.

        **参数解释**： 弹性公网IP的带宽。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :return: The band_width of this PublicIp.
        :rtype: int
        """
        return self._band_width

    @band_width.setter
    def band_width(self, band_width):
        r"""Sets the band_width of this PublicIp.

        **参数解释**： 弹性公网IP的带宽。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :param band_width: The band_width of this PublicIp.
        :type band_width: int
        """
        self._band_width = band_width

    @property
    def status(self):
        r"""Gets the status of this PublicIp.

        **参数解释**： 弹性公网IP的状态。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :return: The status of this PublicIp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PublicIp.

        **参数解释**： 弹性公网IP的状态。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :param status: The status of this PublicIp.
        :type status: str
        """
        self._status = status

    @property
    def error_message(self):
        r"""Gets the error_message of this PublicIp.

        **参数解释**： 弹性公网IP的错误码。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :return: The error_message of this PublicIp.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this PublicIp.

        **参数解释**： 弹性公网IP的错误码。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： null

        :param error_message: The error_message of this PublicIp.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, PublicIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
