# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackgroundTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'start': 'int',
        'limit': 'int',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'start': 'start',
        'limit': 'limit',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, instance_id=None, start=None, limit=None, begin_time=None, end_time=None):
        r"""ListBackgroundTasksRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**： 实例ID。获取方法如下：登录RocketMQ控制台，在RocketMQ实例详情页面查找实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type instance_id: str
        :param start: **参数解释**： 开启查询的任务编号。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 不涉及。
        :type start: int
        :param limit: **参数解释**： 查询数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type limit: int
        :param begin_time: **参数解释**： 查询任务的最小时间，格式为YYYYMMDDHHmmss。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 不涉及。
        :type begin_time: str
        :param end_time: **参数解释**： 查询任务的最大时间，格式为YYYYMMDDHHmmss。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type end_time: str
        """
        
        

        self._instance_id = None
        self._start = None
        self._limit = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        self.instance_id = instance_id
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListBackgroundTasksRequest.

        **参数解释**： 实例ID。获取方法如下：登录RocketMQ控制台，在RocketMQ实例详情页面查找实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The instance_id of this ListBackgroundTasksRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListBackgroundTasksRequest.

        **参数解释**： 实例ID。获取方法如下：登录RocketMQ控制台，在RocketMQ实例详情页面查找实例ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param instance_id: The instance_id of this ListBackgroundTasksRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start(self):
        r"""Gets the start of this ListBackgroundTasksRequest.

        **参数解释**： 开启查询的任务编号。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 不涉及。

        :return: The start of this ListBackgroundTasksRequest.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this ListBackgroundTasksRequest.

        **参数解释**： 开启查询的任务编号。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 不涉及。

        :param start: The start of this ListBackgroundTasksRequest.
        :type start: int
        """
        self._start = start

    @property
    def limit(self):
        r"""Gets the limit of this ListBackgroundTasksRequest.

        **参数解释**： 查询数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The limit of this ListBackgroundTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBackgroundTasksRequest.

        **参数解释**： 查询数量。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param limit: The limit of this ListBackgroundTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListBackgroundTasksRequest.

        **参数解释**： 查询任务的最小时间，格式为YYYYMMDDHHmmss。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 不涉及。

        :return: The begin_time of this ListBackgroundTasksRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListBackgroundTasksRequest.

        **参数解释**： 查询任务的最小时间，格式为YYYYMMDDHHmmss。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 不涉及。

        :param begin_time: The begin_time of this ListBackgroundTasksRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListBackgroundTasksRequest.

        **参数解释**： 查询任务的最大时间，格式为YYYYMMDDHHmmss。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The end_time of this ListBackgroundTasksRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListBackgroundTasksRequest.

        **参数解释**： 查询任务的最大时间，格式为YYYYMMDDHHmmss。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param end_time: The end_time of this ListBackgroundTasksRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListBackgroundTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
