# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceEipResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'can_enable_public_access': 'bool',
        'id': 'str',
        'type': 'str',
        'port_id': 'str',
        'public_ip_address': 'str',
        'private_ip_address': 'str',
        'status': 'str',
        'tenant_id': 'str',
        'create_time': 'str',
        'bandwidth_id': 'str',
        'bandwidth_name': 'str',
        'bandwidth_size': 'str',
        'bandwidth_share_type': 'str',
        'profile': 'object'
    }

    attribute_map = {
        'can_enable_public_access': 'can_enable_public_access',
        'id': 'id',
        'type': 'type',
        'port_id': 'port_id',
        'public_ip_address': 'public_ip_address',
        'private_ip_address': 'private_ip_address',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'create_time': 'create_time',
        'bandwidth_id': 'bandwidth_id',
        'bandwidth_name': 'bandwidth_name',
        'bandwidth_size': 'bandwidth_size',
        'bandwidth_share_type': 'bandwidth_share_type',
        'profile': 'profile'
    }

    def __init__(self, can_enable_public_access=None, id=None, type=None, port_id=None, public_ip_address=None, private_ip_address=None, status=None, tenant_id=None, create_time=None, bandwidth_id=None, bandwidth_name=None, bandwidth_size=None, bandwidth_share_type=None, profile=None):
        r"""ShowInstanceEipResponse

        The model defined in huaweicloud sdk

        :param can_enable_public_access: 是否能访问公网
        :type can_enable_public_access: bool
        :param id: 弹性公网ID。
        :type id: str
        :param type: 弹性公网IP的网络类型。
        :type type: str
        :param port_id: 端口ID。
        :type port_id: str
        :param public_ip_address: 弹性公网IP地址。
        :type public_ip_address: str
        :param private_ip_address: 私网IP地址。
        :type private_ip_address: str
        :param status: 弹性公网IP地址。
        :type status: str
        :param tenant_id: 租户ID。
        :type tenant_id: str
        :param create_time: 创建时间。
        :type create_time: str
        :param bandwidth_id: 带宽ID。
        :type bandwidth_id: str
        :param bandwidth_name: 带宽名称。
        :type bandwidth_name: str
        :param bandwidth_size: 带宽大小。
        :type bandwidth_size: str
        :param bandwidth_share_type: 带宽类型。枚举值：PER 和WHOLE。
        :type bandwidth_share_type: str
        :param profile: 额外参数，包括订单id、产品id等信息。如果profile不为空，说明是包周期的弹性公网IP。
        :type profile: object
        """
        
        super(ShowInstanceEipResponse, self).__init__()

        self._can_enable_public_access = None
        self._id = None
        self._type = None
        self._port_id = None
        self._public_ip_address = None
        self._private_ip_address = None
        self._status = None
        self._tenant_id = None
        self._create_time = None
        self._bandwidth_id = None
        self._bandwidth_name = None
        self._bandwidth_size = None
        self._bandwidth_share_type = None
        self._profile = None
        self.discriminator = None

        if can_enable_public_access is not None:
            self.can_enable_public_access = can_enable_public_access
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if port_id is not None:
            self.port_id = port_id
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address
        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if status is not None:
            self.status = status
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if create_time is not None:
            self.create_time = create_time
        if bandwidth_id is not None:
            self.bandwidth_id = bandwidth_id
        if bandwidth_name is not None:
            self.bandwidth_name = bandwidth_name
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        if bandwidth_share_type is not None:
            self.bandwidth_share_type = bandwidth_share_type
        if profile is not None:
            self.profile = profile

    @property
    def can_enable_public_access(self):
        r"""Gets the can_enable_public_access of this ShowInstanceEipResponse.

        是否能访问公网

        :return: The can_enable_public_access of this ShowInstanceEipResponse.
        :rtype: bool
        """
        return self._can_enable_public_access

    @can_enable_public_access.setter
    def can_enable_public_access(self, can_enable_public_access):
        r"""Sets the can_enable_public_access of this ShowInstanceEipResponse.

        是否能访问公网

        :param can_enable_public_access: The can_enable_public_access of this ShowInstanceEipResponse.
        :type can_enable_public_access: bool
        """
        self._can_enable_public_access = can_enable_public_access

    @property
    def id(self):
        r"""Gets the id of this ShowInstanceEipResponse.

        弹性公网ID。

        :return: The id of this ShowInstanceEipResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowInstanceEipResponse.

        弹性公网ID。

        :param id: The id of this ShowInstanceEipResponse.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ShowInstanceEipResponse.

        弹性公网IP的网络类型。

        :return: The type of this ShowInstanceEipResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowInstanceEipResponse.

        弹性公网IP的网络类型。

        :param type: The type of this ShowInstanceEipResponse.
        :type type: str
        """
        self._type = type

    @property
    def port_id(self):
        r"""Gets the port_id of this ShowInstanceEipResponse.

        端口ID。

        :return: The port_id of this ShowInstanceEipResponse.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this ShowInstanceEipResponse.

        端口ID。

        :param port_id: The port_id of this ShowInstanceEipResponse.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def public_ip_address(self):
        r"""Gets the public_ip_address of this ShowInstanceEipResponse.

        弹性公网IP地址。

        :return: The public_ip_address of this ShowInstanceEipResponse.
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        r"""Sets the public_ip_address of this ShowInstanceEipResponse.

        弹性公网IP地址。

        :param public_ip_address: The public_ip_address of this ShowInstanceEipResponse.
        :type public_ip_address: str
        """
        self._public_ip_address = public_ip_address

    @property
    def private_ip_address(self):
        r"""Gets the private_ip_address of this ShowInstanceEipResponse.

        私网IP地址。

        :return: The private_ip_address of this ShowInstanceEipResponse.
        :rtype: str
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        r"""Sets the private_ip_address of this ShowInstanceEipResponse.

        私网IP地址。

        :param private_ip_address: The private_ip_address of this ShowInstanceEipResponse.
        :type private_ip_address: str
        """
        self._private_ip_address = private_ip_address

    @property
    def status(self):
        r"""Gets the status of this ShowInstanceEipResponse.

        弹性公网IP地址。

        :return: The status of this ShowInstanceEipResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowInstanceEipResponse.

        弹性公网IP地址。

        :param status: The status of this ShowInstanceEipResponse.
        :type status: str
        """
        self._status = status

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ShowInstanceEipResponse.

        租户ID。

        :return: The tenant_id of this ShowInstanceEipResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ShowInstanceEipResponse.

        租户ID。

        :param tenant_id: The tenant_id of this ShowInstanceEipResponse.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowInstanceEipResponse.

        创建时间。

        :return: The create_time of this ShowInstanceEipResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowInstanceEipResponse.

        创建时间。

        :param create_time: The create_time of this ShowInstanceEipResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def bandwidth_id(self):
        r"""Gets the bandwidth_id of this ShowInstanceEipResponse.

        带宽ID。

        :return: The bandwidth_id of this ShowInstanceEipResponse.
        :rtype: str
        """
        return self._bandwidth_id

    @bandwidth_id.setter
    def bandwidth_id(self, bandwidth_id):
        r"""Sets the bandwidth_id of this ShowInstanceEipResponse.

        带宽ID。

        :param bandwidth_id: The bandwidth_id of this ShowInstanceEipResponse.
        :type bandwidth_id: str
        """
        self._bandwidth_id = bandwidth_id

    @property
    def bandwidth_name(self):
        r"""Gets the bandwidth_name of this ShowInstanceEipResponse.

        带宽名称。

        :return: The bandwidth_name of this ShowInstanceEipResponse.
        :rtype: str
        """
        return self._bandwidth_name

    @bandwidth_name.setter
    def bandwidth_name(self, bandwidth_name):
        r"""Sets the bandwidth_name of this ShowInstanceEipResponse.

        带宽名称。

        :param bandwidth_name: The bandwidth_name of this ShowInstanceEipResponse.
        :type bandwidth_name: str
        """
        self._bandwidth_name = bandwidth_name

    @property
    def bandwidth_size(self):
        r"""Gets the bandwidth_size of this ShowInstanceEipResponse.

        带宽大小。

        :return: The bandwidth_size of this ShowInstanceEipResponse.
        :rtype: str
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        r"""Sets the bandwidth_size of this ShowInstanceEipResponse.

        带宽大小。

        :param bandwidth_size: The bandwidth_size of this ShowInstanceEipResponse.
        :type bandwidth_size: str
        """
        self._bandwidth_size = bandwidth_size

    @property
    def bandwidth_share_type(self):
        r"""Gets the bandwidth_share_type of this ShowInstanceEipResponse.

        带宽类型。枚举值：PER 和WHOLE。

        :return: The bandwidth_share_type of this ShowInstanceEipResponse.
        :rtype: str
        """
        return self._bandwidth_share_type

    @bandwidth_share_type.setter
    def bandwidth_share_type(self, bandwidth_share_type):
        r"""Sets the bandwidth_share_type of this ShowInstanceEipResponse.

        带宽类型。枚举值：PER 和WHOLE。

        :param bandwidth_share_type: The bandwidth_share_type of this ShowInstanceEipResponse.
        :type bandwidth_share_type: str
        """
        self._bandwidth_share_type = bandwidth_share_type

    @property
    def profile(self):
        r"""Gets the profile of this ShowInstanceEipResponse.

        额外参数，包括订单id、产品id等信息。如果profile不为空，说明是包周期的弹性公网IP。

        :return: The profile of this ShowInstanceEipResponse.
        :rtype: object
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        r"""Sets the profile of this ShowInstanceEipResponse.

        额外参数，包括订单id、产品id等信息。如果profile不为空，说明是包周期的弹性公网IP。

        :param profile: The profile of this ShowInstanceEipResponse.
        :type profile: object
        """
        self._profile = profile

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowInstanceEipResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
