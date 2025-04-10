# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProtectedIpInPolicyBody:

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
        'ip': 'str',
        'type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ip': 'ip',
        'type': 'type',
        'name': 'name'
    }

    def __init__(self, id=None, ip=None, type=None, name=None):
        r"""UpdateProtectedIpInPolicyBody

        The model defined in huaweicloud sdk

        :param id: 防护ip的id
        :type id: str
        :param ip: 防护ip
        :type ip: str
        :param type: 类型。VPN：VPN；NAT：NAT；VIP：VIP；CCI：CCI；EIP：弹性公网IP；ELB：弹性负载均衡；REROUTING_IP：REROUTING_IP；SubEni：SubEni；NetInterFace：NetInterFace；
        :type type: str
        :param name: 名字
        :type name: str
        """
        
        

        self._id = None
        self._ip = None
        self._type = None
        self._name = None
        self.discriminator = None

        self.id = id
        self.ip = ip
        self.type = type
        if name is not None:
            self.name = name

    @property
    def id(self):
        r"""Gets the id of this UpdateProtectedIpInPolicyBody.

        防护ip的id

        :return: The id of this UpdateProtectedIpInPolicyBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateProtectedIpInPolicyBody.

        防护ip的id

        :param id: The id of this UpdateProtectedIpInPolicyBody.
        :type id: str
        """
        self._id = id

    @property
    def ip(self):
        r"""Gets the ip of this UpdateProtectedIpInPolicyBody.

        防护ip

        :return: The ip of this UpdateProtectedIpInPolicyBody.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this UpdateProtectedIpInPolicyBody.

        防护ip

        :param ip: The ip of this UpdateProtectedIpInPolicyBody.
        :type ip: str
        """
        self._ip = ip

    @property
    def type(self):
        r"""Gets the type of this UpdateProtectedIpInPolicyBody.

        类型。VPN：VPN；NAT：NAT；VIP：VIP；CCI：CCI；EIP：弹性公网IP；ELB：弹性负载均衡；REROUTING_IP：REROUTING_IP；SubEni：SubEni；NetInterFace：NetInterFace；

        :return: The type of this UpdateProtectedIpInPolicyBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateProtectedIpInPolicyBody.

        类型。VPN：VPN；NAT：NAT；VIP：VIP；CCI：CCI；EIP：弹性公网IP；ELB：弹性负载均衡；REROUTING_IP：REROUTING_IP；SubEni：SubEni；NetInterFace：NetInterFace；

        :param type: The type of this UpdateProtectedIpInPolicyBody.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this UpdateProtectedIpInPolicyBody.

        名字

        :return: The name of this UpdateProtectedIpInPolicyBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateProtectedIpInPolicyBody.

        名字

        :param name: The name of this UpdateProtectedIpInPolicyBody.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, UpdateProtectedIpInPolicyBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
