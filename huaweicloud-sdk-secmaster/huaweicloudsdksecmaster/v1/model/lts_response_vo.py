# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LtsResponseVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_id': 'str',
        'config_name': 'str',
        'enable': 'str',
        'log_group_id': 'str',
        'log_stream_id': 'str',
        'log_type': 'str',
        'log_types': 'LtsResponseVoLogTypes',
        'lts_infos': 'list[LtsResponseVoLtsInfos]',
        'pipe_alias': 'str',
        'type_prefix': 'str'
    }

    attribute_map = {
        'config_id': 'config_id',
        'config_name': 'config_name',
        'enable': 'enable',
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id',
        'log_type': 'log_type',
        'log_types': 'log_types',
        'lts_infos': 'lts_infos',
        'pipe_alias': 'pipe_alias',
        'type_prefix': 'type_prefix'
    }

    def __init__(self, config_id=None, config_name=None, enable=None, log_group_id=None, log_stream_id=None, log_type=None, log_types=None, lts_infos=None, pipe_alias=None, type_prefix=None):
        r"""LtsResponseVo

        The model defined in huaweicloud sdk

        :param config_id: 配置id
        :type config_id: str
        :param config_name: 配置名称
        :type config_name: str
        :param enable: 是否开启
        :type enable: str
        :param log_group_id: 日志组Id
        :type log_group_id: str
        :param log_stream_id: 日志流ID
        :type log_stream_id: str
        :param log_type: 日志类型
        :type log_type: str
        :param log_types: 
        :type log_types: :class:`huaweicloudsdksecmaster.v1.LtsResponseVoLogTypes`
        :param lts_infos: lts日志信息map
        :type lts_infos: list[:class:`huaweicloudsdksecmaster.v1.LtsResponseVoLtsInfos`]
        :param pipe_alias: 管道别名
        :type pipe_alias: str
        :param type_prefix: 类型前缀
        :type type_prefix: str
        """
        
        

        self._config_id = None
        self._config_name = None
        self._enable = None
        self._log_group_id = None
        self._log_stream_id = None
        self._log_type = None
        self._log_types = None
        self._lts_infos = None
        self._pipe_alias = None
        self._type_prefix = None
        self.discriminator = None

        if config_id is not None:
            self.config_id = config_id
        if config_name is not None:
            self.config_name = config_name
        if enable is not None:
            self.enable = enable
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if log_type is not None:
            self.log_type = log_type
        if log_types is not None:
            self.log_types = log_types
        if lts_infos is not None:
            self.lts_infos = lts_infos
        if pipe_alias is not None:
            self.pipe_alias = pipe_alias
        if type_prefix is not None:
            self.type_prefix = type_prefix

    @property
    def config_id(self):
        r"""Gets the config_id of this LtsResponseVo.

        配置id

        :return: The config_id of this LtsResponseVo.
        :rtype: str
        """
        return self._config_id

    @config_id.setter
    def config_id(self, config_id):
        r"""Sets the config_id of this LtsResponseVo.

        配置id

        :param config_id: The config_id of this LtsResponseVo.
        :type config_id: str
        """
        self._config_id = config_id

    @property
    def config_name(self):
        r"""Gets the config_name of this LtsResponseVo.

        配置名称

        :return: The config_name of this LtsResponseVo.
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        r"""Sets the config_name of this LtsResponseVo.

        配置名称

        :param config_name: The config_name of this LtsResponseVo.
        :type config_name: str
        """
        self._config_name = config_name

    @property
    def enable(self):
        r"""Gets the enable of this LtsResponseVo.

        是否开启

        :return: The enable of this LtsResponseVo.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this LtsResponseVo.

        是否开启

        :param enable: The enable of this LtsResponseVo.
        :type enable: str
        """
        self._enable = enable

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this LtsResponseVo.

        日志组Id

        :return: The log_group_id of this LtsResponseVo.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this LtsResponseVo.

        日志组Id

        :param log_group_id: The log_group_id of this LtsResponseVo.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this LtsResponseVo.

        日志流ID

        :return: The log_stream_id of this LtsResponseVo.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this LtsResponseVo.

        日志流ID

        :param log_stream_id: The log_stream_id of this LtsResponseVo.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_type(self):
        r"""Gets the log_type of this LtsResponseVo.

        日志类型

        :return: The log_type of this LtsResponseVo.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        r"""Sets the log_type of this LtsResponseVo.

        日志类型

        :param log_type: The log_type of this LtsResponseVo.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def log_types(self):
        r"""Gets the log_types of this LtsResponseVo.

        :return: The log_types of this LtsResponseVo.
        :rtype: :class:`huaweicloudsdksecmaster.v1.LtsResponseVoLogTypes`
        """
        return self._log_types

    @log_types.setter
    def log_types(self, log_types):
        r"""Sets the log_types of this LtsResponseVo.

        :param log_types: The log_types of this LtsResponseVo.
        :type log_types: :class:`huaweicloudsdksecmaster.v1.LtsResponseVoLogTypes`
        """
        self._log_types = log_types

    @property
    def lts_infos(self):
        r"""Gets the lts_infos of this LtsResponseVo.

        lts日志信息map

        :return: The lts_infos of this LtsResponseVo.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.LtsResponseVoLtsInfos`]
        """
        return self._lts_infos

    @lts_infos.setter
    def lts_infos(self, lts_infos):
        r"""Sets the lts_infos of this LtsResponseVo.

        lts日志信息map

        :param lts_infos: The lts_infos of this LtsResponseVo.
        :type lts_infos: list[:class:`huaweicloudsdksecmaster.v1.LtsResponseVoLtsInfos`]
        """
        self._lts_infos = lts_infos

    @property
    def pipe_alias(self):
        r"""Gets the pipe_alias of this LtsResponseVo.

        管道别名

        :return: The pipe_alias of this LtsResponseVo.
        :rtype: str
        """
        return self._pipe_alias

    @pipe_alias.setter
    def pipe_alias(self, pipe_alias):
        r"""Sets the pipe_alias of this LtsResponseVo.

        管道别名

        :param pipe_alias: The pipe_alias of this LtsResponseVo.
        :type pipe_alias: str
        """
        self._pipe_alias = pipe_alias

    @property
    def type_prefix(self):
        r"""Gets the type_prefix of this LtsResponseVo.

        类型前缀

        :return: The type_prefix of this LtsResponseVo.
        :rtype: str
        """
        return self._type_prefix

    @type_prefix.setter
    def type_prefix(self, type_prefix):
        r"""Sets the type_prefix of this LtsResponseVo.

        类型前缀

        :param type_prefix: The type_prefix of this LtsResponseVo.
        :type type_prefix: str
        """
        self._type_prefix = type_prefix

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
        if not isinstance(other, LtsResponseVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
