# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowShortJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_type': 'str',
        'job_id': 'str',
        'state': 'str',
        'job_failed_code': 'str',
        'job_failed_reason': 'str',
        'create_time': 'int',
        'lastupdate_time': 'int',
        'assess_result': 'AssessResult'
    }

    attribute_map = {
        'job_type': 'job_type',
        'job_id': 'job_id',
        'state': 'state',
        'job_failed_code': 'job_failed_code',
        'job_failed_reason': 'job_failed_reason',
        'create_time': 'create_time',
        'lastupdate_time': 'lastupdate_time',
        'assess_result': 'assess_result'
    }

    def __init__(self, job_type=None, job_id=None, state=None, job_failed_code=None, job_failed_reason=None, create_time=None, lastupdate_time=None, assess_result=None):
        r"""ShowShortJobResponse

        The model defined in huaweicloud sdk

        :param job_type: 短任务类型。 * VOICE_ASSESS: 声音质量检测
        :type job_type: str
        :param job_id: 任务id。
        :type job_id: str
        :param state: 任务状态。 * CREATING: 创建中 * SYSTEM_AUDITING: 系统审核中 * AUDITING: 人工审核中 * WAITING_SPLIT: 等待切割 * SPLITTING: 切割中 * SPLIT_FAILED: 切割失败 * ANNOTATING: 标注中 * WAITING: 等待训练 * PROCESSING: 任务训练中 * RESULT_REVIEW: 审核结果 * AUDIT_FAILED: 审核失败,等待用户重传数据 * UPLOADING: 上传中 * FAILED: 失败 * SUCCEED: 成功
        :type state: str
        :param job_failed_code: 当任务失败时呈现,失败错误码。
        :type job_failed_code: str
        :param job_failed_reason: 当任务失败时呈现,失败原因。
        :type job_failed_reason: str
        :param create_time: 任务创建时间。
        :type create_time: int
        :param lastupdate_time: 任务状态更新时间。
        :type lastupdate_time: int
        :param assess_result: 
        :type assess_result: :class:`huaweicloudsdkmetastudio.v1.AssessResult`
        """
        
        super().__init__()

        self._job_type = None
        self._job_id = None
        self._state = None
        self._job_failed_code = None
        self._job_failed_reason = None
        self._create_time = None
        self._lastupdate_time = None
        self._assess_result = None
        self.discriminator = None

        if job_type is not None:
            self.job_type = job_type
        if job_id is not None:
            self.job_id = job_id
        if state is not None:
            self.state = state
        if job_failed_code is not None:
            self.job_failed_code = job_failed_code
        if job_failed_reason is not None:
            self.job_failed_reason = job_failed_reason
        if create_time is not None:
            self.create_time = create_time
        if lastupdate_time is not None:
            self.lastupdate_time = lastupdate_time
        if assess_result is not None:
            self.assess_result = assess_result

    @property
    def job_type(self):
        r"""Gets the job_type of this ShowShortJobResponse.

        短任务类型。 * VOICE_ASSESS: 声音质量检测

        :return: The job_type of this ShowShortJobResponse.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ShowShortJobResponse.

        短任务类型。 * VOICE_ASSESS: 声音质量检测

        :param job_type: The job_type of this ShowShortJobResponse.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowShortJobResponse.

        任务id。

        :return: The job_id of this ShowShortJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowShortJobResponse.

        任务id。

        :param job_id: The job_id of this ShowShortJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def state(self):
        r"""Gets the state of this ShowShortJobResponse.

        任务状态。 * CREATING: 创建中 * SYSTEM_AUDITING: 系统审核中 * AUDITING: 人工审核中 * WAITING_SPLIT: 等待切割 * SPLITTING: 切割中 * SPLIT_FAILED: 切割失败 * ANNOTATING: 标注中 * WAITING: 等待训练 * PROCESSING: 任务训练中 * RESULT_REVIEW: 审核结果 * AUDIT_FAILED: 审核失败,等待用户重传数据 * UPLOADING: 上传中 * FAILED: 失败 * SUCCEED: 成功

        :return: The state of this ShowShortJobResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowShortJobResponse.

        任务状态。 * CREATING: 创建中 * SYSTEM_AUDITING: 系统审核中 * AUDITING: 人工审核中 * WAITING_SPLIT: 等待切割 * SPLITTING: 切割中 * SPLIT_FAILED: 切割失败 * ANNOTATING: 标注中 * WAITING: 等待训练 * PROCESSING: 任务训练中 * RESULT_REVIEW: 审核结果 * AUDIT_FAILED: 审核失败,等待用户重传数据 * UPLOADING: 上传中 * FAILED: 失败 * SUCCEED: 成功

        :param state: The state of this ShowShortJobResponse.
        :type state: str
        """
        self._state = state

    @property
    def job_failed_code(self):
        r"""Gets the job_failed_code of this ShowShortJobResponse.

        当任务失败时呈现,失败错误码。

        :return: The job_failed_code of this ShowShortJobResponse.
        :rtype: str
        """
        return self._job_failed_code

    @job_failed_code.setter
    def job_failed_code(self, job_failed_code):
        r"""Sets the job_failed_code of this ShowShortJobResponse.

        当任务失败时呈现,失败错误码。

        :param job_failed_code: The job_failed_code of this ShowShortJobResponse.
        :type job_failed_code: str
        """
        self._job_failed_code = job_failed_code

    @property
    def job_failed_reason(self):
        r"""Gets the job_failed_reason of this ShowShortJobResponse.

        当任务失败时呈现,失败原因。

        :return: The job_failed_reason of this ShowShortJobResponse.
        :rtype: str
        """
        return self._job_failed_reason

    @job_failed_reason.setter
    def job_failed_reason(self, job_failed_reason):
        r"""Sets the job_failed_reason of this ShowShortJobResponse.

        当任务失败时呈现,失败原因。

        :param job_failed_reason: The job_failed_reason of this ShowShortJobResponse.
        :type job_failed_reason: str
        """
        self._job_failed_reason = job_failed_reason

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowShortJobResponse.

        任务创建时间。

        :return: The create_time of this ShowShortJobResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowShortJobResponse.

        任务创建时间。

        :param create_time: The create_time of this ShowShortJobResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def lastupdate_time(self):
        r"""Gets the lastupdate_time of this ShowShortJobResponse.

        任务状态更新时间。

        :return: The lastupdate_time of this ShowShortJobResponse.
        :rtype: int
        """
        return self._lastupdate_time

    @lastupdate_time.setter
    def lastupdate_time(self, lastupdate_time):
        r"""Sets the lastupdate_time of this ShowShortJobResponse.

        任务状态更新时间。

        :param lastupdate_time: The lastupdate_time of this ShowShortJobResponse.
        :type lastupdate_time: int
        """
        self._lastupdate_time = lastupdate_time

    @property
    def assess_result(self):
        r"""Gets the assess_result of this ShowShortJobResponse.

        :return: The assess_result of this ShowShortJobResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AssessResult`
        """
        return self._assess_result

    @assess_result.setter
    def assess_result(self, assess_result):
        r"""Sets the assess_result of this ShowShortJobResponse.

        :param assess_result: The assess_result of this ShowShortJobResponse.
        :type assess_result: :class:`huaweicloudsdkmetastudio.v1.AssessResult`
        """
        self._assess_result = assess_result

    def to_dict(self):
        import warnings
        warnings.warn("ShowShortJobResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowShortJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
