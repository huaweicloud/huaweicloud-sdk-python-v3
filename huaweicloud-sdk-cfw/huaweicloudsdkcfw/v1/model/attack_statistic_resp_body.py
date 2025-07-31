# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttackStatisticRespBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'apps': 'list[TopInfo]',
        'associated_name': 'str',
        'associated_type': 'str',
        'attack_count': 'int',
        'attack_type': 'str',
        'deny_count': 'int',
        'dst_ports': 'list[TopInfo]',
        'ip': 'str',
        'latest_time': 'int',
        'region_id': 'str',
        'region_name': 'str',
        'src_type': 'str',
        'vgw_id': 'str'
    }

    attribute_map = {
        'apps': 'apps',
        'associated_name': 'associated_name',
        'associated_type': 'associated_type',
        'attack_count': 'attack_count',
        'attack_type': 'attack_type',
        'deny_count': 'deny_count',
        'dst_ports': 'dst_ports',
        'ip': 'ip',
        'latest_time': 'latest_time',
        'region_id': 'region_id',
        'region_name': 'region_name',
        'src_type': 'src_type',
        'vgw_id': 'vgw_id'
    }

    def __init__(self, apps=None, associated_name=None, associated_type=None, attack_count=None, attack_type=None, deny_count=None, dst_ports=None, ip=None, latest_time=None, region_id=None, region_name=None, src_type=None, vgw_id=None):
        r"""AttackStatisticRespBody

        The model defined in huaweicloud sdk

        :param apps: **参数解释**： 应用列表 **取值范围**： 不涉及
        :type apps: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        :param associated_name: **参数解释**： 绑定资源名称 **取值范围**： 不涉及
        :type associated_name: str
        :param associated_type: **参数解释**： 绑定资源类型 **取值范围**： 不涉及
        :type associated_type: str
        :param attack_count: **参数解释**： 攻击次数 **取值范围**： 不涉及
        :type attack_count: int
        :param attack_type: **参数解释**： 攻击类型 **取值范围**： 不涉及
        :type attack_type: str
        :param deny_count: **参数解释**： 拦截次数 **取值范围**： 不涉及
        :type deny_count: int
        :param dst_ports: **参数解释**： 目的端口列表 **取值范围**： 不涉及
        :type dst_ports: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        :param ip: **参数解释**： IP地址 **取值范围**： 不涉及
        :type ip: str
        :param latest_time: **参数解释**： 最近攻击时间 **取值范围**： 不涉及
        :type latest_time: int
        :param region_id: **参数解释**： 地区ID **取值范围**： 不涉及
        :type region_id: str
        :param region_name: **参数解释**： 地区名称 **取值范围**： 不涉及
        :type region_name: str
        :param src_type: **参数解释**： 攻击来源类型 **取值范围**： 不涉及
        :type src_type: str
        :param vgw_id: **参数解释**： vgw Id **取值范围**： 不涉及
        :type vgw_id: str
        """
        
        

        self._apps = None
        self._associated_name = None
        self._associated_type = None
        self._attack_count = None
        self._attack_type = None
        self._deny_count = None
        self._dst_ports = None
        self._ip = None
        self._latest_time = None
        self._region_id = None
        self._region_name = None
        self._src_type = None
        self._vgw_id = None
        self.discriminator = None

        if apps is not None:
            self.apps = apps
        if associated_name is not None:
            self.associated_name = associated_name
        if associated_type is not None:
            self.associated_type = associated_type
        if attack_count is not None:
            self.attack_count = attack_count
        if attack_type is not None:
            self.attack_type = attack_type
        if deny_count is not None:
            self.deny_count = deny_count
        if dst_ports is not None:
            self.dst_ports = dst_ports
        if ip is not None:
            self.ip = ip
        if latest_time is not None:
            self.latest_time = latest_time
        if region_id is not None:
            self.region_id = region_id
        if region_name is not None:
            self.region_name = region_name
        if src_type is not None:
            self.src_type = src_type
        if vgw_id is not None:
            self.vgw_id = vgw_id

    @property
    def apps(self):
        r"""Gets the apps of this AttackStatisticRespBody.

        **参数解释**： 应用列表 **取值范围**： 不涉及

        :return: The apps of this AttackStatisticRespBody.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        r"""Sets the apps of this AttackStatisticRespBody.

        **参数解释**： 应用列表 **取值范围**： 不涉及

        :param apps: The apps of this AttackStatisticRespBody.
        :type apps: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        self._apps = apps

    @property
    def associated_name(self):
        r"""Gets the associated_name of this AttackStatisticRespBody.

        **参数解释**： 绑定资源名称 **取值范围**： 不涉及

        :return: The associated_name of this AttackStatisticRespBody.
        :rtype: str
        """
        return self._associated_name

    @associated_name.setter
    def associated_name(self, associated_name):
        r"""Sets the associated_name of this AttackStatisticRespBody.

        **参数解释**： 绑定资源名称 **取值范围**： 不涉及

        :param associated_name: The associated_name of this AttackStatisticRespBody.
        :type associated_name: str
        """
        self._associated_name = associated_name

    @property
    def associated_type(self):
        r"""Gets the associated_type of this AttackStatisticRespBody.

        **参数解释**： 绑定资源类型 **取值范围**： 不涉及

        :return: The associated_type of this AttackStatisticRespBody.
        :rtype: str
        """
        return self._associated_type

    @associated_type.setter
    def associated_type(self, associated_type):
        r"""Sets the associated_type of this AttackStatisticRespBody.

        **参数解释**： 绑定资源类型 **取值范围**： 不涉及

        :param associated_type: The associated_type of this AttackStatisticRespBody.
        :type associated_type: str
        """
        self._associated_type = associated_type

    @property
    def attack_count(self):
        r"""Gets the attack_count of this AttackStatisticRespBody.

        **参数解释**： 攻击次数 **取值范围**： 不涉及

        :return: The attack_count of this AttackStatisticRespBody.
        :rtype: int
        """
        return self._attack_count

    @attack_count.setter
    def attack_count(self, attack_count):
        r"""Sets the attack_count of this AttackStatisticRespBody.

        **参数解释**： 攻击次数 **取值范围**： 不涉及

        :param attack_count: The attack_count of this AttackStatisticRespBody.
        :type attack_count: int
        """
        self._attack_count = attack_count

    @property
    def attack_type(self):
        r"""Gets the attack_type of this AttackStatisticRespBody.

        **参数解释**： 攻击类型 **取值范围**： 不涉及

        :return: The attack_type of this AttackStatisticRespBody.
        :rtype: str
        """
        return self._attack_type

    @attack_type.setter
    def attack_type(self, attack_type):
        r"""Sets the attack_type of this AttackStatisticRespBody.

        **参数解释**： 攻击类型 **取值范围**： 不涉及

        :param attack_type: The attack_type of this AttackStatisticRespBody.
        :type attack_type: str
        """
        self._attack_type = attack_type

    @property
    def deny_count(self):
        r"""Gets the deny_count of this AttackStatisticRespBody.

        **参数解释**： 拦截次数 **取值范围**： 不涉及

        :return: The deny_count of this AttackStatisticRespBody.
        :rtype: int
        """
        return self._deny_count

    @deny_count.setter
    def deny_count(self, deny_count):
        r"""Sets the deny_count of this AttackStatisticRespBody.

        **参数解释**： 拦截次数 **取值范围**： 不涉及

        :param deny_count: The deny_count of this AttackStatisticRespBody.
        :type deny_count: int
        """
        self._deny_count = deny_count

    @property
    def dst_ports(self):
        r"""Gets the dst_ports of this AttackStatisticRespBody.

        **参数解释**： 目的端口列表 **取值范围**： 不涉及

        :return: The dst_ports of this AttackStatisticRespBody.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        return self._dst_ports

    @dst_ports.setter
    def dst_ports(self, dst_ports):
        r"""Sets the dst_ports of this AttackStatisticRespBody.

        **参数解释**： 目的端口列表 **取值范围**： 不涉及

        :param dst_ports: The dst_ports of this AttackStatisticRespBody.
        :type dst_ports: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        self._dst_ports = dst_ports

    @property
    def ip(self):
        r"""Gets the ip of this AttackStatisticRespBody.

        **参数解释**： IP地址 **取值范围**： 不涉及

        :return: The ip of this AttackStatisticRespBody.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this AttackStatisticRespBody.

        **参数解释**： IP地址 **取值范围**： 不涉及

        :param ip: The ip of this AttackStatisticRespBody.
        :type ip: str
        """
        self._ip = ip

    @property
    def latest_time(self):
        r"""Gets the latest_time of this AttackStatisticRespBody.

        **参数解释**： 最近攻击时间 **取值范围**： 不涉及

        :return: The latest_time of this AttackStatisticRespBody.
        :rtype: int
        """
        return self._latest_time

    @latest_time.setter
    def latest_time(self, latest_time):
        r"""Sets the latest_time of this AttackStatisticRespBody.

        **参数解释**： 最近攻击时间 **取值范围**： 不涉及

        :param latest_time: The latest_time of this AttackStatisticRespBody.
        :type latest_time: int
        """
        self._latest_time = latest_time

    @property
    def region_id(self):
        r"""Gets the region_id of this AttackStatisticRespBody.

        **参数解释**： 地区ID **取值范围**： 不涉及

        :return: The region_id of this AttackStatisticRespBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this AttackStatisticRespBody.

        **参数解释**： 地区ID **取值范围**： 不涉及

        :param region_id: The region_id of this AttackStatisticRespBody.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def region_name(self):
        r"""Gets the region_name of this AttackStatisticRespBody.

        **参数解释**： 地区名称 **取值范围**： 不涉及

        :return: The region_name of this AttackStatisticRespBody.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this AttackStatisticRespBody.

        **参数解释**： 地区名称 **取值范围**： 不涉及

        :param region_name: The region_name of this AttackStatisticRespBody.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def src_type(self):
        r"""Gets the src_type of this AttackStatisticRespBody.

        **参数解释**： 攻击来源类型 **取值范围**： 不涉及

        :return: The src_type of this AttackStatisticRespBody.
        :rtype: str
        """
        return self._src_type

    @src_type.setter
    def src_type(self, src_type):
        r"""Sets the src_type of this AttackStatisticRespBody.

        **参数解释**： 攻击来源类型 **取值范围**： 不涉及

        :param src_type: The src_type of this AttackStatisticRespBody.
        :type src_type: str
        """
        self._src_type = src_type

    @property
    def vgw_id(self):
        r"""Gets the vgw_id of this AttackStatisticRespBody.

        **参数解释**： vgw Id **取值范围**： 不涉及

        :return: The vgw_id of this AttackStatisticRespBody.
        :rtype: str
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        r"""Sets the vgw_id of this AttackStatisticRespBody.

        **参数解释**： vgw Id **取值范围**： 不涉及

        :param vgw_id: The vgw_id of this AttackStatisticRespBody.
        :type vgw_id: str
        """
        self._vgw_id = vgw_id

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
        if not isinstance(other, AttackStatisticRespBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
