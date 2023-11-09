# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRequestEip:

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
        'type': 'str',
        'charge_mode': 'str',
        'bandwidth_size': 'int',
        'bandwidth_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'charge_mode': 'charge_mode',
        'bandwidth_size': 'bandwidth_size',
        'bandwidth_name': 'bandwidth_name'
    }

    def __init__(self, id=None, type=None, charge_mode=None, bandwidth_size=None, bandwidth_name=None):
        """CreateRequestEip

        The model defined in huaweicloud sdk

        :param id: 功能说明：公网IP的唯一标识
        :type id: str
        :param type: 功能说明：EIP的类型  取值范围：5_bgp（全动态BGP），5_sbgp（静态BGP）  华南-广州：5_bgp、5_sbgp  华东-上海一：5_bgp、5_sbgp  华东-上海二：5_bgp、5_sbgp  华北-北京一：5_bgp、5_sbgp  中国-香港：5_bgp  亚太-曼谷：5_bgp  亚太-新加坡：5_bgp  非洲-约翰内斯堡：5_bgp  西南-贵阳一：5_bgp、5_sbgp  华北-北京四：5_bgp、5_sbgp  拉美-圣地亚哥：5_bgp  拉美-圣保罗一：5_bgp  拉美-墨西哥城一：5_bgp  拉美-布宜诺斯艾利一：5_bgp  拉美-利马一：5_bgp  拉美-圣地亚哥二： 5_bgp 约束：必须是系统具体支持的类型。
        :type type: str
        :param charge_mode: 功能说明：按流量计费还是按带宽计费  取值范围：bandwidth，traffic
        :type charge_mode: str
        :param bandwidth_size: 带宽大小Mbit/s。flavor为Basic时，取值不能大于100；flavor为Professional1时，取值不能大于300；flavor为Professional2时，取值不能大于1024
        :type bandwidth_size: int
        :param bandwidth_name: 带宽名称
        :type bandwidth_name: str
        """
        
        

        self._id = None
        self._type = None
        self._charge_mode = None
        self._bandwidth_size = None
        self._bandwidth_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        if bandwidth_name is not None:
            self.bandwidth_name = bandwidth_name

    @property
    def id(self):
        """Gets the id of this CreateRequestEip.

        功能说明：公网IP的唯一标识

        :return: The id of this CreateRequestEip.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateRequestEip.

        功能说明：公网IP的唯一标识

        :param id: The id of this CreateRequestEip.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this CreateRequestEip.

        功能说明：EIP的类型  取值范围：5_bgp（全动态BGP），5_sbgp（静态BGP）  华南-广州：5_bgp、5_sbgp  华东-上海一：5_bgp、5_sbgp  华东-上海二：5_bgp、5_sbgp  华北-北京一：5_bgp、5_sbgp  中国-香港：5_bgp  亚太-曼谷：5_bgp  亚太-新加坡：5_bgp  非洲-约翰内斯堡：5_bgp  西南-贵阳一：5_bgp、5_sbgp  华北-北京四：5_bgp、5_sbgp  拉美-圣地亚哥：5_bgp  拉美-圣保罗一：5_bgp  拉美-墨西哥城一：5_bgp  拉美-布宜诺斯艾利一：5_bgp  拉美-利马一：5_bgp  拉美-圣地亚哥二： 5_bgp 约束：必须是系统具体支持的类型。

        :return: The type of this CreateRequestEip.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateRequestEip.

        功能说明：EIP的类型  取值范围：5_bgp（全动态BGP），5_sbgp（静态BGP）  华南-广州：5_bgp、5_sbgp  华东-上海一：5_bgp、5_sbgp  华东-上海二：5_bgp、5_sbgp  华北-北京一：5_bgp、5_sbgp  中国-香港：5_bgp  亚太-曼谷：5_bgp  亚太-新加坡：5_bgp  非洲-约翰内斯堡：5_bgp  西南-贵阳一：5_bgp、5_sbgp  华北-北京四：5_bgp、5_sbgp  拉美-圣地亚哥：5_bgp  拉美-圣保罗一：5_bgp  拉美-墨西哥城一：5_bgp  拉美-布宜诺斯艾利一：5_bgp  拉美-利马一：5_bgp  拉美-圣地亚哥二： 5_bgp 约束：必须是系统具体支持的类型。

        :param type: The type of this CreateRequestEip.
        :type type: str
        """
        self._type = type

    @property
    def charge_mode(self):
        """Gets the charge_mode of this CreateRequestEip.

        功能说明：按流量计费还是按带宽计费  取值范围：bandwidth，traffic

        :return: The charge_mode of this CreateRequestEip.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this CreateRequestEip.

        功能说明：按流量计费还是按带宽计费  取值范围：bandwidth，traffic

        :param charge_mode: The charge_mode of this CreateRequestEip.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this CreateRequestEip.

        带宽大小Mbit/s。flavor为Basic时，取值不能大于100；flavor为Professional1时，取值不能大于300；flavor为Professional2时，取值不能大于1024

        :return: The bandwidth_size of this CreateRequestEip.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this CreateRequestEip.

        带宽大小Mbit/s。flavor为Basic时，取值不能大于100；flavor为Professional1时，取值不能大于300；flavor为Professional2时，取值不能大于1024

        :param bandwidth_size: The bandwidth_size of this CreateRequestEip.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def bandwidth_name(self):
        """Gets the bandwidth_name of this CreateRequestEip.

        带宽名称

        :return: The bandwidth_name of this CreateRequestEip.
        :rtype: str
        """
        return self._bandwidth_name

    @bandwidth_name.setter
    def bandwidth_name(self, bandwidth_name):
        """Sets the bandwidth_name of this CreateRequestEip.

        带宽名称

        :param bandwidth_name: The bandwidth_name of this CreateRequestEip.
        :type bandwidth_name: str
        """
        self._bandwidth_name = bandwidth_name

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
        if not isinstance(other, CreateRequestEip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
