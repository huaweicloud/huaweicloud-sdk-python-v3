# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveSnapshotConfig:

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
        'auth_key': 'str',
        'time_interval': 'int',
        'object_write_mode': 'int',
        'obs_location': 'ObsFileAddr',
        'call_back_enable': 'str',
        'call_back_url': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'app_name': 'app_name',
        'auth_key': 'auth_key',
        'time_interval': 'time_interval',
        'object_write_mode': 'object_write_mode',
        'obs_location': 'obs_location',
        'call_back_enable': 'call_back_enable',
        'call_back_url': 'call_back_url'
    }

    def __init__(self, domain=None, app_name=None, auth_key=None, time_interval=None, object_write_mode=None, obs_location=None, call_back_enable=None, call_back_url=None):
        """LiveSnapshotConfig

        The model defined in huaweicloud sdk

        :param domain: 直播推流域名
        :type domain: str
        :param app_name: 应用名称
        :type app_name: str
        :param auth_key: 回调鉴权密钥值  长度范围：[32-128]  若需要使用回调鉴权功能，请配置鉴权密钥，否则，留空即可。
        :type auth_key: str
        :param time_interval: 截图频率  取值范围：[5-3600]  单位：秒
        :type time_interval: int
        :param object_write_mode: 在OBS桶存储截图的方式：  - 0：实时截图，以时间戳命名截图文件，保存所有截图文件到OBS桶。例：snapshot/{domain}/{app_name}/{stream_name}/{UnixTimestamp}.jpg  - 1：覆盖截图，只保存最新的截图文件，新的截图会覆盖原来的截图文件。例：snapshot/{domain}/{app_name}/{stream_name}.jpg
        :type object_write_mode: int
        :param obs_location: 
        :type obs_location: :class:`huaweicloudsdklive.v1.ObsFileAddr`
        :param call_back_enable: 是否启用回调通知 - on：启用。 - off：不启用。
        :type call_back_enable: str
        :param call_back_url: 通知服务器地址，必须是合法的URL且携带协议，协议支持http和https。截图完成后直播服务会向此地址推送截图状态信息。
        :type call_back_url: str
        """
        
        

        self._domain = None
        self._app_name = None
        self._auth_key = None
        self._time_interval = None
        self._object_write_mode = None
        self._obs_location = None
        self._call_back_enable = None
        self._call_back_url = None
        self.discriminator = None

        self.domain = domain
        self.app_name = app_name
        if auth_key is not None:
            self.auth_key = auth_key
        self.time_interval = time_interval
        self.object_write_mode = object_write_mode
        self.obs_location = obs_location
        if call_back_enable is not None:
            self.call_back_enable = call_back_enable
        if call_back_url is not None:
            self.call_back_url = call_back_url

    @property
    def domain(self):
        """Gets the domain of this LiveSnapshotConfig.

        直播推流域名

        :return: The domain of this LiveSnapshotConfig.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this LiveSnapshotConfig.

        直播推流域名

        :param domain: The domain of this LiveSnapshotConfig.
        :type domain: str
        """
        self._domain = domain

    @property
    def app_name(self):
        """Gets the app_name of this LiveSnapshotConfig.

        应用名称

        :return: The app_name of this LiveSnapshotConfig.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this LiveSnapshotConfig.

        应用名称

        :param app_name: The app_name of this LiveSnapshotConfig.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def auth_key(self):
        """Gets the auth_key of this LiveSnapshotConfig.

        回调鉴权密钥值  长度范围：[32-128]  若需要使用回调鉴权功能，请配置鉴权密钥，否则，留空即可。

        :return: The auth_key of this LiveSnapshotConfig.
        :rtype: str
        """
        return self._auth_key

    @auth_key.setter
    def auth_key(self, auth_key):
        """Sets the auth_key of this LiveSnapshotConfig.

        回调鉴权密钥值  长度范围：[32-128]  若需要使用回调鉴权功能，请配置鉴权密钥，否则，留空即可。

        :param auth_key: The auth_key of this LiveSnapshotConfig.
        :type auth_key: str
        """
        self._auth_key = auth_key

    @property
    def time_interval(self):
        """Gets the time_interval of this LiveSnapshotConfig.

        截图频率  取值范围：[5-3600]  单位：秒

        :return: The time_interval of this LiveSnapshotConfig.
        :rtype: int
        """
        return self._time_interval

    @time_interval.setter
    def time_interval(self, time_interval):
        """Sets the time_interval of this LiveSnapshotConfig.

        截图频率  取值范围：[5-3600]  单位：秒

        :param time_interval: The time_interval of this LiveSnapshotConfig.
        :type time_interval: int
        """
        self._time_interval = time_interval

    @property
    def object_write_mode(self):
        """Gets the object_write_mode of this LiveSnapshotConfig.

        在OBS桶存储截图的方式：  - 0：实时截图，以时间戳命名截图文件，保存所有截图文件到OBS桶。例：snapshot/{domain}/{app_name}/{stream_name}/{UnixTimestamp}.jpg  - 1：覆盖截图，只保存最新的截图文件，新的截图会覆盖原来的截图文件。例：snapshot/{domain}/{app_name}/{stream_name}.jpg

        :return: The object_write_mode of this LiveSnapshotConfig.
        :rtype: int
        """
        return self._object_write_mode

    @object_write_mode.setter
    def object_write_mode(self, object_write_mode):
        """Sets the object_write_mode of this LiveSnapshotConfig.

        在OBS桶存储截图的方式：  - 0：实时截图，以时间戳命名截图文件，保存所有截图文件到OBS桶。例：snapshot/{domain}/{app_name}/{stream_name}/{UnixTimestamp}.jpg  - 1：覆盖截图，只保存最新的截图文件，新的截图会覆盖原来的截图文件。例：snapshot/{domain}/{app_name}/{stream_name}.jpg

        :param object_write_mode: The object_write_mode of this LiveSnapshotConfig.
        :type object_write_mode: int
        """
        self._object_write_mode = object_write_mode

    @property
    def obs_location(self):
        """Gets the obs_location of this LiveSnapshotConfig.

        :return: The obs_location of this LiveSnapshotConfig.
        :rtype: :class:`huaweicloudsdklive.v1.ObsFileAddr`
        """
        return self._obs_location

    @obs_location.setter
    def obs_location(self, obs_location):
        """Sets the obs_location of this LiveSnapshotConfig.

        :param obs_location: The obs_location of this LiveSnapshotConfig.
        :type obs_location: :class:`huaweicloudsdklive.v1.ObsFileAddr`
        """
        self._obs_location = obs_location

    @property
    def call_back_enable(self):
        """Gets the call_back_enable of this LiveSnapshotConfig.

        是否启用回调通知 - on：启用。 - off：不启用。

        :return: The call_back_enable of this LiveSnapshotConfig.
        :rtype: str
        """
        return self._call_back_enable

    @call_back_enable.setter
    def call_back_enable(self, call_back_enable):
        """Sets the call_back_enable of this LiveSnapshotConfig.

        是否启用回调通知 - on：启用。 - off：不启用。

        :param call_back_enable: The call_back_enable of this LiveSnapshotConfig.
        :type call_back_enable: str
        """
        self._call_back_enable = call_back_enable

    @property
    def call_back_url(self):
        """Gets the call_back_url of this LiveSnapshotConfig.

        通知服务器地址，必须是合法的URL且携带协议，协议支持http和https。截图完成后直播服务会向此地址推送截图状态信息。

        :return: The call_back_url of this LiveSnapshotConfig.
        :rtype: str
        """
        return self._call_back_url

    @call_back_url.setter
    def call_back_url(self, call_back_url):
        """Sets the call_back_url of this LiveSnapshotConfig.

        通知服务器地址，必须是合法的URL且携带协议，协议支持http和https。截图完成后直播服务会向此地址推送截图状态信息。

        :param call_back_url: The call_back_url of this LiveSnapshotConfig.
        :type call_back_url: str
        """
        self._call_back_url = call_back_url

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
        if not isinstance(other, LiveSnapshotConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
