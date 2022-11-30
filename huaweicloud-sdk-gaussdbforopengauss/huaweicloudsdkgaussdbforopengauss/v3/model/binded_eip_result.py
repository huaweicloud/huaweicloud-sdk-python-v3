# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindedEipResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'public_ip_id': 'str',
        'public_ip_type': 'str',
        'port_id': 'str',
        'public_ip_address': 'str',
        'private_ip_address': 'str',
        'bandwidth_id': 'str',
        'bandwidth_name': 'str',
        'bandwidth_share_type': 'str',
        'bandwidth_size': 'int',
        'applied_at': 'str'
    }

    attribute_map = {
        'public_ip_id': 'public_ip_id',
        'public_ip_type': 'public_ip_type',
        'port_id': 'port_id',
        'public_ip_address': 'public_ip_address',
        'private_ip_address': 'private_ip_address',
        'bandwidth_id': 'bandwidth_id',
        'bandwidth_name': 'bandwidth_name',
        'bandwidth_share_type': 'bandwidth_share_type',
        'bandwidth_size': 'bandwidth_size',
        'applied_at': 'applied_at'
    }

    def __init__(self, public_ip_id=None, public_ip_type=None, port_id=None, public_ip_address=None, private_ip_address=None, bandwidth_id=None, bandwidth_name=None, bandwidth_share_type=None, bandwidth_size=None, applied_at=None):
        """BindedEipResult

        The model defined in huaweicloud sdk

        :param public_ip_id: 弹性公网ID。
        :type public_ip_id: str
        :param public_ip_type: 弹性公网类型。
        :type public_ip_type: str
        :param port_id: 端口ID。
        :type port_id: str
        :param public_ip_address: 弹性公网IP。
        :type public_ip_address: str
        :param private_ip_address: 内网地址。
        :type private_ip_address: str
        :param bandwidth_id: 带宽ID。
        :type bandwidth_id: str
        :param bandwidth_name: 带宽名称。
        :type bandwidth_name: str
        :param bandwidth_share_type: 带宽共享类型。
        :type bandwidth_share_type: str
        :param bandwidth_size: 带宽大小。
        :type bandwidth_size: int
        :param applied_at: 修改时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+08:00。
        :type applied_at: str
        """
        
        

        self._public_ip_id = None
        self._public_ip_type = None
        self._port_id = None
        self._public_ip_address = None
        self._private_ip_address = None
        self._bandwidth_id = None
        self._bandwidth_name = None
        self._bandwidth_share_type = None
        self._bandwidth_size = None
        self._applied_at = None
        self.discriminator = None

        self.public_ip_id = public_ip_id
        self.public_ip_type = public_ip_type
        self.port_id = port_id
        self.public_ip_address = public_ip_address
        self.private_ip_address = private_ip_address
        self.bandwidth_id = bandwidth_id
        self.bandwidth_name = bandwidth_name
        self.bandwidth_share_type = bandwidth_share_type
        self.bandwidth_size = bandwidth_size
        self.applied_at = applied_at

    @property
    def public_ip_id(self):
        """Gets the public_ip_id of this BindedEipResult.

        弹性公网ID。

        :return: The public_ip_id of this BindedEipResult.
        :rtype: str
        """
        return self._public_ip_id

    @public_ip_id.setter
    def public_ip_id(self, public_ip_id):
        """Sets the public_ip_id of this BindedEipResult.

        弹性公网ID。

        :param public_ip_id: The public_ip_id of this BindedEipResult.
        :type public_ip_id: str
        """
        self._public_ip_id = public_ip_id

    @property
    def public_ip_type(self):
        """Gets the public_ip_type of this BindedEipResult.

        弹性公网类型。

        :return: The public_ip_type of this BindedEipResult.
        :rtype: str
        """
        return self._public_ip_type

    @public_ip_type.setter
    def public_ip_type(self, public_ip_type):
        """Sets the public_ip_type of this BindedEipResult.

        弹性公网类型。

        :param public_ip_type: The public_ip_type of this BindedEipResult.
        :type public_ip_type: str
        """
        self._public_ip_type = public_ip_type

    @property
    def port_id(self):
        """Gets the port_id of this BindedEipResult.

        端口ID。

        :return: The port_id of this BindedEipResult.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this BindedEipResult.

        端口ID。

        :param port_id: The port_id of this BindedEipResult.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def public_ip_address(self):
        """Gets the public_ip_address of this BindedEipResult.

        弹性公网IP。

        :return: The public_ip_address of this BindedEipResult.
        :rtype: str
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """Sets the public_ip_address of this BindedEipResult.

        弹性公网IP。

        :param public_ip_address: The public_ip_address of this BindedEipResult.
        :type public_ip_address: str
        """
        self._public_ip_address = public_ip_address

    @property
    def private_ip_address(self):
        """Gets the private_ip_address of this BindedEipResult.

        内网地址。

        :return: The private_ip_address of this BindedEipResult.
        :rtype: str
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        """Sets the private_ip_address of this BindedEipResult.

        内网地址。

        :param private_ip_address: The private_ip_address of this BindedEipResult.
        :type private_ip_address: str
        """
        self._private_ip_address = private_ip_address

    @property
    def bandwidth_id(self):
        """Gets the bandwidth_id of this BindedEipResult.

        带宽ID。

        :return: The bandwidth_id of this BindedEipResult.
        :rtype: str
        """
        return self._bandwidth_id

    @bandwidth_id.setter
    def bandwidth_id(self, bandwidth_id):
        """Sets the bandwidth_id of this BindedEipResult.

        带宽ID。

        :param bandwidth_id: The bandwidth_id of this BindedEipResult.
        :type bandwidth_id: str
        """
        self._bandwidth_id = bandwidth_id

    @property
    def bandwidth_name(self):
        """Gets the bandwidth_name of this BindedEipResult.

        带宽名称。

        :return: The bandwidth_name of this BindedEipResult.
        :rtype: str
        """
        return self._bandwidth_name

    @bandwidth_name.setter
    def bandwidth_name(self, bandwidth_name):
        """Sets the bandwidth_name of this BindedEipResult.

        带宽名称。

        :param bandwidth_name: The bandwidth_name of this BindedEipResult.
        :type bandwidth_name: str
        """
        self._bandwidth_name = bandwidth_name

    @property
    def bandwidth_share_type(self):
        """Gets the bandwidth_share_type of this BindedEipResult.

        带宽共享类型。

        :return: The bandwidth_share_type of this BindedEipResult.
        :rtype: str
        """
        return self._bandwidth_share_type

    @bandwidth_share_type.setter
    def bandwidth_share_type(self, bandwidth_share_type):
        """Sets the bandwidth_share_type of this BindedEipResult.

        带宽共享类型。

        :param bandwidth_share_type: The bandwidth_share_type of this BindedEipResult.
        :type bandwidth_share_type: str
        """
        self._bandwidth_share_type = bandwidth_share_type

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this BindedEipResult.

        带宽大小。

        :return: The bandwidth_size of this BindedEipResult.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this BindedEipResult.

        带宽大小。

        :param bandwidth_size: The bandwidth_size of this BindedEipResult.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def applied_at(self):
        """Gets the applied_at of this BindedEipResult.

        修改时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+08:00。

        :return: The applied_at of this BindedEipResult.
        :rtype: str
        """
        return self._applied_at

    @applied_at.setter
    def applied_at(self, applied_at):
        """Sets the applied_at of this BindedEipResult.

        修改时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+08:00。

        :param applied_at: The applied_at of this BindedEipResult.
        :type applied_at: str
        """
        self._applied_at = applied_at

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
        if not isinstance(other, BindedEipResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
