# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaptureTaskDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'destination': 'CaptureRuleAddressDto',
        'duration': 'int',
        'max_packets': 'int',
        'name': 'str',
        'service': 'CaptureServiceDto',
        'source': 'CaptureRuleAddressDto'
    }

    attribute_map = {
        'destination': 'destination',
        'duration': 'duration',
        'max_packets': 'max_packets',
        'name': 'name',
        'service': 'service',
        'source': 'source'
    }

    def __init__(self, destination=None, duration=None, max_packets=None, name=None, service=None, source=None):
        r"""CaptureTaskDto

        The model defined in huaweicloud sdk

        :param destination: 
        :type destination: :class:`huaweicloudsdkcfw.v1.CaptureRuleAddressDto`
        :param duration: 抓包时长，以分钟为单位
        :type duration: int
        :param max_packets: 最大抓包数，以个为单位
        :type max_packets: int
        :param name: 抓包任务名称
        :type name: str
        :param service: 
        :type service: :class:`huaweicloudsdkcfw.v1.CaptureServiceDto`
        :param source: 
        :type source: :class:`huaweicloudsdkcfw.v1.CaptureRuleAddressDto`
        """
        
        

        self._destination = None
        self._duration = None
        self._max_packets = None
        self._name = None
        self._service = None
        self._source = None
        self.discriminator = None

        self.destination = destination
        self.duration = duration
        self.max_packets = max_packets
        self.name = name
        self.service = service
        self.source = source

    @property
    def destination(self):
        r"""Gets the destination of this CaptureTaskDto.

        :return: The destination of this CaptureTaskDto.
        :rtype: :class:`huaweicloudsdkcfw.v1.CaptureRuleAddressDto`
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        r"""Sets the destination of this CaptureTaskDto.

        :param destination: The destination of this CaptureTaskDto.
        :type destination: :class:`huaweicloudsdkcfw.v1.CaptureRuleAddressDto`
        """
        self._destination = destination

    @property
    def duration(self):
        r"""Gets the duration of this CaptureTaskDto.

        抓包时长，以分钟为单位

        :return: The duration of this CaptureTaskDto.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this CaptureTaskDto.

        抓包时长，以分钟为单位

        :param duration: The duration of this CaptureTaskDto.
        :type duration: int
        """
        self._duration = duration

    @property
    def max_packets(self):
        r"""Gets the max_packets of this CaptureTaskDto.

        最大抓包数，以个为单位

        :return: The max_packets of this CaptureTaskDto.
        :rtype: int
        """
        return self._max_packets

    @max_packets.setter
    def max_packets(self, max_packets):
        r"""Sets the max_packets of this CaptureTaskDto.

        最大抓包数，以个为单位

        :param max_packets: The max_packets of this CaptureTaskDto.
        :type max_packets: int
        """
        self._max_packets = max_packets

    @property
    def name(self):
        r"""Gets the name of this CaptureTaskDto.

        抓包任务名称

        :return: The name of this CaptureTaskDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CaptureTaskDto.

        抓包任务名称

        :param name: The name of this CaptureTaskDto.
        :type name: str
        """
        self._name = name

    @property
    def service(self):
        r"""Gets the service of this CaptureTaskDto.

        :return: The service of this CaptureTaskDto.
        :rtype: :class:`huaweicloudsdkcfw.v1.CaptureServiceDto`
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this CaptureTaskDto.

        :param service: The service of this CaptureTaskDto.
        :type service: :class:`huaweicloudsdkcfw.v1.CaptureServiceDto`
        """
        self._service = service

    @property
    def source(self):
        r"""Gets the source of this CaptureTaskDto.

        :return: The source of this CaptureTaskDto.
        :rtype: :class:`huaweicloudsdkcfw.v1.CaptureRuleAddressDto`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CaptureTaskDto.

        :param source: The source of this CaptureTaskDto.
        :type source: :class:`huaweicloudsdkcfw.v1.CaptureRuleAddressDto`
        """
        self._source = source

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
        if not isinstance(other, CaptureTaskDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
