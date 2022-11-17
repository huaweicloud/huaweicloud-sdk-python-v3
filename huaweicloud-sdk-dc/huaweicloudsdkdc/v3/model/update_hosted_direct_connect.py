# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHostedDirectConnect:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'bandwidth': 'int',
        'peer_location': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'bandwidth': 'bandwidth',
        'peer_location': 'peer_location'
    }

    def __init__(self, name=None, description=None, bandwidth=None, peer_location=None):
        """UpdateHostedDirectConnect

        The model defined in huaweicloud sdk

        :param name: 物理专线的名字
        :type name: str
        :param description: 物理专线的描述信息
        :type description: str
        :param bandwidth: 指定托管专线接入带宽,单位Mbps
        :type bandwidth: int
        :param peer_location: 物理专线对端所在的物理位置，省/市/街道或IDC名字
        :type peer_location: str
        """
        
        

        self._name = None
        self._description = None
        self._bandwidth = None
        self._peer_location = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if peer_location is not None:
            self.peer_location = peer_location

    @property
    def name(self):
        """Gets the name of this UpdateHostedDirectConnect.

        物理专线的名字

        :return: The name of this UpdateHostedDirectConnect.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateHostedDirectConnect.

        物理专线的名字

        :param name: The name of this UpdateHostedDirectConnect.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateHostedDirectConnect.

        物理专线的描述信息

        :return: The description of this UpdateHostedDirectConnect.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateHostedDirectConnect.

        物理专线的描述信息

        :param description: The description of this UpdateHostedDirectConnect.
        :type description: str
        """
        self._description = description

    @property
    def bandwidth(self):
        """Gets the bandwidth of this UpdateHostedDirectConnect.

        指定托管专线接入带宽,单位Mbps

        :return: The bandwidth of this UpdateHostedDirectConnect.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this UpdateHostedDirectConnect.

        指定托管专线接入带宽,单位Mbps

        :param bandwidth: The bandwidth of this UpdateHostedDirectConnect.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def peer_location(self):
        """Gets the peer_location of this UpdateHostedDirectConnect.

        物理专线对端所在的物理位置，省/市/街道或IDC名字

        :return: The peer_location of this UpdateHostedDirectConnect.
        :rtype: str
        """
        return self._peer_location

    @peer_location.setter
    def peer_location(self, peer_location):
        """Sets the peer_location of this UpdateHostedDirectConnect.

        物理专线对端所在的物理位置，省/市/街道或IDC名字

        :param peer_location: The peer_location of this UpdateHostedDirectConnect.
        :type peer_location: str
        """
        self._peer_location = peer_location

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
        if not isinstance(other, UpdateHostedDirectConnect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
