# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDecoyPortStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_num': 'int',
        'policy_num': 'int',
        'event_num': 'int',
        'linux_propose': 'list[DecoyPortBasePortStruct]',
        'windows_propose': 'list[DecoyPortBasePortStruct]'
    }

    attribute_map = {
        'host_num': 'host_num',
        'policy_num': 'policy_num',
        'event_num': 'event_num',
        'linux_propose': 'linux_propose',
        'windows_propose': 'windows_propose'
    }

    def __init__(self, host_num=None, policy_num=None, event_num=None, linux_propose=None, windows_propose=None):
        r"""ShowDecoyPortStatisticsResponse

        The model defined in huaweicloud sdk

        :param host_num: **参数解释**： 开启防护的主机数量 **取值范围**： 最小值0，最大值2147483647 
        :type host_num: int
        :param policy_num: **参数解释**： 策略数量 **取值范围**： 最小值0，最大值2147483647 
        :type policy_num: int
        :param event_num: **参数解释**： 未处理的事件数量 **取值范围**： 最小值0，最大值2147483647 
        :type event_num: int
        :param linux_propose: **参数解释**： linux的推荐端口配置 **取值范围**： 不涉及 
        :type linux_propose: list[:class:`huaweicloudsdkhss.v5.DecoyPortBasePortStruct`]
        :param windows_propose: **参数解释**： windows的推荐端口配置 **取值范围**： 不涉及 
        :type windows_propose: list[:class:`huaweicloudsdkhss.v5.DecoyPortBasePortStruct`]
        """
        
        super().__init__()

        self._host_num = None
        self._policy_num = None
        self._event_num = None
        self._linux_propose = None
        self._windows_propose = None
        self.discriminator = None

        if host_num is not None:
            self.host_num = host_num
        if policy_num is not None:
            self.policy_num = policy_num
        if event_num is not None:
            self.event_num = event_num
        if linux_propose is not None:
            self.linux_propose = linux_propose
        if windows_propose is not None:
            self.windows_propose = windows_propose

    @property
    def host_num(self):
        r"""Gets the host_num of this ShowDecoyPortStatisticsResponse.

        **参数解释**： 开启防护的主机数量 **取值范围**： 最小值0，最大值2147483647 

        :return: The host_num of this ShowDecoyPortStatisticsResponse.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this ShowDecoyPortStatisticsResponse.

        **参数解释**： 开启防护的主机数量 **取值范围**： 最小值0，最大值2147483647 

        :param host_num: The host_num of this ShowDecoyPortStatisticsResponse.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def policy_num(self):
        r"""Gets the policy_num of this ShowDecoyPortStatisticsResponse.

        **参数解释**： 策略数量 **取值范围**： 最小值0，最大值2147483647 

        :return: The policy_num of this ShowDecoyPortStatisticsResponse.
        :rtype: int
        """
        return self._policy_num

    @policy_num.setter
    def policy_num(self, policy_num):
        r"""Sets the policy_num of this ShowDecoyPortStatisticsResponse.

        **参数解释**： 策略数量 **取值范围**： 最小值0，最大值2147483647 

        :param policy_num: The policy_num of this ShowDecoyPortStatisticsResponse.
        :type policy_num: int
        """
        self._policy_num = policy_num

    @property
    def event_num(self):
        r"""Gets the event_num of this ShowDecoyPortStatisticsResponse.

        **参数解释**： 未处理的事件数量 **取值范围**： 最小值0，最大值2147483647 

        :return: The event_num of this ShowDecoyPortStatisticsResponse.
        :rtype: int
        """
        return self._event_num

    @event_num.setter
    def event_num(self, event_num):
        r"""Sets the event_num of this ShowDecoyPortStatisticsResponse.

        **参数解释**： 未处理的事件数量 **取值范围**： 最小值0，最大值2147483647 

        :param event_num: The event_num of this ShowDecoyPortStatisticsResponse.
        :type event_num: int
        """
        self._event_num = event_num

    @property
    def linux_propose(self):
        r"""Gets the linux_propose of this ShowDecoyPortStatisticsResponse.

        **参数解释**： linux的推荐端口配置 **取值范围**： 不涉及 

        :return: The linux_propose of this ShowDecoyPortStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.DecoyPortBasePortStruct`]
        """
        return self._linux_propose

    @linux_propose.setter
    def linux_propose(self, linux_propose):
        r"""Sets the linux_propose of this ShowDecoyPortStatisticsResponse.

        **参数解释**： linux的推荐端口配置 **取值范围**： 不涉及 

        :param linux_propose: The linux_propose of this ShowDecoyPortStatisticsResponse.
        :type linux_propose: list[:class:`huaweicloudsdkhss.v5.DecoyPortBasePortStruct`]
        """
        self._linux_propose = linux_propose

    @property
    def windows_propose(self):
        r"""Gets the windows_propose of this ShowDecoyPortStatisticsResponse.

        **参数解释**： windows的推荐端口配置 **取值范围**： 不涉及 

        :return: The windows_propose of this ShowDecoyPortStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.DecoyPortBasePortStruct`]
        """
        return self._windows_propose

    @windows_propose.setter
    def windows_propose(self, windows_propose):
        r"""Sets the windows_propose of this ShowDecoyPortStatisticsResponse.

        **参数解释**： windows的推荐端口配置 **取值范围**： 不涉及 

        :param windows_propose: The windows_propose of this ShowDecoyPortStatisticsResponse.
        :type windows_propose: list[:class:`huaweicloudsdkhss.v5.DecoyPortBasePortStruct`]
        """
        self._windows_propose = windows_propose

    def to_dict(self):
        import warnings
        warnings.warn("ShowDecoyPortStatisticsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowDecoyPortStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
