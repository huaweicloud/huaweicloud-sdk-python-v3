# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEventSeverityResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'low_num': 'int',
        'medium_num': 'int',
        'high_num': 'int',
        'critical_num': 'int'
    }

    attribute_map = {
        'total_num': 'total_num',
        'low_num': 'low_num',
        'medium_num': 'medium_num',
        'high_num': 'high_num',
        'critical_num': 'critical_num'
    }

    def __init__(self, total_num=None, low_num=None, medium_num=None, high_num=None, critical_num=None):
        r"""ShowEventSeverityResponse

        The model defined in huaweicloud sdk

        :param total_num: **参数解释**: 总数 **取值范围**: 最小值0，最大值2147483647 
        :type total_num: int
        :param low_num: 低危数量
        :type low_num: int
        :param medium_num: 中危数量
        :type medium_num: int
        :param high_num: 高危数量
        :type high_num: int
        :param critical_num: 危急数量
        :type critical_num: int
        """
        
        super().__init__()

        self._total_num = None
        self._low_num = None
        self._medium_num = None
        self._high_num = None
        self._critical_num = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if low_num is not None:
            self.low_num = low_num
        if medium_num is not None:
            self.medium_num = medium_num
        if high_num is not None:
            self.high_num = high_num
        if critical_num is not None:
            self.critical_num = critical_num

    @property
    def total_num(self):
        r"""Gets the total_num of this ShowEventSeverityResponse.

        **参数解释**: 总数 **取值范围**: 最小值0，最大值2147483647 

        :return: The total_num of this ShowEventSeverityResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ShowEventSeverityResponse.

        **参数解释**: 总数 **取值范围**: 最小值0，最大值2147483647 

        :param total_num: The total_num of this ShowEventSeverityResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def low_num(self):
        r"""Gets the low_num of this ShowEventSeverityResponse.

        低危数量

        :return: The low_num of this ShowEventSeverityResponse.
        :rtype: int
        """
        return self._low_num

    @low_num.setter
    def low_num(self, low_num):
        r"""Sets the low_num of this ShowEventSeverityResponse.

        低危数量

        :param low_num: The low_num of this ShowEventSeverityResponse.
        :type low_num: int
        """
        self._low_num = low_num

    @property
    def medium_num(self):
        r"""Gets the medium_num of this ShowEventSeverityResponse.

        中危数量

        :return: The medium_num of this ShowEventSeverityResponse.
        :rtype: int
        """
        return self._medium_num

    @medium_num.setter
    def medium_num(self, medium_num):
        r"""Sets the medium_num of this ShowEventSeverityResponse.

        中危数量

        :param medium_num: The medium_num of this ShowEventSeverityResponse.
        :type medium_num: int
        """
        self._medium_num = medium_num

    @property
    def high_num(self):
        r"""Gets the high_num of this ShowEventSeverityResponse.

        高危数量

        :return: The high_num of this ShowEventSeverityResponse.
        :rtype: int
        """
        return self._high_num

    @high_num.setter
    def high_num(self, high_num):
        r"""Sets the high_num of this ShowEventSeverityResponse.

        高危数量

        :param high_num: The high_num of this ShowEventSeverityResponse.
        :type high_num: int
        """
        self._high_num = high_num

    @property
    def critical_num(self):
        r"""Gets the critical_num of this ShowEventSeverityResponse.

        危急数量

        :return: The critical_num of this ShowEventSeverityResponse.
        :rtype: int
        """
        return self._critical_num

    @critical_num.setter
    def critical_num(self, critical_num):
        r"""Sets the critical_num of this ShowEventSeverityResponse.

        危急数量

        :param critical_num: The critical_num of this ShowEventSeverityResponse.
        :type critical_num: int
        """
        self._critical_num = critical_num

    def to_dict(self):
        import warnings
        warnings.warn("ShowEventSeverityResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowEventSeverityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
