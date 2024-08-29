# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimDeviceMultiplyVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sim_card_id': 'int',
        'cid': 'str',
        'online_carrier': 'int',
        'network_switch_policy_id': 'int',
        'policy_name': 'str',
        'version': 'int'
    }

    attribute_map = {
        'sim_card_id': 'sim_card_id',
        'cid': 'cid',
        'online_carrier': 'online_carrier',
        'network_switch_policy_id': 'network_switch_policy_id',
        'policy_name': 'policy_name',
        'version': 'version'
    }

    def __init__(self, sim_card_id=None, cid=None, online_carrier=None, network_switch_policy_id=None, policy_name=None, version=None):
        """SimDeviceMultiplyVO

        The model defined in huaweicloud sdk

        :param sim_card_id: sim卡id
        :type sim_card_id: int
        :param cid: 三网卡标识
        :type cid: str
        :param online_carrier: 在线运营商标识
        :type online_carrier: int
        :param network_switch_policy_id: 网络切换策略id
        :type network_switch_policy_id: int
        :param policy_name: 网络切换策略名称
        :type policy_name: str
        :param version: 版本信息
        :type version: int
        """
        
        

        self._sim_card_id = None
        self._cid = None
        self._online_carrier = None
        self._network_switch_policy_id = None
        self._policy_name = None
        self._version = None
        self.discriminator = None

        if sim_card_id is not None:
            self.sim_card_id = sim_card_id
        if cid is not None:
            self.cid = cid
        if online_carrier is not None:
            self.online_carrier = online_carrier
        if network_switch_policy_id is not None:
            self.network_switch_policy_id = network_switch_policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if version is not None:
            self.version = version

    @property
    def sim_card_id(self):
        """Gets the sim_card_id of this SimDeviceMultiplyVO.

        sim卡id

        :return: The sim_card_id of this SimDeviceMultiplyVO.
        :rtype: int
        """
        return self._sim_card_id

    @sim_card_id.setter
    def sim_card_id(self, sim_card_id):
        """Sets the sim_card_id of this SimDeviceMultiplyVO.

        sim卡id

        :param sim_card_id: The sim_card_id of this SimDeviceMultiplyVO.
        :type sim_card_id: int
        """
        self._sim_card_id = sim_card_id

    @property
    def cid(self):
        """Gets the cid of this SimDeviceMultiplyVO.

        三网卡标识

        :return: The cid of this SimDeviceMultiplyVO.
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        """Sets the cid of this SimDeviceMultiplyVO.

        三网卡标识

        :param cid: The cid of this SimDeviceMultiplyVO.
        :type cid: str
        """
        self._cid = cid

    @property
    def online_carrier(self):
        """Gets the online_carrier of this SimDeviceMultiplyVO.

        在线运营商标识

        :return: The online_carrier of this SimDeviceMultiplyVO.
        :rtype: int
        """
        return self._online_carrier

    @online_carrier.setter
    def online_carrier(self, online_carrier):
        """Sets the online_carrier of this SimDeviceMultiplyVO.

        在线运营商标识

        :param online_carrier: The online_carrier of this SimDeviceMultiplyVO.
        :type online_carrier: int
        """
        self._online_carrier = online_carrier

    @property
    def network_switch_policy_id(self):
        """Gets the network_switch_policy_id of this SimDeviceMultiplyVO.

        网络切换策略id

        :return: The network_switch_policy_id of this SimDeviceMultiplyVO.
        :rtype: int
        """
        return self._network_switch_policy_id

    @network_switch_policy_id.setter
    def network_switch_policy_id(self, network_switch_policy_id):
        """Sets the network_switch_policy_id of this SimDeviceMultiplyVO.

        网络切换策略id

        :param network_switch_policy_id: The network_switch_policy_id of this SimDeviceMultiplyVO.
        :type network_switch_policy_id: int
        """
        self._network_switch_policy_id = network_switch_policy_id

    @property
    def policy_name(self):
        """Gets the policy_name of this SimDeviceMultiplyVO.

        网络切换策略名称

        :return: The policy_name of this SimDeviceMultiplyVO.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this SimDeviceMultiplyVO.

        网络切换策略名称

        :param policy_name: The policy_name of this SimDeviceMultiplyVO.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def version(self):
        """Gets the version of this SimDeviceMultiplyVO.

        版本信息

        :return: The version of this SimDeviceMultiplyVO.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SimDeviceMultiplyVO.

        版本信息

        :param version: The version of this SimDeviceMultiplyVO.
        :type version: int
        """
        self._version = version

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
        if not isinstance(other, SimDeviceMultiplyVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
