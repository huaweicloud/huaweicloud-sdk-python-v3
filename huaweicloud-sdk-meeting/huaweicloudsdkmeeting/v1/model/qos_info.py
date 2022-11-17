# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QosInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'send': 'QosSendReceiveInfo',
        'receive': 'QosSendReceiveInfo',
        'cpu': 'QosCpuInfo'
    }

    attribute_map = {
        'type': 'type',
        'send': 'send',
        'receive': 'receive',
        'cpu': 'cpu'
    }

    def __init__(self, type=None, send=None, receive=None, cpu=None):
        """QosInfo

        The model defined in huaweicloud sdk

        :param type: Qos类型 - aduio：音频 - video：视频 - screen：屏幕共享 - cpu：cpu
        :type type: str
        :param send: 
        :type send: :class:`huaweicloudsdkmeeting.v1.QosSendReceiveInfo`
        :param receive: 
        :type receive: :class:`huaweicloudsdkmeeting.v1.QosSendReceiveInfo`
        :param cpu: 
        :type cpu: :class:`huaweicloudsdkmeeting.v1.QosCpuInfo`
        """
        
        

        self._type = None
        self._send = None
        self._receive = None
        self._cpu = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if send is not None:
            self.send = send
        if receive is not None:
            self.receive = receive
        if cpu is not None:
            self.cpu = cpu

    @property
    def type(self):
        """Gets the type of this QosInfo.

        Qos类型 - aduio：音频 - video：视频 - screen：屏幕共享 - cpu：cpu

        :return: The type of this QosInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QosInfo.

        Qos类型 - aduio：音频 - video：视频 - screen：屏幕共享 - cpu：cpu

        :param type: The type of this QosInfo.
        :type type: str
        """
        self._type = type

    @property
    def send(self):
        """Gets the send of this QosInfo.

        :return: The send of this QosInfo.
        :rtype: :class:`huaweicloudsdkmeeting.v1.QosSendReceiveInfo`
        """
        return self._send

    @send.setter
    def send(self, send):
        """Sets the send of this QosInfo.

        :param send: The send of this QosInfo.
        :type send: :class:`huaweicloudsdkmeeting.v1.QosSendReceiveInfo`
        """
        self._send = send

    @property
    def receive(self):
        """Gets the receive of this QosInfo.

        :return: The receive of this QosInfo.
        :rtype: :class:`huaweicloudsdkmeeting.v1.QosSendReceiveInfo`
        """
        return self._receive

    @receive.setter
    def receive(self, receive):
        """Sets the receive of this QosInfo.

        :param receive: The receive of this QosInfo.
        :type receive: :class:`huaweicloudsdkmeeting.v1.QosSendReceiveInfo`
        """
        self._receive = receive

    @property
    def cpu(self):
        """Gets the cpu of this QosInfo.

        :return: The cpu of this QosInfo.
        :rtype: :class:`huaweicloudsdkmeeting.v1.QosCpuInfo`
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this QosInfo.

        :param cpu: The cpu of this QosInfo.
        :type cpu: :class:`huaweicloudsdkmeeting.v1.QosCpuInfo`
        """
        self._cpu = cpu

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
        if not isinstance(other, QosInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
