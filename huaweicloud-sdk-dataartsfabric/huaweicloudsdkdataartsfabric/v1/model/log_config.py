# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_lts_log': 'bool',
        'enable_obs_log': 'bool',
        'obs_path': 'str'
    }

    attribute_map = {
        'enable_lts_log': 'enable_lts_log',
        'enable_obs_log': 'enable_obs_log',
        'obs_path': 'obs_path'
    }

    def __init__(self, enable_lts_log=None, enable_obs_log=None, obs_path=None):
        r"""LogConfig

        The model defined in huaweicloud sdk

        :param enable_lts_log: 是否开启日志并记录到LTS,默认不开启
        :type enable_lts_log: bool
        :param enable_obs_log: 是否开启日志转储到OBS，默认不开启 开启的时候需要先开启日志记录到LTS，否则无法开启。
        :type enable_obs_log: bool
        :param obs_path: 日志存储的OBS路径
        :type obs_path: str
        """
        
        

        self._enable_lts_log = None
        self._enable_obs_log = None
        self._obs_path = None
        self.discriminator = None

        if enable_lts_log is not None:
            self.enable_lts_log = enable_lts_log
        if enable_obs_log is not None:
            self.enable_obs_log = enable_obs_log
        if obs_path is not None:
            self.obs_path = obs_path

    @property
    def enable_lts_log(self):
        r"""Gets the enable_lts_log of this LogConfig.

        是否开启日志并记录到LTS,默认不开启

        :return: The enable_lts_log of this LogConfig.
        :rtype: bool
        """
        return self._enable_lts_log

    @enable_lts_log.setter
    def enable_lts_log(self, enable_lts_log):
        r"""Sets the enable_lts_log of this LogConfig.

        是否开启日志并记录到LTS,默认不开启

        :param enable_lts_log: The enable_lts_log of this LogConfig.
        :type enable_lts_log: bool
        """
        self._enable_lts_log = enable_lts_log

    @property
    def enable_obs_log(self):
        r"""Gets the enable_obs_log of this LogConfig.

        是否开启日志转储到OBS，默认不开启 开启的时候需要先开启日志记录到LTS，否则无法开启。

        :return: The enable_obs_log of this LogConfig.
        :rtype: bool
        """
        return self._enable_obs_log

    @enable_obs_log.setter
    def enable_obs_log(self, enable_obs_log):
        r"""Sets the enable_obs_log of this LogConfig.

        是否开启日志转储到OBS，默认不开启 开启的时候需要先开启日志记录到LTS，否则无法开启。

        :param enable_obs_log: The enable_obs_log of this LogConfig.
        :type enable_obs_log: bool
        """
        self._enable_obs_log = enable_obs_log

    @property
    def obs_path(self):
        r"""Gets the obs_path of this LogConfig.

        日志存储的OBS路径

        :return: The obs_path of this LogConfig.
        :rtype: str
        """
        return self._obs_path

    @obs_path.setter
    def obs_path(self, obs_path):
        r"""Sets the obs_path of this LogConfig.

        日志存储的OBS路径

        :param obs_path: The obs_path of this LogConfig.
        :type obs_path: str
        """
        self._obs_path = obs_path

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
        if not isinstance(other, LogConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
