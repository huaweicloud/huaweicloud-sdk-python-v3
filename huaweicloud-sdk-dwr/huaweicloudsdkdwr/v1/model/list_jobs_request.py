# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'offset': 'int',
        'limit': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, start_time=None, end_time=None, status=None, offset=None, limit=None):
        r"""ListJobsRequest

        The model defined in huaweicloud sdk

        :param start_time: **参数解释：** 查询开始时间。 **约束限制：** 格式为“yyyy-mm-ddThh:mm:ssZ”。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type start_time: str
        :param end_time: **参数解释：** 查询结束时间。 **约束限制：** 格式为“yyyy-mm-ddThh:mm:ssZ”。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type end_time: str
        :param status: **参数解释：** 任务状态。 **约束限制：** 不涉及。 **取值范围：** 1、“Running”：执行中； 2、“Completed”：完成； 3、“Failed”：失败。 **默认取值:** 不涉及。
        :type status: str
        :param offset: **参数解释：** 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制：** 必须为数字，不能为负数。 **取值范围：** [0-4096] **默认取值:** 默认为0（偏移0条数据，表示从第一条数据开始查询）。
        :type offset: int
        :param limit: **参数解释：** 查询记录数。 **约束限制：** 不能为负数。 **取值范围：** [1-100]。 **默认取值:** 1。
        :type limit: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def start_time(self):
        r"""Gets the start_time of this ListJobsRequest.

        **参数解释：** 查询开始时间。 **约束限制：** 格式为“yyyy-mm-ddThh:mm:ssZ”。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The start_time of this ListJobsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListJobsRequest.

        **参数解释：** 查询开始时间。 **约束限制：** 格式为“yyyy-mm-ddThh:mm:ssZ”。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param start_time: The start_time of this ListJobsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListJobsRequest.

        **参数解释：** 查询结束时间。 **约束限制：** 格式为“yyyy-mm-ddThh:mm:ssZ”。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The end_time of this ListJobsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListJobsRequest.

        **参数解释：** 查询结束时间。 **约束限制：** 格式为“yyyy-mm-ddThh:mm:ssZ”。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param end_time: The end_time of this ListJobsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this ListJobsRequest.

        **参数解释：** 任务状态。 **约束限制：** 不涉及。 **取值范围：** 1、“Running”：执行中； 2、“Completed”：完成； 3、“Failed”：失败。 **默认取值:** 不涉及。

        :return: The status of this ListJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListJobsRequest.

        **参数解释：** 任务状态。 **约束限制：** 不涉及。 **取值范围：** 1、“Running”：执行中； 2、“Completed”：完成； 3、“Failed”：失败。 **默认取值:** 不涉及。

        :param status: The status of this ListJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def offset(self):
        r"""Gets the offset of this ListJobsRequest.

        **参数解释：** 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制：** 必须为数字，不能为负数。 **取值范围：** [0-4096] **默认取值:** 默认为0（偏移0条数据，表示从第一条数据开始查询）。

        :return: The offset of this ListJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListJobsRequest.

        **参数解释：** 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制：** 必须为数字，不能为负数。 **取值范围：** [0-4096] **默认取值:** 默认为0（偏移0条数据，表示从第一条数据开始查询）。

        :param offset: The offset of this ListJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListJobsRequest.

        **参数解释：** 查询记录数。 **约束限制：** 不能为负数。 **取值范围：** [1-100]。 **默认取值:** 1。

        :return: The limit of this ListJobsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListJobsRequest.

        **参数解释：** 查询记录数。 **约束限制：** 不能为负数。 **取值范围：** [1-100]。 **默认取值:** 1。

        :param limit: The limit of this ListJobsRequest.
        :type limit: str
        """
        self._limit = limit

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
        if not isinstance(other, ListJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
