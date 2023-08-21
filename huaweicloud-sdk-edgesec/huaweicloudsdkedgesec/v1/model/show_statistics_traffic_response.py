# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatisticsTrafficResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'value': 'int',
        'flow': 'list[TimeSeriesData]',
        'drop': 'list[TimeSeriesData]',
        'waf': 'list[TimeSeriesData]',
        'bot': 'list[TimeSeriesData]',
        'cc': 'list[TimeSeriesData]',
        'ddos': 'list[TimeSeriesData]'
    }

    attribute_map = {
        'value': 'value',
        'flow': 'flow',
        'drop': 'drop',
        'waf': 'waf',
        'bot': 'bot',
        'cc': 'cc',
        'ddos': 'ddos'
    }

    def __init__(self, value=None, flow=None, drop=None, waf=None, bot=None, cc=None, ddos=None):
        """ShowStatisticsTrafficResponse

        The model defined in huaweicloud sdk

        :param value: 流量数据值，type&#x3D;max_flow_bandwidth/max_drop_bandwidth/ddos_flow时返回，单位：Kbps
        :type value: int
        :param flow: 入流量，type&#x3D;flow_drop_traffic时返回
        :type flow: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        :param drop: 清洗流量，type&#x3D;flow_drop_traffic时返回
        :type drop: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        :param waf: WAF攻击流量，type&#x3D;attack_traffic时返回
        :type waf: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        :param bot: BOT攻击流量，type&#x3D;attack_traffic时返回
        :type bot: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        :param cc: CC攻击流量，type&#x3D;attack_traffic时返回
        :type cc: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        :param ddos: DDoS攻击流量，type&#x3D;attack_traffic时返回
        :type ddos: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        
        super(ShowStatisticsTrafficResponse, self).__init__()

        self._value = None
        self._flow = None
        self._drop = None
        self._waf = None
        self._bot = None
        self._cc = None
        self._ddos = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if flow is not None:
            self.flow = flow
        if drop is not None:
            self.drop = drop
        if waf is not None:
            self.waf = waf
        if bot is not None:
            self.bot = bot
        if cc is not None:
            self.cc = cc
        if ddos is not None:
            self.ddos = ddos

    @property
    def value(self):
        """Gets the value of this ShowStatisticsTrafficResponse.

        流量数据值，type=max_flow_bandwidth/max_drop_bandwidth/ddos_flow时返回，单位：Kbps

        :return: The value of this ShowStatisticsTrafficResponse.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ShowStatisticsTrafficResponse.

        流量数据值，type=max_flow_bandwidth/max_drop_bandwidth/ddos_flow时返回，单位：Kbps

        :param value: The value of this ShowStatisticsTrafficResponse.
        :type value: int
        """
        self._value = value

    @property
    def flow(self):
        """Gets the flow of this ShowStatisticsTrafficResponse.

        入流量，type=flow_drop_traffic时返回

        :return: The flow of this ShowStatisticsTrafficResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this ShowStatisticsTrafficResponse.

        入流量，type=flow_drop_traffic时返回

        :param flow: The flow of this ShowStatisticsTrafficResponse.
        :type flow: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        self._flow = flow

    @property
    def drop(self):
        """Gets the drop of this ShowStatisticsTrafficResponse.

        清洗流量，type=flow_drop_traffic时返回

        :return: The drop of this ShowStatisticsTrafficResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        return self._drop

    @drop.setter
    def drop(self, drop):
        """Sets the drop of this ShowStatisticsTrafficResponse.

        清洗流量，type=flow_drop_traffic时返回

        :param drop: The drop of this ShowStatisticsTrafficResponse.
        :type drop: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        self._drop = drop

    @property
    def waf(self):
        """Gets the waf of this ShowStatisticsTrafficResponse.

        WAF攻击流量，type=attack_traffic时返回

        :return: The waf of this ShowStatisticsTrafficResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        return self._waf

    @waf.setter
    def waf(self, waf):
        """Sets the waf of this ShowStatisticsTrafficResponse.

        WAF攻击流量，type=attack_traffic时返回

        :param waf: The waf of this ShowStatisticsTrafficResponse.
        :type waf: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        self._waf = waf

    @property
    def bot(self):
        """Gets the bot of this ShowStatisticsTrafficResponse.

        BOT攻击流量，type=attack_traffic时返回

        :return: The bot of this ShowStatisticsTrafficResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        return self._bot

    @bot.setter
    def bot(self, bot):
        """Sets the bot of this ShowStatisticsTrafficResponse.

        BOT攻击流量，type=attack_traffic时返回

        :param bot: The bot of this ShowStatisticsTrafficResponse.
        :type bot: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        self._bot = bot

    @property
    def cc(self):
        """Gets the cc of this ShowStatisticsTrafficResponse.

        CC攻击流量，type=attack_traffic时返回

        :return: The cc of this ShowStatisticsTrafficResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this ShowStatisticsTrafficResponse.

        CC攻击流量，type=attack_traffic时返回

        :param cc: The cc of this ShowStatisticsTrafficResponse.
        :type cc: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        self._cc = cc

    @property
    def ddos(self):
        """Gets the ddos of this ShowStatisticsTrafficResponse.

        DDoS攻击流量，type=attack_traffic时返回

        :return: The ddos of this ShowStatisticsTrafficResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        return self._ddos

    @ddos.setter
    def ddos(self, ddos):
        """Sets the ddos of this ShowStatisticsTrafficResponse.

        DDoS攻击流量，type=attack_traffic时返回

        :param ddos: The ddos of this ShowStatisticsTrafficResponse.
        :type ddos: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        self._ddos = ddos

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
        if not isinstance(other, ShowStatisticsTrafficResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
