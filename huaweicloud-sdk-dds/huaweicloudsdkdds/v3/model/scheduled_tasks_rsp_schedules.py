# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduledTasksRspSchedules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'job_name': 'str',
        'job_status': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_status': 'str',
        'create_time': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_name': 'job_name',
        'job_status': 'job_status',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'instance_status': 'instance_status',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, job_id=None, job_name=None, job_status=None, instance_id=None, instance_name=None, instance_status=None, create_time=None, start_time=None, end_time=None):
        r"""ScheduledTasksRspSchedules

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param job_name: 任务名称。对应取值如下：   \&quot;RESIZE_FLAVOR\&quot;：变更实例的CPU和内存规格
        :type job_name: str
        :param job_status: 任务执行状态。 取值：  值为\&quot;Running\&quot;，表示任务正在执行。  值为\&quot;Completed\&quot;，表示任务执行成功。  值为\&quot;Failed\&quot;，表示任务执行失败。  值为\&quot;Pending\&quot;，表示任务未执行。
        :type job_status: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param instance_status: 实例状态。 取值：  值为“createfail”，表示实例创建失败。  值为“creating”，表示实例创建中。  值为“normal”，表示实例正常。  值为“abnormal”，表示实例异常。  值为“deleted”，表示实例已删除。
        :type instance_status: str
        :param create_time: 任务创建时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type create_time: str
        :param start_time: 任务开始时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type start_time: str
        :param end_time: 任务结束时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type end_time: str
        """
        
        

        self._job_id = None
        self._job_name = None
        self._job_status = None
        self._instance_id = None
        self._instance_name = None
        self._instance_status = None
        self._create_time = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if job_status is not None:
            self.job_status = job_status
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_status is not None:
            self.instance_status = instance_status
        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def job_id(self):
        r"""Gets the job_id of this ScheduledTasksRspSchedules.

        任务ID。

        :return: The job_id of this ScheduledTasksRspSchedules.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ScheduledTasksRspSchedules.

        任务ID。

        :param job_id: The job_id of this ScheduledTasksRspSchedules.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        r"""Gets the job_name of this ScheduledTasksRspSchedules.

        任务名称。对应取值如下：   \"RESIZE_FLAVOR\"：变更实例的CPU和内存规格

        :return: The job_name of this ScheduledTasksRspSchedules.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ScheduledTasksRspSchedules.

        任务名称。对应取值如下：   \"RESIZE_FLAVOR\"：变更实例的CPU和内存规格

        :param job_name: The job_name of this ScheduledTasksRspSchedules.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_status(self):
        r"""Gets the job_status of this ScheduledTasksRspSchedules.

        任务执行状态。 取值：  值为\"Running\"，表示任务正在执行。  值为\"Completed\"，表示任务执行成功。  值为\"Failed\"，表示任务执行失败。  值为\"Pending\"，表示任务未执行。

        :return: The job_status of this ScheduledTasksRspSchedules.
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        r"""Sets the job_status of this ScheduledTasksRspSchedules.

        任务执行状态。 取值：  值为\"Running\"，表示任务正在执行。  值为\"Completed\"，表示任务执行成功。  值为\"Failed\"，表示任务执行失败。  值为\"Pending\"，表示任务未执行。

        :param job_status: The job_status of this ScheduledTasksRspSchedules.
        :type job_status: str
        """
        self._job_status = job_status

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ScheduledTasksRspSchedules.

        实例ID。

        :return: The instance_id of this ScheduledTasksRspSchedules.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ScheduledTasksRspSchedules.

        实例ID。

        :param instance_id: The instance_id of this ScheduledTasksRspSchedules.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ScheduledTasksRspSchedules.

        实例名称。

        :return: The instance_name of this ScheduledTasksRspSchedules.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ScheduledTasksRspSchedules.

        实例名称。

        :param instance_name: The instance_name of this ScheduledTasksRspSchedules.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_status(self):
        r"""Gets the instance_status of this ScheduledTasksRspSchedules.

        实例状态。 取值：  值为“createfail”，表示实例创建失败。  值为“creating”，表示实例创建中。  值为“normal”，表示实例正常。  值为“abnormal”，表示实例异常。  值为“deleted”，表示实例已删除。

        :return: The instance_status of this ScheduledTasksRspSchedules.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this ScheduledTasksRspSchedules.

        实例状态。 取值：  值为“createfail”，表示实例创建失败。  值为“creating”，表示实例创建中。  值为“normal”，表示实例正常。  值为“abnormal”，表示实例异常。  值为“deleted”，表示实例已删除。

        :param instance_status: The instance_status of this ScheduledTasksRspSchedules.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def create_time(self):
        r"""Gets the create_time of this ScheduledTasksRspSchedules.

        任务创建时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The create_time of this ScheduledTasksRspSchedules.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ScheduledTasksRspSchedules.

        任务创建时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param create_time: The create_time of this ScheduledTasksRspSchedules.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def start_time(self):
        r"""Gets the start_time of this ScheduledTasksRspSchedules.

        任务开始时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The start_time of this ScheduledTasksRspSchedules.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ScheduledTasksRspSchedules.

        任务开始时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param start_time: The start_time of this ScheduledTasksRspSchedules.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ScheduledTasksRspSchedules.

        任务结束时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The end_time of this ScheduledTasksRspSchedules.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ScheduledTasksRspSchedules.

        任务结束时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param end_time: The end_time of this ScheduledTasksRspSchedules.
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
        if not isinstance(other, ScheduledTasksRspSchedules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
