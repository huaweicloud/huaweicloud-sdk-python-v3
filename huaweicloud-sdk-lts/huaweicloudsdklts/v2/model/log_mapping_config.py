# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogMappingConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_log_group_id': 'str',
        'target_log_group_id': 'str',
        'target_log_group_name': 'str',
        'log_stream_config': 'list[LogMappingStreamInfo]'
    }

    attribute_map = {
        'source_log_group_id': 'source_log_group_id',
        'target_log_group_id': 'target_log_group_id',
        'target_log_group_name': 'target_log_group_name',
        'log_stream_config': 'log_stream_config'
    }

    def __init__(self, source_log_group_id=None, target_log_group_id=None, target_log_group_name=None, log_stream_config=None):
        r"""LogMappingConfig

        The model defined in huaweicloud sdk

        :param source_log_group_id: 源日志组ID
        :type source_log_group_id: str
        :param target_log_group_id: 目标日志组ID
        :type target_log_group_id: str
        :param target_log_group_name: 目标日志组名称
        :type target_log_group_name: str
        :param log_stream_config: 日志流配置
        :type log_stream_config: list[:class:`huaweicloudsdklts.v2.LogMappingStreamInfo`]
        """
        
        

        self._source_log_group_id = None
        self._target_log_group_id = None
        self._target_log_group_name = None
        self._log_stream_config = None
        self.discriminator = None

        self.source_log_group_id = source_log_group_id
        if target_log_group_id is not None:
            self.target_log_group_id = target_log_group_id
        self.target_log_group_name = target_log_group_name
        if log_stream_config is not None:
            self.log_stream_config = log_stream_config

    @property
    def source_log_group_id(self):
        r"""Gets the source_log_group_id of this LogMappingConfig.

        源日志组ID

        :return: The source_log_group_id of this LogMappingConfig.
        :rtype: str
        """
        return self._source_log_group_id

    @source_log_group_id.setter
    def source_log_group_id(self, source_log_group_id):
        r"""Sets the source_log_group_id of this LogMappingConfig.

        源日志组ID

        :param source_log_group_id: The source_log_group_id of this LogMappingConfig.
        :type source_log_group_id: str
        """
        self._source_log_group_id = source_log_group_id

    @property
    def target_log_group_id(self):
        r"""Gets the target_log_group_id of this LogMappingConfig.

        目标日志组ID

        :return: The target_log_group_id of this LogMappingConfig.
        :rtype: str
        """
        return self._target_log_group_id

    @target_log_group_id.setter
    def target_log_group_id(self, target_log_group_id):
        r"""Sets the target_log_group_id of this LogMappingConfig.

        目标日志组ID

        :param target_log_group_id: The target_log_group_id of this LogMappingConfig.
        :type target_log_group_id: str
        """
        self._target_log_group_id = target_log_group_id

    @property
    def target_log_group_name(self):
        r"""Gets the target_log_group_name of this LogMappingConfig.

        目标日志组名称

        :return: The target_log_group_name of this LogMappingConfig.
        :rtype: str
        """
        return self._target_log_group_name

    @target_log_group_name.setter
    def target_log_group_name(self, target_log_group_name):
        r"""Sets the target_log_group_name of this LogMappingConfig.

        目标日志组名称

        :param target_log_group_name: The target_log_group_name of this LogMappingConfig.
        :type target_log_group_name: str
        """
        self._target_log_group_name = target_log_group_name

    @property
    def log_stream_config(self):
        r"""Gets the log_stream_config of this LogMappingConfig.

        日志流配置

        :return: The log_stream_config of this LogMappingConfig.
        :rtype: list[:class:`huaweicloudsdklts.v2.LogMappingStreamInfo`]
        """
        return self._log_stream_config

    @log_stream_config.setter
    def log_stream_config(self, log_stream_config):
        r"""Sets the log_stream_config of this LogMappingConfig.

        日志流配置

        :param log_stream_config: The log_stream_config of this LogMappingConfig.
        :type log_stream_config: list[:class:`huaweicloudsdklts.v2.LogMappingStreamInfo`]
        """
        self._log_stream_config = log_stream_config

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
        if not isinstance(other, LogMappingConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
