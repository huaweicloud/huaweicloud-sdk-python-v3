# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetLogBackupReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_name': 'str',
        'level': 'str',
        'log_type': 'str',
        'limit': 'int',
        'time_index': 'str',
        'keyword': 'str'
    }

    attribute_map = {
        'instance_name': 'instance_name',
        'level': 'level',
        'log_type': 'log_type',
        'limit': 'limit',
        'time_index': 'time_index',
        'keyword': 'keyword'
    }

    def __init__(self, instance_name=None, level=None, log_type=None, limit=None, time_index=None, keyword=None):
        r"""GetLogBackupReq

        The model defined in huaweicloud sdk

        :param instance_name: 节点名称。通过[查询集群详情](ShowClusterDetail.xml)获取instances中的name属性。
        :type instance_name: str
        :param level: 日志级别。可查询的日志级别为：INFO，ERROR，DEBUG，WARN。
        :type level: str
        :param log_type: 日志类型。可查询的日志类型为：deprecation，indexingSlow，searchSlow， instance。
        :type log_type: str
        :param limit: 指定返回日志的条数，默认返回100条，最大返回10000条日志，且日志大小不超过1MB。
        :type limit: int
        :param time_index: 返回指定时间之前的日志。
        :type time_index: str
        :param keyword: 基于日志内容字段值需要过滤的关键字，注意搜索到的日志包含关键字。
        :type keyword: str
        """
        
        

        self._instance_name = None
        self._level = None
        self._log_type = None
        self._limit = None
        self._time_index = None
        self._keyword = None
        self.discriminator = None

        self.instance_name = instance_name
        self.level = level
        self.log_type = log_type
        if limit is not None:
            self.limit = limit
        if time_index is not None:
            self.time_index = time_index
        if keyword is not None:
            self.keyword = keyword

    @property
    def instance_name(self):
        r"""Gets the instance_name of this GetLogBackupReq.

        节点名称。通过[查询集群详情](ShowClusterDetail.xml)获取instances中的name属性。

        :return: The instance_name of this GetLogBackupReq.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this GetLogBackupReq.

        节点名称。通过[查询集群详情](ShowClusterDetail.xml)获取instances中的name属性。

        :param instance_name: The instance_name of this GetLogBackupReq.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def level(self):
        r"""Gets the level of this GetLogBackupReq.

        日志级别。可查询的日志级别为：INFO，ERROR，DEBUG，WARN。

        :return: The level of this GetLogBackupReq.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this GetLogBackupReq.

        日志级别。可查询的日志级别为：INFO，ERROR，DEBUG，WARN。

        :param level: The level of this GetLogBackupReq.
        :type level: str
        """
        self._level = level

    @property
    def log_type(self):
        r"""Gets the log_type of this GetLogBackupReq.

        日志类型。可查询的日志类型为：deprecation，indexingSlow，searchSlow， instance。

        :return: The log_type of this GetLogBackupReq.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        r"""Sets the log_type of this GetLogBackupReq.

        日志类型。可查询的日志类型为：deprecation，indexingSlow，searchSlow， instance。

        :param log_type: The log_type of this GetLogBackupReq.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def limit(self):
        r"""Gets the limit of this GetLogBackupReq.

        指定返回日志的条数，默认返回100条，最大返回10000条日志，且日志大小不超过1MB。

        :return: The limit of this GetLogBackupReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this GetLogBackupReq.

        指定返回日志的条数，默认返回100条，最大返回10000条日志，且日志大小不超过1MB。

        :param limit: The limit of this GetLogBackupReq.
        :type limit: int
        """
        self._limit = limit

    @property
    def time_index(self):
        r"""Gets the time_index of this GetLogBackupReq.

        返回指定时间之前的日志。

        :return: The time_index of this GetLogBackupReq.
        :rtype: str
        """
        return self._time_index

    @time_index.setter
    def time_index(self, time_index):
        r"""Sets the time_index of this GetLogBackupReq.

        返回指定时间之前的日志。

        :param time_index: The time_index of this GetLogBackupReq.
        :type time_index: str
        """
        self._time_index = time_index

    @property
    def keyword(self):
        r"""Gets the keyword of this GetLogBackupReq.

        基于日志内容字段值需要过滤的关键字，注意搜索到的日志包含关键字。

        :return: The keyword of this GetLogBackupReq.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this GetLogBackupReq.

        基于日志内容字段值需要过滤的关键字，注意搜索到的日志包含关键字。

        :param keyword: The keyword of this GetLogBackupReq.
        :type keyword: str
        """
        self._keyword = keyword

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
        if not isinstance(other, GetLogBackupReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
