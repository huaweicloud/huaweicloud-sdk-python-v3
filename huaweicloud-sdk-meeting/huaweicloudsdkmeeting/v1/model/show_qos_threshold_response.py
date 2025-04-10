# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQosThresholdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'latency': 'ThresholdData',
        'jitter': 'ThresholdData',
        'packet_loss': 'PacketThresholdData',
        'client_cpu_max': 'CPUThresholdData',
        'system_cpu_max': 'CPUThresholdData'
    }

    attribute_map = {
        'latency': 'latency',
        'jitter': 'jitter',
        'packet_loss': 'packetLoss',
        'client_cpu_max': 'clientCpuMax',
        'system_cpu_max': 'systemCpuMax'
    }

    def __init__(self, latency=None, jitter=None, packet_loss=None, client_cpu_max=None, system_cpu_max=None):
        r"""ShowQosThresholdResponse

        The model defined in huaweicloud sdk

        :param latency: 
        :type latency: :class:`huaweicloudsdkmeeting.v1.ThresholdData`
        :param jitter: 
        :type jitter: :class:`huaweicloudsdkmeeting.v1.ThresholdData`
        :param packet_loss: 
        :type packet_loss: :class:`huaweicloudsdkmeeting.v1.PacketThresholdData`
        :param client_cpu_max: 
        :type client_cpu_max: :class:`huaweicloudsdkmeeting.v1.CPUThresholdData`
        :param system_cpu_max: 
        :type system_cpu_max: :class:`huaweicloudsdkmeeting.v1.CPUThresholdData`
        """
        
        super(ShowQosThresholdResponse, self).__init__()

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
        r"""Gets the latency of this ShowQosThresholdResponse.

        :return: The latency of this ShowQosThresholdResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.ThresholdData`
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        r"""Sets the latency of this ShowQosThresholdResponse.

        :param latency: The latency of this ShowQosThresholdResponse.
        :type latency: :class:`huaweicloudsdkmeeting.v1.ThresholdData`
        """
        self._latency = latency

    @property
    def jitter(self):
        r"""Gets the jitter of this ShowQosThresholdResponse.

        :return: The jitter of this ShowQosThresholdResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.ThresholdData`
        """
        return self._jitter

    @jitter.setter
    def jitter(self, jitter):
        r"""Sets the jitter of this ShowQosThresholdResponse.

        :param jitter: The jitter of this ShowQosThresholdResponse.
        :type jitter: :class:`huaweicloudsdkmeeting.v1.ThresholdData`
        """
        self._jitter = jitter

    @property
    def packet_loss(self):
        r"""Gets the packet_loss of this ShowQosThresholdResponse.

        :return: The packet_loss of this ShowQosThresholdResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.PacketThresholdData`
        """
        return self._packet_loss

    @packet_loss.setter
    def packet_loss(self, packet_loss):
        r"""Sets the packet_loss of this ShowQosThresholdResponse.

        :param packet_loss: The packet_loss of this ShowQosThresholdResponse.
        :type packet_loss: :class:`huaweicloudsdkmeeting.v1.PacketThresholdData`
        """
        self._packet_loss = packet_loss

    @property
    def client_cpu_max(self):
        r"""Gets the client_cpu_max of this ShowQosThresholdResponse.

        :return: The client_cpu_max of this ShowQosThresholdResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.CPUThresholdData`
        """
        return self._client_cpu_max

    @client_cpu_max.setter
    def client_cpu_max(self, client_cpu_max):
        r"""Sets the client_cpu_max of this ShowQosThresholdResponse.

        :param client_cpu_max: The client_cpu_max of this ShowQosThresholdResponse.
        :type client_cpu_max: :class:`huaweicloudsdkmeeting.v1.CPUThresholdData`
        """
        self._client_cpu_max = client_cpu_max

    @property
    def system_cpu_max(self):
        r"""Gets the system_cpu_max of this ShowQosThresholdResponse.

        :return: The system_cpu_max of this ShowQosThresholdResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.CPUThresholdData`
        """
        return self._system_cpu_max

    @system_cpu_max.setter
    def system_cpu_max(self, system_cpu_max):
        r"""Sets the system_cpu_max of this ShowQosThresholdResponse.

        :param system_cpu_max: The system_cpu_max of this ShowQosThresholdResponse.
        :type system_cpu_max: :class:`huaweicloudsdkmeeting.v1.CPUThresholdData`
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
        if not isinstance(other, ShowQosThresholdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
