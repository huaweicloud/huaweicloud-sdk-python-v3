# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubTrainingJobInfoDto:

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
        'sub_job_type': 'str',
        'heart_beat_id': 'str',
        'state': 'str',
        'create_time': 'int',
        'last_update_time': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'sub_job_type': 'sub_job_type',
        'heart_beat_id': 'heart_beat_id',
        'state': 'state',
        'create_time': 'create_time',
        'last_update_time': 'last_update_time'
    }

    def __init__(self, job_id=None, sub_job_type=None, heart_beat_id=None, state=None, create_time=None, last_update_time=None):
        r"""SubTrainingJobInfoDto

        The model defined in huaweicloud sdk

        :param job_id: 任务id
        :type job_id: str
        :param sub_job_type: 子任务类型
        :type sub_job_type: str
        :param heart_beat_id: 子任务心跳id
        :type heart_beat_id: str
        :param state: 任务状态
        :type state: str
        :param create_time: 创建时间
        :type create_time: int
        :param last_update_time: 最后更新时间
        :type last_update_time: int
        """
        
        

        self._job_id = None
        self._sub_job_type = None
        self._heart_beat_id = None
        self._state = None
        self._create_time = None
        self._last_update_time = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if sub_job_type is not None:
            self.sub_job_type = sub_job_type
        if heart_beat_id is not None:
            self.heart_beat_id = heart_beat_id
        if state is not None:
            self.state = state
        if create_time is not None:
            self.create_time = create_time
        if last_update_time is not None:
            self.last_update_time = last_update_time

    @property
    def job_id(self):
        r"""Gets the job_id of this SubTrainingJobInfoDto.

        任务id

        :return: The job_id of this SubTrainingJobInfoDto.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this SubTrainingJobInfoDto.

        任务id

        :param job_id: The job_id of this SubTrainingJobInfoDto.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def sub_job_type(self):
        r"""Gets the sub_job_type of this SubTrainingJobInfoDto.

        子任务类型

        :return: The sub_job_type of this SubTrainingJobInfoDto.
        :rtype: str
        """
        return self._sub_job_type

    @sub_job_type.setter
    def sub_job_type(self, sub_job_type):
        r"""Sets the sub_job_type of this SubTrainingJobInfoDto.

        子任务类型

        :param sub_job_type: The sub_job_type of this SubTrainingJobInfoDto.
        :type sub_job_type: str
        """
        self._sub_job_type = sub_job_type

    @property
    def heart_beat_id(self):
        r"""Gets the heart_beat_id of this SubTrainingJobInfoDto.

        子任务心跳id

        :return: The heart_beat_id of this SubTrainingJobInfoDto.
        :rtype: str
        """
        return self._heart_beat_id

    @heart_beat_id.setter
    def heart_beat_id(self, heart_beat_id):
        r"""Sets the heart_beat_id of this SubTrainingJobInfoDto.

        子任务心跳id

        :param heart_beat_id: The heart_beat_id of this SubTrainingJobInfoDto.
        :type heart_beat_id: str
        """
        self._heart_beat_id = heart_beat_id

    @property
    def state(self):
        r"""Gets the state of this SubTrainingJobInfoDto.

        任务状态

        :return: The state of this SubTrainingJobInfoDto.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this SubTrainingJobInfoDto.

        任务状态

        :param state: The state of this SubTrainingJobInfoDto.
        :type state: str
        """
        self._state = state

    @property
    def create_time(self):
        r"""Gets the create_time of this SubTrainingJobInfoDto.

        创建时间

        :return: The create_time of this SubTrainingJobInfoDto.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SubTrainingJobInfoDto.

        创建时间

        :param create_time: The create_time of this SubTrainingJobInfoDto.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this SubTrainingJobInfoDto.

        最后更新时间

        :return: The last_update_time of this SubTrainingJobInfoDto.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this SubTrainingJobInfoDto.

        最后更新时间

        :param last_update_time: The last_update_time of this SubTrainingJobInfoDto.
        :type last_update_time: int
        """
        self._last_update_time = last_update_time

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
        if not isinstance(other, SubTrainingJobInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
