# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLogDumpObsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'log_group_id': 'str',
        'log_stream_ids': 'list[str]',
        'obs_bucket_name': 'str',
        'type': 'str',
        'storage_format': 'str',
        'switch_on': 'bool',
        'prefix_name': 'str',
        'dir_prefix_name': 'str',
        'period': 'int',
        'period_unit': 'str'
    }

    attribute_map = {
        'log_group_id': 'log_group_id',
        'log_stream_ids': 'log_stream_ids',
        'obs_bucket_name': 'obs_bucket_name',
        'type': 'type',
        'storage_format': 'storage_format',
        'switch_on': 'switch_on',
        'prefix_name': 'prefix_name',
        'dir_prefix_name': 'dir_prefix_name',
        'period': 'period',
        'period_unit': 'period_unit'
    }

    def __init__(self, log_group_id=None, log_stream_ids=None, obs_bucket_name=None, type=None, storage_format=None, switch_on=None, prefix_name=None, dir_prefix_name=None, period=None, period_unit=None):
        """CreateLogDumpObsRequestBody

        The model defined in huaweicloud sdk

        :param log_group_id: 日志组id。
        :type log_group_id: str
        :param log_stream_ids: 日志流id列表, 可以指定一个或多个日志流进行obs周期性转储
        :type log_stream_ids: list[str]
        :param obs_bucket_name: obs 桶名称。
        :type obs_bucket_name: str
        :param type: 周期性转储, 必须填 cycle。
        :type type: str
        :param storage_format: 转储格式 RAW/JSON， 默认为 RAW。
        :type storage_format: str
        :param switch_on: 是否开启转储 true/false, 默认为 true
        :type switch_on: bool
        :param prefix_name: 转储至OBS桶中的日志文件前缀。
        :type prefix_name: str
        :param dir_prefix_name: 自定义文件夹路径。
        :type dir_prefix_name: str
        :param period: 转储周期的长度， 与 period_unit 拼接后必须在该列表中 [\&quot;2min\&quot;,\&quot;5min\&quot;,\&quot;30min\&quot;,\&quot;1hour\&quot;,\&quot;3hour\&quot;,\&quot;6hour\&quot;,\&quot;12hour\&quot;]。
        :type period: int
        :param period_unit: 转储周期的单位， 与 period 拼接后必须在该列表中 [\&quot;2min\&quot;,\&quot;5min\&quot;,\&quot;30min\&quot;,\&quot;1hour\&quot;,\&quot;3hour\&quot;,\&quot;6hour\&quot;,\&quot;12hour\&quot;]。
        :type period_unit: str
        """
        
        

        self._log_group_id = None
        self._log_stream_ids = None
        self._obs_bucket_name = None
        self._type = None
        self._storage_format = None
        self._switch_on = None
        self._prefix_name = None
        self._dir_prefix_name = None
        self._period = None
        self._period_unit = None
        self.discriminator = None

        self.log_group_id = log_group_id
        self.log_stream_ids = log_stream_ids
        self.obs_bucket_name = obs_bucket_name
        self.type = type
        self.storage_format = storage_format
        if switch_on is not None:
            self.switch_on = switch_on
        if prefix_name is not None:
            self.prefix_name = prefix_name
        if dir_prefix_name is not None:
            self.dir_prefix_name = dir_prefix_name
        self.period = period
        self.period_unit = period_unit

    @property
    def log_group_id(self):
        """Gets the log_group_id of this CreateLogDumpObsRequestBody.

        日志组id。

        :return: The log_group_id of this CreateLogDumpObsRequestBody.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this CreateLogDumpObsRequestBody.

        日志组id。

        :param log_group_id: The log_group_id of this CreateLogDumpObsRequestBody.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_ids(self):
        """Gets the log_stream_ids of this CreateLogDumpObsRequestBody.

        日志流id列表, 可以指定一个或多个日志流进行obs周期性转储

        :return: The log_stream_ids of this CreateLogDumpObsRequestBody.
        :rtype: list[str]
        """
        return self._log_stream_ids

    @log_stream_ids.setter
    def log_stream_ids(self, log_stream_ids):
        """Sets the log_stream_ids of this CreateLogDumpObsRequestBody.

        日志流id列表, 可以指定一个或多个日志流进行obs周期性转储

        :param log_stream_ids: The log_stream_ids of this CreateLogDumpObsRequestBody.
        :type log_stream_ids: list[str]
        """
        self._log_stream_ids = log_stream_ids

    @property
    def obs_bucket_name(self):
        """Gets the obs_bucket_name of this CreateLogDumpObsRequestBody.

        obs 桶名称。

        :return: The obs_bucket_name of this CreateLogDumpObsRequestBody.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        """Sets the obs_bucket_name of this CreateLogDumpObsRequestBody.

        obs 桶名称。

        :param obs_bucket_name: The obs_bucket_name of this CreateLogDumpObsRequestBody.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def type(self):
        """Gets the type of this CreateLogDumpObsRequestBody.

        周期性转储, 必须填 cycle。

        :return: The type of this CreateLogDumpObsRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateLogDumpObsRequestBody.

        周期性转储, 必须填 cycle。

        :param type: The type of this CreateLogDumpObsRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def storage_format(self):
        """Gets the storage_format of this CreateLogDumpObsRequestBody.

        转储格式 RAW/JSON， 默认为 RAW。

        :return: The storage_format of this CreateLogDumpObsRequestBody.
        :rtype: str
        """
        return self._storage_format

    @storage_format.setter
    def storage_format(self, storage_format):
        """Sets the storage_format of this CreateLogDumpObsRequestBody.

        转储格式 RAW/JSON， 默认为 RAW。

        :param storage_format: The storage_format of this CreateLogDumpObsRequestBody.
        :type storage_format: str
        """
        self._storage_format = storage_format

    @property
    def switch_on(self):
        """Gets the switch_on of this CreateLogDumpObsRequestBody.

        是否开启转储 true/false, 默认为 true

        :return: The switch_on of this CreateLogDumpObsRequestBody.
        :rtype: bool
        """
        return self._switch_on

    @switch_on.setter
    def switch_on(self, switch_on):
        """Sets the switch_on of this CreateLogDumpObsRequestBody.

        是否开启转储 true/false, 默认为 true

        :param switch_on: The switch_on of this CreateLogDumpObsRequestBody.
        :type switch_on: bool
        """
        self._switch_on = switch_on

    @property
    def prefix_name(self):
        """Gets the prefix_name of this CreateLogDumpObsRequestBody.

        转储至OBS桶中的日志文件前缀。

        :return: The prefix_name of this CreateLogDumpObsRequestBody.
        :rtype: str
        """
        return self._prefix_name

    @prefix_name.setter
    def prefix_name(self, prefix_name):
        """Sets the prefix_name of this CreateLogDumpObsRequestBody.

        转储至OBS桶中的日志文件前缀。

        :param prefix_name: The prefix_name of this CreateLogDumpObsRequestBody.
        :type prefix_name: str
        """
        self._prefix_name = prefix_name

    @property
    def dir_prefix_name(self):
        """Gets the dir_prefix_name of this CreateLogDumpObsRequestBody.

        自定义文件夹路径。

        :return: The dir_prefix_name of this CreateLogDumpObsRequestBody.
        :rtype: str
        """
        return self._dir_prefix_name

    @dir_prefix_name.setter
    def dir_prefix_name(self, dir_prefix_name):
        """Sets the dir_prefix_name of this CreateLogDumpObsRequestBody.

        自定义文件夹路径。

        :param dir_prefix_name: The dir_prefix_name of this CreateLogDumpObsRequestBody.
        :type dir_prefix_name: str
        """
        self._dir_prefix_name = dir_prefix_name

    @property
    def period(self):
        """Gets the period of this CreateLogDumpObsRequestBody.

        转储周期的长度， 与 period_unit 拼接后必须在该列表中 [\"2min\",\"5min\",\"30min\",\"1hour\",\"3hour\",\"6hour\",\"12hour\"]。

        :return: The period of this CreateLogDumpObsRequestBody.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this CreateLogDumpObsRequestBody.

        转储周期的长度， 与 period_unit 拼接后必须在该列表中 [\"2min\",\"5min\",\"30min\",\"1hour\",\"3hour\",\"6hour\",\"12hour\"]。

        :param period: The period of this CreateLogDumpObsRequestBody.
        :type period: int
        """
        self._period = period

    @property
    def period_unit(self):
        """Gets the period_unit of this CreateLogDumpObsRequestBody.

        转储周期的单位， 与 period 拼接后必须在该列表中 [\"2min\",\"5min\",\"30min\",\"1hour\",\"3hour\",\"6hour\",\"12hour\"]。

        :return: The period_unit of this CreateLogDumpObsRequestBody.
        :rtype: str
        """
        return self._period_unit

    @period_unit.setter
    def period_unit(self, period_unit):
        """Sets the period_unit of this CreateLogDumpObsRequestBody.

        转储周期的单位， 与 period 拼接后必须在该列表中 [\"2min\",\"5min\",\"30min\",\"1hour\",\"3hour\",\"6hour\",\"12hour\"]。

        :param period_unit: The period_unit of this CreateLogDumpObsRequestBody.
        :type period_unit: str
        """
        self._period_unit = period_unit

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
        if not isinstance(other, CreateLogDumpObsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
