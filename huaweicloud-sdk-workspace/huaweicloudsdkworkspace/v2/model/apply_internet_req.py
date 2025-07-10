# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyInternetReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nat_spec': 'str',
        'eip_charge_mode': 'str',
        'bandwidth_size': 'int',
        'eip_type': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'enterprise_project_id': 'str',
        'nat_id': 'str',
        'nat_name': 'str',
        'eip_name': 'str'
    }

    attribute_map = {
        'nat_spec': 'nat_spec',
        'eip_charge_mode': 'eip_charge_mode',
        'bandwidth_size': 'bandwidth_size',
        'eip_type': 'eip_type',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'enterprise_project_id': 'enterprise_project_id',
        'nat_id': 'nat_id',
        'nat_name': 'nat_name',
        'eip_name': 'eip_name'
    }

    def __init__(self, nat_spec=None, eip_charge_mode=None, bandwidth_size=None, eip_type=None, vpc_id=None, subnet_id=None, enterprise_project_id=None, nat_id=None, nat_name=None, eip_name=None):
        r"""ApplyInternetReq

        The model defined in huaweicloud sdk

        :param nat_spec: 公网NAT网关的规格，1：小型，2：中型，3：大型，4：超大型。
        :type nat_spec: str
        :param eip_charge_mode: traffic（按流量计费），bandwidth（按带宽计费）。
        :type eip_charge_mode: str
        :param bandwidth_size: 带宽大小。
        :type bandwidth_size: int
        :param eip_type: EIP的类型，5_bgp（全动态BGP），5_sbgp（静态BGP），默认值：5_bgp。
        :type eip_type: str
        :param vpc_id: vpc的id。
        :type vpc_id: str
        :param subnet_id: 子网的id。
        :type subnet_id: str
        :param enterprise_project_id: 企业项目ID，默认\&quot;0。\&quot;
        :type enterprise_project_id: str
        :param nat_id: nat的id，有传则使用该NAT，否则新建。
        :type nat_id: str
        :param nat_name: nat名称，默认值：nat-workspace。
        :type nat_name: str
        :param eip_name: eip名称，默认值：eip-workspace。
        :type eip_name: str
        """
        
        

        self._nat_spec = None
        self._eip_charge_mode = None
        self._bandwidth_size = None
        self._eip_type = None
        self._vpc_id = None
        self._subnet_id = None
        self._enterprise_project_id = None
        self._nat_id = None
        self._nat_name = None
        self._eip_name = None
        self.discriminator = None

        self.nat_spec = nat_spec
        self.eip_charge_mode = eip_charge_mode
        self.bandwidth_size = bandwidth_size
        if eip_type is not None:
            self.eip_type = eip_type
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if nat_id is not None:
            self.nat_id = nat_id
        if nat_name is not None:
            self.nat_name = nat_name
        if eip_name is not None:
            self.eip_name = eip_name

    @property
    def nat_spec(self):
        r"""Gets the nat_spec of this ApplyInternetReq.

        公网NAT网关的规格，1：小型，2：中型，3：大型，4：超大型。

        :return: The nat_spec of this ApplyInternetReq.
        :rtype: str
        """
        return self._nat_spec

    @nat_spec.setter
    def nat_spec(self, nat_spec):
        r"""Sets the nat_spec of this ApplyInternetReq.

        公网NAT网关的规格，1：小型，2：中型，3：大型，4：超大型。

        :param nat_spec: The nat_spec of this ApplyInternetReq.
        :type nat_spec: str
        """
        self._nat_spec = nat_spec

    @property
    def eip_charge_mode(self):
        r"""Gets the eip_charge_mode of this ApplyInternetReq.

        traffic（按流量计费），bandwidth（按带宽计费）。

        :return: The eip_charge_mode of this ApplyInternetReq.
        :rtype: str
        """
        return self._eip_charge_mode

    @eip_charge_mode.setter
    def eip_charge_mode(self, eip_charge_mode):
        r"""Sets the eip_charge_mode of this ApplyInternetReq.

        traffic（按流量计费），bandwidth（按带宽计费）。

        :param eip_charge_mode: The eip_charge_mode of this ApplyInternetReq.
        :type eip_charge_mode: str
        """
        self._eip_charge_mode = eip_charge_mode

    @property
    def bandwidth_size(self):
        r"""Gets the bandwidth_size of this ApplyInternetReq.

        带宽大小。

        :return: The bandwidth_size of this ApplyInternetReq.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        r"""Sets the bandwidth_size of this ApplyInternetReq.

        带宽大小。

        :param bandwidth_size: The bandwidth_size of this ApplyInternetReq.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def eip_type(self):
        r"""Gets the eip_type of this ApplyInternetReq.

        EIP的类型，5_bgp（全动态BGP），5_sbgp（静态BGP），默认值：5_bgp。

        :return: The eip_type of this ApplyInternetReq.
        :rtype: str
        """
        return self._eip_type

    @eip_type.setter
    def eip_type(self, eip_type):
        r"""Sets the eip_type of this ApplyInternetReq.

        EIP的类型，5_bgp（全动态BGP），5_sbgp（静态BGP），默认值：5_bgp。

        :param eip_type: The eip_type of this ApplyInternetReq.
        :type eip_type: str
        """
        self._eip_type = eip_type

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ApplyInternetReq.

        vpc的id。

        :return: The vpc_id of this ApplyInternetReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ApplyInternetReq.

        vpc的id。

        :param vpc_id: The vpc_id of this ApplyInternetReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ApplyInternetReq.

        子网的id。

        :return: The subnet_id of this ApplyInternetReq.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ApplyInternetReq.

        子网的id。

        :param subnet_id: The subnet_id of this ApplyInternetReq.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ApplyInternetReq.

        企业项目ID，默认\"0。\"

        :return: The enterprise_project_id of this ApplyInternetReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ApplyInternetReq.

        企业项目ID，默认\"0。\"

        :param enterprise_project_id: The enterprise_project_id of this ApplyInternetReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def nat_id(self):
        r"""Gets the nat_id of this ApplyInternetReq.

        nat的id，有传则使用该NAT，否则新建。

        :return: The nat_id of this ApplyInternetReq.
        :rtype: str
        """
        return self._nat_id

    @nat_id.setter
    def nat_id(self, nat_id):
        r"""Sets the nat_id of this ApplyInternetReq.

        nat的id，有传则使用该NAT，否则新建。

        :param nat_id: The nat_id of this ApplyInternetReq.
        :type nat_id: str
        """
        self._nat_id = nat_id

    @property
    def nat_name(self):
        r"""Gets the nat_name of this ApplyInternetReq.

        nat名称，默认值：nat-workspace。

        :return: The nat_name of this ApplyInternetReq.
        :rtype: str
        """
        return self._nat_name

    @nat_name.setter
    def nat_name(self, nat_name):
        r"""Sets the nat_name of this ApplyInternetReq.

        nat名称，默认值：nat-workspace。

        :param nat_name: The nat_name of this ApplyInternetReq.
        :type nat_name: str
        """
        self._nat_name = nat_name

    @property
    def eip_name(self):
        r"""Gets the eip_name of this ApplyInternetReq.

        eip名称，默认值：eip-workspace。

        :return: The eip_name of this ApplyInternetReq.
        :rtype: str
        """
        return self._eip_name

    @eip_name.setter
    def eip_name(self, eip_name):
        r"""Sets the eip_name of this ApplyInternetReq.

        eip名称，默认值：eip-workspace。

        :param eip_name: The eip_name of this ApplyInternetReq.
        :type eip_name: str
        """
        self._eip_name = eip_name

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
        if not isinstance(other, ApplyInternetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
