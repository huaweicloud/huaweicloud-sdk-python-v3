# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProcessesAuditLogRequest:

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
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, start_time=None, end_time=None):
        r"""ShowProcessesAuditLogRequest

        The model defined in huaweicloud sdk

        :param instance_id: DDM实例ID或关联RDS的ID。
        :type instance_id: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0。取值必须为数字，且不能为负数。
        :type offset: int
        :param limit: 查询个数上限值。取值范围：1~128。不传该参数时，默认值为10。
        :type limit: int
        :param start_time: 开始时间，UTC time，精确到毫秒。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type start_time: str
        :param end_time: 结束时间，UTC time，精确到毫秒。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。结束时间与开始时间，间隔不能超过7天。
        :type end_time: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.start_time = start_time
        self.end_time = end_time

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowProcessesAuditLogRequest.

        DDM实例ID或关联RDS的ID。

        :return: The instance_id of this ShowProcessesAuditLogRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowProcessesAuditLogRequest.

        DDM实例ID或关联RDS的ID。

        :param instance_id: The instance_id of this ShowProcessesAuditLogRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ShowProcessesAuditLogRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0。取值必须为数字，且不能为负数。

        :return: The offset of this ShowProcessesAuditLogRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowProcessesAuditLogRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0。取值必须为数字，且不能为负数。

        :param offset: The offset of this ShowProcessesAuditLogRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowProcessesAuditLogRequest.

        查询个数上限值。取值范围：1~128。不传该参数时，默认值为10。

        :return: The limit of this ShowProcessesAuditLogRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowProcessesAuditLogRequest.

        查询个数上限值。取值范围：1~128。不传该参数时，默认值为10。

        :param limit: The limit of this ShowProcessesAuditLogRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowProcessesAuditLogRequest.

        开始时间，UTC time，精确到毫秒。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The start_time of this ShowProcessesAuditLogRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowProcessesAuditLogRequest.

        开始时间，UTC time，精确到毫秒。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param start_time: The start_time of this ShowProcessesAuditLogRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowProcessesAuditLogRequest.

        结束时间，UTC time，精确到毫秒。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。结束时间与开始时间，间隔不能超过7天。

        :return: The end_time of this ShowProcessesAuditLogRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowProcessesAuditLogRequest.

        结束时间，UTC time，精确到毫秒。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。结束时间与开始时间，间隔不能超过7天。

        :param end_time: The end_time of this ShowProcessesAuditLogRequest.
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
        if not isinstance(other, ShowProcessesAuditLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
