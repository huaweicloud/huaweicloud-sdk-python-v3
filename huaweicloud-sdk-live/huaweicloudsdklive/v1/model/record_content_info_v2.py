# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordContentInfoV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publish_domain': 'str',
        'file_name': 'str',
        'app': 'str',
        'stream': 'str',
        'record_format': 'str',
        'record_type': 'str',
        'obs_addr': 'RecordObsFileAddr',
        'vod_info': 'VodInfoV2',
        'download_url': 'str',
        'start_time': 'date',
        'end_time': 'date',
        'duration': 'int'
    }

    attribute_map = {
        'publish_domain': 'publish_domain',
        'file_name': 'file_name',
        'app': 'app',
        'stream': 'stream',
        'record_format': 'record_format',
        'record_type': 'record_type',
        'obs_addr': 'obs_addr',
        'vod_info': 'vod_info',
        'download_url': 'download_url',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'duration': 'duration'
    }

    def __init__(self, publish_domain=None, file_name=None, app=None, stream=None, record_format=None, record_type=None, obs_addr=None, vod_info=None, download_url=None, start_time=None, end_time=None, duration=None):
        r"""RecordContentInfoV2

        The model defined in huaweicloud sdk

        :param publish_domain: 直播推流域名
        :type publish_domain: str
        :param file_name: 录制文件名
        :type file_name: str
        :param app: 应用名
        :type app: str
        :param stream: 录制的流名
        :type stream: str
        :param record_format: 录制格式flv，hls，mp4
        :type record_format: str
        :param record_type: 录制类型，CONTINUOUS_RECORD，COMMAND_RECORD。默认CONTINUOUS_RECORD。 - CONTINUOUS_RECORD：持续录制，在该规则类型配置后，只要有流到推送到录制系统，就触发录制。 - COMMAND_RECORD：命令录制，在该规则类型配置后，在流推送到录制系统后，租户需要通过命令控制该流的录制开始和结束。 
        :type record_type: str
        :param obs_addr: 
        :type obs_addr: :class:`huaweicloudsdklive.v1.RecordObsFileAddr`
        :param vod_info: 
        :type vod_info: :class:`huaweicloudsdklive.v1.VodInfoV2`
        :param download_url: OBS下载地址
        :type download_url: str
        :param start_time: 录制开始时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。对record_type为PLAN_RECORD有效
        :type start_time: date
        :param end_time: 录制结束时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。对record_type为PLAN_RECORD有效
        :type end_time: date
        :param duration: 该录制文件时长，单位为秒
        :type duration: int
        """
        
        

        self._publish_domain = None
        self._file_name = None
        self._app = None
        self._stream = None
        self._record_format = None
        self._record_type = None
        self._obs_addr = None
        self._vod_info = None
        self._download_url = None
        self._start_time = None
        self._end_time = None
        self._duration = None
        self.discriminator = None

        if publish_domain is not None:
            self.publish_domain = publish_domain
        if file_name is not None:
            self.file_name = file_name
        if app is not None:
            self.app = app
        if stream is not None:
            self.stream = stream
        if record_format is not None:
            self.record_format = record_format
        if record_type is not None:
            self.record_type = record_type
        if obs_addr is not None:
            self.obs_addr = obs_addr
        if vod_info is not None:
            self.vod_info = vod_info
        if download_url is not None:
            self.download_url = download_url
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if duration is not None:
            self.duration = duration

    @property
    def publish_domain(self):
        r"""Gets the publish_domain of this RecordContentInfoV2.

        直播推流域名

        :return: The publish_domain of this RecordContentInfoV2.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        r"""Sets the publish_domain of this RecordContentInfoV2.

        直播推流域名

        :param publish_domain: The publish_domain of this RecordContentInfoV2.
        :type publish_domain: str
        """
        self._publish_domain = publish_domain

    @property
    def file_name(self):
        r"""Gets the file_name of this RecordContentInfoV2.

        录制文件名

        :return: The file_name of this RecordContentInfoV2.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this RecordContentInfoV2.

        录制文件名

        :param file_name: The file_name of this RecordContentInfoV2.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def app(self):
        r"""Gets the app of this RecordContentInfoV2.

        应用名

        :return: The app of this RecordContentInfoV2.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this RecordContentInfoV2.

        应用名

        :param app: The app of this RecordContentInfoV2.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        r"""Gets the stream of this RecordContentInfoV2.

        录制的流名

        :return: The stream of this RecordContentInfoV2.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        r"""Sets the stream of this RecordContentInfoV2.

        录制的流名

        :param stream: The stream of this RecordContentInfoV2.
        :type stream: str
        """
        self._stream = stream

    @property
    def record_format(self):
        r"""Gets the record_format of this RecordContentInfoV2.

        录制格式flv，hls，mp4

        :return: The record_format of this RecordContentInfoV2.
        :rtype: str
        """
        return self._record_format

    @record_format.setter
    def record_format(self, record_format):
        r"""Sets the record_format of this RecordContentInfoV2.

        录制格式flv，hls，mp4

        :param record_format: The record_format of this RecordContentInfoV2.
        :type record_format: str
        """
        self._record_format = record_format

    @property
    def record_type(self):
        r"""Gets the record_type of this RecordContentInfoV2.

        录制类型，CONTINUOUS_RECORD，COMMAND_RECORD。默认CONTINUOUS_RECORD。 - CONTINUOUS_RECORD：持续录制，在该规则类型配置后，只要有流到推送到录制系统，就触发录制。 - COMMAND_RECORD：命令录制，在该规则类型配置后，在流推送到录制系统后，租户需要通过命令控制该流的录制开始和结束。 

        :return: The record_type of this RecordContentInfoV2.
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        r"""Sets the record_type of this RecordContentInfoV2.

        录制类型，CONTINUOUS_RECORD，COMMAND_RECORD。默认CONTINUOUS_RECORD。 - CONTINUOUS_RECORD：持续录制，在该规则类型配置后，只要有流到推送到录制系统，就触发录制。 - COMMAND_RECORD：命令录制，在该规则类型配置后，在流推送到录制系统后，租户需要通过命令控制该流的录制开始和结束。 

        :param record_type: The record_type of this RecordContentInfoV2.
        :type record_type: str
        """
        self._record_type = record_type

    @property
    def obs_addr(self):
        r"""Gets the obs_addr of this RecordContentInfoV2.

        :return: The obs_addr of this RecordContentInfoV2.
        :rtype: :class:`huaweicloudsdklive.v1.RecordObsFileAddr`
        """
        return self._obs_addr

    @obs_addr.setter
    def obs_addr(self, obs_addr):
        r"""Sets the obs_addr of this RecordContentInfoV2.

        :param obs_addr: The obs_addr of this RecordContentInfoV2.
        :type obs_addr: :class:`huaweicloudsdklive.v1.RecordObsFileAddr`
        """
        self._obs_addr = obs_addr

    @property
    def vod_info(self):
        r"""Gets the vod_info of this RecordContentInfoV2.

        :return: The vod_info of this RecordContentInfoV2.
        :rtype: :class:`huaweicloudsdklive.v1.VodInfoV2`
        """
        return self._vod_info

    @vod_info.setter
    def vod_info(self, vod_info):
        r"""Sets the vod_info of this RecordContentInfoV2.

        :param vod_info: The vod_info of this RecordContentInfoV2.
        :type vod_info: :class:`huaweicloudsdklive.v1.VodInfoV2`
        """
        self._vod_info = vod_info

    @property
    def download_url(self):
        r"""Gets the download_url of this RecordContentInfoV2.

        OBS下载地址

        :return: The download_url of this RecordContentInfoV2.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        r"""Sets the download_url of this RecordContentInfoV2.

        OBS下载地址

        :param download_url: The download_url of this RecordContentInfoV2.
        :type download_url: str
        """
        self._download_url = download_url

    @property
    def start_time(self):
        r"""Gets the start_time of this RecordContentInfoV2.

        录制开始时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。对record_type为PLAN_RECORD有效

        :return: The start_time of this RecordContentInfoV2.
        :rtype: date
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this RecordContentInfoV2.

        录制开始时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。对record_type为PLAN_RECORD有效

        :param start_time: The start_time of this RecordContentInfoV2.
        :type start_time: date
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this RecordContentInfoV2.

        录制结束时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。对record_type为PLAN_RECORD有效

        :return: The end_time of this RecordContentInfoV2.
        :rtype: date
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this RecordContentInfoV2.

        录制结束时间，格式：yyyy-mm-ddThh:mm:ssZ，UTC时间。对record_type为PLAN_RECORD有效

        :param end_time: The end_time of this RecordContentInfoV2.
        :type end_time: date
        """
        self._end_time = end_time

    @property
    def duration(self):
        r"""Gets the duration of this RecordContentInfoV2.

        该录制文件时长，单位为秒

        :return: The duration of this RecordContentInfoV2.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this RecordContentInfoV2.

        该录制文件时长，单位为秒

        :param duration: The duration of this RecordContentInfoV2.
        :type duration: int
        """
        self._duration = duration

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
        if not isinstance(other, RecordContentInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
