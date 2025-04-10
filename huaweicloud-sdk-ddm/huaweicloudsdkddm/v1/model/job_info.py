# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobInfo:

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
        'created_time': 'str',
        'end_time': 'str',
        'process': 'str',
        'instance': 'Instance'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'created_time': 'created_time',
        'end_time': 'end_time',
        'process': 'process',
        'instance': 'instance'
    }

    def __init__(self, id=None, name=None, status=None, created_time=None, end_time=None, process=None, instance=None):
        r"""JobInfo

        The model defined in huaweicloud sdk

        :param id: 任务ID。
        :type id: str
        :param name: 任务名称。
        :type name: str
        :param status: 任务执行状态。  取值： 值为“Running”，表示任务正在执行。 值为“Completed”，表示任务执行成功。 值为“Failed”，表示任务执行失败。
        :type status: str
        :param created_time: 创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type created_time: str
        :param end_time: 结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type end_time: str
        :param process: 任务执行进度。  执行中状态才返回执行进度，例如“60%”，表示任务执行进度为60%，否则返回“”。
        :type process: str
        :param instance: 
        :type instance: :class:`huaweicloudsdkddm.v1.Instance`
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._created_time = None
        self._end_time = None
        self._process = None
        self._instance = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.created_time = created_time
        self.end_time = end_time
        if process is not None:
            self.process = process
        self.instance = instance

    @property
    def id(self):
        r"""Gets the id of this JobInfo.

        任务ID。

        :return: The id of this JobInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this JobInfo.

        任务ID。

        :param id: The id of this JobInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this JobInfo.

        任务名称。

        :return: The name of this JobInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobInfo.

        任务名称。

        :param name: The name of this JobInfo.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this JobInfo.

        任务执行状态。  取值： 值为“Running”，表示任务正在执行。 值为“Completed”，表示任务执行成功。 值为“Failed”，表示任务执行失败。

        :return: The status of this JobInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this JobInfo.

        任务执行状态。  取值： 值为“Running”，表示任务正在执行。 值为“Completed”，表示任务执行成功。 值为“Failed”，表示任务执行失败。

        :param status: The status of this JobInfo.
        :type status: str
        """
        self._status = status

    @property
    def created_time(self):
        r"""Gets the created_time of this JobInfo.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The created_time of this JobInfo.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this JobInfo.

        创建时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param created_time: The created_time of this JobInfo.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def end_time(self):
        r"""Gets the end_time of this JobInfo.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The end_time of this JobInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this JobInfo.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param end_time: The end_time of this JobInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def process(self):
        r"""Gets the process of this JobInfo.

        任务执行进度。  执行中状态才返回执行进度，例如“60%”，表示任务执行进度为60%，否则返回“”。

        :return: The process of this JobInfo.
        :rtype: str
        """
        return self._process

    @process.setter
    def process(self, process):
        r"""Sets the process of this JobInfo.

        任务执行进度。  执行中状态才返回执行进度，例如“60%”，表示任务执行进度为60%，否则返回“”。

        :param process: The process of this JobInfo.
        :type process: str
        """
        self._process = process

    @property
    def instance(self):
        r"""Gets the instance of this JobInfo.

        :return: The instance of this JobInfo.
        :rtype: :class:`huaweicloudsdkddm.v1.Instance`
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        r"""Sets the instance of this JobInfo.

        :param instance: The instance of this JobInfo.
        :type instance: :class:`huaweicloudsdkddm.v1.Instance`
        """
        self._instance = instance

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
        if not isinstance(other, JobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
