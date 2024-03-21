# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InputStreamInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input_protocol': 'str',
        'sources': 'list[SourcesInfo]',
        'secondary_sources': 'list[SecondarySourcesInfo]',
        'failover_conditions': 'FailoverConditions',
        'max_bandwidth_limit': 'int',
        'ip_port_mode': 'bool'
    }

    attribute_map = {
        'input_protocol': 'input_protocol',
        'sources': 'sources',
        'secondary_sources': 'secondary_sources',
        'failover_conditions': 'failover_conditions',
        'max_bandwidth_limit': 'max_bandwidth_limit',
        'ip_port_mode': 'ip_port_mode'
    }

    def __init__(self, input_protocol=None, sources=None, secondary_sources=None, failover_conditions=None, max_bandwidth_limit=None, ip_port_mode=None):
        """InputStreamInfo

        The model defined in huaweicloud sdk

        :param input_protocol: 频道入流协议 - FLV_PULL - RTMP_PUSH - RTMP_PULL - HLS_PULL - SRT_PULL - SRT_PUSH
        :type input_protocol: str
        :param sources: 频道主源流信息。入流协议为RTMP_PUSH和SRT_PUSH时，非必填项。其他情况下，均为必填项。
        :type sources: list[:class:`huaweicloudsdklive.v1.SourcesInfo`]
        :param secondary_sources: 备入流数组，非必填项。如果有备入流，则主备入流必须保证路数、codec和分辨率均一致。入流协议为RTMP_PUSH时，无需填写。
        :type secondary_sources: list[:class:`huaweicloudsdklive.v1.SecondarySourcesInfo`]
        :param failover_conditions: 
        :type failover_conditions: :class:`huaweicloudsdklive.v1.FailoverConditions`
        :param max_bandwidth_limit: 当入流协议为HLS_PULL时，最大带宽限制。 未配置会默认选择BANDWIDTH最高的流
        :type max_bandwidth_limit: int
        :param ip_port_mode: 当推流协议为SRT_PUSH时，如果配置了直推源站，编码器不支持输入streamid，需要打开设置为true
        :type ip_port_mode: bool
        """
        
        

        self._input_protocol = None
        self._sources = None
        self._secondary_sources = None
        self._failover_conditions = None
        self._max_bandwidth_limit = None
        self._ip_port_mode = None
        self.discriminator = None

        self.input_protocol = input_protocol
        if sources is not None:
            self.sources = sources
        if secondary_sources is not None:
            self.secondary_sources = secondary_sources
        if failover_conditions is not None:
            self.failover_conditions = failover_conditions
        if max_bandwidth_limit is not None:
            self.max_bandwidth_limit = max_bandwidth_limit
        if ip_port_mode is not None:
            self.ip_port_mode = ip_port_mode

    @property
    def input_protocol(self):
        """Gets the input_protocol of this InputStreamInfo.

        频道入流协议 - FLV_PULL - RTMP_PUSH - RTMP_PULL - HLS_PULL - SRT_PULL - SRT_PUSH

        :return: The input_protocol of this InputStreamInfo.
        :rtype: str
        """
        return self._input_protocol

    @input_protocol.setter
    def input_protocol(self, input_protocol):
        """Sets the input_protocol of this InputStreamInfo.

        频道入流协议 - FLV_PULL - RTMP_PUSH - RTMP_PULL - HLS_PULL - SRT_PULL - SRT_PUSH

        :param input_protocol: The input_protocol of this InputStreamInfo.
        :type input_protocol: str
        """
        self._input_protocol = input_protocol

    @property
    def sources(self):
        """Gets the sources of this InputStreamInfo.

        频道主源流信息。入流协议为RTMP_PUSH和SRT_PUSH时，非必填项。其他情况下，均为必填项。

        :return: The sources of this InputStreamInfo.
        :rtype: list[:class:`huaweicloudsdklive.v1.SourcesInfo`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this InputStreamInfo.

        频道主源流信息。入流协议为RTMP_PUSH和SRT_PUSH时，非必填项。其他情况下，均为必填项。

        :param sources: The sources of this InputStreamInfo.
        :type sources: list[:class:`huaweicloudsdklive.v1.SourcesInfo`]
        """
        self._sources = sources

    @property
    def secondary_sources(self):
        """Gets the secondary_sources of this InputStreamInfo.

        备入流数组，非必填项。如果有备入流，则主备入流必须保证路数、codec和分辨率均一致。入流协议为RTMP_PUSH时，无需填写。

        :return: The secondary_sources of this InputStreamInfo.
        :rtype: list[:class:`huaweicloudsdklive.v1.SecondarySourcesInfo`]
        """
        return self._secondary_sources

    @secondary_sources.setter
    def secondary_sources(self, secondary_sources):
        """Sets the secondary_sources of this InputStreamInfo.

        备入流数组，非必填项。如果有备入流，则主备入流必须保证路数、codec和分辨率均一致。入流协议为RTMP_PUSH时，无需填写。

        :param secondary_sources: The secondary_sources of this InputStreamInfo.
        :type secondary_sources: list[:class:`huaweicloudsdklive.v1.SecondarySourcesInfo`]
        """
        self._secondary_sources = secondary_sources

    @property
    def failover_conditions(self):
        """Gets the failover_conditions of this InputStreamInfo.

        :return: The failover_conditions of this InputStreamInfo.
        :rtype: :class:`huaweicloudsdklive.v1.FailoverConditions`
        """
        return self._failover_conditions

    @failover_conditions.setter
    def failover_conditions(self, failover_conditions):
        """Sets the failover_conditions of this InputStreamInfo.

        :param failover_conditions: The failover_conditions of this InputStreamInfo.
        :type failover_conditions: :class:`huaweicloudsdklive.v1.FailoverConditions`
        """
        self._failover_conditions = failover_conditions

    @property
    def max_bandwidth_limit(self):
        """Gets the max_bandwidth_limit of this InputStreamInfo.

        当入流协议为HLS_PULL时，最大带宽限制。 未配置会默认选择BANDWIDTH最高的流

        :return: The max_bandwidth_limit of this InputStreamInfo.
        :rtype: int
        """
        return self._max_bandwidth_limit

    @max_bandwidth_limit.setter
    def max_bandwidth_limit(self, max_bandwidth_limit):
        """Sets the max_bandwidth_limit of this InputStreamInfo.

        当入流协议为HLS_PULL时，最大带宽限制。 未配置会默认选择BANDWIDTH最高的流

        :param max_bandwidth_limit: The max_bandwidth_limit of this InputStreamInfo.
        :type max_bandwidth_limit: int
        """
        self._max_bandwidth_limit = max_bandwidth_limit

    @property
    def ip_port_mode(self):
        """Gets the ip_port_mode of this InputStreamInfo.

        当推流协议为SRT_PUSH时，如果配置了直推源站，编码器不支持输入streamid，需要打开设置为true

        :return: The ip_port_mode of this InputStreamInfo.
        :rtype: bool
        """
        return self._ip_port_mode

    @ip_port_mode.setter
    def ip_port_mode(self, ip_port_mode):
        """Sets the ip_port_mode of this InputStreamInfo.

        当推流协议为SRT_PUSH时，如果配置了直推源站，编码器不支持输入streamid，需要打开设置为true

        :param ip_port_mode: The ip_port_mode of this InputStreamInfo.
        :type ip_port_mode: bool
        """
        self._ip_port_mode = ip_port_mode

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
        if not isinstance(other, InputStreamInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
