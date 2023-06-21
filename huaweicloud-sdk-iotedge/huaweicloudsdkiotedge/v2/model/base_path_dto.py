# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BasePathDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_base_path': 'str',
        'config_base_path': 'str',
        'db_base_path': 'str',
        'offline_cache_configs': 'OfflineCacheConfigsDTO'
    }

    attribute_map = {
        'log_base_path': 'log_base_path',
        'config_base_path': 'config_base_path',
        'db_base_path': 'db_base_path',
        'offline_cache_configs': 'offline_cache_configs'
    }

    def __init__(self, log_base_path=None, config_base_path=None, db_base_path=None, offline_cache_configs=None):
        """BasePathDTO

        The model defined in huaweicloud sdk

        :param log_base_path: 节点日志根目录
        :type log_base_path: str
        :param config_base_path: 节点配置根目录
        :type config_base_path: str
        :param db_base_path: 节点数据存储根目录
        :type db_base_path: str
        :param offline_cache_configs: 
        :type offline_cache_configs: :class:`huaweicloudsdkiotedge.v2.OfflineCacheConfigsDTO`
        """
        
        

        self._log_base_path = None
        self._config_base_path = None
        self._db_base_path = None
        self._offline_cache_configs = None
        self.discriminator = None

        if log_base_path is not None:
            self.log_base_path = log_base_path
        if config_base_path is not None:
            self.config_base_path = config_base_path
        if db_base_path is not None:
            self.db_base_path = db_base_path
        if offline_cache_configs is not None:
            self.offline_cache_configs = offline_cache_configs

    @property
    def log_base_path(self):
        """Gets the log_base_path of this BasePathDTO.

        节点日志根目录

        :return: The log_base_path of this BasePathDTO.
        :rtype: str
        """
        return self._log_base_path

    @log_base_path.setter
    def log_base_path(self, log_base_path):
        """Sets the log_base_path of this BasePathDTO.

        节点日志根目录

        :param log_base_path: The log_base_path of this BasePathDTO.
        :type log_base_path: str
        """
        self._log_base_path = log_base_path

    @property
    def config_base_path(self):
        """Gets the config_base_path of this BasePathDTO.

        节点配置根目录

        :return: The config_base_path of this BasePathDTO.
        :rtype: str
        """
        return self._config_base_path

    @config_base_path.setter
    def config_base_path(self, config_base_path):
        """Sets the config_base_path of this BasePathDTO.

        节点配置根目录

        :param config_base_path: The config_base_path of this BasePathDTO.
        :type config_base_path: str
        """
        self._config_base_path = config_base_path

    @property
    def db_base_path(self):
        """Gets the db_base_path of this BasePathDTO.

        节点数据存储根目录

        :return: The db_base_path of this BasePathDTO.
        :rtype: str
        """
        return self._db_base_path

    @db_base_path.setter
    def db_base_path(self, db_base_path):
        """Sets the db_base_path of this BasePathDTO.

        节点数据存储根目录

        :param db_base_path: The db_base_path of this BasePathDTO.
        :type db_base_path: str
        """
        self._db_base_path = db_base_path

    @property
    def offline_cache_configs(self):
        """Gets the offline_cache_configs of this BasePathDTO.

        :return: The offline_cache_configs of this BasePathDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.OfflineCacheConfigsDTO`
        """
        return self._offline_cache_configs

    @offline_cache_configs.setter
    def offline_cache_configs(self, offline_cache_configs):
        """Sets the offline_cache_configs of this BasePathDTO.

        :param offline_cache_configs: The offline_cache_configs of this BasePathDTO.
        :type offline_cache_configs: :class:`huaweicloudsdkiotedge.v2.OfflineCacheConfigsDTO`
        """
        self._offline_cache_configs = offline_cache_configs

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
        if not isinstance(other, BasePathDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
