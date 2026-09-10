# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachDevServerPortResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mac_addr': 'str',
        'port_id': 'str',
        'port_state': 'str',
        'virsubnet_id': 'str'
    }

    attribute_map = {
        'mac_addr': 'mac_addr',
        'port_id': 'port_id',
        'port_state': 'port_state',
        'virsubnet_id': 'virsubnet_id'
    }

    def __init__(self, mac_addr=None, port_id=None, port_state=None, virsubnet_id=None):
        r"""AttachDevServerPortResponse

        The model defined in huaweicloud sdk

        :param mac_addr: **参数解释**：端口MAC地址，由系统分配。
        :type mac_addr: str
        :param port_id: **参数解释**：网卡ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。
        :type port_id: str
        :param port_state: **参数解释**：端口状态。 **取值范围**： - ACTIVE：端口处于活动状态，可以正常进行网络通信。 - BUILD：端口正在创建或配置中。 - DOWN：端口处于非活动状态，不能进行网络通信。
        :type port_state: str
        :param virsubnet_id: **参数解释**：端口所在子网ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。
        :type virsubnet_id: str
        """
        
        super().__init__()

        self._mac_addr = None
        self._port_id = None
        self._port_state = None
        self._virsubnet_id = None
        self.discriminator = None

        if mac_addr is not None:
            self.mac_addr = mac_addr
        if port_id is not None:
            self.port_id = port_id
        if port_state is not None:
            self.port_state = port_state
        if virsubnet_id is not None:
            self.virsubnet_id = virsubnet_id

    @property
    def mac_addr(self):
        r"""Gets the mac_addr of this AttachDevServerPortResponse.

        **参数解释**：端口MAC地址，由系统分配。

        :return: The mac_addr of this AttachDevServerPortResponse.
        :rtype: str
        """
        return self._mac_addr

    @mac_addr.setter
    def mac_addr(self, mac_addr):
        r"""Sets the mac_addr of this AttachDevServerPortResponse.

        **参数解释**：端口MAC地址，由系统分配。

        :param mac_addr: The mac_addr of this AttachDevServerPortResponse.
        :type mac_addr: str
        """
        self._mac_addr = mac_addr

    @property
    def port_id(self):
        r"""Gets the port_id of this AttachDevServerPortResponse.

        **参数解释**：网卡ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :return: The port_id of this AttachDevServerPortResponse.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this AttachDevServerPortResponse.

        **参数解释**：网卡ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :param port_id: The port_id of this AttachDevServerPortResponse.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def port_state(self):
        r"""Gets the port_state of this AttachDevServerPortResponse.

        **参数解释**：端口状态。 **取值范围**： - ACTIVE：端口处于活动状态，可以正常进行网络通信。 - BUILD：端口正在创建或配置中。 - DOWN：端口处于非活动状态，不能进行网络通信。

        :return: The port_state of this AttachDevServerPortResponse.
        :rtype: str
        """
        return self._port_state

    @port_state.setter
    def port_state(self, port_state):
        r"""Sets the port_state of this AttachDevServerPortResponse.

        **参数解释**：端口状态。 **取值范围**： - ACTIVE：端口处于活动状态，可以正常进行网络通信。 - BUILD：端口正在创建或配置中。 - DOWN：端口处于非活动状态，不能进行网络通信。

        :param port_state: The port_state of this AttachDevServerPortResponse.
        :type port_state: str
        """
        self._port_state = port_state

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this AttachDevServerPortResponse.

        **参数解释**：端口所在子网ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :return: The virsubnet_id of this AttachDevServerPortResponse.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this AttachDevServerPortResponse.

        **参数解释**：端口所在子网ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :param virsubnet_id: The virsubnet_id of this AttachDevServerPortResponse.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    def to_dict(self):
        import warnings
        warnings.warn("AttachDevServerPortResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, AttachDevServerPortResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
