# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunQueryVideoModerationJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'job_id': 'str',
        'status': 'str',
        'request_params': 'VideoModerationResultRequestParams',
        'create_time': 'str',
        'update_time': 'str',
        'result': 'VideoModerationResultResult'
    }

    attribute_map = {
        'request_id': 'request_id',
        'job_id': 'job_id',
        'status': 'status',
        'request_params': 'request_params',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'result': 'result'
    }

    def __init__(self, request_id=None, job_id=None, status=None, request_params=None, create_time=None, update_time=None, result=None):
        r"""RunQueryVideoModerationJobResponse

        The model defined in huaweicloud sdk

        :param request_id: 本次请求的唯⼀标识，⽤于问题排查，建议保存。
        :type request_id: str
        :param job_id: 作业id
        :type job_id: str
        :param status: 作业状态，可取值有：  running: 正在运行 succeeded: 运行成功  failed: 运行失败
        :type status: str
        :param request_params: 
        :type request_params: :class:`huaweicloudsdkmoderation.v3.VideoModerationResultRequestParams`
        :param create_time: 作业创建时间
        :type create_time: str
        :param update_time: 作业更新时间
        :type update_time: str
        :param result: 
        :type result: :class:`huaweicloudsdkmoderation.v3.VideoModerationResultResult`
        """
        
        super(RunQueryVideoModerationJobResponse, self).__init__()

        self._request_id = None
        self._job_id = None
        self._status = None
        self._request_params = None
        self._create_time = None
        self._update_time = None
        self._result = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if request_params is not None:
            self.request_params = request_params
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if result is not None:
            self.result = result

    @property
    def request_id(self):
        r"""Gets the request_id of this RunQueryVideoModerationJobResponse.

        本次请求的唯⼀标识，⽤于问题排查，建议保存。

        :return: The request_id of this RunQueryVideoModerationJobResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this RunQueryVideoModerationJobResponse.

        本次请求的唯⼀标识，⽤于问题排查，建议保存。

        :param request_id: The request_id of this RunQueryVideoModerationJobResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def job_id(self):
        r"""Gets the job_id of this RunQueryVideoModerationJobResponse.

        作业id

        :return: The job_id of this RunQueryVideoModerationJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this RunQueryVideoModerationJobResponse.

        作业id

        :param job_id: The job_id of this RunQueryVideoModerationJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        r"""Gets the status of this RunQueryVideoModerationJobResponse.

        作业状态，可取值有：  running: 正在运行 succeeded: 运行成功  failed: 运行失败

        :return: The status of this RunQueryVideoModerationJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RunQueryVideoModerationJobResponse.

        作业状态，可取值有：  running: 正在运行 succeeded: 运行成功  failed: 运行失败

        :param status: The status of this RunQueryVideoModerationJobResponse.
        :type status: str
        """
        self._status = status

    @property
    def request_params(self):
        r"""Gets the request_params of this RunQueryVideoModerationJobResponse.

        :return: The request_params of this RunQueryVideoModerationJobResponse.
        :rtype: :class:`huaweicloudsdkmoderation.v3.VideoModerationResultRequestParams`
        """
        return self._request_params

    @request_params.setter
    def request_params(self, request_params):
        r"""Sets the request_params of this RunQueryVideoModerationJobResponse.

        :param request_params: The request_params of this RunQueryVideoModerationJobResponse.
        :type request_params: :class:`huaweicloudsdkmoderation.v3.VideoModerationResultRequestParams`
        """
        self._request_params = request_params

    @property
    def create_time(self):
        r"""Gets the create_time of this RunQueryVideoModerationJobResponse.

        作业创建时间

        :return: The create_time of this RunQueryVideoModerationJobResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this RunQueryVideoModerationJobResponse.

        作业创建时间

        :param create_time: The create_time of this RunQueryVideoModerationJobResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this RunQueryVideoModerationJobResponse.

        作业更新时间

        :return: The update_time of this RunQueryVideoModerationJobResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this RunQueryVideoModerationJobResponse.

        作业更新时间

        :param update_time: The update_time of this RunQueryVideoModerationJobResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def result(self):
        r"""Gets the result of this RunQueryVideoModerationJobResponse.

        :return: The result of this RunQueryVideoModerationJobResponse.
        :rtype: :class:`huaweicloudsdkmoderation.v3.VideoModerationResultResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this RunQueryVideoModerationJobResponse.

        :param result: The result of this RunQueryVideoModerationJobResponse.
        :type result: :class:`huaweicloudsdkmoderation.v3.VideoModerationResultResult`
        """
        self._result = result

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
        if not isinstance(other, RunQueryVideoModerationJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
