# coding: utf-8

import pprint
import re

import six





class RecordConfigInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'app_name': 'str',
        'record_duration': 'int',
        'record_format': 'str',
        'record_type': 'str',
        'record_location': 'str',
        'record_prefix': 'str',
        'obs_addr': 'ObsFileAddr',
        'create_time': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'app_name': 'app_name',
        'record_duration': 'record_duration',
        'record_format': 'record_format',
        'record_type': 'record_type',
        'record_location': 'record_location',
        'record_prefix': 'record_prefix',
        'obs_addr': 'obs_addr',
        'create_time': 'create_time'
    }

    def __init__(self, domain=None, app_name=None, record_duration=None, record_format='flv', record_type='configer_record', record_location='vod', record_prefix='{DomainName}/{AppName}/{StreamName}/{StartTime}-{EndTime}', obs_addr=None, create_time=None):
        """RecordConfigInfo - a model defined in huaweicloud sdk"""
        
        

        self._domain = None
        self._app_name = None
        self._record_duration = None
        self._record_format = None
        self._record_type = None
        self._record_location = None
        self._record_prefix = None
        self._obs_addr = None
        self._create_time = None
        self.discriminator = None

        self.domain = domain
        self.app_name = app_name
        if record_duration is not None:
            self.record_duration = record_duration
        if record_format is not None:
            self.record_format = record_format
        if record_type is not None:
            self.record_type = record_type
        if record_location is not None:
            self.record_location = record_location
        if record_prefix is not None:
            self.record_prefix = record_prefix
        if obs_addr is not None:
            self.obs_addr = obs_addr
        if create_time is not None:
            self.create_time = create_time

    @property
    def domain(self):
        """Gets the domain of this RecordConfigInfo.

        直播播放域名

        :return: The domain of this RecordConfigInfo.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this RecordConfigInfo.

        直播播放域名

        :param domain: The domain of this RecordConfigInfo.
        :type: str
        """
        self._domain = domain

    @property
    def app_name(self):
        """Gets the app_name of this RecordConfigInfo.

        应用名称。 默认为“live”，若您需要自定义应用名称，请先提交工单申请。 

        :return: The app_name of this RecordConfigInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this RecordConfigInfo.

        应用名称。 默认为“live”，若您需要自定义应用名称，请先提交工单申请。 

        :param app_name: The app_name of this RecordConfigInfo.
        :type: str
        """
        self._app_name = app_name

    @property
    def record_duration(self):
        """Gets the record_duration of this RecordConfigInfo.

        秒，周期录制时常，最小15分钟，最大6小时，默认1小时

        :return: The record_duration of this RecordConfigInfo.
        :rtype: int
        """
        return self._record_duration

    @record_duration.setter
    def record_duration(self, record_duration):
        """Sets the record_duration of this RecordConfigInfo.

        秒，周期录制时常，最小15分钟，最大6小时，默认1小时

        :param record_duration: The record_duration of this RecordConfigInfo.
        :type: int
        """
        self._record_duration = record_duration

    @property
    def record_format(self):
        """Gets the record_format of this RecordConfigInfo.

        录制格式flv，hls，mp4，默认flv（目前仅支持flv）

        :return: The record_format of this RecordConfigInfo.
        :rtype: str
        """
        return self._record_format

    @record_format.setter
    def record_format(self, record_format):
        """Sets the record_format of this RecordConfigInfo.

        录制格式flv，hls，mp4，默认flv（目前仅支持flv）

        :param record_format: The record_format of this RecordConfigInfo.
        :type: str
        """
        self._record_format = record_format

    @property
    def record_type(self):
        """Gets the record_type of this RecordConfigInfo.

        录制类型，configer_record，默认configer_record。表示录制配置好后，只要有流就录制

        :return: The record_type of this RecordConfigInfo.
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this RecordConfigInfo.

        录制类型，configer_record，默认configer_record。表示录制配置好后，只要有流就录制

        :param record_type: The record_type of this RecordConfigInfo.
        :type: str
        """
        self._record_type = record_type

    @property
    def record_location(self):
        """Gets the record_location of this RecordConfigInfo.

        录制位置vod， 默认vod（目前暂只支持vod）

        :return: The record_location of this RecordConfigInfo.
        :rtype: str
        """
        return self._record_location

    @record_location.setter
    def record_location(self, record_location):
        """Sets the record_location of this RecordConfigInfo.

        录制位置vod， 默认vod（目前暂只支持vod）

        :param record_location: The record_location of this RecordConfigInfo.
        :type: str
        """
        self._record_location = record_location

    @property
    def record_prefix(self):
        """Gets the record_prefix of this RecordConfigInfo.

        录制文件前缀， DomainName，AppName，StreamName必须，默认{DomainName}/{AppName}/{StreamName}/{StartTime}-{EndTime}

        :return: The record_prefix of this RecordConfigInfo.
        :rtype: str
        """
        return self._record_prefix

    @record_prefix.setter
    def record_prefix(self, record_prefix):
        """Sets the record_prefix of this RecordConfigInfo.

        录制文件前缀， DomainName，AppName，StreamName必须，默认{DomainName}/{AppName}/{StreamName}/{StartTime}-{EndTime}

        :param record_prefix: The record_prefix of this RecordConfigInfo.
        :type: str
        """
        self._record_prefix = record_prefix

    @property
    def obs_addr(self):
        """Gets the obs_addr of this RecordConfigInfo.


        :return: The obs_addr of this RecordConfigInfo.
        :rtype: ObsFileAddr
        """
        return self._obs_addr

    @obs_addr.setter
    def obs_addr(self, obs_addr):
        """Sets the obs_addr of this RecordConfigInfo.


        :param obs_addr: The obs_addr of this RecordConfigInfo.
        :type: ObsFileAddr
        """
        self._obs_addr = obs_addr

    @property
    def create_time(self):
        """Gets the create_time of this RecordConfigInfo.

        录制配置创建时间，样例2020-02-14T10:45:16.947+08:00

        :return: The create_time of this RecordConfigInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this RecordConfigInfo.

        录制配置创建时间，样例2020-02-14T10:45:16.947+08:00

        :param create_time: The create_time of this RecordConfigInfo.
        :type: str
        """
        self._create_time = create_time

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RecordConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
