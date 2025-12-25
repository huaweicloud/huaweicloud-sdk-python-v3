# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LtsRquestVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_name': 'str',
        'description': 'str',
        'enable': 'str',
        'log_group_id': 'str',
        'log_stream_id': 'str',
        'log_type': 'str',
        'log_type_prefix': 'str',
        'pipe_alias': 'str'
    }

    attribute_map = {
        'config_name': 'config_name',
        'description': 'description',
        'enable': 'enable',
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id',
        'log_type': 'log_type',
        'log_type_prefix': 'log_type_prefix',
        'pipe_alias': 'pipe_alias'
    }

    def __init__(self, config_name=None, description=None, enable=None, log_group_id=None, log_stream_id=None, log_type=None, log_type_prefix=None, pipe_alias=None):
        r"""LtsRquestVo

        The model defined in huaweicloud sdk

        :param config_name: 配置名称
        :type config_name: str
        :param description: 描述
        :type description: str
        :param enable: 是否开启
        :type enable: str
        :param log_group_id: 日志ID
        :type log_group_id: str
        :param log_stream_id: 日志流ID
        :type log_stream_id: str
        :param log_type: 日志类型
        :type log_type: str
        :param log_type_prefix: 日志前缀
        :type log_type_prefix: str
        :param pipe_alias: 日志别名
        :type pipe_alias: str
        """
        
        

        self._config_name = None
        self._description = None
        self._enable = None
        self._log_group_id = None
        self._log_stream_id = None
        self._log_type = None
        self._log_type_prefix = None
        self._pipe_alias = None
        self.discriminator = None

        if config_name is not None:
            self.config_name = config_name
        if description is not None:
            self.description = description
        if enable is not None:
            self.enable = enable
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if log_type is not None:
            self.log_type = log_type
        if log_type_prefix is not None:
            self.log_type_prefix = log_type_prefix
        if pipe_alias is not None:
            self.pipe_alias = pipe_alias

    @property
    def config_name(self):
        r"""Gets the config_name of this LtsRquestVo.

        配置名称

        :return: The config_name of this LtsRquestVo.
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        r"""Sets the config_name of this LtsRquestVo.

        配置名称

        :param config_name: The config_name of this LtsRquestVo.
        :type config_name: str
        """
        self._config_name = config_name

    @property
    def description(self):
        r"""Gets the description of this LtsRquestVo.

        描述

        :return: The description of this LtsRquestVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this LtsRquestVo.

        描述

        :param description: The description of this LtsRquestVo.
        :type description: str
        """
        self._description = description

    @property
    def enable(self):
        r"""Gets the enable of this LtsRquestVo.

        是否开启

        :return: The enable of this LtsRquestVo.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this LtsRquestVo.

        是否开启

        :param enable: The enable of this LtsRquestVo.
        :type enable: str
        """
        self._enable = enable

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this LtsRquestVo.

        日志ID

        :return: The log_group_id of this LtsRquestVo.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this LtsRquestVo.

        日志ID

        :param log_group_id: The log_group_id of this LtsRquestVo.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this LtsRquestVo.

        日志流ID

        :return: The log_stream_id of this LtsRquestVo.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this LtsRquestVo.

        日志流ID

        :param log_stream_id: The log_stream_id of this LtsRquestVo.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_type(self):
        r"""Gets the log_type of this LtsRquestVo.

        日志类型

        :return: The log_type of this LtsRquestVo.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        r"""Sets the log_type of this LtsRquestVo.

        日志类型

        :param log_type: The log_type of this LtsRquestVo.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def log_type_prefix(self):
        r"""Gets the log_type_prefix of this LtsRquestVo.

        日志前缀

        :return: The log_type_prefix of this LtsRquestVo.
        :rtype: str
        """
        return self._log_type_prefix

    @log_type_prefix.setter
    def log_type_prefix(self, log_type_prefix):
        r"""Sets the log_type_prefix of this LtsRquestVo.

        日志前缀

        :param log_type_prefix: The log_type_prefix of this LtsRquestVo.
        :type log_type_prefix: str
        """
        self._log_type_prefix = log_type_prefix

    @property
    def pipe_alias(self):
        r"""Gets the pipe_alias of this LtsRquestVo.

        日志别名

        :return: The pipe_alias of this LtsRquestVo.
        :rtype: str
        """
        return self._pipe_alias

    @pipe_alias.setter
    def pipe_alias(self, pipe_alias):
        r"""Sets the pipe_alias of this LtsRquestVo.

        日志别名

        :param pipe_alias: The pipe_alias of this LtsRquestVo.
        :type pipe_alias: str
        """
        self._pipe_alias = pipe_alias

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
        if not isinstance(other, LtsRquestVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
