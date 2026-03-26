# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobRunBriefInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job': 'JobRef',
        'name': 'str',
        'endpoint_id': 'str',
        'id': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'status': 'StatusEnum',
        'duration': 'int',
        'type': 'JobType',
        'create_user': 'User'
    }

    attribute_map = {
        'job': 'job',
        'name': 'name',
        'endpoint_id': 'endpoint_id',
        'id': 'id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'status': 'status',
        'duration': 'duration',
        'type': 'type',
        'create_user': 'create_user'
    }

    def __init__(self, job=None, name=None, endpoint_id=None, id=None, create_time=None, update_time=None, status=None, duration=None, type=None, create_user=None):
        r"""JobRunBriefInfo

        The model defined in huaweicloud sdk

        :param job: 
        :type job: :class:`huaweicloudsdkdataartsfabricep.v1.JobRef`
        :param name: 作业运行的名称，只能包含中文、字母、数字、下划线、中划线、点、空格
        :type name: str
        :param endpoint_id: endpoint空间id
        :type endpoint_id: str
        :param id: 一种资源ID，32~36位的英文、数字、短横组合
        :type id: str
        :param create_time: 创建时间
        :type create_time: datetime
        :param update_time: 更新时间
        :type update_time: datetime
        :param status: 
        :type status: :class:`huaweicloudsdkdataartsfabricep.v1.StatusEnum`
        :param duration: 运行时间
        :type duration: int
        :param type: 
        :type type: :class:`huaweicloudsdkdataartsfabricep.v1.JobType`
        :param create_user: 
        :type create_user: :class:`huaweicloudsdkdataartsfabricep.v1.User`
        """
        
        

        self._job = None
        self._name = None
        self._endpoint_id = None
        self._id = None
        self._create_time = None
        self._update_time = None
        self._status = None
        self._duration = None
        self._type = None
        self._create_user = None
        self.discriminator = None

        self.job = job
        self.name = name
        self.endpoint_id = endpoint_id
        self.id = id
        self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        self.status = status
        if duration is not None:
            self.duration = duration
        if type is not None:
            self.type = type
        if create_user is not None:
            self.create_user = create_user

    @property
    def job(self):
        r"""Gets the job of this JobRunBriefInfo.

        :return: The job of this JobRunBriefInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.JobRef`
        """
        return self._job

    @job.setter
    def job(self, job):
        r"""Sets the job of this JobRunBriefInfo.

        :param job: The job of this JobRunBriefInfo.
        :type job: :class:`huaweicloudsdkdataartsfabricep.v1.JobRef`
        """
        self._job = job

    @property
    def name(self):
        r"""Gets the name of this JobRunBriefInfo.

        作业运行的名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :return: The name of this JobRunBriefInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobRunBriefInfo.

        作业运行的名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :param name: The name of this JobRunBriefInfo.
        :type name: str
        """
        self._name = name

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this JobRunBriefInfo.

        endpoint空间id

        :return: The endpoint_id of this JobRunBriefInfo.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this JobRunBriefInfo.

        endpoint空间id

        :param endpoint_id: The endpoint_id of this JobRunBriefInfo.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def id(self):
        r"""Gets the id of this JobRunBriefInfo.

        一种资源ID，32~36位的英文、数字、短横组合

        :return: The id of this JobRunBriefInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this JobRunBriefInfo.

        一种资源ID，32~36位的英文、数字、短横组合

        :param id: The id of this JobRunBriefInfo.
        :type id: str
        """
        self._id = id

    @property
    def create_time(self):
        r"""Gets the create_time of this JobRunBriefInfo.

        创建时间

        :return: The create_time of this JobRunBriefInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this JobRunBriefInfo.

        创建时间

        :param create_time: The create_time of this JobRunBriefInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this JobRunBriefInfo.

        更新时间

        :return: The update_time of this JobRunBriefInfo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this JobRunBriefInfo.

        更新时间

        :param update_time: The update_time of this JobRunBriefInfo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def status(self):
        r"""Gets the status of this JobRunBriefInfo.

        :return: The status of this JobRunBriefInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.StatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this JobRunBriefInfo.

        :param status: The status of this JobRunBriefInfo.
        :type status: :class:`huaweicloudsdkdataartsfabricep.v1.StatusEnum`
        """
        self._status = status

    @property
    def duration(self):
        r"""Gets the duration of this JobRunBriefInfo.

        运行时间

        :return: The duration of this JobRunBriefInfo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this JobRunBriefInfo.

        运行时间

        :param duration: The duration of this JobRunBriefInfo.
        :type duration: int
        """
        self._duration = duration

    @property
    def type(self):
        r"""Gets the type of this JobRunBriefInfo.

        :return: The type of this JobRunBriefInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.JobType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this JobRunBriefInfo.

        :param type: The type of this JobRunBriefInfo.
        :type type: :class:`huaweicloudsdkdataartsfabricep.v1.JobType`
        """
        self._type = type

    @property
    def create_user(self):
        r"""Gets the create_user of this JobRunBriefInfo.

        :return: The create_user of this JobRunBriefInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.User`
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this JobRunBriefInfo.

        :param create_user: The create_user of this JobRunBriefInfo.
        :type create_user: :class:`huaweicloudsdkdataartsfabricep.v1.User`
        """
        self._create_user = create_user

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
        if not isinstance(other, JobRunBriefInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
