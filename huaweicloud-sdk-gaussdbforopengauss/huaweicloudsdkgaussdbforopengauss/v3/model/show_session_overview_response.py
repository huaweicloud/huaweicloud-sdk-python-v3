# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSessionOverviewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'active_num': 'str',
        'total_num': 'str',
        'slow_sql_num': 'str',
        'lock_num': 'str'
    }

    attribute_map = {
        'active_num': 'active_num',
        'total_num': 'total_num',
        'slow_sql_num': 'slow_sql_num',
        'lock_num': 'lock_num'
    }

    def __init__(self, active_num=None, total_num=None, slow_sql_num=None, lock_num=None):
        r"""ShowSessionOverviewResponse

        The model defined in huaweicloud sdk

        :param active_num: **参数解释**: 实时会话的活跃会话数。 **取值范围**: 不涉及。
        :type active_num: str
        :param total_num: **参数解释**: 实时会话的总会话数。 **取值范围**: 不涉及。
        :type total_num: str
        :param slow_sql_num: **参数解释**: 实时会话中的慢SQL数量。 **取值范围**: 不涉及。
        :type slow_sql_num: str
        :param lock_num: **参数解释**: 实时会话中的锁等会话数。 **取值范围**: 不涉及。
        :type lock_num: str
        """
        
        super(ShowSessionOverviewResponse, self).__init__()

        self._active_num = None
        self._total_num = None
        self._slow_sql_num = None
        self._lock_num = None
        self.discriminator = None

        if active_num is not None:
            self.active_num = active_num
        if total_num is not None:
            self.total_num = total_num
        if slow_sql_num is not None:
            self.slow_sql_num = slow_sql_num
        if lock_num is not None:
            self.lock_num = lock_num

    @property
    def active_num(self):
        r"""Gets the active_num of this ShowSessionOverviewResponse.

        **参数解释**: 实时会话的活跃会话数。 **取值范围**: 不涉及。

        :return: The active_num of this ShowSessionOverviewResponse.
        :rtype: str
        """
        return self._active_num

    @active_num.setter
    def active_num(self, active_num):
        r"""Sets the active_num of this ShowSessionOverviewResponse.

        **参数解释**: 实时会话的活跃会话数。 **取值范围**: 不涉及。

        :param active_num: The active_num of this ShowSessionOverviewResponse.
        :type active_num: str
        """
        self._active_num = active_num

    @property
    def total_num(self):
        r"""Gets the total_num of this ShowSessionOverviewResponse.

        **参数解释**: 实时会话的总会话数。 **取值范围**: 不涉及。

        :return: The total_num of this ShowSessionOverviewResponse.
        :rtype: str
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ShowSessionOverviewResponse.

        **参数解释**: 实时会话的总会话数。 **取值范围**: 不涉及。

        :param total_num: The total_num of this ShowSessionOverviewResponse.
        :type total_num: str
        """
        self._total_num = total_num

    @property
    def slow_sql_num(self):
        r"""Gets the slow_sql_num of this ShowSessionOverviewResponse.

        **参数解释**: 实时会话中的慢SQL数量。 **取值范围**: 不涉及。

        :return: The slow_sql_num of this ShowSessionOverviewResponse.
        :rtype: str
        """
        return self._slow_sql_num

    @slow_sql_num.setter
    def slow_sql_num(self, slow_sql_num):
        r"""Sets the slow_sql_num of this ShowSessionOverviewResponse.

        **参数解释**: 实时会话中的慢SQL数量。 **取值范围**: 不涉及。

        :param slow_sql_num: The slow_sql_num of this ShowSessionOverviewResponse.
        :type slow_sql_num: str
        """
        self._slow_sql_num = slow_sql_num

    @property
    def lock_num(self):
        r"""Gets the lock_num of this ShowSessionOverviewResponse.

        **参数解释**: 实时会话中的锁等会话数。 **取值范围**: 不涉及。

        :return: The lock_num of this ShowSessionOverviewResponse.
        :rtype: str
        """
        return self._lock_num

    @lock_num.setter
    def lock_num(self, lock_num):
        r"""Sets the lock_num of this ShowSessionOverviewResponse.

        **参数解释**: 实时会话中的锁等会话数。 **取值范围**: 不涉及。

        :param lock_num: The lock_num of this ShowSessionOverviewResponse.
        :type lock_num: str
        """
        self._lock_num = lock_num

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
        if not isinstance(other, ShowSessionOverviewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
