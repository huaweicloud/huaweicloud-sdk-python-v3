# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponseEipInfo:

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
        'ip_version': 'int',
        'ip_billing_info': 'str',
        'type': 'str',
        'ip_address': 'str',
        'charge_mode': 'str',
        'bandwidth_id': 'str',
        'bandwidth_size': 'int',
        'bandwidth_name': 'str',
        'bandwidth_billing_info': 'str',
        'share_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ip_version': 'ip_version',
        'ip_billing_info': 'ip_billing_info',
        'type': 'type',
        'ip_address': 'ip_address',
        'charge_mode': 'charge_mode',
        'bandwidth_id': 'bandwidth_id',
        'bandwidth_size': 'bandwidth_size',
        'bandwidth_name': 'bandwidth_name',
        'bandwidth_billing_info': 'bandwidth_billing_info',
        'share_type': 'share_type'
    }

    def __init__(self, id=None, ip_version=None, ip_billing_info=None, type=None, ip_address=None, charge_mode=None, bandwidth_id=None, bandwidth_size=None, bandwidth_name=None, bandwidth_billing_info=None, share_type=None):
        r"""ResponseEipInfo

        The model defined in huaweicloud sdk

        :param id: 功能说明：公网IP的唯一标识
        :type id: str
        :param ip_version: 功能说明: 公网IP版本号  取值范围：4
        :type ip_version: int
        :param ip_billing_info: 功能说明：公网IP的订单信息 约束：包周期才会有订单信息，按需资源此字段为空
        :type ip_billing_info: str
        :param type: 功能说明：EIP的类型  取值范围：5_bgp（全动态BGP），5_sbgp（静态BGP）  华南-广州：5_bgp、5_sbgp  华东-上海一：5_bgp、5_sbgp  华东-上海二：5_bgp、5_sbgp  华北-北京一：5_bgp、5_sbgp  中国-香港：5_bgp  亚太-曼谷：5_bgp  亚太-新加坡：5_bgp  非洲-约翰内斯堡：5_bgp  西南-贵阳一：5_bgp、5_sbgp  华北-北京四：5_bgp、5_sbgp  拉美-圣地亚哥：5_bgp  拉美-圣保罗一：5_bgp  拉美-墨西哥城一：5_bgp  拉美-布宜诺斯艾利一：5_bgp  拉美-利马一：5_bgp  拉美-圣地亚哥二： 5_bgp 约束：必须是系统具体支持的类型。
        :type type: str
        :param ip_address: 功能说明: 公网IPv4地址
        :type ip_address: str
        :param charge_mode: 功能说明：按流量计费还是按带宽计费  取值范围：bandwidth，traffic
        :type charge_mode: str
        :param bandwidth_id: 功能说明：带宽ID
        :type bandwidth_id: str
        :param bandwidth_size: 带宽大小Mbit/s，flavor为Professional1时，取值不能大于300
        :type bandwidth_size: int
        :param bandwidth_name: 带宽名称
        :type bandwidth_name: str
        :param bandwidth_billing_info: 带宽订单信息
        :type bandwidth_billing_info: str
        :param share_type: 功能说明：类型  \&quot;WHOLE\&quot;为共享带宽，\&quot;PER\&quot;为独占带宽
        :type share_type: str
        """
        
        

        self._id = None
        self._ip_version = None
        self._ip_billing_info = None
        self._type = None
        self._ip_address = None
        self._charge_mode = None
        self._bandwidth_id = None
        self._bandwidth_size = None
        self._bandwidth_name = None
        self._bandwidth_billing_info = None
        self._share_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ip_version is not None:
            self.ip_version = ip_version
        if ip_billing_info is not None:
            self.ip_billing_info = ip_billing_info
        if type is not None:
            self.type = type
        if ip_address is not None:
            self.ip_address = ip_address
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if bandwidth_id is not None:
            self.bandwidth_id = bandwidth_id
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        if bandwidth_name is not None:
            self.bandwidth_name = bandwidth_name
        if bandwidth_billing_info is not None:
            self.bandwidth_billing_info = bandwidth_billing_info
        if share_type is not None:
            self.share_type = share_type

    @property
    def id(self):
        r"""Gets the id of this ResponseEipInfo.

        功能说明：公网IP的唯一标识

        :return: The id of this ResponseEipInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ResponseEipInfo.

        功能说明：公网IP的唯一标识

        :param id: The id of this ResponseEipInfo.
        :type id: str
        """
        self._id = id

    @property
    def ip_version(self):
        r"""Gets the ip_version of this ResponseEipInfo.

        功能说明: 公网IP版本号  取值范围：4

        :return: The ip_version of this ResponseEipInfo.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this ResponseEipInfo.

        功能说明: 公网IP版本号  取值范围：4

        :param ip_version: The ip_version of this ResponseEipInfo.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def ip_billing_info(self):
        r"""Gets the ip_billing_info of this ResponseEipInfo.

        功能说明：公网IP的订单信息 约束：包周期才会有订单信息，按需资源此字段为空

        :return: The ip_billing_info of this ResponseEipInfo.
        :rtype: str
        """
        return self._ip_billing_info

    @ip_billing_info.setter
    def ip_billing_info(self, ip_billing_info):
        r"""Sets the ip_billing_info of this ResponseEipInfo.

        功能说明：公网IP的订单信息 约束：包周期才会有订单信息，按需资源此字段为空

        :param ip_billing_info: The ip_billing_info of this ResponseEipInfo.
        :type ip_billing_info: str
        """
        self._ip_billing_info = ip_billing_info

    @property
    def type(self):
        r"""Gets the type of this ResponseEipInfo.

        功能说明：EIP的类型  取值范围：5_bgp（全动态BGP），5_sbgp（静态BGP）  华南-广州：5_bgp、5_sbgp  华东-上海一：5_bgp、5_sbgp  华东-上海二：5_bgp、5_sbgp  华北-北京一：5_bgp、5_sbgp  中国-香港：5_bgp  亚太-曼谷：5_bgp  亚太-新加坡：5_bgp  非洲-约翰内斯堡：5_bgp  西南-贵阳一：5_bgp、5_sbgp  华北-北京四：5_bgp、5_sbgp  拉美-圣地亚哥：5_bgp  拉美-圣保罗一：5_bgp  拉美-墨西哥城一：5_bgp  拉美-布宜诺斯艾利一：5_bgp  拉美-利马一：5_bgp  拉美-圣地亚哥二： 5_bgp 约束：必须是系统具体支持的类型。

        :return: The type of this ResponseEipInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResponseEipInfo.

        功能说明：EIP的类型  取值范围：5_bgp（全动态BGP），5_sbgp（静态BGP）  华南-广州：5_bgp、5_sbgp  华东-上海一：5_bgp、5_sbgp  华东-上海二：5_bgp、5_sbgp  华北-北京一：5_bgp、5_sbgp  中国-香港：5_bgp  亚太-曼谷：5_bgp  亚太-新加坡：5_bgp  非洲-约翰内斯堡：5_bgp  西南-贵阳一：5_bgp、5_sbgp  华北-北京四：5_bgp、5_sbgp  拉美-圣地亚哥：5_bgp  拉美-圣保罗一：5_bgp  拉美-墨西哥城一：5_bgp  拉美-布宜诺斯艾利一：5_bgp  拉美-利马一：5_bgp  拉美-圣地亚哥二： 5_bgp 约束：必须是系统具体支持的类型。

        :param type: The type of this ResponseEipInfo.
        :type type: str
        """
        self._type = type

    @property
    def ip_address(self):
        r"""Gets the ip_address of this ResponseEipInfo.

        功能说明: 公网IPv4地址

        :return: The ip_address of this ResponseEipInfo.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this ResponseEipInfo.

        功能说明: 公网IPv4地址

        :param ip_address: The ip_address of this ResponseEipInfo.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this ResponseEipInfo.

        功能说明：按流量计费还是按带宽计费  取值范围：bandwidth，traffic

        :return: The charge_mode of this ResponseEipInfo.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this ResponseEipInfo.

        功能说明：按流量计费还是按带宽计费  取值范围：bandwidth，traffic

        :param charge_mode: The charge_mode of this ResponseEipInfo.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def bandwidth_id(self):
        r"""Gets the bandwidth_id of this ResponseEipInfo.

        功能说明：带宽ID

        :return: The bandwidth_id of this ResponseEipInfo.
        :rtype: str
        """
        return self._bandwidth_id

    @bandwidth_id.setter
    def bandwidth_id(self, bandwidth_id):
        r"""Sets the bandwidth_id of this ResponseEipInfo.

        功能说明：带宽ID

        :param bandwidth_id: The bandwidth_id of this ResponseEipInfo.
        :type bandwidth_id: str
        """
        self._bandwidth_id = bandwidth_id

    @property
    def bandwidth_size(self):
        r"""Gets the bandwidth_size of this ResponseEipInfo.

        带宽大小Mbit/s，flavor为Professional1时，取值不能大于300

        :return: The bandwidth_size of this ResponseEipInfo.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        r"""Sets the bandwidth_size of this ResponseEipInfo.

        带宽大小Mbit/s，flavor为Professional1时，取值不能大于300

        :param bandwidth_size: The bandwidth_size of this ResponseEipInfo.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def bandwidth_name(self):
        r"""Gets the bandwidth_name of this ResponseEipInfo.

        带宽名称

        :return: The bandwidth_name of this ResponseEipInfo.
        :rtype: str
        """
        return self._bandwidth_name

    @bandwidth_name.setter
    def bandwidth_name(self, bandwidth_name):
        r"""Sets the bandwidth_name of this ResponseEipInfo.

        带宽名称

        :param bandwidth_name: The bandwidth_name of this ResponseEipInfo.
        :type bandwidth_name: str
        """
        self._bandwidth_name = bandwidth_name

    @property
    def bandwidth_billing_info(self):
        r"""Gets the bandwidth_billing_info of this ResponseEipInfo.

        带宽订单信息

        :return: The bandwidth_billing_info of this ResponseEipInfo.
        :rtype: str
        """
        return self._bandwidth_billing_info

    @bandwidth_billing_info.setter
    def bandwidth_billing_info(self, bandwidth_billing_info):
        r"""Sets the bandwidth_billing_info of this ResponseEipInfo.

        带宽订单信息

        :param bandwidth_billing_info: The bandwidth_billing_info of this ResponseEipInfo.
        :type bandwidth_billing_info: str
        """
        self._bandwidth_billing_info = bandwidth_billing_info

    @property
    def share_type(self):
        r"""Gets the share_type of this ResponseEipInfo.

        功能说明：类型  \"WHOLE\"为共享带宽，\"PER\"为独占带宽

        :return: The share_type of this ResponseEipInfo.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        r"""Sets the share_type of this ResponseEipInfo.

        功能说明：类型  \"WHOLE\"为共享带宽，\"PER\"为独占带宽

        :param share_type: The share_type of this ResponseEipInfo.
        :type share_type: str
        """
        self._share_type = share_type

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
        if not isinstance(other, ResponseEipInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
