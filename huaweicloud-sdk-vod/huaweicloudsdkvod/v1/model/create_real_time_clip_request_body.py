# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRealTimeClipRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'timeshift_domain': 'str',
        'app': 'str',
        'stream': 'str',
        'trans_template_name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'is_persistence': 'int',
        'output_bucket': 'str',
        'output_object': 'str',
        'media_process_task': 'AdditionalObjectProcessReq',
        'callback_url': 'str',
        'session_context': 'str'
    }

    attribute_map = {
        'timeshift_domain': 'timeshift_domain',
        'app': 'app',
        'stream': 'stream',
        'trans_template_name': 'trans_template_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'is_persistence': 'is_persistence',
        'output_bucket': 'output_bucket',
        'output_object': 'output_object',
        'media_process_task': 'media_process_task',
        'callback_url': 'callback_url',
        'session_context': 'session_context'
    }

    def __init__(self, timeshift_domain=None, app=None, stream=None, trans_template_name=None, start_time=None, end_time=None, is_persistence=None, output_bucket=None, output_object=None, media_process_task=None, callback_url=None, session_context=None):
        r"""CreateRealTimeClipRequestBody

        The model defined in huaweicloud sdk

        :param timeshift_domain: 时移域名 
        :type timeshift_domain: str
        :param app: live的应用名，默认可填写live 
        :type app: str
        :param stream: 截取的流名 
        :type stream: str
        :param trans_template_name: 直播时移的转码模板，空表示截取源流 
        :type trans_template_name: str
        :param start_time: 截取流的开始时间，格式为：YYYY-MM-DDTHH:mm:ssZ（UTC时间）,开始时间与结束时间的间隔最大为12小时 
        :type start_time: str
        :param end_time: 截取流的开始时间，格式为：YYYY-MM-DDTHH:mm:ssZ（UTC时间）,开始时间与结束时间的间隔最大为12小时 
        :type end_time: str
        :param is_persistence: 0 非固化，1 固化。默认非固化 
        :type is_persistence: int
        :param output_bucket: 非固化场景为空，固化场景必填，复制到该桶中。 
        :type output_bucket: str
        :param output_object: 截取指定的m3u8文件路径名，仅支持HLS 
        :type output_object: str
        :param media_process_task: 
        :type media_process_task: :class:`huaweicloudsdkvod.v1.AdditionalObjectProcessReq`
        :param callback_url: 回调地址，为空则不回调 
        :type callback_url: str
        :param session_context: 自定义上下文，回调时会回调给用户，透传信息 
        :type session_context: str
        """
        
        

        self._timeshift_domain = None
        self._app = None
        self._stream = None
        self._trans_template_name = None
        self._start_time = None
        self._end_time = None
        self._is_persistence = None
        self._output_bucket = None
        self._output_object = None
        self._media_process_task = None
        self._callback_url = None
        self._session_context = None
        self.discriminator = None

        if timeshift_domain is not None:
            self.timeshift_domain = timeshift_domain
        if app is not None:
            self.app = app
        self.stream = stream
        if trans_template_name is not None:
            self.trans_template_name = trans_template_name
        self.start_time = start_time
        self.end_time = end_time
        if is_persistence is not None:
            self.is_persistence = is_persistence
        if output_bucket is not None:
            self.output_bucket = output_bucket
        if output_object is not None:
            self.output_object = output_object
        if media_process_task is not None:
            self.media_process_task = media_process_task
        if callback_url is not None:
            self.callback_url = callback_url
        if session_context is not None:
            self.session_context = session_context

    @property
    def timeshift_domain(self):
        r"""Gets the timeshift_domain of this CreateRealTimeClipRequestBody.

        时移域名 

        :return: The timeshift_domain of this CreateRealTimeClipRequestBody.
        :rtype: str
        """
        return self._timeshift_domain

    @timeshift_domain.setter
    def timeshift_domain(self, timeshift_domain):
        r"""Sets the timeshift_domain of this CreateRealTimeClipRequestBody.

        时移域名 

        :param timeshift_domain: The timeshift_domain of this CreateRealTimeClipRequestBody.
        :type timeshift_domain: str
        """
        self._timeshift_domain = timeshift_domain

    @property
    def app(self):
        r"""Gets the app of this CreateRealTimeClipRequestBody.

        live的应用名，默认可填写live 

        :return: The app of this CreateRealTimeClipRequestBody.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this CreateRealTimeClipRequestBody.

        live的应用名，默认可填写live 

        :param app: The app of this CreateRealTimeClipRequestBody.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        r"""Gets the stream of this CreateRealTimeClipRequestBody.

        截取的流名 

        :return: The stream of this CreateRealTimeClipRequestBody.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        r"""Sets the stream of this CreateRealTimeClipRequestBody.

        截取的流名 

        :param stream: The stream of this CreateRealTimeClipRequestBody.
        :type stream: str
        """
        self._stream = stream

    @property
    def trans_template_name(self):
        r"""Gets the trans_template_name of this CreateRealTimeClipRequestBody.

        直播时移的转码模板，空表示截取源流 

        :return: The trans_template_name of this CreateRealTimeClipRequestBody.
        :rtype: str
        """
        return self._trans_template_name

    @trans_template_name.setter
    def trans_template_name(self, trans_template_name):
        r"""Sets the trans_template_name of this CreateRealTimeClipRequestBody.

        直播时移的转码模板，空表示截取源流 

        :param trans_template_name: The trans_template_name of this CreateRealTimeClipRequestBody.
        :type trans_template_name: str
        """
        self._trans_template_name = trans_template_name

    @property
    def start_time(self):
        r"""Gets the start_time of this CreateRealTimeClipRequestBody.

        截取流的开始时间，格式为：YYYY-MM-DDTHH:mm:ssZ（UTC时间）,开始时间与结束时间的间隔最大为12小时 

        :return: The start_time of this CreateRealTimeClipRequestBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CreateRealTimeClipRequestBody.

        截取流的开始时间，格式为：YYYY-MM-DDTHH:mm:ssZ（UTC时间）,开始时间与结束时间的间隔最大为12小时 

        :param start_time: The start_time of this CreateRealTimeClipRequestBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this CreateRealTimeClipRequestBody.

        截取流的开始时间，格式为：YYYY-MM-DDTHH:mm:ssZ（UTC时间）,开始时间与结束时间的间隔最大为12小时 

        :return: The end_time of this CreateRealTimeClipRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this CreateRealTimeClipRequestBody.

        截取流的开始时间，格式为：YYYY-MM-DDTHH:mm:ssZ（UTC时间）,开始时间与结束时间的间隔最大为12小时 

        :param end_time: The end_time of this CreateRealTimeClipRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def is_persistence(self):
        r"""Gets the is_persistence of this CreateRealTimeClipRequestBody.

        0 非固化，1 固化。默认非固化 

        :return: The is_persistence of this CreateRealTimeClipRequestBody.
        :rtype: int
        """
        return self._is_persistence

    @is_persistence.setter
    def is_persistence(self, is_persistence):
        r"""Sets the is_persistence of this CreateRealTimeClipRequestBody.

        0 非固化，1 固化。默认非固化 

        :param is_persistence: The is_persistence of this CreateRealTimeClipRequestBody.
        :type is_persistence: int
        """
        self._is_persistence = is_persistence

    @property
    def output_bucket(self):
        r"""Gets the output_bucket of this CreateRealTimeClipRequestBody.

        非固化场景为空，固化场景必填，复制到该桶中。 

        :return: The output_bucket of this CreateRealTimeClipRequestBody.
        :rtype: str
        """
        return self._output_bucket

    @output_bucket.setter
    def output_bucket(self, output_bucket):
        r"""Sets the output_bucket of this CreateRealTimeClipRequestBody.

        非固化场景为空，固化场景必填，复制到该桶中。 

        :param output_bucket: The output_bucket of this CreateRealTimeClipRequestBody.
        :type output_bucket: str
        """
        self._output_bucket = output_bucket

    @property
    def output_object(self):
        r"""Gets the output_object of this CreateRealTimeClipRequestBody.

        截取指定的m3u8文件路径名，仅支持HLS 

        :return: The output_object of this CreateRealTimeClipRequestBody.
        :rtype: str
        """
        return self._output_object

    @output_object.setter
    def output_object(self, output_object):
        r"""Sets the output_object of this CreateRealTimeClipRequestBody.

        截取指定的m3u8文件路径名，仅支持HLS 

        :param output_object: The output_object of this CreateRealTimeClipRequestBody.
        :type output_object: str
        """
        self._output_object = output_object

    @property
    def media_process_task(self):
        r"""Gets the media_process_task of this CreateRealTimeClipRequestBody.

        :return: The media_process_task of this CreateRealTimeClipRequestBody.
        :rtype: :class:`huaweicloudsdkvod.v1.AdditionalObjectProcessReq`
        """
        return self._media_process_task

    @media_process_task.setter
    def media_process_task(self, media_process_task):
        r"""Sets the media_process_task of this CreateRealTimeClipRequestBody.

        :param media_process_task: The media_process_task of this CreateRealTimeClipRequestBody.
        :type media_process_task: :class:`huaweicloudsdkvod.v1.AdditionalObjectProcessReq`
        """
        self._media_process_task = media_process_task

    @property
    def callback_url(self):
        r"""Gets the callback_url of this CreateRealTimeClipRequestBody.

        回调地址，为空则不回调 

        :return: The callback_url of this CreateRealTimeClipRequestBody.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        r"""Sets the callback_url of this CreateRealTimeClipRequestBody.

        回调地址，为空则不回调 

        :param callback_url: The callback_url of this CreateRealTimeClipRequestBody.
        :type callback_url: str
        """
        self._callback_url = callback_url

    @property
    def session_context(self):
        r"""Gets the session_context of this CreateRealTimeClipRequestBody.

        自定义上下文，回调时会回调给用户，透传信息 

        :return: The session_context of this CreateRealTimeClipRequestBody.
        :rtype: str
        """
        return self._session_context

    @session_context.setter
    def session_context(self, session_context):
        r"""Sets the session_context of this CreateRealTimeClipRequestBody.

        自定义上下文，回调时会回调给用户，透传信息 

        :param session_context: The session_context of this CreateRealTimeClipRequestBody.
        :type session_context: str
        """
        self._session_context = session_context

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
        if not isinstance(other, CreateRealTimeClipRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
