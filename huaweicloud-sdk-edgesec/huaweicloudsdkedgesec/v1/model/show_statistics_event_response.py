# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatisticsEventResponse(SdkResponse):

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
        'waf': 'list[TimeSeriesData]',
        'bot': 'list[TimeSeriesData]',
        'cc': 'list[TimeSeriesData]',
        'ddos': 'list[TimeSeriesData]',
        'flow': 'list[TimeSeriesData]',
        'drop': 'list[TimeSeriesData]'
    }

    attribute_map = {
        'value': 'value',
        'waf': 'waf',
        'bot': 'bot',
        'cc': 'cc',
        'ddos': 'ddos',
        'flow': 'flow',
        'drop': 'drop'
    }

    def __init__(self, value=None, waf=None, bot=None, cc=None, ddos=None, flow=None, drop=None):
        """ShowStatisticsEventResponse

        The model defined in huaweicloud sdk

        :param value: DDos攻击事件次数，type&#x3D;ddos_attack_count返回
        :type value: int
        :param waf: WAF攻击事件次数，type&#x3D;attack_count时返回
        :type waf: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        :param bot: BOT攻击事件次数，type&#x3D;attack_count时返回
        :type bot: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        :param cc: CC攻击事件次数，type&#x3D;attack_count时返回
        :type cc: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        :param ddos: DDos攻击事件次数，type&#x3D;attack_count返回
        :type ddos: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        :param flow: 访问次数，type&#x3D;flow_drop_count返回
        :type flow: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        :param drop: 攻击次数，type&#x3D;flow_drop_count返回
        :type drop: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        
        super(ShowStatisticsEventResponse, self).__init__()

        self._value = None
        self._waf = None
        self._bot = None
        self._cc = None
        self._ddos = None
        self._flow = None
        self._drop = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if waf is not None:
            self.waf = waf
        if bot is not None:
            self.bot = bot
        if cc is not None:
            self.cc = cc
        if ddos is not None:
            self.ddos = ddos
        if flow is not None:
            self.flow = flow
        if drop is not None:
            self.drop = drop

    @property
    def value(self):
        """Gets the value of this ShowStatisticsEventResponse.

        DDos攻击事件次数，type=ddos_attack_count返回

        :return: The value of this ShowStatisticsEventResponse.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ShowStatisticsEventResponse.

        DDos攻击事件次数，type=ddos_attack_count返回

        :param value: The value of this ShowStatisticsEventResponse.
        :type value: int
        """
        self._value = value

    @property
    def waf(self):
        """Gets the waf of this ShowStatisticsEventResponse.

        WAF攻击事件次数，type=attack_count时返回

        :return: The waf of this ShowStatisticsEventResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        return self._waf

    @waf.setter
    def waf(self, waf):
        """Sets the waf of this ShowStatisticsEventResponse.

        WAF攻击事件次数，type=attack_count时返回

        :param waf: The waf of this ShowStatisticsEventResponse.
        :type waf: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        self._waf = waf

    @property
    def bot(self):
        """Gets the bot of this ShowStatisticsEventResponse.

        BOT攻击事件次数，type=attack_count时返回

        :return: The bot of this ShowStatisticsEventResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        return self._bot

    @bot.setter
    def bot(self, bot):
        """Sets the bot of this ShowStatisticsEventResponse.

        BOT攻击事件次数，type=attack_count时返回

        :param bot: The bot of this ShowStatisticsEventResponse.
        :type bot: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        self._bot = bot

    @property
    def cc(self):
        """Gets the cc of this ShowStatisticsEventResponse.

        CC攻击事件次数，type=attack_count时返回

        :return: The cc of this ShowStatisticsEventResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this ShowStatisticsEventResponse.

        CC攻击事件次数，type=attack_count时返回

        :param cc: The cc of this ShowStatisticsEventResponse.
        :type cc: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        self._cc = cc

    @property
    def ddos(self):
        """Gets the ddos of this ShowStatisticsEventResponse.

        DDos攻击事件次数，type=attack_count返回

        :return: The ddos of this ShowStatisticsEventResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        return self._ddos

    @ddos.setter
    def ddos(self, ddos):
        """Sets the ddos of this ShowStatisticsEventResponse.

        DDos攻击事件次数，type=attack_count返回

        :param ddos: The ddos of this ShowStatisticsEventResponse.
        :type ddos: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        self._ddos = ddos

    @property
    def flow(self):
        """Gets the flow of this ShowStatisticsEventResponse.

        访问次数，type=flow_drop_count返回

        :return: The flow of this ShowStatisticsEventResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this ShowStatisticsEventResponse.

        访问次数，type=flow_drop_count返回

        :param flow: The flow of this ShowStatisticsEventResponse.
        :type flow: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        self._flow = flow

    @property
    def drop(self):
        """Gets the drop of this ShowStatisticsEventResponse.

        攻击次数，type=flow_drop_count返回

        :return: The drop of this ShowStatisticsEventResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        return self._drop

    @drop.setter
    def drop(self, drop):
        """Sets the drop of this ShowStatisticsEventResponse.

        攻击次数，type=flow_drop_count返回

        :param drop: The drop of this ShowStatisticsEventResponse.
        :type drop: list[:class:`huaweicloudsdkedgesec.v1.TimeSeriesData`]
        """
        self._drop = drop

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
        if not isinstance(other, ShowStatisticsEventResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
