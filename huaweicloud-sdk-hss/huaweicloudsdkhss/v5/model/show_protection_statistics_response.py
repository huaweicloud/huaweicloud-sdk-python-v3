# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProtectionStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count_protected_server': 'int',
        'count_need_protected_server': 'int',
        'count_protection_event': 'int'
    }

    attribute_map = {
        'count_protected_server': 'count_protected_server',
        'count_need_protected_server': 'count_need_protected_server',
        'count_protection_event': 'count_protection_event'
    }

    def __init__(self, count_protected_server=None, count_need_protected_server=None, count_protection_event=None):
        r"""ShowProtectionStatisticsResponse

        The model defined in huaweicloud sdk

        :param count_protected_server: **参数解释**： 已防护服务器数量 **取值范围**： 最小值0，最大值2147483647 
        :type count_protected_server: int
        :param count_need_protected_server: **参数解释**： 未防护服务器数量 **取值范围**： 最小值0，最大值2147483647 
        :type count_need_protected_server: int
        :param count_protection_event: **参数解释**： 防护事件 **取值范围**： 最小值0，最大值2147483647 
        :type count_protection_event: int
        """
        
        super().__init__()

        self._count_protected_server = None
        self._count_need_protected_server = None
        self._count_protection_event = None
        self.discriminator = None

        if count_protected_server is not None:
            self.count_protected_server = count_protected_server
        if count_need_protected_server is not None:
            self.count_need_protected_server = count_need_protected_server
        if count_protection_event is not None:
            self.count_protection_event = count_protection_event

    @property
    def count_protected_server(self):
        r"""Gets the count_protected_server of this ShowProtectionStatisticsResponse.

        **参数解释**： 已防护服务器数量 **取值范围**： 最小值0，最大值2147483647 

        :return: The count_protected_server of this ShowProtectionStatisticsResponse.
        :rtype: int
        """
        return self._count_protected_server

    @count_protected_server.setter
    def count_protected_server(self, count_protected_server):
        r"""Sets the count_protected_server of this ShowProtectionStatisticsResponse.

        **参数解释**： 已防护服务器数量 **取值范围**： 最小值0，最大值2147483647 

        :param count_protected_server: The count_protected_server of this ShowProtectionStatisticsResponse.
        :type count_protected_server: int
        """
        self._count_protected_server = count_protected_server

    @property
    def count_need_protected_server(self):
        r"""Gets the count_need_protected_server of this ShowProtectionStatisticsResponse.

        **参数解释**： 未防护服务器数量 **取值范围**： 最小值0，最大值2147483647 

        :return: The count_need_protected_server of this ShowProtectionStatisticsResponse.
        :rtype: int
        """
        return self._count_need_protected_server

    @count_need_protected_server.setter
    def count_need_protected_server(self, count_need_protected_server):
        r"""Sets the count_need_protected_server of this ShowProtectionStatisticsResponse.

        **参数解释**： 未防护服务器数量 **取值范围**： 最小值0，最大值2147483647 

        :param count_need_protected_server: The count_need_protected_server of this ShowProtectionStatisticsResponse.
        :type count_need_protected_server: int
        """
        self._count_need_protected_server = count_need_protected_server

    @property
    def count_protection_event(self):
        r"""Gets the count_protection_event of this ShowProtectionStatisticsResponse.

        **参数解释**： 防护事件 **取值范围**： 最小值0，最大值2147483647 

        :return: The count_protection_event of this ShowProtectionStatisticsResponse.
        :rtype: int
        """
        return self._count_protection_event

    @count_protection_event.setter
    def count_protection_event(self, count_protection_event):
        r"""Sets the count_protection_event of this ShowProtectionStatisticsResponse.

        **参数解释**： 防护事件 **取值范围**： 最小值0，最大值2147483647 

        :param count_protection_event: The count_protection_event of this ShowProtectionStatisticsResponse.
        :type count_protection_event: int
        """
        self._count_protection_event = count_protection_event

    def to_dict(self):
        import warnings
        warnings.warn("ShowProtectionStatisticsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowProtectionStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
