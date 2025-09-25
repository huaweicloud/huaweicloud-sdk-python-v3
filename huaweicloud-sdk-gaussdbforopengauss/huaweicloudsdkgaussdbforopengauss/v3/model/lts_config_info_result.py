# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LtsConfigInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_group_name': 'str',
        'log_group_id': 'str',
        'group_log_type': 'str',
        'group_ttl_in_days': 'int',
        'log_stream_name': 'str',
        'log_stream_id': 'str',
        'stream_log_type': 'str',
        'stream_ttl_in_days': 'int',
        'stream_structure_config_id': 'str',
        'stream_index_config_id': 'str'
    }

    attribute_map = {
        'log_group_name': 'log_group_name',
        'log_group_id': 'log_group_id',
        'group_log_type': 'group_log_type',
        'group_ttl_in_days': 'group_ttl_in_days',
        'log_stream_name': 'log_stream_name',
        'log_stream_id': 'log_stream_id',
        'stream_log_type': 'stream_log_type',
        'stream_ttl_in_days': 'stream_ttl_in_days',
        'stream_structure_config_id': 'stream_structure_config_id',
        'stream_index_config_id': 'stream_index_config_id'
    }

    def __init__(self, log_group_name=None, log_group_id=None, group_log_type=None, group_ttl_in_days=None, log_stream_name=None, log_stream_id=None, stream_log_type=None, stream_ttl_in_days=None, stream_structure_config_id=None, stream_index_config_id=None):
        r"""LtsConfigInfoResult

        The model defined in huaweicloud sdk

        :param log_group_name: **参数解释**: LTS日志组名称。 **取值范围**: 不涉及。
        :type log_group_name: str
        :param log_group_id: **参数解释**: LTS日志组ID。 **取值范围**: 不涉及。LTS日志组ID
        :type log_group_id: str
        :param group_log_type: **参数解释**: LTS日志组类别。 **取值范围**: 通常为asp_log，标识为智能运维专用日志组。
        :type group_log_type: str
        :param group_ttl_in_days: **参数解释**: LTS日志组中数据最大保留天数。 **取值范围**: [1,30]
        :type group_ttl_in_days: int
        :param log_stream_name: **参数解释**: LTS日志流名称。 **取值范围**: 通常为STREAM_APS_FULL_SQL-实例ID。
        :type log_stream_name: str
        :param log_stream_id: **参数解释**: LTS日志流ID。 **取值范围**: 不涉及。
        :type log_stream_id: str
        :param stream_log_type: **参数解释**: LTS日志流类别。 **取值范围**: 通常为full_sql，标识为全量SQL专用日志流。
        :type stream_log_type: str
        :param stream_ttl_in_days: **参数解释**: LTS日志流中数据最大保留天数。 **取值范围**: [1,30]
        :type stream_ttl_in_days: int
        :param stream_structure_config_id: **参数解释**: LTS日志流结构化配置ID。 **取值范围**: 不涉及。
        :type stream_structure_config_id: str
        :param stream_index_config_id: **参数解释**: LTS日志流索引配置ID。 **取值范围**: 不涉及。
        :type stream_index_config_id: str
        """
        
        

        self._log_group_name = None
        self._log_group_id = None
        self._group_log_type = None
        self._group_ttl_in_days = None
        self._log_stream_name = None
        self._log_stream_id = None
        self._stream_log_type = None
        self._stream_ttl_in_days = None
        self._stream_structure_config_id = None
        self._stream_index_config_id = None
        self.discriminator = None

        if log_group_name is not None:
            self.log_group_name = log_group_name
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if group_log_type is not None:
            self.group_log_type = group_log_type
        if group_ttl_in_days is not None:
            self.group_ttl_in_days = group_ttl_in_days
        if log_stream_name is not None:
            self.log_stream_name = log_stream_name
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if stream_log_type is not None:
            self.stream_log_type = stream_log_type
        if stream_ttl_in_days is not None:
            self.stream_ttl_in_days = stream_ttl_in_days
        if stream_structure_config_id is not None:
            self.stream_structure_config_id = stream_structure_config_id
        if stream_index_config_id is not None:
            self.stream_index_config_id = stream_index_config_id

    @property
    def log_group_name(self):
        r"""Gets the log_group_name of this LtsConfigInfoResult.

        **参数解释**: LTS日志组名称。 **取值范围**: 不涉及。

        :return: The log_group_name of this LtsConfigInfoResult.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        r"""Sets the log_group_name of this LtsConfigInfoResult.

        **参数解释**: LTS日志组名称。 **取值范围**: 不涉及。

        :param log_group_name: The log_group_name of this LtsConfigInfoResult.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this LtsConfigInfoResult.

        **参数解释**: LTS日志组ID。 **取值范围**: 不涉及。LTS日志组ID

        :return: The log_group_id of this LtsConfigInfoResult.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this LtsConfigInfoResult.

        **参数解释**: LTS日志组ID。 **取值范围**: 不涉及。LTS日志组ID

        :param log_group_id: The log_group_id of this LtsConfigInfoResult.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def group_log_type(self):
        r"""Gets the group_log_type of this LtsConfigInfoResult.

        **参数解释**: LTS日志组类别。 **取值范围**: 通常为asp_log，标识为智能运维专用日志组。

        :return: The group_log_type of this LtsConfigInfoResult.
        :rtype: str
        """
        return self._group_log_type

    @group_log_type.setter
    def group_log_type(self, group_log_type):
        r"""Sets the group_log_type of this LtsConfigInfoResult.

        **参数解释**: LTS日志组类别。 **取值范围**: 通常为asp_log，标识为智能运维专用日志组。

        :param group_log_type: The group_log_type of this LtsConfigInfoResult.
        :type group_log_type: str
        """
        self._group_log_type = group_log_type

    @property
    def group_ttl_in_days(self):
        r"""Gets the group_ttl_in_days of this LtsConfigInfoResult.

        **参数解释**: LTS日志组中数据最大保留天数。 **取值范围**: [1,30]

        :return: The group_ttl_in_days of this LtsConfigInfoResult.
        :rtype: int
        """
        return self._group_ttl_in_days

    @group_ttl_in_days.setter
    def group_ttl_in_days(self, group_ttl_in_days):
        r"""Sets the group_ttl_in_days of this LtsConfigInfoResult.

        **参数解释**: LTS日志组中数据最大保留天数。 **取值范围**: [1,30]

        :param group_ttl_in_days: The group_ttl_in_days of this LtsConfigInfoResult.
        :type group_ttl_in_days: int
        """
        self._group_ttl_in_days = group_ttl_in_days

    @property
    def log_stream_name(self):
        r"""Gets the log_stream_name of this LtsConfigInfoResult.

        **参数解释**: LTS日志流名称。 **取值范围**: 通常为STREAM_APS_FULL_SQL-实例ID。

        :return: The log_stream_name of this LtsConfigInfoResult.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        r"""Sets the log_stream_name of this LtsConfigInfoResult.

        **参数解释**: LTS日志流名称。 **取值范围**: 通常为STREAM_APS_FULL_SQL-实例ID。

        :param log_stream_name: The log_stream_name of this LtsConfigInfoResult.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this LtsConfigInfoResult.

        **参数解释**: LTS日志流ID。 **取值范围**: 不涉及。

        :return: The log_stream_id of this LtsConfigInfoResult.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this LtsConfigInfoResult.

        **参数解释**: LTS日志流ID。 **取值范围**: 不涉及。

        :param log_stream_id: The log_stream_id of this LtsConfigInfoResult.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def stream_log_type(self):
        r"""Gets the stream_log_type of this LtsConfigInfoResult.

        **参数解释**: LTS日志流类别。 **取值范围**: 通常为full_sql，标识为全量SQL专用日志流。

        :return: The stream_log_type of this LtsConfigInfoResult.
        :rtype: str
        """
        return self._stream_log_type

    @stream_log_type.setter
    def stream_log_type(self, stream_log_type):
        r"""Sets the stream_log_type of this LtsConfigInfoResult.

        **参数解释**: LTS日志流类别。 **取值范围**: 通常为full_sql，标识为全量SQL专用日志流。

        :param stream_log_type: The stream_log_type of this LtsConfigInfoResult.
        :type stream_log_type: str
        """
        self._stream_log_type = stream_log_type

    @property
    def stream_ttl_in_days(self):
        r"""Gets the stream_ttl_in_days of this LtsConfigInfoResult.

        **参数解释**: LTS日志流中数据最大保留天数。 **取值范围**: [1,30]

        :return: The stream_ttl_in_days of this LtsConfigInfoResult.
        :rtype: int
        """
        return self._stream_ttl_in_days

    @stream_ttl_in_days.setter
    def stream_ttl_in_days(self, stream_ttl_in_days):
        r"""Sets the stream_ttl_in_days of this LtsConfigInfoResult.

        **参数解释**: LTS日志流中数据最大保留天数。 **取值范围**: [1,30]

        :param stream_ttl_in_days: The stream_ttl_in_days of this LtsConfigInfoResult.
        :type stream_ttl_in_days: int
        """
        self._stream_ttl_in_days = stream_ttl_in_days

    @property
    def stream_structure_config_id(self):
        r"""Gets the stream_structure_config_id of this LtsConfigInfoResult.

        **参数解释**: LTS日志流结构化配置ID。 **取值范围**: 不涉及。

        :return: The stream_structure_config_id of this LtsConfigInfoResult.
        :rtype: str
        """
        return self._stream_structure_config_id

    @stream_structure_config_id.setter
    def stream_structure_config_id(self, stream_structure_config_id):
        r"""Sets the stream_structure_config_id of this LtsConfigInfoResult.

        **参数解释**: LTS日志流结构化配置ID。 **取值范围**: 不涉及。

        :param stream_structure_config_id: The stream_structure_config_id of this LtsConfigInfoResult.
        :type stream_structure_config_id: str
        """
        self._stream_structure_config_id = stream_structure_config_id

    @property
    def stream_index_config_id(self):
        r"""Gets the stream_index_config_id of this LtsConfigInfoResult.

        **参数解释**: LTS日志流索引配置ID。 **取值范围**: 不涉及。

        :return: The stream_index_config_id of this LtsConfigInfoResult.
        :rtype: str
        """
        return self._stream_index_config_id

    @stream_index_config_id.setter
    def stream_index_config_id(self, stream_index_config_id):
        r"""Sets the stream_index_config_id of this LtsConfigInfoResult.

        **参数解释**: LTS日志流索引配置ID。 **取值范围**: 不涉及。

        :param stream_index_config_id: The stream_index_config_id of this LtsConfigInfoResult.
        :type stream_index_config_id: str
        """
        self._stream_index_config_id = stream_index_config_id

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
        if not isinstance(other, LtsConfigInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
