# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepositoryStatisticsStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'can_statistics': 'bool',
        'reason': 'int',
        'event': 'StatisticEventsDto',
        'x_total': 'str'
    }

    attribute_map = {
        'can_statistics': 'can_statistics',
        'reason': 'reason',
        'event': 'event',
        'x_total': 'X-Total'
    }

    def __init__(self, can_statistics=None, reason=None, event=None, x_total=None):
        r"""ShowRepositoryStatisticsStatusResponse

        The model defined in huaweicloud sdk

        :param can_statistics: **参数解释：** 是否能被统计。 **取值范围：** - true，可以被统计。 - false，不可被统计。
        :type can_statistics: bool
        :param reason: **参数解释：** 是否能被统计。 **取值范围：** - 0，表示用户次数和仓库次数都没用完。 - 1，表示仓库次数用完。 - 2，表示用户次数用完。 - 3, 表示仓库次数和用户次数都用完
        :type reason: int
        :param event: 
        :type event: :class:`huaweicloudsdkcodehub.v4.StatisticEventsDto`
        :param x_total: 
        :type x_total: str
        """
        
        super(ShowRepositoryStatisticsStatusResponse, self).__init__()

        self._can_statistics = None
        self._reason = None
        self._event = None
        self._x_total = None
        self.discriminator = None

        if can_statistics is not None:
            self.can_statistics = can_statistics
        if reason is not None:
            self.reason = reason
        if event is not None:
            self.event = event
        if x_total is not None:
            self.x_total = x_total

    @property
    def can_statistics(self):
        r"""Gets the can_statistics of this ShowRepositoryStatisticsStatusResponse.

        **参数解释：** 是否能被统计。 **取值范围：** - true，可以被统计。 - false，不可被统计。

        :return: The can_statistics of this ShowRepositoryStatisticsStatusResponse.
        :rtype: bool
        """
        return self._can_statistics

    @can_statistics.setter
    def can_statistics(self, can_statistics):
        r"""Sets the can_statistics of this ShowRepositoryStatisticsStatusResponse.

        **参数解释：** 是否能被统计。 **取值范围：** - true，可以被统计。 - false，不可被统计。

        :param can_statistics: The can_statistics of this ShowRepositoryStatisticsStatusResponse.
        :type can_statistics: bool
        """
        self._can_statistics = can_statistics

    @property
    def reason(self):
        r"""Gets the reason of this ShowRepositoryStatisticsStatusResponse.

        **参数解释：** 是否能被统计。 **取值范围：** - 0，表示用户次数和仓库次数都没用完。 - 1，表示仓库次数用完。 - 2，表示用户次数用完。 - 3, 表示仓库次数和用户次数都用完

        :return: The reason of this ShowRepositoryStatisticsStatusResponse.
        :rtype: int
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this ShowRepositoryStatisticsStatusResponse.

        **参数解释：** 是否能被统计。 **取值范围：** - 0，表示用户次数和仓库次数都没用完。 - 1，表示仓库次数用完。 - 2，表示用户次数用完。 - 3, 表示仓库次数和用户次数都用完

        :param reason: The reason of this ShowRepositoryStatisticsStatusResponse.
        :type reason: int
        """
        self._reason = reason

    @property
    def event(self):
        r"""Gets the event of this ShowRepositoryStatisticsStatusResponse.

        :return: The event of this ShowRepositoryStatisticsStatusResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.StatisticEventsDto`
        """
        return self._event

    @event.setter
    def event(self, event):
        r"""Sets the event of this ShowRepositoryStatisticsStatusResponse.

        :param event: The event of this ShowRepositoryStatisticsStatusResponse.
        :type event: :class:`huaweicloudsdkcodehub.v4.StatisticEventsDto`
        """
        self._event = event

    @property
    def x_total(self):
        r"""Gets the x_total of this ShowRepositoryStatisticsStatusResponse.

        :return: The x_total of this ShowRepositoryStatisticsStatusResponse.
        :rtype: str
        """
        return self._x_total

    @x_total.setter
    def x_total(self, x_total):
        r"""Sets the x_total of this ShowRepositoryStatisticsStatusResponse.

        :param x_total: The x_total of this ShowRepositoryStatisticsStatusResponse.
        :type x_total: str
        """
        self._x_total = x_total

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
        if not isinstance(other, ShowRepositoryStatisticsStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
