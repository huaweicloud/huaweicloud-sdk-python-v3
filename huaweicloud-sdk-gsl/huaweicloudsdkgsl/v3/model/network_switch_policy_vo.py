# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkSwitchPolicyVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'policy_name': 'str',
        'preferred_carrier': 'int',
        'least_preferred_carrier': 'int',
        'optimal_signal': 'bool',
        'auto_switch': 'bool',
        'weak_signal_switch': 'bool',
        'connect_ip': 'str',
        'create_time': 'datetime',
        'modify_time': 'datetime',
        'status': 'int',
        'type': 'int',
        'used': 'bool',
        'version': 'int',
        'switch_order': 'str',
        'blacklist': 'int'
    }

    attribute_map = {
        'id': 'id',
        'policy_name': 'policy_name',
        'preferred_carrier': 'preferred_carrier',
        'least_preferred_carrier': 'least_preferred_carrier',
        'optimal_signal': 'optimal_signal',
        'auto_switch': 'auto_switch',
        'weak_signal_switch': 'weak_signal_switch',
        'connect_ip': 'connect_ip',
        'create_time': 'create_time',
        'modify_time': 'modify_time',
        'status': 'status',
        'type': 'type',
        'used': 'used',
        'version': 'version',
        'switch_order': 'switch_order',
        'blacklist': 'blacklist'
    }

    def __init__(self, id=None, policy_name=None, preferred_carrier=None, least_preferred_carrier=None, optimal_signal=None, auto_switch=None, weak_signal_switch=None, connect_ip=None, create_time=None, modify_time=None, status=None, type=None, used=None, version=None, switch_order=None, blacklist=None):
        r"""NetworkSwitchPolicyVO

        The model defined in huaweicloud sdk

        :param id: 策略主键id
        :type id: int
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
        :param create_time: 创建时间
        :type create_time: datetime
        :param modify_time: 修改时间
        :type modify_time: datetime
        :param status: 状态,1:启用、0:禁用
        :type status: int
        :param type: 策略类型,0:系统策略,1:私有策略
        :type type: int
        :param used: 策略是否已被使用过，即是否已被执行过策略切换，false：未被使用过，true：已被使用过
        :type used: bool
        :param version: 版本枚举1-SDK版 2-无SDK版
        :type version: int
        :param switch_order: 切卡顺序，运营商以英文逗号分隔
        :type switch_order: str
        :param blacklist: 黑名单，只支持单个运营商
        :type blacklist: int
        """
        
        

        self._id = None
        self._policy_name = None
        self._preferred_carrier = None
        self._least_preferred_carrier = None
        self._optimal_signal = None
        self._auto_switch = None
        self._weak_signal_switch = None
        self._connect_ip = None
        self._create_time = None
        self._modify_time = None
        self._status = None
        self._type = None
        self._used = None
        self._version = None
        self._switch_order = None
        self._blacklist = None
        self.discriminator = None

        if id is not None:
            self.id = id
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
        if create_time is not None:
            self.create_time = create_time
        if modify_time is not None:
            self.modify_time = modify_time
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if used is not None:
            self.used = used
        if version is not None:
            self.version = version
        if switch_order is not None:
            self.switch_order = switch_order
        if blacklist is not None:
            self.blacklist = blacklist

    @property
    def id(self):
        r"""Gets the id of this NetworkSwitchPolicyVO.

        策略主键id

        :return: The id of this NetworkSwitchPolicyVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NetworkSwitchPolicyVO.

        策略主键id

        :param id: The id of this NetworkSwitchPolicyVO.
        :type id: int
        """
        self._id = id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this NetworkSwitchPolicyVO.

        策略名称

        :return: The policy_name of this NetworkSwitchPolicyVO.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this NetworkSwitchPolicyVO.

        策略名称

        :param policy_name: The policy_name of this NetworkSwitchPolicyVO.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def preferred_carrier(self):
        r"""Gets the preferred_carrier of this NetworkSwitchPolicyVO.

        最优选运营商,1:移动、2:电信、3:联通、4:上次使用的运营商

        :return: The preferred_carrier of this NetworkSwitchPolicyVO.
        :rtype: int
        """
        return self._preferred_carrier

    @preferred_carrier.setter
    def preferred_carrier(self, preferred_carrier):
        r"""Sets the preferred_carrier of this NetworkSwitchPolicyVO.

        最优选运营商,1:移动、2:电信、3:联通、4:上次使用的运营商

        :param preferred_carrier: The preferred_carrier of this NetworkSwitchPolicyVO.
        :type preferred_carrier: int
        """
        self._preferred_carrier = preferred_carrier

    @property
    def least_preferred_carrier(self):
        r"""Gets the least_preferred_carrier of this NetworkSwitchPolicyVO.

        最不优选运营商,1:移动、2:电信、3:联通

        :return: The least_preferred_carrier of this NetworkSwitchPolicyVO.
        :rtype: int
        """
        return self._least_preferred_carrier

    @least_preferred_carrier.setter
    def least_preferred_carrier(self, least_preferred_carrier):
        r"""Sets the least_preferred_carrier of this NetworkSwitchPolicyVO.

        最不优选运营商,1:移动、2:电信、3:联通

        :param least_preferred_carrier: The least_preferred_carrier of this NetworkSwitchPolicyVO.
        :type least_preferred_carrier: int
        """
        self._least_preferred_carrier = least_preferred_carrier

    @property
    def optimal_signal(self):
        r"""Gets the optimal_signal of this NetworkSwitchPolicyVO.

        最优信号选取策略是否开启,true:开启,false:不开启

        :return: The optimal_signal of this NetworkSwitchPolicyVO.
        :rtype: bool
        """
        return self._optimal_signal

    @optimal_signal.setter
    def optimal_signal(self, optimal_signal):
        r"""Sets the optimal_signal of this NetworkSwitchPolicyVO.

        最优信号选取策略是否开启,true:开启,false:不开启

        :param optimal_signal: The optimal_signal of this NetworkSwitchPolicyVO.
        :type optimal_signal: bool
        """
        self._optimal_signal = optimal_signal

    @property
    def auto_switch(self):
        r"""Gets the auto_switch of this NetworkSwitchPolicyVO.

        自动切卡是否开启,true:开启,false:不开启

        :return: The auto_switch of this NetworkSwitchPolicyVO.
        :rtype: bool
        """
        return self._auto_switch

    @auto_switch.setter
    def auto_switch(self, auto_switch):
        r"""Sets the auto_switch of this NetworkSwitchPolicyVO.

        自动切卡是否开启,true:开启,false:不开启

        :param auto_switch: The auto_switch of this NetworkSwitchPolicyVO.
        :type auto_switch: bool
        """
        self._auto_switch = auto_switch

    @property
    def weak_signal_switch(self):
        r"""Gets the weak_signal_switch of this NetworkSwitchPolicyVO.

        弱信号切换策略是否开启,true:开启,false:不开启

        :return: The weak_signal_switch of this NetworkSwitchPolicyVO.
        :rtype: bool
        """
        return self._weak_signal_switch

    @weak_signal_switch.setter
    def weak_signal_switch(self, weak_signal_switch):
        r"""Sets the weak_signal_switch of this NetworkSwitchPolicyVO.

        弱信号切换策略是否开启,true:开启,false:不开启

        :param weak_signal_switch: The weak_signal_switch of this NetworkSwitchPolicyVO.
        :type weak_signal_switch: bool
        """
        self._weak_signal_switch = weak_signal_switch

    @property
    def connect_ip(self):
        r"""Gets the connect_ip of this NetworkSwitchPolicyVO.

        连接延时切换策略，连接延时时需要ping的ip地址

        :return: The connect_ip of this NetworkSwitchPolicyVO.
        :rtype: str
        """
        return self._connect_ip

    @connect_ip.setter
    def connect_ip(self, connect_ip):
        r"""Sets the connect_ip of this NetworkSwitchPolicyVO.

        连接延时切换策略，连接延时时需要ping的ip地址

        :param connect_ip: The connect_ip of this NetworkSwitchPolicyVO.
        :type connect_ip: str
        """
        self._connect_ip = connect_ip

    @property
    def create_time(self):
        r"""Gets the create_time of this NetworkSwitchPolicyVO.

        创建时间

        :return: The create_time of this NetworkSwitchPolicyVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this NetworkSwitchPolicyVO.

        创建时间

        :param create_time: The create_time of this NetworkSwitchPolicyVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def modify_time(self):
        r"""Gets the modify_time of this NetworkSwitchPolicyVO.

        修改时间

        :return: The modify_time of this NetworkSwitchPolicyVO.
        :rtype: datetime
        """
        return self._modify_time

    @modify_time.setter
    def modify_time(self, modify_time):
        r"""Sets the modify_time of this NetworkSwitchPolicyVO.

        修改时间

        :param modify_time: The modify_time of this NetworkSwitchPolicyVO.
        :type modify_time: datetime
        """
        self._modify_time = modify_time

    @property
    def status(self):
        r"""Gets the status of this NetworkSwitchPolicyVO.

        状态,1:启用、0:禁用

        :return: The status of this NetworkSwitchPolicyVO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NetworkSwitchPolicyVO.

        状态,1:启用、0:禁用

        :param status: The status of this NetworkSwitchPolicyVO.
        :type status: int
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this NetworkSwitchPolicyVO.

        策略类型,0:系统策略,1:私有策略

        :return: The type of this NetworkSwitchPolicyVO.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this NetworkSwitchPolicyVO.

        策略类型,0:系统策略,1:私有策略

        :param type: The type of this NetworkSwitchPolicyVO.
        :type type: int
        """
        self._type = type

    @property
    def used(self):
        r"""Gets the used of this NetworkSwitchPolicyVO.

        策略是否已被使用过，即是否已被执行过策略切换，false：未被使用过，true：已被使用过

        :return: The used of this NetworkSwitchPolicyVO.
        :rtype: bool
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this NetworkSwitchPolicyVO.

        策略是否已被使用过，即是否已被执行过策略切换，false：未被使用过，true：已被使用过

        :param used: The used of this NetworkSwitchPolicyVO.
        :type used: bool
        """
        self._used = used

    @property
    def version(self):
        r"""Gets the version of this NetworkSwitchPolicyVO.

        版本枚举1-SDK版 2-无SDK版

        :return: The version of this NetworkSwitchPolicyVO.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this NetworkSwitchPolicyVO.

        版本枚举1-SDK版 2-无SDK版

        :param version: The version of this NetworkSwitchPolicyVO.
        :type version: int
        """
        self._version = version

    @property
    def switch_order(self):
        r"""Gets the switch_order of this NetworkSwitchPolicyVO.

        切卡顺序，运营商以英文逗号分隔

        :return: The switch_order of this NetworkSwitchPolicyVO.
        :rtype: str
        """
        return self._switch_order

    @switch_order.setter
    def switch_order(self, switch_order):
        r"""Sets the switch_order of this NetworkSwitchPolicyVO.

        切卡顺序，运营商以英文逗号分隔

        :param switch_order: The switch_order of this NetworkSwitchPolicyVO.
        :type switch_order: str
        """
        self._switch_order = switch_order

    @property
    def blacklist(self):
        r"""Gets the blacklist of this NetworkSwitchPolicyVO.

        黑名单，只支持单个运营商

        :return: The blacklist of this NetworkSwitchPolicyVO.
        :rtype: int
        """
        return self._blacklist

    @blacklist.setter
    def blacklist(self, blacklist):
        r"""Sets the blacklist of this NetworkSwitchPolicyVO.

        黑名单，只支持单个运营商

        :param blacklist: The blacklist of this NetworkSwitchPolicyVO.
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
        if not isinstance(other, NetworkSwitchPolicyVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
