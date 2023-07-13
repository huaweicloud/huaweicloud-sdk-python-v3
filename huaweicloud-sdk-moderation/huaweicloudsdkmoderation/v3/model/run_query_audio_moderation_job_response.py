# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunQueryAudioModerationJobResponse(SdkResponse):

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
        'status': 'str',
        'result': 'AudioModerationResultResult',
        'request_params': 'AudioModerationResultRequestParams',
        'create_time': 'str',
        'update_time': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'status': 'status',
        'result': 'result',
        'request_params': 'request_params',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'request_id': 'request_id'
    }

    def __init__(self, job_id=None, status=None, result=None, request_params=None, create_time=None, update_time=None, request_id=None):
        """RunQueryAudioModerationJobResponse

        The model defined in huaweicloud sdk

        :param job_id: 作业id
        :type job_id: str
        :param status: 作业状态，可取值有： running: 正在运行 succeeded: 运行成功 failed: 运行失败
        :type status: str
        :param result: 
        :type result: :class:`huaweicloudsdkmoderation.v3.AudioModerationResultResult`
        :param request_params: 
        :type request_params: :class:`huaweicloudsdkmoderation.v3.AudioModerationResultRequestParams`
        :param create_time: 作业创建时间
        :type create_time: str
        :param update_time: 作业更新时间
        :type update_time: str
        :param request_id: 本次请求的唯⼀标识，⽤于问题排查，建议保存。
        :type request_id: str
        """
        
        super(RunQueryAudioModerationJobResponse, self).__init__()

        self._job_id = None
        self._status = None
        self._result = None
        self._request_params = None
        self._create_time = None
        self._update_time = None
        self._request_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if result is not None:
            self.result = result
        if request_params is not None:
            self.request_params = request_params
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if request_id is not None:
            self.request_id = request_id

    @property
    def job_id(self):
        """Gets the job_id of this RunQueryAudioModerationJobResponse.

        作业id

        :return: The job_id of this RunQueryAudioModerationJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this RunQueryAudioModerationJobResponse.

        作业id

        :param job_id: The job_id of this RunQueryAudioModerationJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        """Gets the status of this RunQueryAudioModerationJobResponse.

        作业状态，可取值有： running: 正在运行 succeeded: 运行成功 failed: 运行失败

        :return: The status of this RunQueryAudioModerationJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RunQueryAudioModerationJobResponse.

        作业状态，可取值有： running: 正在运行 succeeded: 运行成功 failed: 运行失败

        :param status: The status of this RunQueryAudioModerationJobResponse.
        :type status: str
        """
        self._status = status

    @property
    def result(self):
        """Gets the result of this RunQueryAudioModerationJobResponse.

        :return: The result of this RunQueryAudioModerationJobResponse.
        :rtype: :class:`huaweicloudsdkmoderation.v3.AudioModerationResultResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this RunQueryAudioModerationJobResponse.

        :param result: The result of this RunQueryAudioModerationJobResponse.
        :type result: :class:`huaweicloudsdkmoderation.v3.AudioModerationResultResult`
        """
        self._result = result

    @property
    def request_params(self):
        """Gets the request_params of this RunQueryAudioModerationJobResponse.

        :return: The request_params of this RunQueryAudioModerationJobResponse.
        :rtype: :class:`huaweicloudsdkmoderation.v3.AudioModerationResultRequestParams`
        """
        return self._request_params

    @request_params.setter
    def request_params(self, request_params):
        """Sets the request_params of this RunQueryAudioModerationJobResponse.

        :param request_params: The request_params of this RunQueryAudioModerationJobResponse.
        :type request_params: :class:`huaweicloudsdkmoderation.v3.AudioModerationResultRequestParams`
        """
        self._request_params = request_params

    @property
    def create_time(self):
        """Gets the create_time of this RunQueryAudioModerationJobResponse.

        作业创建时间

        :return: The create_time of this RunQueryAudioModerationJobResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this RunQueryAudioModerationJobResponse.

        作业创建时间

        :param create_time: The create_time of this RunQueryAudioModerationJobResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this RunQueryAudioModerationJobResponse.

        作业更新时间

        :return: The update_time of this RunQueryAudioModerationJobResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this RunQueryAudioModerationJobResponse.

        作业更新时间

        :param update_time: The update_time of this RunQueryAudioModerationJobResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def request_id(self):
        """Gets the request_id of this RunQueryAudioModerationJobResponse.

        本次请求的唯⼀标识，⽤于问题排查，建议保存。

        :return: The request_id of this RunQueryAudioModerationJobResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this RunQueryAudioModerationJobResponse.

        本次请求的唯⼀标识，⽤于问题排查，建议保存。

        :param request_id: The request_id of this RunQueryAudioModerationJobResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, RunQueryAudioModerationJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
