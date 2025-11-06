# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSessionWaitEventStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'wait_event_info': 'list[SessionWaitEventStatisticInfo]'
    }

    attribute_map = {
        'total': 'total',
        'wait_event_info': 'wait_event_info'
    }

    def __init__(self, total=None, wait_event_info=None):
        r"""ListSessionWaitEventStatisticsResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**: 统计总条数。 **取值范围**: 不涉及。 
        :type total: int
        :param wait_event_info: **参数解释**: 统计数据。 
        :type wait_event_info: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SessionWaitEventStatisticInfo`]
        """
        
        super().__init__()

        self._total = None
        self._wait_event_info = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if wait_event_info is not None:
            self.wait_event_info = wait_event_info

    @property
    def total(self):
        r"""Gets the total of this ListSessionWaitEventStatisticsResponse.

        **参数解释**: 统计总条数。 **取值范围**: 不涉及。 

        :return: The total of this ListSessionWaitEventStatisticsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSessionWaitEventStatisticsResponse.

        **参数解释**: 统计总条数。 **取值范围**: 不涉及。 

        :param total: The total of this ListSessionWaitEventStatisticsResponse.
        :type total: int
        """
        self._total = total

    @property
    def wait_event_info(self):
        r"""Gets the wait_event_info of this ListSessionWaitEventStatisticsResponse.

        **参数解释**: 统计数据。 

        :return: The wait_event_info of this ListSessionWaitEventStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SessionWaitEventStatisticInfo`]
        """
        return self._wait_event_info

    @wait_event_info.setter
    def wait_event_info(self, wait_event_info):
        r"""Sets the wait_event_info of this ListSessionWaitEventStatisticsResponse.

        **参数解释**: 统计数据。 

        :param wait_event_info: The wait_event_info of this ListSessionWaitEventStatisticsResponse.
        :type wait_event_info: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SessionWaitEventStatisticInfo`]
        """
        self._wait_event_info = wait_event_info

    def to_dict(self):
        import warnings
        warnings.warn("ListSessionWaitEventStatisticsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListSessionWaitEventStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
