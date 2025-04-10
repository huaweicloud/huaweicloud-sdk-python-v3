# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSlowLogsRequest:

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
        'offset': 'int',
        'limit': 'int',
        'start_date': 'str',
        'end_date': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'start_date': 'start_date',
        'end_date': 'end_date'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, start_date=None, end_date=None):
        r"""ListSlowLogsRequest

        The model defined in huaweicloud sdk

        :param instance_id: DDM实例ID。
        :type instance_id: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0。取值必须为数字，且不能为负数。
        :type offset: int
        :param limit: 分页参数：每页多少条。
        :type limit: int
        :param start_date: 开始时间，UTC time，精确到毫秒。
        :type start_date: str
        :param end_date: 结束时间，UTC time，精确到毫秒。结束时间与开始时间，间隔不能超过7天。
        :type end_date: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.start_date = start_date
        self.end_date = end_date

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListSlowLogsRequest.

        DDM实例ID。

        :return: The instance_id of this ListSlowLogsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListSlowLogsRequest.

        DDM实例ID。

        :param instance_id: The instance_id of this ListSlowLogsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ListSlowLogsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0。取值必须为数字，且不能为负数。

        :return: The offset of this ListSlowLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSlowLogsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0。取值必须为数字，且不能为负数。

        :param offset: The offset of this ListSlowLogsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSlowLogsRequest.

        分页参数：每页多少条。

        :return: The limit of this ListSlowLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSlowLogsRequest.

        分页参数：每页多少条。

        :param limit: The limit of this ListSlowLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def start_date(self):
        r"""Gets the start_date of this ListSlowLogsRequest.

        开始时间，UTC time，精确到毫秒。

        :return: The start_date of this ListSlowLogsRequest.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this ListSlowLogsRequest.

        开始时间，UTC time，精确到毫秒。

        :param start_date: The start_date of this ListSlowLogsRequest.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        r"""Gets the end_date of this ListSlowLogsRequest.

        结束时间，UTC time，精确到毫秒。结束时间与开始时间，间隔不能超过7天。

        :return: The end_date of this ListSlowLogsRequest.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        r"""Sets the end_date of this ListSlowLogsRequest.

        结束时间，UTC time，精确到毫秒。结束时间与开始时间，间隔不能超过7天。

        :param end_date: The end_date of this ListSlowLogsRequest.
        :type end_date: str
        """
        self._end_date = end_date

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
        if not isinstance(other, ListSlowLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
