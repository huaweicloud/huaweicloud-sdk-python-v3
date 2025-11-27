# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_key': 'str',
        'config_value': 'str',
        'config_status': 'str'
    }

    attribute_map = {
        'config_key': 'config_key',
        'config_value': 'config_value',
        'config_status': 'config_status'
    }

    def __init__(self, config_key=None, config_value=None, config_status=None):
        r"""ConfigBody

        The model defined in huaweicloud sdk

        :param config_key: 配置类型 MIGRATE_EXCLUDE_DIR: 迁移时设定的不迁移目录 SYNC_EXCLUDE_DIR: 同步时设定的不同步目录 ONLY_SYNC_DIR: 同步时设定的同步目录 CONSISTENCY_DIR: 一致性校验的目录 CONSISTENCY_DIR_ILLEGAL: 一致性校验后非法目录 LINUX_BLOCK_COMPRESS_THREAD_NUM: linux块迁移压缩线程个数 MIGRATE_DST_IP: 迁移目的ip LINUX_BLOCK_CACHE_SIZE: linux块迁移缓存大小 LINUX_CPU_LIMIT: linux的cpu限制 LINUX_MEM_LIMIT: linux的内存限制 LINUX_IO_LIMIT: linux的IO限制 NUM_PROCESS_MIGRATE: 迁移进程数 NUM_PROCESS_SYNC: 同步进程数 CONSISTENCY_RECHECK: 一致性校验再检 CONSISTENCY_MODE: 一致性校验模式 DYNAMIC_PORT: 动态端口
        :type config_key: str
        :param config_value: 具体配置参数字段，保存于数据库，最终在agent端进行解析
        :type config_value: str
        :param config_status: 描述配置状态的保留字段
        :type config_status: str
        """
        
        

        self._config_key = None
        self._config_value = None
        self._config_status = None
        self.discriminator = None

        self.config_key = config_key
        self.config_value = config_value
        if config_status is not None:
            self.config_status = config_status

    @property
    def config_key(self):
        r"""Gets the config_key of this ConfigBody.

        配置类型 MIGRATE_EXCLUDE_DIR: 迁移时设定的不迁移目录 SYNC_EXCLUDE_DIR: 同步时设定的不同步目录 ONLY_SYNC_DIR: 同步时设定的同步目录 CONSISTENCY_DIR: 一致性校验的目录 CONSISTENCY_DIR_ILLEGAL: 一致性校验后非法目录 LINUX_BLOCK_COMPRESS_THREAD_NUM: linux块迁移压缩线程个数 MIGRATE_DST_IP: 迁移目的ip LINUX_BLOCK_CACHE_SIZE: linux块迁移缓存大小 LINUX_CPU_LIMIT: linux的cpu限制 LINUX_MEM_LIMIT: linux的内存限制 LINUX_IO_LIMIT: linux的IO限制 NUM_PROCESS_MIGRATE: 迁移进程数 NUM_PROCESS_SYNC: 同步进程数 CONSISTENCY_RECHECK: 一致性校验再检 CONSISTENCY_MODE: 一致性校验模式 DYNAMIC_PORT: 动态端口

        :return: The config_key of this ConfigBody.
        :rtype: str
        """
        return self._config_key

    @config_key.setter
    def config_key(self, config_key):
        r"""Sets the config_key of this ConfigBody.

        配置类型 MIGRATE_EXCLUDE_DIR: 迁移时设定的不迁移目录 SYNC_EXCLUDE_DIR: 同步时设定的不同步目录 ONLY_SYNC_DIR: 同步时设定的同步目录 CONSISTENCY_DIR: 一致性校验的目录 CONSISTENCY_DIR_ILLEGAL: 一致性校验后非法目录 LINUX_BLOCK_COMPRESS_THREAD_NUM: linux块迁移压缩线程个数 MIGRATE_DST_IP: 迁移目的ip LINUX_BLOCK_CACHE_SIZE: linux块迁移缓存大小 LINUX_CPU_LIMIT: linux的cpu限制 LINUX_MEM_LIMIT: linux的内存限制 LINUX_IO_LIMIT: linux的IO限制 NUM_PROCESS_MIGRATE: 迁移进程数 NUM_PROCESS_SYNC: 同步进程数 CONSISTENCY_RECHECK: 一致性校验再检 CONSISTENCY_MODE: 一致性校验模式 DYNAMIC_PORT: 动态端口

        :param config_key: The config_key of this ConfigBody.
        :type config_key: str
        """
        self._config_key = config_key

    @property
    def config_value(self):
        r"""Gets the config_value of this ConfigBody.

        具体配置参数字段，保存于数据库，最终在agent端进行解析

        :return: The config_value of this ConfigBody.
        :rtype: str
        """
        return self._config_value

    @config_value.setter
    def config_value(self, config_value):
        r"""Sets the config_value of this ConfigBody.

        具体配置参数字段，保存于数据库，最终在agent端进行解析

        :param config_value: The config_value of this ConfigBody.
        :type config_value: str
        """
        self._config_value = config_value

    @property
    def config_status(self):
        r"""Gets the config_status of this ConfigBody.

        描述配置状态的保留字段

        :return: The config_status of this ConfigBody.
        :rtype: str
        """
        return self._config_status

    @config_status.setter
    def config_status(self, config_status):
        r"""Sets the config_status of this ConfigBody.

        描述配置状态的保留字段

        :param config_status: The config_status of this ConfigBody.
        :type config_status: str
        """
        self._config_status = config_status

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConfigBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
