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
        'ip_port_mode': 'bool',
        'ip_whitelist': 'str',
        'scte35_source': 'str',
        'ad_triggers': 'list[str]',
        'audio_selectors': 'list[InputAudioSelector]'
    }

    attribute_map = {
        'input_protocol': 'input_protocol',
        'sources': 'sources',
        'secondary_sources': 'secondary_sources',
        'failover_conditions': 'failover_conditions',
        'max_bandwidth_limit': 'max_bandwidth_limit',
        'ip_port_mode': 'ip_port_mode',
        'ip_whitelist': 'ip_whitelist',
        'scte35_source': 'scte35_source',
        'ad_triggers': 'ad_triggers',
        'audio_selectors': 'audio_selectors'
    }

    def __init__(self, input_protocol=None, sources=None, secondary_sources=None, failover_conditions=None, max_bandwidth_limit=None, ip_port_mode=None, ip_whitelist=None, scte35_source=None, ad_triggers=None, audio_selectors=None):
        r"""InputStreamInfo

        The model defined in huaweicloud sdk

        :param input_protocol: 频道入流协议 - FLV_PULL - RTMP_PUSH - HLS_PULL - SRT_PULL - SRT_PUSH
        :type input_protocol: str
        :param sources: 频道主源流信息。入流协议为RTMP_PUSH和SRT_PUSH时，非必填项。其他情况下，均为必填项。
        :type sources: list[:class:`huaweicloudsdklive.v1.SourcesInfo`]
        :param secondary_sources: 备入流数组，非必填项。如果有备入流，则主备入流必须保证路数、codec和分辨率均一致。入流协议为RTMP_PUSH时，无需填写。
        :type secondary_sources: list[:class:`huaweicloudsdklive.v1.SecondarySourcesInfo`]
        :param failover_conditions: 
        :type failover_conditions: :class:`huaweicloudsdklive.v1.FailoverConditions`
        :param max_bandwidth_limit: 当入流协议为HLS_PULL时，需要配置的最大带宽。  用户提供的拉流URL中，针对不同码率的音视频，均会携带带宽参数“BANDWIDTH”。 - 如果这里配置最大带宽，媒体直播服务从URL拉流时，会选择小于最大带宽且码率最大的音视频流，推流到源站。 - 如果这里未配置最大带宽，媒体直播服务从URL拉流时，会默认选择“BANDWIDTH”最高的音视频流，推流到源站。
        :type max_bandwidth_limit: int
        :param ip_port_mode: 当推流协议为SRT_PUSH时，如果配置了直推源站，编码器不支持输入streamid，需要打开设置为true
        :type ip_port_mode: bool
        :param ip_whitelist: SRT_PUSH类型时，客户push ip白名单
        :type ip_whitelist: str
        :param scte35_source: 广告的scte35信号源。  仅HLS_PULL类型的频道支持此配置，且目前仅支持SEGMENTS。
        :type scte35_source: str
        :param ad_triggers: 广告触发器配置。  包含如下取值： - Splice insert：拼接插入 - Provider advertisement：提供商广告 - Distributor advertisement：分销商广告 - Provider placement opportunity：提供商置放机会 - Distributor placement opportunity：分销商置放机会
        :type ad_triggers: list[str]
        :param audio_selectors: 设置音频选择器，最多设置8个音频选择器
        :type audio_selectors: list[:class:`huaweicloudsdklive.v1.InputAudioSelector`]
        """
        
        

        self._input_protocol = None
        self._sources = None
        self._secondary_sources = None
        self._failover_conditions = None
        self._max_bandwidth_limit = None
        self._ip_port_mode = None
        self._ip_whitelist = None
        self._scte35_source = None
        self._ad_triggers = None
        self._audio_selectors = None
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
        if ip_whitelist is not None:
            self.ip_whitelist = ip_whitelist
        if scte35_source is not None:
            self.scte35_source = scte35_source
        if ad_triggers is not None:
            self.ad_triggers = ad_triggers
        if audio_selectors is not None:
            self.audio_selectors = audio_selectors

    @property
    def input_protocol(self):
        r"""Gets the input_protocol of this InputStreamInfo.

        频道入流协议 - FLV_PULL - RTMP_PUSH - HLS_PULL - SRT_PULL - SRT_PUSH

        :return: The input_protocol of this InputStreamInfo.
        :rtype: str
        """
        return self._input_protocol

    @input_protocol.setter
    def input_protocol(self, input_protocol):
        r"""Sets the input_protocol of this InputStreamInfo.

        频道入流协议 - FLV_PULL - RTMP_PUSH - HLS_PULL - SRT_PULL - SRT_PUSH

        :param input_protocol: The input_protocol of this InputStreamInfo.
        :type input_protocol: str
        """
        self._input_protocol = input_protocol

    @property
    def sources(self):
        r"""Gets the sources of this InputStreamInfo.

        频道主源流信息。入流协议为RTMP_PUSH和SRT_PUSH时，非必填项。其他情况下，均为必填项。

        :return: The sources of this InputStreamInfo.
        :rtype: list[:class:`huaweicloudsdklive.v1.SourcesInfo`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this InputStreamInfo.

        频道主源流信息。入流协议为RTMP_PUSH和SRT_PUSH时，非必填项。其他情况下，均为必填项。

        :param sources: The sources of this InputStreamInfo.
        :type sources: list[:class:`huaweicloudsdklive.v1.SourcesInfo`]
        """
        self._sources = sources

    @property
    def secondary_sources(self):
        r"""Gets the secondary_sources of this InputStreamInfo.

        备入流数组，非必填项。如果有备入流，则主备入流必须保证路数、codec和分辨率均一致。入流协议为RTMP_PUSH时，无需填写。

        :return: The secondary_sources of this InputStreamInfo.
        :rtype: list[:class:`huaweicloudsdklive.v1.SecondarySourcesInfo`]
        """
        return self._secondary_sources

    @secondary_sources.setter
    def secondary_sources(self, secondary_sources):
        r"""Sets the secondary_sources of this InputStreamInfo.

        备入流数组，非必填项。如果有备入流，则主备入流必须保证路数、codec和分辨率均一致。入流协议为RTMP_PUSH时，无需填写。

        :param secondary_sources: The secondary_sources of this InputStreamInfo.
        :type secondary_sources: list[:class:`huaweicloudsdklive.v1.SecondarySourcesInfo`]
        """
        self._secondary_sources = secondary_sources

    @property
    def failover_conditions(self):
        r"""Gets the failover_conditions of this InputStreamInfo.

        :return: The failover_conditions of this InputStreamInfo.
        :rtype: :class:`huaweicloudsdklive.v1.FailoverConditions`
        """
        return self._failover_conditions

    @failover_conditions.setter
    def failover_conditions(self, failover_conditions):
        r"""Sets the failover_conditions of this InputStreamInfo.

        :param failover_conditions: The failover_conditions of this InputStreamInfo.
        :type failover_conditions: :class:`huaweicloudsdklive.v1.FailoverConditions`
        """
        self._failover_conditions = failover_conditions

    @property
    def max_bandwidth_limit(self):
        r"""Gets the max_bandwidth_limit of this InputStreamInfo.

        当入流协议为HLS_PULL时，需要配置的最大带宽。  用户提供的拉流URL中，针对不同码率的音视频，均会携带带宽参数“BANDWIDTH”。 - 如果这里配置最大带宽，媒体直播服务从URL拉流时，会选择小于最大带宽且码率最大的音视频流，推流到源站。 - 如果这里未配置最大带宽，媒体直播服务从URL拉流时，会默认选择“BANDWIDTH”最高的音视频流，推流到源站。

        :return: The max_bandwidth_limit of this InputStreamInfo.
        :rtype: int
        """
        return self._max_bandwidth_limit

    @max_bandwidth_limit.setter
    def max_bandwidth_limit(self, max_bandwidth_limit):
        r"""Sets the max_bandwidth_limit of this InputStreamInfo.

        当入流协议为HLS_PULL时，需要配置的最大带宽。  用户提供的拉流URL中，针对不同码率的音视频，均会携带带宽参数“BANDWIDTH”。 - 如果这里配置最大带宽，媒体直播服务从URL拉流时，会选择小于最大带宽且码率最大的音视频流，推流到源站。 - 如果这里未配置最大带宽，媒体直播服务从URL拉流时，会默认选择“BANDWIDTH”最高的音视频流，推流到源站。

        :param max_bandwidth_limit: The max_bandwidth_limit of this InputStreamInfo.
        :type max_bandwidth_limit: int
        """
        self._max_bandwidth_limit = max_bandwidth_limit

    @property
    def ip_port_mode(self):
        r"""Gets the ip_port_mode of this InputStreamInfo.

        当推流协议为SRT_PUSH时，如果配置了直推源站，编码器不支持输入streamid，需要打开设置为true

        :return: The ip_port_mode of this InputStreamInfo.
        :rtype: bool
        """
        return self._ip_port_mode

    @ip_port_mode.setter
    def ip_port_mode(self, ip_port_mode):
        r"""Sets the ip_port_mode of this InputStreamInfo.

        当推流协议为SRT_PUSH时，如果配置了直推源站，编码器不支持输入streamid，需要打开设置为true

        :param ip_port_mode: The ip_port_mode of this InputStreamInfo.
        :type ip_port_mode: bool
        """
        self._ip_port_mode = ip_port_mode

    @property
    def ip_whitelist(self):
        r"""Gets the ip_whitelist of this InputStreamInfo.

        SRT_PUSH类型时，客户push ip白名单

        :return: The ip_whitelist of this InputStreamInfo.
        :rtype: str
        """
        return self._ip_whitelist

    @ip_whitelist.setter
    def ip_whitelist(self, ip_whitelist):
        r"""Sets the ip_whitelist of this InputStreamInfo.

        SRT_PUSH类型时，客户push ip白名单

        :param ip_whitelist: The ip_whitelist of this InputStreamInfo.
        :type ip_whitelist: str
        """
        self._ip_whitelist = ip_whitelist

    @property
    def scte35_source(self):
        r"""Gets the scte35_source of this InputStreamInfo.

        广告的scte35信号源。  仅HLS_PULL类型的频道支持此配置，且目前仅支持SEGMENTS。

        :return: The scte35_source of this InputStreamInfo.
        :rtype: str
        """
        return self._scte35_source

    @scte35_source.setter
    def scte35_source(self, scte35_source):
        r"""Sets the scte35_source of this InputStreamInfo.

        广告的scte35信号源。  仅HLS_PULL类型的频道支持此配置，且目前仅支持SEGMENTS。

        :param scte35_source: The scte35_source of this InputStreamInfo.
        :type scte35_source: str
        """
        self._scte35_source = scte35_source

    @property
    def ad_triggers(self):
        r"""Gets the ad_triggers of this InputStreamInfo.

        广告触发器配置。  包含如下取值： - Splice insert：拼接插入 - Provider advertisement：提供商广告 - Distributor advertisement：分销商广告 - Provider placement opportunity：提供商置放机会 - Distributor placement opportunity：分销商置放机会

        :return: The ad_triggers of this InputStreamInfo.
        :rtype: list[str]
        """
        return self._ad_triggers

    @ad_triggers.setter
    def ad_triggers(self, ad_triggers):
        r"""Sets the ad_triggers of this InputStreamInfo.

        广告触发器配置。  包含如下取值： - Splice insert：拼接插入 - Provider advertisement：提供商广告 - Distributor advertisement：分销商广告 - Provider placement opportunity：提供商置放机会 - Distributor placement opportunity：分销商置放机会

        :param ad_triggers: The ad_triggers of this InputStreamInfo.
        :type ad_triggers: list[str]
        """
        self._ad_triggers = ad_triggers

    @property
    def audio_selectors(self):
        r"""Gets the audio_selectors of this InputStreamInfo.

        设置音频选择器，最多设置8个音频选择器

        :return: The audio_selectors of this InputStreamInfo.
        :rtype: list[:class:`huaweicloudsdklive.v1.InputAudioSelector`]
        """
        return self._audio_selectors

    @audio_selectors.setter
    def audio_selectors(self, audio_selectors):
        r"""Sets the audio_selectors of this InputStreamInfo.

        设置音频选择器，最多设置8个音频选择器

        :param audio_selectors: The audio_selectors of this InputStreamInfo.
        :type audio_selectors: list[:class:`huaweicloudsdklive.v1.InputAudioSelector`]
        """
        self._audio_selectors = audio_selectors

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
