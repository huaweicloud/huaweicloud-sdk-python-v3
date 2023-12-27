# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'progress': 'str',
        'instance': 'JobInstanceInfo',
        'fail_reason': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'progress': 'progress',
        'instance': 'instance',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, id=None, name=None, status=None, start_time=None, end_time=None, progress=None, instance=None, fail_reason=None):
        """JobDetail

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: str
        :param name: 任务名称。
        :type name: str
        :param status: 任务执行状态。 取值： Running：表示任务正在执行。 Completed：表示任务执行成功。 Failed：表示任务执行失败。  枚举值： Running Completed Failed
        :type status: str
        :param start_time: 创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量[，例如北京时间偏移显示为+0800。](tag:hc)
        :type start_time: str
        :param end_time: 结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量[，例如北京时间偏移显示为+0800。](tag:hc)
        :type end_time: str
        :param progress: 任务执行进度。 &gt; 执行中状态才返回执行进度，例如“60%”，表示任务执行进度为60%，否则返回“”。
        :type progress: str
        :param instance: 
        :type instance: :class:`huaweicloudsdkgaussdbfornosql.v3.JobInstanceInfo`
        :param fail_reason: 任务执行失败时的错误信息。
        :type fail_reason: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._progress = None
        self._instance = None
        self._fail_reason = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.progress = progress
        self.instance = instance
        self.fail_reason = fail_reason

    @property
    def id(self):
        """Gets the id of this JobDetail.

        任务ID

        :return: The id of this JobDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobDetail.

        任务ID

        :param id: The id of this JobDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this JobDetail.

        任务名称。

        :return: The name of this JobDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobDetail.

        任务名称。

        :param name: The name of this JobDetail.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this JobDetail.

        任务执行状态。 取值： Running：表示任务正在执行。 Completed：表示任务执行成功。 Failed：表示任务执行失败。  枚举值： Running Completed Failed

        :return: The status of this JobDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobDetail.

        任务执行状态。 取值： Running：表示任务正在执行。 Completed：表示任务执行成功。 Failed：表示任务执行失败。  枚举值： Running Completed Failed

        :param status: The status of this JobDetail.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        """Gets the start_time of this JobDetail.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量[，例如北京时间偏移显示为+0800。](tag:hc)

        :return: The start_time of this JobDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this JobDetail.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量[，例如北京时间偏移显示为+0800。](tag:hc)

        :param start_time: The start_time of this JobDetail.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this JobDetail.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量[，例如北京时间偏移显示为+0800。](tag:hc)

        :return: The end_time of this JobDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this JobDetail.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量[，例如北京时间偏移显示为+0800。](tag:hc)

        :param end_time: The end_time of this JobDetail.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def progress(self):
        """Gets the progress of this JobDetail.

        任务执行进度。 > 执行中状态才返回执行进度，例如“60%”，表示任务执行进度为60%，否则返回“”。

        :return: The progress of this JobDetail.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this JobDetail.

        任务执行进度。 > 执行中状态才返回执行进度，例如“60%”，表示任务执行进度为60%，否则返回“”。

        :param progress: The progress of this JobDetail.
        :type progress: str
        """
        self._progress = progress

    @property
    def instance(self):
        """Gets the instance of this JobDetail.

        :return: The instance of this JobDetail.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.JobInstanceInfo`
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this JobDetail.

        :param instance: The instance of this JobDetail.
        :type instance: :class:`huaweicloudsdkgaussdbfornosql.v3.JobInstanceInfo`
        """
        self._instance = instance

    @property
    def fail_reason(self):
        """Gets the fail_reason of this JobDetail.

        任务执行失败时的错误信息。

        :return: The fail_reason of this JobDetail.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this JobDetail.

        任务执行失败时的错误信息。

        :param fail_reason: The fail_reason of this JobDetail.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

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
        if not isinstance(other, JobDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
