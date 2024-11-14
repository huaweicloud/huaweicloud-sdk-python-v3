# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNosqlTaskListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_name': 'str',
        'job_status': 'str',
        'instance_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'offset': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'job_name': 'job_name',
        'job_status': 'job_status',
        'instance_id': 'instance_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, job_name=None, job_status=None, instance_id=None, start_time=None, end_time=None, offset=None, limit=None):
        """ListNosqlTaskListRequest

        The model defined in huaweicloud sdk

        :param job_name: 任务名称，默认为空。对应取值如下：  \&quot;REBOOT\&quot;：重启实例  \&quot;RESIZE_FLAVOR\&quot;：变更实例的CPU和内存规格  \&quot;UPGRADE_DATABASE\&quot;：补丁升级
        :type job_name: str
        :param job_status: 任务执行状态，默认为空。 取值：  值为\&quot;Pending\&quot;，表示任务未执行。  值为\&quot;Running\&quot;，表示任务正在执行。  值为\&quot;Completed\&quot;，表示任务执行成功。  值为\&quot;Failed\&quot;，表示任务执行失败。  值为\&quot;Canceled\&quot;，表示任务取消执行。
        :type job_status: str
        :param instance_id: 实例ID，不传该值默认查所有符合条件的实例。
        :type instance_id: str
        :param start_time: 任务创建起始时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100，不传默认为当前时间前七天。
        :type start_time: str
        :param end_time: 任务创建结束时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100，不传默认为当前时间。
        :type end_time: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0。
        :type offset: str
        :param limit: 查询记录数。不传该参数时，默认为10,取值范围1-100。
        :type limit: str
        """
        
        

        self._job_name = None
        self._job_status = None
        self._instance_id = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if job_name is not None:
            self.job_name = job_name
        if job_status is not None:
            self.job_status = job_status
        if instance_id is not None:
            self.instance_id = instance_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def job_name(self):
        """Gets the job_name of this ListNosqlTaskListRequest.

        任务名称，默认为空。对应取值如下：  \"REBOOT\"：重启实例  \"RESIZE_FLAVOR\"：变更实例的CPU和内存规格  \"UPGRADE_DATABASE\"：补丁升级

        :return: The job_name of this ListNosqlTaskListRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ListNosqlTaskListRequest.

        任务名称，默认为空。对应取值如下：  \"REBOOT\"：重启实例  \"RESIZE_FLAVOR\"：变更实例的CPU和内存规格  \"UPGRADE_DATABASE\"：补丁升级

        :param job_name: The job_name of this ListNosqlTaskListRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_status(self):
        """Gets the job_status of this ListNosqlTaskListRequest.

        任务执行状态，默认为空。 取值：  值为\"Pending\"，表示任务未执行。  值为\"Running\"，表示任务正在执行。  值为\"Completed\"，表示任务执行成功。  值为\"Failed\"，表示任务执行失败。  值为\"Canceled\"，表示任务取消执行。

        :return: The job_status of this ListNosqlTaskListRequest.
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this ListNosqlTaskListRequest.

        任务执行状态，默认为空。 取值：  值为\"Pending\"，表示任务未执行。  值为\"Running\"，表示任务正在执行。  值为\"Completed\"，表示任务执行成功。  值为\"Failed\"，表示任务执行失败。  值为\"Canceled\"，表示任务取消执行。

        :param job_status: The job_status of this ListNosqlTaskListRequest.
        :type job_status: str
        """
        self._job_status = job_status

    @property
    def instance_id(self):
        """Gets the instance_id of this ListNosqlTaskListRequest.

        实例ID，不传该值默认查所有符合条件的实例。

        :return: The instance_id of this ListNosqlTaskListRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListNosqlTaskListRequest.

        实例ID，不传该值默认查所有符合条件的实例。

        :param instance_id: The instance_id of this ListNosqlTaskListRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_time(self):
        """Gets the start_time of this ListNosqlTaskListRequest.

        任务创建起始时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100，不传默认为当前时间前七天。

        :return: The start_time of this ListNosqlTaskListRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListNosqlTaskListRequest.

        任务创建起始时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100，不传默认为当前时间前七天。

        :param start_time: The start_time of this ListNosqlTaskListRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListNosqlTaskListRequest.

        任务创建结束时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100，不传默认为当前时间。

        :return: The end_time of this ListNosqlTaskListRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListNosqlTaskListRequest.

        任务创建结束时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100，不传默认为当前时间。

        :param end_time: The end_time of this ListNosqlTaskListRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        """Gets the offset of this ListNosqlTaskListRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0。

        :return: The offset of this ListNosqlTaskListRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListNosqlTaskListRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0。

        :param offset: The offset of this ListNosqlTaskListRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListNosqlTaskListRequest.

        查询记录数。不传该参数时，默认为10,取值范围1-100。

        :return: The limit of this ListNosqlTaskListRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListNosqlTaskListRequest.

        查询记录数。不传该参数时，默认为10,取值范围1-100。

        :param limit: The limit of this ListNosqlTaskListRequest.
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
        if not isinstance(other, ListNosqlTaskListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
