# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetQosThresholdReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'latency': 'SetThresholdData',
        'jitter': 'SetThresholdData',
        'packet_loss': 'SetPacketThresholdData',
        'client_cpu_max': 'SetCPUThresholdData',
        'system_cpu_max': 'SetCPUThresholdData'
    }

    attribute_map = {
        'latency': 'latency',
        'jitter': 'jitter',
        'packet_loss': 'packetLoss',
        'client_cpu_max': 'clientCpuMax',
        'system_cpu_max': 'systemCpuMax'
    }

    def __init__(self, latency=None, jitter=None, packet_loss=None, client_cpu_max=None, system_cpu_max=None):
        """SetQosThresholdReq

        The model defined in huaweicloud sdk

        :param latency: 
        :type latency: :class:`huaweicloudsdkmeeting.v1.SetThresholdData`
        :param jitter: 
        :type jitter: :class:`huaweicloudsdkmeeting.v1.SetThresholdData`
        :param packet_loss: 
        :type packet_loss: :class:`huaweicloudsdkmeeting.v1.SetPacketThresholdData`
        :param client_cpu_max: 
        :type client_cpu_max: :class:`huaweicloudsdkmeeting.v1.SetCPUThresholdData`
        :param system_cpu_max: 
        :type system_cpu_max: :class:`huaweicloudsdkmeeting.v1.SetCPUThresholdData`
        """
        
        

        self._latency = None
        self._jitter = None
        self._packet_loss = None
        self._client_cpu_max = None
        self._system_cpu_max = None
        self.discriminator = None

        if latency is not None:
            self.latency = latency
        if jitter is not None:
            self.jitter = jitter
        if packet_loss is not None:
            self.packet_loss = packet_loss
        if client_cpu_max is not None:
            self.client_cpu_max = client_cpu_max
        if system_cpu_max is not None:
            self.system_cpu_max = system_cpu_max

    @property
    def latency(self):
        """Gets the latency of this SetQosThresholdReq.

        :return: The latency of this SetQosThresholdReq.
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetThresholdData`
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this SetQosThresholdReq.

        :param latency: The latency of this SetQosThresholdReq.
        :type latency: :class:`huaweicloudsdkmeeting.v1.SetThresholdData`
        """
        self._latency = latency

    @property
    def jitter(self):
        """Gets the jitter of this SetQosThresholdReq.

        :return: The jitter of this SetQosThresholdReq.
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetThresholdData`
        """
        return self._jitter

    @jitter.setter
    def jitter(self, jitter):
        """Sets the jitter of this SetQosThresholdReq.

        :param jitter: The jitter of this SetQosThresholdReq.
        :type jitter: :class:`huaweicloudsdkmeeting.v1.SetThresholdData`
        """
        self._jitter = jitter

    @property
    def packet_loss(self):
        """Gets the packet_loss of this SetQosThresholdReq.

        :return: The packet_loss of this SetQosThresholdReq.
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetPacketThresholdData`
        """
        return self._packet_loss

    @packet_loss.setter
    def packet_loss(self, packet_loss):
        """Sets the packet_loss of this SetQosThresholdReq.

        :param packet_loss: The packet_loss of this SetQosThresholdReq.
        :type packet_loss: :class:`huaweicloudsdkmeeting.v1.SetPacketThresholdData`
        """
        self._packet_loss = packet_loss

    @property
    def client_cpu_max(self):
        """Gets the client_cpu_max of this SetQosThresholdReq.

        :return: The client_cpu_max of this SetQosThresholdReq.
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetCPUThresholdData`
        """
        return self._client_cpu_max

    @client_cpu_max.setter
    def client_cpu_max(self, client_cpu_max):
        """Sets the client_cpu_max of this SetQosThresholdReq.

        :param client_cpu_max: The client_cpu_max of this SetQosThresholdReq.
        :type client_cpu_max: :class:`huaweicloudsdkmeeting.v1.SetCPUThresholdData`
        """
        self._client_cpu_max = client_cpu_max

    @property
    def system_cpu_max(self):
        """Gets the system_cpu_max of this SetQosThresholdReq.

        :return: The system_cpu_max of this SetQosThresholdReq.
        :rtype: :class:`huaweicloudsdkmeeting.v1.SetCPUThresholdData`
        """
        return self._system_cpu_max

    @system_cpu_max.setter
    def system_cpu_max(self, system_cpu_max):
        """Sets the system_cpu_max of this SetQosThresholdReq.

        :param system_cpu_max: The system_cpu_max of this SetQosThresholdReq.
        :type system_cpu_max: :class:`huaweicloudsdkmeeting.v1.SetCPUThresholdData`
        """
        self._system_cpu_max = system_cpu_max

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
        if not isinstance(other, SetQosThresholdReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
