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
        'instance_id': 'str',
        'instance_name': 'str',
        'status': 'str',
        'progress': 'str',
        'fail_reason': 'str',
        'created_at': 'str',
        'ended_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'status': 'status',
        'progress': 'progress',
        'fail_reason': 'fail_reason',
        'created_at': 'created_at',
        'ended_at': 'ended_at'
    }

    def __init__(self, id=None, name=None, instance_id=None, instance_name=None, status=None, progress=None, fail_reason=None, created_at=None, ended_at=None):
        r"""JobInfo

        The model defined in huaweicloud sdk

        :param id: 任务ID。
        :type id: str
        :param name: 任务名称。
        :type name: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param status: 任务状态。取值为“Running”为执行中； 取值为“Completed”为完成； 取值为“Failed” 为失败。
        :type status: str
        :param progress: 任务执行进度。 说明 执行中状态才返回执行进度，例如“60%”，表示任务执行进度为60%，否则返回“”。 任务执行进度。
        :type progress: str
        :param fail_reason: 任务执行失败时的错误信息。
        :type fail_reason: str
        :param created_at: 创建时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type created_at: str
        :param ended_at: 结束时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type ended_at: str
        """
        
        

        self._id = None
        self._name = None
        self._instance_id = None
        self._instance_name = None
        self._status = None
        self._progress = None
        self._fail_reason = None
        self._created_at = None
        self._ended_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.status = status
        self.progress = progress
        self.fail_reason = fail_reason
        self.created_at = created_at
        self.ended_at = ended_at

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
    def instance_id(self):
        r"""Gets the instance_id of this JobInfo.

        实例ID。

        :return: The instance_id of this JobInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this JobInfo.

        实例ID。

        :param instance_id: The instance_id of this JobInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this JobInfo.

        实例名称。

        :return: The instance_name of this JobInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this JobInfo.

        实例名称。

        :param instance_name: The instance_name of this JobInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def status(self):
        r"""Gets the status of this JobInfo.

        任务状态。取值为“Running”为执行中； 取值为“Completed”为完成； 取值为“Failed” 为失败。

        :return: The status of this JobInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this JobInfo.

        任务状态。取值为“Running”为执行中； 取值为“Completed”为完成； 取值为“Failed” 为失败。

        :param status: The status of this JobInfo.
        :type status: str
        """
        self._status = status

    @property
    def progress(self):
        r"""Gets the progress of this JobInfo.

        任务执行进度。 说明 执行中状态才返回执行进度，例如“60%”，表示任务执行进度为60%，否则返回“”。 任务执行进度。

        :return: The progress of this JobInfo.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this JobInfo.

        任务执行进度。 说明 执行中状态才返回执行进度，例如“60%”，表示任务执行进度为60%，否则返回“”。 任务执行进度。

        :param progress: The progress of this JobInfo.
        :type progress: str
        """
        self._progress = progress

    @property
    def fail_reason(self):
        r"""Gets the fail_reason of this JobInfo.

        任务执行失败时的错误信息。

        :return: The fail_reason of this JobInfo.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        r"""Sets the fail_reason of this JobInfo.

        任务执行失败时的错误信息。

        :param fail_reason: The fail_reason of this JobInfo.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def created_at(self):
        r"""Gets the created_at of this JobInfo.

        创建时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The created_at of this JobInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this JobInfo.

        创建时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param created_at: The created_at of this JobInfo.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def ended_at(self):
        r"""Gets the ended_at of this JobInfo.

        结束时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The ended_at of this JobInfo.
        :rtype: str
        """
        return self._ended_at

    @ended_at.setter
    def ended_at(self, ended_at):
        r"""Sets the ended_at of this JobInfo.

        结束时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param ended_at: The ended_at of this JobInfo.
        :type ended_at: str
        """
        self._ended_at = ended_at

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
