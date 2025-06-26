# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Job:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'policy_id': 'int',
        'event_type': 'str',
        'notify_type': 'str',
        'status': 'str',
        'status_text': 'str',
        'job_detail': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'policy_id': 'policy_id',
        'event_type': 'event_type',
        'notify_type': 'notify_type',
        'status': 'status',
        'status_text': 'status_text',
        'job_detail': 'job_detail',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, policy_id=None, event_type=None, notify_type=None, status=None, status_text=None, job_detail=None, created_at=None, updated_at=None):
        r"""Job

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: int
        :param policy_id: 触发器策略ID
        :type policy_id: int
        :param event_type: 事件类型
        :type event_type: str
        :param notify_type: 通知类型
        :type notify_type: str
        :param status: 任务状态
        :type status: str
        :param status_text: 状态原因
        :type status_text: str
        :param job_detail: 任务详情
        :type job_detail: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        """
        
        

        self._id = None
        self._policy_id = None
        self._event_type = None
        self._notify_type = None
        self._status = None
        self._status_text = None
        self._job_detail = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.policy_id = policy_id
        self.event_type = event_type
        self.notify_type = notify_type
        self.status = status
        self.status_text = status_text
        self.job_detail = job_detail
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this Job.

        任务ID

        :return: The id of this Job.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Job.

        任务ID

        :param id: The id of this Job.
        :type id: int
        """
        self._id = id

    @property
    def policy_id(self):
        r"""Gets the policy_id of this Job.

        触发器策略ID

        :return: The policy_id of this Job.
        :rtype: int
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this Job.

        触发器策略ID

        :param policy_id: The policy_id of this Job.
        :type policy_id: int
        """
        self._policy_id = policy_id

    @property
    def event_type(self):
        r"""Gets the event_type of this Job.

        事件类型

        :return: The event_type of this Job.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this Job.

        事件类型

        :param event_type: The event_type of this Job.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def notify_type(self):
        r"""Gets the notify_type of this Job.

        通知类型

        :return: The notify_type of this Job.
        :rtype: str
        """
        return self._notify_type

    @notify_type.setter
    def notify_type(self, notify_type):
        r"""Sets the notify_type of this Job.

        通知类型

        :param notify_type: The notify_type of this Job.
        :type notify_type: str
        """
        self._notify_type = notify_type

    @property
    def status(self):
        r"""Gets the status of this Job.

        任务状态

        :return: The status of this Job.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Job.

        任务状态

        :param status: The status of this Job.
        :type status: str
        """
        self._status = status

    @property
    def status_text(self):
        r"""Gets the status_text of this Job.

        状态原因

        :return: The status_text of this Job.
        :rtype: str
        """
        return self._status_text

    @status_text.setter
    def status_text(self, status_text):
        r"""Sets the status_text of this Job.

        状态原因

        :param status_text: The status_text of this Job.
        :type status_text: str
        """
        self._status_text = status_text

    @property
    def job_detail(self):
        r"""Gets the job_detail of this Job.

        任务详情

        :return: The job_detail of this Job.
        :rtype: str
        """
        return self._job_detail

    @job_detail.setter
    def job_detail(self, job_detail):
        r"""Sets the job_detail of this Job.

        任务详情

        :param job_detail: The job_detail of this Job.
        :type job_detail: str
        """
        self._job_detail = job_detail

    @property
    def created_at(self):
        r"""Gets the created_at of this Job.

        创建时间

        :return: The created_at of this Job.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Job.

        创建时间

        :param created_at: The created_at of this Job.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Job.

        更新时间

        :return: The updated_at of this Job.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Job.

        更新时间

        :param updated_at: The updated_at of this Job.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
