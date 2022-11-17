# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListChartsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'sql': 'str',
        'title': 'str',
        'type': 'str',
        'log_group_id': 'str',
        'log_group_name': 'str',
        'log_stream_id': 'str',
        'log_stream_name': 'str',
        'config': 'ChartConfig'
    }

    attribute_map = {
        'id': 'id',
        'sql': 'sql',
        'title': 'title',
        'type': 'type',
        'log_group_id': 'log_group_id',
        'log_group_name': 'log_group_name',
        'log_stream_id': 'log_stream_id',
        'log_stream_name': 'log_stream_name',
        'config': 'config'
    }

    def __init__(self, id=None, sql=None, title=None, type=None, log_group_id=None, log_group_name=None, log_stream_id=None, log_stream_name=None, config=None):
        """ListChartsResponse

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param sql: sql语句
        :type sql: str
        :param title: 图表名称
        :type title: str
        :param type: 图表类型
        :type type: str
        :param log_group_id: 日志组id
        :type log_group_id: str
        :param log_group_name: 日志组名称
        :type log_group_name: str
        :param log_stream_id: 日志组id
        :type log_stream_id: str
        :param log_stream_name: 日志流名称
        :type log_stream_name: str
        :param config: 图表配置详情
        :type config: :class:`huaweicloudsdklts.v2.ChartConfig`
        """
        
        super(ListChartsResponse, self).__init__()

        self._id = None
        self._sql = None
        self._title = None
        self._type = None
        self._log_group_id = None
        self._log_group_name = None
        self._log_stream_id = None
        self._log_stream_name = None
        self._config = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if sql is not None:
            self.sql = sql
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_group_name is not None:
            self.log_group_name = log_group_name
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if log_stream_name is not None:
            self.log_stream_name = log_stream_name
        if config is not None:
            self.config = config

    @property
    def id(self):
        """Gets the id of this ListChartsResponse.

        id

        :return: The id of this ListChartsResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListChartsResponse.

        id

        :param id: The id of this ListChartsResponse.
        :type id: str
        """
        self._id = id

    @property
    def sql(self):
        """Gets the sql of this ListChartsResponse.

        sql语句

        :return: The sql of this ListChartsResponse.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        """Sets the sql of this ListChartsResponse.

        sql语句

        :param sql: The sql of this ListChartsResponse.
        :type sql: str
        """
        self._sql = sql

    @property
    def title(self):
        """Gets the title of this ListChartsResponse.

        图表名称

        :return: The title of this ListChartsResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ListChartsResponse.

        图表名称

        :param title: The title of this ListChartsResponse.
        :type title: str
        """
        self._title = title

    @property
    def type(self):
        """Gets the type of this ListChartsResponse.

        图表类型

        :return: The type of this ListChartsResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListChartsResponse.

        图表类型

        :param type: The type of this ListChartsResponse.
        :type type: str
        """
        self._type = type

    @property
    def log_group_id(self):
        """Gets the log_group_id of this ListChartsResponse.

        日志组id

        :return: The log_group_id of this ListChartsResponse.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this ListChartsResponse.

        日志组id

        :param log_group_id: The log_group_id of this ListChartsResponse.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_group_name(self):
        """Gets the log_group_name of this ListChartsResponse.

        日志组名称

        :return: The log_group_name of this ListChartsResponse.
        :rtype: str
        """
        return self._log_group_name

    @log_group_name.setter
    def log_group_name(self, log_group_name):
        """Sets the log_group_name of this ListChartsResponse.

        日志组名称

        :param log_group_name: The log_group_name of this ListChartsResponse.
        :type log_group_name: str
        """
        self._log_group_name = log_group_name

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this ListChartsResponse.

        日志组id

        :return: The log_stream_id of this ListChartsResponse.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this ListChartsResponse.

        日志组id

        :param log_stream_id: The log_stream_id of this ListChartsResponse.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_stream_name(self):
        """Gets the log_stream_name of this ListChartsResponse.

        日志流名称

        :return: The log_stream_name of this ListChartsResponse.
        :rtype: str
        """
        return self._log_stream_name

    @log_stream_name.setter
    def log_stream_name(self, log_stream_name):
        """Sets the log_stream_name of this ListChartsResponse.

        日志流名称

        :param log_stream_name: The log_stream_name of this ListChartsResponse.
        :type log_stream_name: str
        """
        self._log_stream_name = log_stream_name

    @property
    def config(self):
        """Gets the config of this ListChartsResponse.

        图表配置详情

        :return: The config of this ListChartsResponse.
        :rtype: :class:`huaweicloudsdklts.v2.ChartConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this ListChartsResponse.

        图表配置详情

        :param config: The config of this ListChartsResponse.
        :type config: :class:`huaweicloudsdklts.v2.ChartConfig`
        """
        self._config = config

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
        if not isinstance(other, ListChartsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
