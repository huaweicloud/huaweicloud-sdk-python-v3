# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRealTimeClipResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'publish_domain': 'str',
        'app': 'str',
        'stream': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'file_url': 'str',
        'output': 'ObsInfo',
        'meta_data': 'ObjectMetaData'
    }

    attribute_map = {
        'task_id': 'task_id',
        'publish_domain': 'publish_domain',
        'app': 'app',
        'stream': 'stream',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'file_url': 'file_url',
        'output': 'output',
        'meta_data': 'meta_data'
    }

    def __init__(self, task_id=None, publish_domain=None, app=None, stream=None, start_time=None, end_time=None, file_url=None, output=None, meta_data=None):
        r"""CreateRealTimeClipResponse

        The model defined in huaweicloud sdk

        :param task_id: 截取的任务id，回调时会返回该任务id 
        :type task_id: str
        :param publish_domain: 直播推流域名 
        :type publish_domain: str
        :param app: 应用名 
        :type app: str
        :param stream: 录制的流名 
        :type stream: str
        :param start_time: 录制完成文件对应的启动录制时间，UNIX时间戳 
        :type start_time: int
        :param end_time: 录制完成文件对应的完成录制时间，UNIX时间戳 
        :type end_time: int
        :param file_url: 粉丝截取响应的obs地址 
        :type file_url: str
        :param output: 
        :type output: :class:`huaweicloudsdkvod.v1.ObsInfo`
        :param meta_data: 
        :type meta_data: :class:`huaweicloudsdkvod.v1.ObjectMetaData`
        """
        
        super(CreateRealTimeClipResponse, self).__init__()

        self._task_id = None
        self._publish_domain = None
        self._app = None
        self._stream = None
        self._start_time = None
        self._end_time = None
        self._file_url = None
        self._output = None
        self._meta_data = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if publish_domain is not None:
            self.publish_domain = publish_domain
        if app is not None:
            self.app = app
        if stream is not None:
            self.stream = stream
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if file_url is not None:
            self.file_url = file_url
        if output is not None:
            self.output = output
        if meta_data is not None:
            self.meta_data = meta_data

    @property
    def task_id(self):
        r"""Gets the task_id of this CreateRealTimeClipResponse.

        截取的任务id，回调时会返回该任务id 

        :return: The task_id of this CreateRealTimeClipResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this CreateRealTimeClipResponse.

        截取的任务id，回调时会返回该任务id 

        :param task_id: The task_id of this CreateRealTimeClipResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def publish_domain(self):
        r"""Gets the publish_domain of this CreateRealTimeClipResponse.

        直播推流域名 

        :return: The publish_domain of this CreateRealTimeClipResponse.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        r"""Sets the publish_domain of this CreateRealTimeClipResponse.

        直播推流域名 

        :param publish_domain: The publish_domain of this CreateRealTimeClipResponse.
        :type publish_domain: str
        """
        self._publish_domain = publish_domain

    @property
    def app(self):
        r"""Gets the app of this CreateRealTimeClipResponse.

        应用名 

        :return: The app of this CreateRealTimeClipResponse.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this CreateRealTimeClipResponse.

        应用名 

        :param app: The app of this CreateRealTimeClipResponse.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        r"""Gets the stream of this CreateRealTimeClipResponse.

        录制的流名 

        :return: The stream of this CreateRealTimeClipResponse.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        r"""Sets the stream of this CreateRealTimeClipResponse.

        录制的流名 

        :param stream: The stream of this CreateRealTimeClipResponse.
        :type stream: str
        """
        self._stream = stream

    @property
    def start_time(self):
        r"""Gets the start_time of this CreateRealTimeClipResponse.

        录制完成文件对应的启动录制时间，UNIX时间戳 

        :return: The start_time of this CreateRealTimeClipResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CreateRealTimeClipResponse.

        录制完成文件对应的启动录制时间，UNIX时间戳 

        :param start_time: The start_time of this CreateRealTimeClipResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this CreateRealTimeClipResponse.

        录制完成文件对应的完成录制时间，UNIX时间戳 

        :return: The end_time of this CreateRealTimeClipResponse.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this CreateRealTimeClipResponse.

        录制完成文件对应的完成录制时间，UNIX时间戳 

        :param end_time: The end_time of this CreateRealTimeClipResponse.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def file_url(self):
        r"""Gets the file_url of this CreateRealTimeClipResponse.

        粉丝截取响应的obs地址 

        :return: The file_url of this CreateRealTimeClipResponse.
        :rtype: str
        """
        return self._file_url

    @file_url.setter
    def file_url(self, file_url):
        r"""Sets the file_url of this CreateRealTimeClipResponse.

        粉丝截取响应的obs地址 

        :param file_url: The file_url of this CreateRealTimeClipResponse.
        :type file_url: str
        """
        self._file_url = file_url

    @property
    def output(self):
        r"""Gets the output of this CreateRealTimeClipResponse.

        :return: The output of this CreateRealTimeClipResponse.
        :rtype: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this CreateRealTimeClipResponse.

        :param output: The output of this CreateRealTimeClipResponse.
        :type output: :class:`huaweicloudsdkvod.v1.ObsInfo`
        """
        self._output = output

    @property
    def meta_data(self):
        r"""Gets the meta_data of this CreateRealTimeClipResponse.

        :return: The meta_data of this CreateRealTimeClipResponse.
        :rtype: :class:`huaweicloudsdkvod.v1.ObjectMetaData`
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        r"""Sets the meta_data of this CreateRealTimeClipResponse.

        :param meta_data: The meta_data of this CreateRealTimeClipResponse.
        :type meta_data: :class:`huaweicloudsdkvod.v1.ObjectMetaData`
        """
        self._meta_data = meta_data

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
        if not isinstance(other, CreateRealTimeClipResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
