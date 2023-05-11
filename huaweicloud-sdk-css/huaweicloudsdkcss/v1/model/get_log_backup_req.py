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
        'log_type': 'str'
    }

    attribute_map = {
        'instance_name': 'instanceName',
        'level': 'level',
        'log_type': 'logType'
    }

    def __init__(self, instance_name=None, level=None, log_type=None):
        """GetLogBackupReq

        The model defined in huaweicloud sdk

        :param instance_name: 节点名称。通过[查询集群详情](ShowClusterDetail.xml)获取instances中的name属性。
        :type instance_name: str
        :param level: 日志级别。可查询的日志级别为：INFO，ERROR，DEBUG，WARN。
        :type level: str
        :param log_type: 日志类型。可查询的日志类型为：deprecation，indexingSlow，searchSlow， instance。
        :type log_type: str
        """
        
        

        self._instance_name = None
        self._level = None
        self._log_type = None
        self.discriminator = None

        self.instance_name = instance_name
        self.level = level
        self.log_type = log_type

    @property
    def instance_name(self):
        """Gets the instance_name of this GetLogBackupReq.

        节点名称。通过[查询集群详情](ShowClusterDetail.xml)获取instances中的name属性。

        :return: The instance_name of this GetLogBackupReq.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this GetLogBackupReq.

        节点名称。通过[查询集群详情](ShowClusterDetail.xml)获取instances中的name属性。

        :param instance_name: The instance_name of this GetLogBackupReq.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def level(self):
        """Gets the level of this GetLogBackupReq.

        日志级别。可查询的日志级别为：INFO，ERROR，DEBUG，WARN。

        :return: The level of this GetLogBackupReq.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this GetLogBackupReq.

        日志级别。可查询的日志级别为：INFO，ERROR，DEBUG，WARN。

        :param level: The level of this GetLogBackupReq.
        :type level: str
        """
        self._level = level

    @property
    def log_type(self):
        """Gets the log_type of this GetLogBackupReq.

        日志类型。可查询的日志类型为：deprecation，indexingSlow，searchSlow， instance。

        :return: The log_type of this GetLogBackupReq.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        """Sets the log_type of this GetLogBackupReq.

        日志类型。可查询的日志类型为：deprecation，indexingSlow，searchSlow， instance。

        :param log_type: The log_type of this GetLogBackupReq.
        :type log_type: str
        """
        self._log_type = log_type

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
