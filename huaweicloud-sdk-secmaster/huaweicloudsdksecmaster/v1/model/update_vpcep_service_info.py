# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVpcepServiceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subnet_id': 'str',
        'type': 'str',
        'vpc_endpoint_address': 'str',
        'vpc_endpoint_id': 'str',
        'vpc_endpoint_service_id': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'subnet_id': 'subnet_id',
        'type': 'type',
        'vpc_endpoint_address': 'vpc_endpoint_address',
        'vpc_endpoint_id': 'vpc_endpoint_id',
        'vpc_endpoint_service_id': 'vpc_endpoint_service_id',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, subnet_id=None, type=None, vpc_endpoint_address=None, vpc_endpoint_id=None, vpc_endpoint_service_id=None, vpc_id=None):
        r"""UpdateVpcepServiceInfo

        The model defined in huaweicloud sdk

        :param subnet_id: 子网ID
        :type subnet_id: str
        :param type: **参数解释**: Vpc服务状态 - MANAGE 管理通道 - DATA 数据通道  **约束限制** 不涉及  **取值范围**: - MANAGE - DATA  **默认值** 不涉及
        :type type: str
        :param vpc_endpoint_address: Vpc 端点地址
        :type vpc_endpoint_address: str
        :param vpc_endpoint_id: Vpc 端点ID
        :type vpc_endpoint_id: str
        :param vpc_endpoint_service_id: Vpc端点服务ID
        :type vpc_endpoint_service_id: str
        :param vpc_id: UUID
        :type vpc_id: str
        """
        
        

        self._subnet_id = None
        self._type = None
        self._vpc_endpoint_address = None
        self._vpc_endpoint_id = None
        self._vpc_endpoint_service_id = None
        self._vpc_id = None
        self.discriminator = None

        if subnet_id is not None:
            self.subnet_id = subnet_id
        if type is not None:
            self.type = type
        if vpc_endpoint_address is not None:
            self.vpc_endpoint_address = vpc_endpoint_address
        if vpc_endpoint_id is not None:
            self.vpc_endpoint_id = vpc_endpoint_id
        if vpc_endpoint_service_id is not None:
            self.vpc_endpoint_service_id = vpc_endpoint_service_id
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this UpdateVpcepServiceInfo.

        子网ID

        :return: The subnet_id of this UpdateVpcepServiceInfo.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this UpdateVpcepServiceInfo.

        子网ID

        :param subnet_id: The subnet_id of this UpdateVpcepServiceInfo.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def type(self):
        r"""Gets the type of this UpdateVpcepServiceInfo.

        **参数解释**: Vpc服务状态 - MANAGE 管理通道 - DATA 数据通道  **约束限制** 不涉及  **取值范围**: - MANAGE - DATA  **默认值** 不涉及

        :return: The type of this UpdateVpcepServiceInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateVpcepServiceInfo.

        **参数解释**: Vpc服务状态 - MANAGE 管理通道 - DATA 数据通道  **约束限制** 不涉及  **取值范围**: - MANAGE - DATA  **默认值** 不涉及

        :param type: The type of this UpdateVpcepServiceInfo.
        :type type: str
        """
        self._type = type

    @property
    def vpc_endpoint_address(self):
        r"""Gets the vpc_endpoint_address of this UpdateVpcepServiceInfo.

        Vpc 端点地址

        :return: The vpc_endpoint_address of this UpdateVpcepServiceInfo.
        :rtype: str
        """
        return self._vpc_endpoint_address

    @vpc_endpoint_address.setter
    def vpc_endpoint_address(self, vpc_endpoint_address):
        r"""Sets the vpc_endpoint_address of this UpdateVpcepServiceInfo.

        Vpc 端点地址

        :param vpc_endpoint_address: The vpc_endpoint_address of this UpdateVpcepServiceInfo.
        :type vpc_endpoint_address: str
        """
        self._vpc_endpoint_address = vpc_endpoint_address

    @property
    def vpc_endpoint_id(self):
        r"""Gets the vpc_endpoint_id of this UpdateVpcepServiceInfo.

        Vpc 端点ID

        :return: The vpc_endpoint_id of this UpdateVpcepServiceInfo.
        :rtype: str
        """
        return self._vpc_endpoint_id

    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, vpc_endpoint_id):
        r"""Sets the vpc_endpoint_id of this UpdateVpcepServiceInfo.

        Vpc 端点ID

        :param vpc_endpoint_id: The vpc_endpoint_id of this UpdateVpcepServiceInfo.
        :type vpc_endpoint_id: str
        """
        self._vpc_endpoint_id = vpc_endpoint_id

    @property
    def vpc_endpoint_service_id(self):
        r"""Gets the vpc_endpoint_service_id of this UpdateVpcepServiceInfo.

        Vpc端点服务ID

        :return: The vpc_endpoint_service_id of this UpdateVpcepServiceInfo.
        :rtype: str
        """
        return self._vpc_endpoint_service_id

    @vpc_endpoint_service_id.setter
    def vpc_endpoint_service_id(self, vpc_endpoint_service_id):
        r"""Sets the vpc_endpoint_service_id of this UpdateVpcepServiceInfo.

        Vpc端点服务ID

        :param vpc_endpoint_service_id: The vpc_endpoint_service_id of this UpdateVpcepServiceInfo.
        :type vpc_endpoint_service_id: str
        """
        self._vpc_endpoint_service_id = vpc_endpoint_service_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this UpdateVpcepServiceInfo.

        UUID

        :return: The vpc_id of this UpdateVpcepServiceInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this UpdateVpcepServiceInfo.

        UUID

        :param vpc_id: The vpc_id of this UpdateVpcepServiceInfo.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, UpdateVpcepServiceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
