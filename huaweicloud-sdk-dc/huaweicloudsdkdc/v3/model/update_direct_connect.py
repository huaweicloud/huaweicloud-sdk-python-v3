# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDirectConnect:

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
        'peer_location': 'str',
        'status': 'str',
        'provider_status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'bandwidth': 'bandwidth',
        'peer_location': 'peer_location',
        'status': 'status',
        'provider_status': 'provider_status'
    }

    def __init__(self, name=None, description=None, bandwidth=None, peer_location=None, status=None, provider_status=None):
        """UpdateDirectConnect

        The model defined in huaweicloud sdk

        :param name: 物理专线的名字
        :type name: str
        :param description: 物理专线的描述信息
        :type description: str
        :param bandwidth: 指定托管专线接入带宽,单位Mbps
        :type bandwidth: int
        :param peer_location: 物理专线对端所在的物理位置，省/市/街道或IDC名字
        :type peer_location: str
        :param status: 更新资源状态，合法值是：PENDING_PAY
        :type status: str
        :param provider_status: 更新运营商状态，合法值是：ACTIVE,DOWN
        :type provider_status: str
        """
        
        

        self._name = None
        self._description = None
        self._bandwidth = None
        self._peer_location = None
        self._status = None
        self._provider_status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if peer_location is not None:
            self.peer_location = peer_location
        if status is not None:
            self.status = status
        if provider_status is not None:
            self.provider_status = provider_status

    @property
    def name(self):
        """Gets the name of this UpdateDirectConnect.

        物理专线的名字

        :return: The name of this UpdateDirectConnect.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateDirectConnect.

        物理专线的名字

        :param name: The name of this UpdateDirectConnect.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateDirectConnect.

        物理专线的描述信息

        :return: The description of this UpdateDirectConnect.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateDirectConnect.

        物理专线的描述信息

        :param description: The description of this UpdateDirectConnect.
        :type description: str
        """
        self._description = description

    @property
    def bandwidth(self):
        """Gets the bandwidth of this UpdateDirectConnect.

        指定托管专线接入带宽,单位Mbps

        :return: The bandwidth of this UpdateDirectConnect.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this UpdateDirectConnect.

        指定托管专线接入带宽,单位Mbps

        :param bandwidth: The bandwidth of this UpdateDirectConnect.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def peer_location(self):
        """Gets the peer_location of this UpdateDirectConnect.

        物理专线对端所在的物理位置，省/市/街道或IDC名字

        :return: The peer_location of this UpdateDirectConnect.
        :rtype: str
        """
        return self._peer_location

    @peer_location.setter
    def peer_location(self, peer_location):
        """Sets the peer_location of this UpdateDirectConnect.

        物理专线对端所在的物理位置，省/市/街道或IDC名字

        :param peer_location: The peer_location of this UpdateDirectConnect.
        :type peer_location: str
        """
        self._peer_location = peer_location

    @property
    def status(self):
        """Gets the status of this UpdateDirectConnect.

        更新资源状态，合法值是：PENDING_PAY

        :return: The status of this UpdateDirectConnect.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateDirectConnect.

        更新资源状态，合法值是：PENDING_PAY

        :param status: The status of this UpdateDirectConnect.
        :type status: str
        """
        self._status = status

    @property
    def provider_status(self):
        """Gets the provider_status of this UpdateDirectConnect.

        更新运营商状态，合法值是：ACTIVE,DOWN

        :return: The provider_status of this UpdateDirectConnect.
        :rtype: str
        """
        return self._provider_status

    @provider_status.setter
    def provider_status(self, provider_status):
        """Sets the provider_status of this UpdateDirectConnect.

        更新运营商状态，合法值是：ACTIVE,DOWN

        :param provider_status: The provider_status of this UpdateDirectConnect.
        :type provider_status: str
        """
        self._provider_status = provider_status

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
        if not isinstance(other, UpdateDirectConnect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
