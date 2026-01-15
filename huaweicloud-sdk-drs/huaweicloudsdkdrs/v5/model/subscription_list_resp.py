# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionListResp:

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
        'create_time': 'str',
        'begin_time': 'str',
        'description': 'str',
        'now_time': 'str',
        'job_action': 'JobActions',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'create_time': 'create_time',
        'begin_time': 'begin_time',
        'description': 'description',
        'now_time': 'now_time',
        'job_action': 'job_action',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, name=None, status=None, create_time=None, begin_time=None, description=None, now_time=None, job_action=None, enterprise_project_id=None):
        r"""SubscriptionListResp

        The model defined in huaweicloud sdk

        :param id: 任务ID。
        :type id: str
        :param name: 任务名称。
        :type name: str
        :param status: 任务状态。
        :type status: str
        :param create_time: 任务创建时间。
        :type create_time: str
        :param begin_time: 消费开始时间。
        :type begin_time: str
        :param description: 任务描述。
        :type description: str
        :param now_time: 当前时间。
        :type now_time: str
        :param job_action: 
        :type job_action: :class:`huaweicloudsdkdrs.v5.JobActions`
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._create_time = None
        self._begin_time = None
        self._description = None
        self._now_time = None
        self._job_action = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.create_time = create_time
        self.begin_time = begin_time
        self.description = description
        self.now_time = now_time
        self.job_action = job_action
        self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        r"""Gets the id of this SubscriptionListResp.

        任务ID。

        :return: The id of this SubscriptionListResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SubscriptionListResp.

        任务ID。

        :param id: The id of this SubscriptionListResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SubscriptionListResp.

        任务名称。

        :return: The name of this SubscriptionListResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SubscriptionListResp.

        任务名称。

        :param name: The name of this SubscriptionListResp.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this SubscriptionListResp.

        任务状态。

        :return: The status of this SubscriptionListResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SubscriptionListResp.

        任务状态。

        :param status: The status of this SubscriptionListResp.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this SubscriptionListResp.

        任务创建时间。

        :return: The create_time of this SubscriptionListResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SubscriptionListResp.

        任务创建时间。

        :param create_time: The create_time of this SubscriptionListResp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def begin_time(self):
        r"""Gets the begin_time of this SubscriptionListResp.

        消费开始时间。

        :return: The begin_time of this SubscriptionListResp.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this SubscriptionListResp.

        消费开始时间。

        :param begin_time: The begin_time of this SubscriptionListResp.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def description(self):
        r"""Gets the description of this SubscriptionListResp.

        任务描述。

        :return: The description of this SubscriptionListResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SubscriptionListResp.

        任务描述。

        :param description: The description of this SubscriptionListResp.
        :type description: str
        """
        self._description = description

    @property
    def now_time(self):
        r"""Gets the now_time of this SubscriptionListResp.

        当前时间。

        :return: The now_time of this SubscriptionListResp.
        :rtype: str
        """
        return self._now_time

    @now_time.setter
    def now_time(self, now_time):
        r"""Sets the now_time of this SubscriptionListResp.

        当前时间。

        :param now_time: The now_time of this SubscriptionListResp.
        :type now_time: str
        """
        self._now_time = now_time

    @property
    def job_action(self):
        r"""Gets the job_action of this SubscriptionListResp.

        :return: The job_action of this SubscriptionListResp.
        :rtype: :class:`huaweicloudsdkdrs.v5.JobActions`
        """
        return self._job_action

    @job_action.setter
    def job_action(self, job_action):
        r"""Sets the job_action of this SubscriptionListResp.

        :param job_action: The job_action of this SubscriptionListResp.
        :type job_action: :class:`huaweicloudsdkdrs.v5.JobActions`
        """
        self._job_action = job_action

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this SubscriptionListResp.

        企业项目ID。

        :return: The enterprise_project_id of this SubscriptionListResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this SubscriptionListResp.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this SubscriptionListResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SubscriptionListResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
