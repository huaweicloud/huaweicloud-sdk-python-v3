# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopoInstanceInfo:

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
        'name': 'str',
        'manage_ip': 'str',
        'traffic_ip': 'str',
        'internal_ip': 'str',
        'internal_mgnt_ip': 'str',
        'eip': 'str',
        'elb': 'str',
        'status': 'str',
        'az_code': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'manage_ip': 'manage_ip',
        'traffic_ip': 'traffic_ip',
        'internal_ip': 'internal_ip',
        'internal_mgnt_ip': 'internal_mgnt_ip',
        'eip': 'eip',
        'elb': 'elb',
        'status': 'status',
        'az_code': 'az_code'
    }

    def __init__(self, id=None, name=None, manage_ip=None, traffic_ip=None, internal_ip=None, internal_mgnt_ip=None, eip=None, elb=None, status=None, az_code=None):
        r"""TopoInstanceInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 实例ID。 **取值范围**： 不涉及。
        :type id: str
        :param name: **参数解释**： 实例名称。 **取值范围**： 不涉及。
        :type name: str
        :param manage_ip: **参数解释**： 实例管理IP。 **取值范围**： 不涉及。
        :type manage_ip: str
        :param traffic_ip: **参数解释**： 业务IP。 **取值范围**： 不涉及。
        :type traffic_ip: str
        :param internal_ip: **参数解释**： 内部通信IP。 **取值范围**： 不涉及。
        :type internal_ip: str
        :param internal_mgnt_ip: **参数解释**： 内部管理IP。 **取值范围**： 不涉及。
        :type internal_mgnt_ip: str
        :param eip: **参数解释**： 公网IP信息。 **取值范围**： 不涉及。
        :type eip: str
        :param elb: **参数解释**： elb地址。 **取值范围**： 不涉及。
        :type elb: str
        :param status: **参数解释**： 实例状态。 **取值范围**： 不涉及。
        :type status: str
        :param az_code: **参数解释**： 可用区编码。 **取值范围**： 不涉及。
        :type az_code: str
        """
        
        

        self._id = None
        self._name = None
        self._manage_ip = None
        self._traffic_ip = None
        self._internal_ip = None
        self._internal_mgnt_ip = None
        self._eip = None
        self._elb = None
        self._status = None
        self._az_code = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if manage_ip is not None:
            self.manage_ip = manage_ip
        if traffic_ip is not None:
            self.traffic_ip = traffic_ip
        if internal_ip is not None:
            self.internal_ip = internal_ip
        if internal_mgnt_ip is not None:
            self.internal_mgnt_ip = internal_mgnt_ip
        if eip is not None:
            self.eip = eip
        if elb is not None:
            self.elb = elb
        if status is not None:
            self.status = status
        if az_code is not None:
            self.az_code = az_code

    @property
    def id(self):
        r"""Gets the id of this TopoInstanceInfo.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。

        :return: The id of this TopoInstanceInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TopoInstanceInfo.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。

        :param id: The id of this TopoInstanceInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this TopoInstanceInfo.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :return: The name of this TopoInstanceInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TopoInstanceInfo.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :param name: The name of this TopoInstanceInfo.
        :type name: str
        """
        self._name = name

    @property
    def manage_ip(self):
        r"""Gets the manage_ip of this TopoInstanceInfo.

        **参数解释**： 实例管理IP。 **取值范围**： 不涉及。

        :return: The manage_ip of this TopoInstanceInfo.
        :rtype: str
        """
        return self._manage_ip

    @manage_ip.setter
    def manage_ip(self, manage_ip):
        r"""Sets the manage_ip of this TopoInstanceInfo.

        **参数解释**： 实例管理IP。 **取值范围**： 不涉及。

        :param manage_ip: The manage_ip of this TopoInstanceInfo.
        :type manage_ip: str
        """
        self._manage_ip = manage_ip

    @property
    def traffic_ip(self):
        r"""Gets the traffic_ip of this TopoInstanceInfo.

        **参数解释**： 业务IP。 **取值范围**： 不涉及。

        :return: The traffic_ip of this TopoInstanceInfo.
        :rtype: str
        """
        return self._traffic_ip

    @traffic_ip.setter
    def traffic_ip(self, traffic_ip):
        r"""Sets the traffic_ip of this TopoInstanceInfo.

        **参数解释**： 业务IP。 **取值范围**： 不涉及。

        :param traffic_ip: The traffic_ip of this TopoInstanceInfo.
        :type traffic_ip: str
        """
        self._traffic_ip = traffic_ip

    @property
    def internal_ip(self):
        r"""Gets the internal_ip of this TopoInstanceInfo.

        **参数解释**： 内部通信IP。 **取值范围**： 不涉及。

        :return: The internal_ip of this TopoInstanceInfo.
        :rtype: str
        """
        return self._internal_ip

    @internal_ip.setter
    def internal_ip(self, internal_ip):
        r"""Sets the internal_ip of this TopoInstanceInfo.

        **参数解释**： 内部通信IP。 **取值范围**： 不涉及。

        :param internal_ip: The internal_ip of this TopoInstanceInfo.
        :type internal_ip: str
        """
        self._internal_ip = internal_ip

    @property
    def internal_mgnt_ip(self):
        r"""Gets the internal_mgnt_ip of this TopoInstanceInfo.

        **参数解释**： 内部管理IP。 **取值范围**： 不涉及。

        :return: The internal_mgnt_ip of this TopoInstanceInfo.
        :rtype: str
        """
        return self._internal_mgnt_ip

    @internal_mgnt_ip.setter
    def internal_mgnt_ip(self, internal_mgnt_ip):
        r"""Sets the internal_mgnt_ip of this TopoInstanceInfo.

        **参数解释**： 内部管理IP。 **取值范围**： 不涉及。

        :param internal_mgnt_ip: The internal_mgnt_ip of this TopoInstanceInfo.
        :type internal_mgnt_ip: str
        """
        self._internal_mgnt_ip = internal_mgnt_ip

    @property
    def eip(self):
        r"""Gets the eip of this TopoInstanceInfo.

        **参数解释**： 公网IP信息。 **取值范围**： 不涉及。

        :return: The eip of this TopoInstanceInfo.
        :rtype: str
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        r"""Sets the eip of this TopoInstanceInfo.

        **参数解释**： 公网IP信息。 **取值范围**： 不涉及。

        :param eip: The eip of this TopoInstanceInfo.
        :type eip: str
        """
        self._eip = eip

    @property
    def elb(self):
        r"""Gets the elb of this TopoInstanceInfo.

        **参数解释**： elb地址。 **取值范围**： 不涉及。

        :return: The elb of this TopoInstanceInfo.
        :rtype: str
        """
        return self._elb

    @elb.setter
    def elb(self, elb):
        r"""Sets the elb of this TopoInstanceInfo.

        **参数解释**： elb地址。 **取值范围**： 不涉及。

        :param elb: The elb of this TopoInstanceInfo.
        :type elb: str
        """
        self._elb = elb

    @property
    def status(self):
        r"""Gets the status of this TopoInstanceInfo.

        **参数解释**： 实例状态。 **取值范围**： 不涉及。

        :return: The status of this TopoInstanceInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TopoInstanceInfo.

        **参数解释**： 实例状态。 **取值范围**： 不涉及。

        :param status: The status of this TopoInstanceInfo.
        :type status: str
        """
        self._status = status

    @property
    def az_code(self):
        r"""Gets the az_code of this TopoInstanceInfo.

        **参数解释**： 可用区编码。 **取值范围**： 不涉及。

        :return: The az_code of this TopoInstanceInfo.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        r"""Sets the az_code of this TopoInstanceInfo.

        **参数解释**： 可用区编码。 **取值范围**： 不涉及。

        :param az_code: The az_code of this TopoInstanceInfo.
        :type az_code: str
        """
        self._az_code = az_code

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
        if not isinstance(other, TopoInstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
