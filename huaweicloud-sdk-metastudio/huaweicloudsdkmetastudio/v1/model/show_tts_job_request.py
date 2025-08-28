# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTtsJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'create_since': 'str',
        'create_until': 'str',
        'job_id': 'str',
        'job_type': 'str',
        'tts_service_enum': 'str',
        'business_type': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'limit': 'limit',
        'offset': 'offset',
        'create_since': 'create_since',
        'create_until': 'create_until',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'tts_service_enum': 'tts_service_enum',
        'business_type': 'business_type'
    }

    def __init__(self, x_app_user_id=None, limit=None, offset=None, create_since=None, create_until=None, job_id=None, job_type=None, tts_service_enum=None, business_type=None):
        r"""ShowTtsJobRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 第三方用户ID。不允许输入中文。
        :type x_app_user_id: str
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询。
        :type offset: int
        :param create_since: 过滤创建时间&gt;&#x3D;输入时间的记录。
        :type create_since: str
        :param create_until: 过滤创建时间&lt;&#x3D;输入时间的记录。
        :type create_until: str
        :param job_id: 任务ID。
        :type job_id: str
        :param job_type: 任务类型。 * AUDITION:试听任务 * ASYNC_JOB：异步任务 * WEBSOCKET：websocket接口合成任务
        :type job_type: str
        :param tts_service_enum: tts版本。 * TTS_LLM: 530大模型（V7版本） * TTS_LLM_VC：530大模型VC版本（V7版本） * TTS_LAB：lab小模型（V5版本） * TTS_LAB_GPU：lab小模型GPU版本（V5版本） * GPU_CLONE：V4模型 * TTS_LLM_VQ：VQ模型（V10版本）
        :type tts_service_enum: str
        :param business_type: 业务类型。
        :type business_type: str
        """
        
        

        self._x_app_user_id = None
        self._limit = None
        self._offset = None
        self._create_since = None
        self._create_until = None
        self._job_id = None
        self._job_type = None
        self._tts_service_enum = None
        self._business_type = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if create_since is not None:
            self.create_since = create_since
        if create_until is not None:
            self.create_until = create_until
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if tts_service_enum is not None:
            self.tts_service_enum = tts_service_enum
        if business_type is not None:
            self.business_type = business_type

    @property
    def x_app_user_id(self):
        r"""Gets the x_app_user_id of this ShowTtsJobRequest.

        第三方用户ID。不允许输入中文。

        :return: The x_app_user_id of this ShowTtsJobRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        r"""Sets the x_app_user_id of this ShowTtsJobRequest.

        第三方用户ID。不允许输入中文。

        :param x_app_user_id: The x_app_user_id of this ShowTtsJobRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def limit(self):
        r"""Gets the limit of this ShowTtsJobRequest.

        每页显示的条目数量。

        :return: The limit of this ShowTtsJobRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowTtsJobRequest.

        每页显示的条目数量。

        :param limit: The limit of this ShowTtsJobRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowTtsJobRequest.

        偏移量，表示从此偏移量开始查询。

        :return: The offset of this ShowTtsJobRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowTtsJobRequest.

        偏移量，表示从此偏移量开始查询。

        :param offset: The offset of this ShowTtsJobRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def create_since(self):
        r"""Gets the create_since of this ShowTtsJobRequest.

        过滤创建时间>=输入时间的记录。

        :return: The create_since of this ShowTtsJobRequest.
        :rtype: str
        """
        return self._create_since

    @create_since.setter
    def create_since(self, create_since):
        r"""Sets the create_since of this ShowTtsJobRequest.

        过滤创建时间>=输入时间的记录。

        :param create_since: The create_since of this ShowTtsJobRequest.
        :type create_since: str
        """
        self._create_since = create_since

    @property
    def create_until(self):
        r"""Gets the create_until of this ShowTtsJobRequest.

        过滤创建时间<=输入时间的记录。

        :return: The create_until of this ShowTtsJobRequest.
        :rtype: str
        """
        return self._create_until

    @create_until.setter
    def create_until(self, create_until):
        r"""Sets the create_until of this ShowTtsJobRequest.

        过滤创建时间<=输入时间的记录。

        :param create_until: The create_until of this ShowTtsJobRequest.
        :type create_until: str
        """
        self._create_until = create_until

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowTtsJobRequest.

        任务ID。

        :return: The job_id of this ShowTtsJobRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowTtsJobRequest.

        任务ID。

        :param job_id: The job_id of this ShowTtsJobRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        r"""Gets the job_type of this ShowTtsJobRequest.

        任务类型。 * AUDITION:试听任务 * ASYNC_JOB：异步任务 * WEBSOCKET：websocket接口合成任务

        :return: The job_type of this ShowTtsJobRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ShowTtsJobRequest.

        任务类型。 * AUDITION:试听任务 * ASYNC_JOB：异步任务 * WEBSOCKET：websocket接口合成任务

        :param job_type: The job_type of this ShowTtsJobRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def tts_service_enum(self):
        r"""Gets the tts_service_enum of this ShowTtsJobRequest.

        tts版本。 * TTS_LLM: 530大模型（V7版本） * TTS_LLM_VC：530大模型VC版本（V7版本） * TTS_LAB：lab小模型（V5版本） * TTS_LAB_GPU：lab小模型GPU版本（V5版本） * GPU_CLONE：V4模型 * TTS_LLM_VQ：VQ模型（V10版本）

        :return: The tts_service_enum of this ShowTtsJobRequest.
        :rtype: str
        """
        return self._tts_service_enum

    @tts_service_enum.setter
    def tts_service_enum(self, tts_service_enum):
        r"""Sets the tts_service_enum of this ShowTtsJobRequest.

        tts版本。 * TTS_LLM: 530大模型（V7版本） * TTS_LLM_VC：530大模型VC版本（V7版本） * TTS_LAB：lab小模型（V5版本） * TTS_LAB_GPU：lab小模型GPU版本（V5版本） * GPU_CLONE：V4模型 * TTS_LLM_VQ：VQ模型（V10版本）

        :param tts_service_enum: The tts_service_enum of this ShowTtsJobRequest.
        :type tts_service_enum: str
        """
        self._tts_service_enum = tts_service_enum

    @property
    def business_type(self):
        r"""Gets the business_type of this ShowTtsJobRequest.

        业务类型。

        :return: The business_type of this ShowTtsJobRequest.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        r"""Sets the business_type of this ShowTtsJobRequest.

        业务类型。

        :param business_type: The business_type of this ShowTtsJobRequest.
        :type business_type: str
        """
        self._business_type = business_type

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
        if not isinstance(other, ShowTtsJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
