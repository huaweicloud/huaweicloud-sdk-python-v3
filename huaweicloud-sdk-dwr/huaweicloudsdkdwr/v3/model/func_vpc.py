# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FuncVpc:

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
        'vpc_id': 'str',
        'vpc_name': 'str',
        'subnet_name': 'str',
        'cidr': 'str',
        'gateway': 'str'
    }

    attribute_map = {
        'subnet_id': 'subnet_id',
        'vpc_id': 'vpc_id',
        'vpc_name': 'vpc_name',
        'subnet_name': 'subnet_name',
        'cidr': 'cidr',
        'gateway': 'gateway'
    }

    def __init__(self, subnet_id=None, vpc_id=None, vpc_name=None, subnet_name=None, cidr=None, gateway=None):
        """FuncVpc

        The model defined in huaweicloud sdk

        :param subnet_id: 子网编号。当func_vpc非空时必选。
        :type subnet_id: str
        :param vpc_id: 虚拟私有云唯一标识。当func_vpc非空时必选。
        :type vpc_id: str
        :param vpc_name: VPC名称。
        :type vpc_name: str
        :param subnet_name: 子网名称。
        :type subnet_name: str
        :param cidr: 子网掩码。
        :type cidr: str
        :param gateway: 网关。
        :type gateway: str
        """
        
        

        self._subnet_id = None
        self._vpc_id = None
        self._vpc_name = None
        self._subnet_name = None
        self._cidr = None
        self._gateway = None
        self.discriminator = None

        if subnet_id is not None:
            self.subnet_id = subnet_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if vpc_name is not None:
            self.vpc_name = vpc_name
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if cidr is not None:
            self.cidr = cidr
        if gateway is not None:
            self.gateway = gateway

    @property
    def subnet_id(self):
        """Gets the subnet_id of this FuncVpc.

        子网编号。当func_vpc非空时必选。

        :return: The subnet_id of this FuncVpc.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this FuncVpc.

        子网编号。当func_vpc非空时必选。

        :param subnet_id: The subnet_id of this FuncVpc.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this FuncVpc.

        虚拟私有云唯一标识。当func_vpc非空时必选。

        :return: The vpc_id of this FuncVpc.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this FuncVpc.

        虚拟私有云唯一标识。当func_vpc非空时必选。

        :param vpc_id: The vpc_id of this FuncVpc.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def vpc_name(self):
        """Gets the vpc_name of this FuncVpc.

        VPC名称。

        :return: The vpc_name of this FuncVpc.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this FuncVpc.

        VPC名称。

        :param vpc_name: The vpc_name of this FuncVpc.
        :type vpc_name: str
        """
        self._vpc_name = vpc_name

    @property
    def subnet_name(self):
        """Gets the subnet_name of this FuncVpc.

        子网名称。

        :return: The subnet_name of this FuncVpc.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        """Sets the subnet_name of this FuncVpc.

        子网名称。

        :param subnet_name: The subnet_name of this FuncVpc.
        :type subnet_name: str
        """
        self._subnet_name = subnet_name

    @property
    def cidr(self):
        """Gets the cidr of this FuncVpc.

        子网掩码。

        :return: The cidr of this FuncVpc.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this FuncVpc.

        子网掩码。

        :param cidr: The cidr of this FuncVpc.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def gateway(self):
        """Gets the gateway of this FuncVpc.

        网关。

        :return: The gateway of this FuncVpc.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this FuncVpc.

        网关。

        :param gateway: The gateway of this FuncVpc.
        :type gateway: str
        """
        self._gateway = gateway

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
        if not isinstance(other, FuncVpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
