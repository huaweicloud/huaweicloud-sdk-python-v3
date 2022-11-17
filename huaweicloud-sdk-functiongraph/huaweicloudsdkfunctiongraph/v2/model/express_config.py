# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExpressConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_level': 'str'
    }

    attribute_map = {
        'log_level': 'log_level'
    }

    def __init__(self, log_level=None):
        """ExpressConfig

        The model defined in huaweicloud sdk

        :param log_level: 快速模式相关配置，仅在mode配置为EXPRESS时生效 快速模式下流程的执行日志级别，当前支持： ALL: 记录所有节点的执行日志 ERROR：仅记录异常节点执行日志 NONE：不记录日志 注意：当配置为ALL和ERROR级别时租户需要开启LTS相关权限
        :type log_level: str
        """
        
        

        self._log_level = None
        self.discriminator = None

        if log_level is not None:
            self.log_level = log_level

    @property
    def log_level(self):
        """Gets the log_level of this ExpressConfig.

        快速模式相关配置，仅在mode配置为EXPRESS时生效 快速模式下流程的执行日志级别，当前支持： ALL: 记录所有节点的执行日志 ERROR：仅记录异常节点执行日志 NONE：不记录日志 注意：当配置为ALL和ERROR级别时租户需要开启LTS相关权限

        :return: The log_level of this ExpressConfig.
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this ExpressConfig.

        快速模式相关配置，仅在mode配置为EXPRESS时生效 快速模式下流程的执行日志级别，当前支持： ALL: 记录所有节点的执行日志 ERROR：仅记录异常节点执行日志 NONE：不记录日志 注意：当配置为ALL和ERROR级别时租户需要开启LTS相关权限

        :param log_level: The log_level of this ExpressConfig.
        :type log_level: str
        """
        self._log_level = log_level

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
        if not isinstance(other, ExpressConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
