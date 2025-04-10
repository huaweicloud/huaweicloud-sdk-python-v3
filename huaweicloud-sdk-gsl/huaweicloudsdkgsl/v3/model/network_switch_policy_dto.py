# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkSwitchPolicyDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'preferred_carrier': 'int',
        'least_preferred_carrier': 'int',
        'optimal_signal': 'bool',
        'auto_switch': 'bool',
        'weak_signal_switch': 'bool',
        'connect_ip': 'str',
        'version': 'int',
        'switch_order': 'str',
        'blacklist': 'int'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'preferred_carrier': 'preferred_carrier',
        'least_preferred_carrier': 'least_preferred_carrier',
        'optimal_signal': 'optimal_signal',
        'auto_switch': 'auto_switch',
        'weak_signal_switch': 'weak_signal_switch',
        'connect_ip': 'connect_ip',
        'version': 'version',
        'switch_order': 'switch_order',
        'blacklist': 'blacklist'
    }

    def __init__(self, policy_name=None, preferred_carrier=None, least_preferred_carrier=None, optimal_signal=None, auto_switch=None, weak_signal_switch=None, connect_ip=None, version=None, switch_order=None, blacklist=None):
        r"""NetworkSwitchPolicyDTO

        The model defined in huaweicloud sdk

        :param policy_name: 策略名称
        :type policy_name: str
        :param preferred_carrier: 最优选运营商,1:移动、2:电信、3:联通、4:上次使用的运营商
        :type preferred_carrier: int
        :param least_preferred_carrier: 最不优选运营商,1:移动、2:电信、3:联通
        :type least_preferred_carrier: int
        :param optimal_signal: 最优信号选取策略是否开启,true:开启,false:不开启
        :type optimal_signal: bool
        :param auto_switch: 自动切卡是否开启,true:开启,false:不开启
        :type auto_switch: bool
        :param weak_signal_switch: 弱信号切换策略是否开启,true:开启,false:不开启
        :type weak_signal_switch: bool
        :param connect_ip: 连接延时切换策略，连接延时时需要ping的ip地址
        :type connect_ip: str
        :param version: 版本枚举1-SDK版 2-无SDK版
        :type version: int
        :param switch_order: 切卡顺序，运营商以英文逗号分隔
        :type switch_order: str
        :param blacklist: 黑名单，只支持单个运营商
        :type blacklist: int
        """
        
        

        self._policy_name = None
        self._preferred_carrier = None
        self._least_preferred_carrier = None
        self._optimal_signal = None
        self._auto_switch = None
        self._weak_signal_switch = None
        self._connect_ip = None
        self._version = None
        self._switch_order = None
        self._blacklist = None
        self.discriminator = None

        if policy_name is not None:
            self.policy_name = policy_name
        if preferred_carrier is not None:
            self.preferred_carrier = preferred_carrier
        if least_preferred_carrier is not None:
            self.least_preferred_carrier = least_preferred_carrier
        if optimal_signal is not None:
            self.optimal_signal = optimal_signal
        if auto_switch is not None:
            self.auto_switch = auto_switch
        if weak_signal_switch is not None:
            self.weak_signal_switch = weak_signal_switch
        if connect_ip is not None:
            self.connect_ip = connect_ip
        self.version = version
        if switch_order is not None:
            self.switch_order = switch_order
        if blacklist is not None:
            self.blacklist = blacklist

    @property
    def policy_name(self):
        r"""Gets the policy_name of this NetworkSwitchPolicyDTO.

        策略名称

        :return: The policy_name of this NetworkSwitchPolicyDTO.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this NetworkSwitchPolicyDTO.

        策略名称

        :param policy_name: The policy_name of this NetworkSwitchPolicyDTO.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def preferred_carrier(self):
        r"""Gets the preferred_carrier of this NetworkSwitchPolicyDTO.

        最优选运营商,1:移动、2:电信、3:联通、4:上次使用的运营商

        :return: The preferred_carrier of this NetworkSwitchPolicyDTO.
        :rtype: int
        """
        return self._preferred_carrier

    @preferred_carrier.setter
    def preferred_carrier(self, preferred_carrier):
        r"""Sets the preferred_carrier of this NetworkSwitchPolicyDTO.

        最优选运营商,1:移动、2:电信、3:联通、4:上次使用的运营商

        :param preferred_carrier: The preferred_carrier of this NetworkSwitchPolicyDTO.
        :type preferred_carrier: int
        """
        self._preferred_carrier = preferred_carrier

    @property
    def least_preferred_carrier(self):
        r"""Gets the least_preferred_carrier of this NetworkSwitchPolicyDTO.

        最不优选运营商,1:移动、2:电信、3:联通

        :return: The least_preferred_carrier of this NetworkSwitchPolicyDTO.
        :rtype: int
        """
        return self._least_preferred_carrier

    @least_preferred_carrier.setter
    def least_preferred_carrier(self, least_preferred_carrier):
        r"""Sets the least_preferred_carrier of this NetworkSwitchPolicyDTO.

        最不优选运营商,1:移动、2:电信、3:联通

        :param least_preferred_carrier: The least_preferred_carrier of this NetworkSwitchPolicyDTO.
        :type least_preferred_carrier: int
        """
        self._least_preferred_carrier = least_preferred_carrier

    @property
    def optimal_signal(self):
        r"""Gets the optimal_signal of this NetworkSwitchPolicyDTO.

        最优信号选取策略是否开启,true:开启,false:不开启

        :return: The optimal_signal of this NetworkSwitchPolicyDTO.
        :rtype: bool
        """
        return self._optimal_signal

    @optimal_signal.setter
    def optimal_signal(self, optimal_signal):
        r"""Sets the optimal_signal of this NetworkSwitchPolicyDTO.

        最优信号选取策略是否开启,true:开启,false:不开启

        :param optimal_signal: The optimal_signal of this NetworkSwitchPolicyDTO.
        :type optimal_signal: bool
        """
        self._optimal_signal = optimal_signal

    @property
    def auto_switch(self):
        r"""Gets the auto_switch of this NetworkSwitchPolicyDTO.

        自动切卡是否开启,true:开启,false:不开启

        :return: The auto_switch of this NetworkSwitchPolicyDTO.
        :rtype: bool
        """
        return self._auto_switch

    @auto_switch.setter
    def auto_switch(self, auto_switch):
        r"""Sets the auto_switch of this NetworkSwitchPolicyDTO.

        自动切卡是否开启,true:开启,false:不开启

        :param auto_switch: The auto_switch of this NetworkSwitchPolicyDTO.
        :type auto_switch: bool
        """
        self._auto_switch = auto_switch

    @property
    def weak_signal_switch(self):
        r"""Gets the weak_signal_switch of this NetworkSwitchPolicyDTO.

        弱信号切换策略是否开启,true:开启,false:不开启

        :return: The weak_signal_switch of this NetworkSwitchPolicyDTO.
        :rtype: bool
        """
        return self._weak_signal_switch

    @weak_signal_switch.setter
    def weak_signal_switch(self, weak_signal_switch):
        r"""Sets the weak_signal_switch of this NetworkSwitchPolicyDTO.

        弱信号切换策略是否开启,true:开启,false:不开启

        :param weak_signal_switch: The weak_signal_switch of this NetworkSwitchPolicyDTO.
        :type weak_signal_switch: bool
        """
        self._weak_signal_switch = weak_signal_switch

    @property
    def connect_ip(self):
        r"""Gets the connect_ip of this NetworkSwitchPolicyDTO.

        连接延时切换策略，连接延时时需要ping的ip地址

        :return: The connect_ip of this NetworkSwitchPolicyDTO.
        :rtype: str
        """
        return self._connect_ip

    @connect_ip.setter
    def connect_ip(self, connect_ip):
        r"""Sets the connect_ip of this NetworkSwitchPolicyDTO.

        连接延时切换策略，连接延时时需要ping的ip地址

        :param connect_ip: The connect_ip of this NetworkSwitchPolicyDTO.
        :type connect_ip: str
        """
        self._connect_ip = connect_ip

    @property
    def version(self):
        r"""Gets the version of this NetworkSwitchPolicyDTO.

        版本枚举1-SDK版 2-无SDK版

        :return: The version of this NetworkSwitchPolicyDTO.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this NetworkSwitchPolicyDTO.

        版本枚举1-SDK版 2-无SDK版

        :param version: The version of this NetworkSwitchPolicyDTO.
        :type version: int
        """
        self._version = version

    @property
    def switch_order(self):
        r"""Gets the switch_order of this NetworkSwitchPolicyDTO.

        切卡顺序，运营商以英文逗号分隔

        :return: The switch_order of this NetworkSwitchPolicyDTO.
        :rtype: str
        """
        return self._switch_order

    @switch_order.setter
    def switch_order(self, switch_order):
        r"""Sets the switch_order of this NetworkSwitchPolicyDTO.

        切卡顺序，运营商以英文逗号分隔

        :param switch_order: The switch_order of this NetworkSwitchPolicyDTO.
        :type switch_order: str
        """
        self._switch_order = switch_order

    @property
    def blacklist(self):
        r"""Gets the blacklist of this NetworkSwitchPolicyDTO.

        黑名单，只支持单个运营商

        :return: The blacklist of this NetworkSwitchPolicyDTO.
        :rtype: int
        """
        return self._blacklist

    @blacklist.setter
    def blacklist(self, blacklist):
        r"""Sets the blacklist of this NetworkSwitchPolicyDTO.

        黑名单，只支持单个运营商

        :param blacklist: The blacklist of this NetworkSwitchPolicyDTO.
        :type blacklist: int
        """
        self._blacklist = blacklist

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
        if not isinstance(other, NetworkSwitchPolicyDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
