# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListElasticResourcePoolScaleRecordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'elastic_resource_pool_name': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'status': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'elastic_resource_pool_name': 'elastic_resource_pool_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, elastic_resource_pool_name=None, start_time=None, end_time=None, status=None, offset=None, limit=None):
        r"""ListElasticResourcePoolScaleRecordsRequest

        The model defined in huaweicloud sdk

        :param elastic_resource_pool_name: 弹性资源池名称
        :type elastic_resource_pool_name: str
        :param start_time: start_time用于查询扩缩容历史的开始时间，该时间点需大于当前时间点减30天，必须小于end_time 。时间格式为unix时间戳，单位：毫秒。 ①若start_time为空，则查询end_time前七天到end_time的数据（end_time最大不能大于当前时间30天）。 ②查询当前时间点前15天到当前时间点的数据（start_time和end_time同时为空）。
        :type start_time: int
        :param end_time: end_time用于查询扩缩容历史的结束时间，该时间点不能小于开始时间，不能大于当前时间。时间格式为unix时间戳，单位：毫秒。 ①若end_time为空，则查询start_time到当前时间点的数据。 ②查询当前时间点前15天到当前时间的数据（start_time和end_time同时为空）。
        :type end_time: int
        :param status: 弹性资源池扩缩容的状态
        :type status: str
        :param offset: 偏移量
        :type offset: int
        :param limit: 当前分页条数
        :type limit: int
        """
        
        

        self._elastic_resource_pool_name = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.elastic_resource_pool_name = elastic_resource_pool_name
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
    def elastic_resource_pool_name(self):
        r"""Gets the elastic_resource_pool_name of this ListElasticResourcePoolScaleRecordsRequest.

        弹性资源池名称

        :return: The elastic_resource_pool_name of this ListElasticResourcePoolScaleRecordsRequest.
        :rtype: str
        """
        return self._elastic_resource_pool_name

    @elastic_resource_pool_name.setter
    def elastic_resource_pool_name(self, elastic_resource_pool_name):
        r"""Sets the elastic_resource_pool_name of this ListElasticResourcePoolScaleRecordsRequest.

        弹性资源池名称

        :param elastic_resource_pool_name: The elastic_resource_pool_name of this ListElasticResourcePoolScaleRecordsRequest.
        :type elastic_resource_pool_name: str
        """
        self._elastic_resource_pool_name = elastic_resource_pool_name

    @property
    def start_time(self):
        r"""Gets the start_time of this ListElasticResourcePoolScaleRecordsRequest.

        start_time用于查询扩缩容历史的开始时间，该时间点需大于当前时间点减30天，必须小于end_time 。时间格式为unix时间戳，单位：毫秒。 ①若start_time为空，则查询end_time前七天到end_time的数据（end_time最大不能大于当前时间30天）。 ②查询当前时间点前15天到当前时间点的数据（start_time和end_time同时为空）。

        :return: The start_time of this ListElasticResourcePoolScaleRecordsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListElasticResourcePoolScaleRecordsRequest.

        start_time用于查询扩缩容历史的开始时间，该时间点需大于当前时间点减30天，必须小于end_time 。时间格式为unix时间戳，单位：毫秒。 ①若start_time为空，则查询end_time前七天到end_time的数据（end_time最大不能大于当前时间30天）。 ②查询当前时间点前15天到当前时间点的数据（start_time和end_time同时为空）。

        :param start_time: The start_time of this ListElasticResourcePoolScaleRecordsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListElasticResourcePoolScaleRecordsRequest.

        end_time用于查询扩缩容历史的结束时间，该时间点不能小于开始时间，不能大于当前时间。时间格式为unix时间戳，单位：毫秒。 ①若end_time为空，则查询start_time到当前时间点的数据。 ②查询当前时间点前15天到当前时间的数据（start_time和end_time同时为空）。

        :return: The end_time of this ListElasticResourcePoolScaleRecordsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListElasticResourcePoolScaleRecordsRequest.

        end_time用于查询扩缩容历史的结束时间，该时间点不能小于开始时间，不能大于当前时间。时间格式为unix时间戳，单位：毫秒。 ①若end_time为空，则查询start_time到当前时间点的数据。 ②查询当前时间点前15天到当前时间的数据（start_time和end_time同时为空）。

        :param end_time: The end_time of this ListElasticResourcePoolScaleRecordsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this ListElasticResourcePoolScaleRecordsRequest.

        弹性资源池扩缩容的状态

        :return: The status of this ListElasticResourcePoolScaleRecordsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListElasticResourcePoolScaleRecordsRequest.

        弹性资源池扩缩容的状态

        :param status: The status of this ListElasticResourcePoolScaleRecordsRequest.
        :type status: str
        """
        self._status = status

    @property
    def offset(self):
        r"""Gets the offset of this ListElasticResourcePoolScaleRecordsRequest.

        偏移量

        :return: The offset of this ListElasticResourcePoolScaleRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListElasticResourcePoolScaleRecordsRequest.

        偏移量

        :param offset: The offset of this ListElasticResourcePoolScaleRecordsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListElasticResourcePoolScaleRecordsRequest.

        当前分页条数

        :return: The limit of this ListElasticResourcePoolScaleRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListElasticResourcePoolScaleRecordsRequest.

        当前分页条数

        :param limit: The limit of this ListElasticResourcePoolScaleRecordsRequest.
        :type limit: int
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
        if not isinstance(other, ListElasticResourcePoolScaleRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
