# coding: utf-8

import re
import six



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
        'id': 'str',
        'status': 'str',
        'port_id': 'str',
        'public_ip_address': 'str',
        'private_ip_address': 'str',
        'create_time': 'str',
        'bandwidth_id': 'str',
        'bandwidth_name': 'str',
        'bandwidth_share_type': 'str',
        'bandwidth_size': 'int',
        'ip_version': 'int',
        'site_id': 'str',
        'site_info': 'str',
        'operator': 'Operator',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'port_id': 'port_id',
        'public_ip_address': 'public_ip_address',
        'private_ip_address': 'private_ip_address',
        'create_time': 'create_time',
        'bandwidth_id': 'bandwidth_id',
        'bandwidth_name': 'bandwidth_name',
        'bandwidth_share_type': 'bandwidth_share_type',
        'bandwidth_size': 'bandwidth_size',
        'ip_version': 'ip_version',
        'site_id': 'site_id',
        'site_info': 'site_info',
        'operator': 'operator',
        'type': 'type'
    }

    def __init__(self, id=None, status=None, port_id=None, public_ip_address=None, private_ip_address=None, create_time=None, bandwidth_id=None, bandwidth_name=None, bandwidth_share_type=None, bandwidth_size=None, ip_version=None, site_id=None, site_info=None, operator=None, type=None):
        """PublicIp

        The model defined in huaweicloud sdk

        :param id: 弹性公网IP唯一标识。
        :type id: str
        :param status: 弹性公网IP的状态。
        :type status: str
        :param port_id: 端口的ID。
        :type port_id: str
        :param public_ip_address: 弹性公网IP的地址。
        :type public_ip_address: str
        :param private_ip_address: 绑定弹性公网IP的私有IP地址。
        :type private_ip_address: str
        :param create_time: 创建时间。
        :type create_time: str
        :param bandwidth_id: 带宽的ID。
        :type bandwidth_id: str
        :param bandwidth_name: 带宽的名称。
        :type bandwidth_name: str
        :param bandwidth_share_type: 带宽的类型。
        :type bandwidth_share_type: str
        :param bandwidth_size: 带宽的大小。
        :type bandwidth_size: int
        :param ip_version: IP版本的信息。
        :type ip_version: int
        :param site_id: 子网所属的站点ID。
        :type site_id: str
        :param site_info: 子网所属的站点信息。
        :type site_info: str
        :param operator: 
        :type operator: :class:`huaweicloudsdkiec.v1.Operator`
        :param type: 弹性公网IP的类型。
        :type type: str
        """
        
        

        self._id = None
        self._status = None
        self._port_id = None
        self._public_ip_address = None
        self._private_ip_address = None
        self._create_time = None
        self._bandwidth_id = None
        self._bandwidth_name = None
        self._bandwidth_share_type = None
        self._bandwidth_size = None
        self._ip_version = None
        self._site_id = None
        self._site_info = None
        self._operator = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if port_id is not None:
            self.port_id = port_id
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address
        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if create_time is not None:
            self.create_time = create_time
        if bandwidth_id is not None:
            self.bandwidth_id = bandwidth_id
        if bandwidth_name is not None:
            self.bandwidth_name = bandwidth_name
        if bandwidth_share_type is not None:
            self.bandwidth_share_type = bandwidth_share_type
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        if ip_version is not None:
            self.ip_version = ip_version
        if site_id is not None:
            self.site_id = site_id
        if site_info is not None:
            self.site_info = site_info
        if operator is not None:
            self.operator = operator
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this PublicIp.

        弹性公网IP唯一标识。

        :return: The id of this PublicIp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PublicIp.

        弹性公网IP唯一标识。

        :param id: The id of this PublicIp.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this PublicIp.

        弹性公网IP的状态。

        :return: The status of this PublicIp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PublicIp.

        弹性公网IP的状态。

        :param status: The status of this PublicIp.
        :type status: str
        """
        self._status = status

    @property
    def port_id(self):
        """Gets the port_id of this PublicIp.

        端口的ID。

        :return: The port_id of this PublicIp.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this PublicIp.

        端口的ID。

        :param port_id: The port_id of this PublicIp.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def public_ip_address(self):
        """Gets the public_ip_address of this PublicIp.

        弹性公网IP的地址。

        :return: The public_ip_address of this PublicIp.
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """Sets the public_ip_address of this PublicIp.

        弹性公网IP的地址。

        :param public_ip_address: The public_ip_address of this PublicIp.
        :type public_ip_address: str
        """
        self._public_ip_address = public_ip_address

    @property
    def private_ip_address(self):
        """Gets the private_ip_address of this PublicIp.

        绑定弹性公网IP的私有IP地址。

        :return: The private_ip_address of this PublicIp.
        :rtype: str
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        """Sets the private_ip_address of this PublicIp.

        绑定弹性公网IP的私有IP地址。

        :param private_ip_address: The private_ip_address of this PublicIp.
        :type private_ip_address: str
        """
        self._private_ip_address = private_ip_address

    @property
    def create_time(self):
        """Gets the create_time of this PublicIp.

        创建时间。

        :return: The create_time of this PublicIp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PublicIp.

        创建时间。

        :param create_time: The create_time of this PublicIp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def bandwidth_id(self):
        """Gets the bandwidth_id of this PublicIp.

        带宽的ID。

        :return: The bandwidth_id of this PublicIp.
        :rtype: str
        """
        return self._bandwidth_id

    @bandwidth_id.setter
    def bandwidth_id(self, bandwidth_id):
        """Sets the bandwidth_id of this PublicIp.

        带宽的ID。

        :param bandwidth_id: The bandwidth_id of this PublicIp.
        :type bandwidth_id: str
        """
        self._bandwidth_id = bandwidth_id

    @property
    def bandwidth_name(self):
        """Gets the bandwidth_name of this PublicIp.

        带宽的名称。

        :return: The bandwidth_name of this PublicIp.
        :rtype: str
        """
        return self._bandwidth_name

    @bandwidth_name.setter
    def bandwidth_name(self, bandwidth_name):
        """Sets the bandwidth_name of this PublicIp.

        带宽的名称。

        :param bandwidth_name: The bandwidth_name of this PublicIp.
        :type bandwidth_name: str
        """
        self._bandwidth_name = bandwidth_name

    @property
    def bandwidth_share_type(self):
        """Gets the bandwidth_share_type of this PublicIp.

        带宽的类型。

        :return: The bandwidth_share_type of this PublicIp.
        :rtype: str
        """
        return self._bandwidth_share_type

    @bandwidth_share_type.setter
    def bandwidth_share_type(self, bandwidth_share_type):
        """Sets the bandwidth_share_type of this PublicIp.

        带宽的类型。

        :param bandwidth_share_type: The bandwidth_share_type of this PublicIp.
        :type bandwidth_share_type: str
        """
        self._bandwidth_share_type = bandwidth_share_type

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this PublicIp.

        带宽的大小。

        :return: The bandwidth_size of this PublicIp.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this PublicIp.

        带宽的大小。

        :param bandwidth_size: The bandwidth_size of this PublicIp.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def ip_version(self):
        """Gets the ip_version of this PublicIp.

        IP版本的信息。

        :return: The ip_version of this PublicIp.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this PublicIp.

        IP版本的信息。

        :param ip_version: The ip_version of this PublicIp.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def site_id(self):
        """Gets the site_id of this PublicIp.

        子网所属的站点ID。

        :return: The site_id of this PublicIp.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this PublicIp.

        子网所属的站点ID。

        :param site_id: The site_id of this PublicIp.
        :type site_id: str
        """
        self._site_id = site_id

    @property
    def site_info(self):
        """Gets the site_info of this PublicIp.

        子网所属的站点信息。

        :return: The site_info of this PublicIp.
        :rtype: str
        """
        return self._site_info

    @site_info.setter
    def site_info(self, site_info):
        """Sets the site_info of this PublicIp.

        子网所属的站点信息。

        :param site_info: The site_info of this PublicIp.
        :type site_info: str
        """
        self._site_info = site_info

    @property
    def operator(self):
        """Gets the operator of this PublicIp.


        :return: The operator of this PublicIp.
        :rtype: :class:`huaweicloudsdkiec.v1.Operator`
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this PublicIp.


        :param operator: The operator of this PublicIp.
        :type operator: :class:`huaweicloudsdkiec.v1.Operator`
        """
        self._operator = operator

    @property
    def type(self):
        """Gets the type of this PublicIp.

        弹性公网IP的类型。

        :return: The type of this PublicIp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PublicIp.

        弹性公网IP的类型。

        :param type: The type of this PublicIp.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, PublicIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
