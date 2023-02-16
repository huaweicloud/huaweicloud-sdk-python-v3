# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLogSettingReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agency': 'str',
        'log_base_path': 'str',
        'log_bucket': 'str'
    }

    attribute_map = {
        'agency': 'agency',
        'log_base_path': 'logBasePath',
        'log_bucket': 'logBucket'
    }

    def __init__(self, agency=None, log_base_path=None, log_bucket=None):
        """UpdateLogSettingReq

        The model defined in huaweicloud sdk

        :param agency: 委托名称，委托给CSS，允许CSS调用您的其他云服务。
        :type agency: str
        :param log_base_path: 日志在OBS桶中的备份路径。
        :type log_base_path: str
        :param log_bucket: 用于存储日志的OBS桶的桶名。
        :type log_bucket: str
        """
        
        

        self._agency = None
        self._log_base_path = None
        self._log_bucket = None
        self.discriminator = None

        self.agency = agency
        self.log_base_path = log_base_path
        self.log_bucket = log_bucket

    @property
    def agency(self):
        """Gets the agency of this UpdateLogSettingReq.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。

        :return: The agency of this UpdateLogSettingReq.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        """Sets the agency of this UpdateLogSettingReq.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。

        :param agency: The agency of this UpdateLogSettingReq.
        :type agency: str
        """
        self._agency = agency

    @property
    def log_base_path(self):
        """Gets the log_base_path of this UpdateLogSettingReq.

        日志在OBS桶中的备份路径。

        :return: The log_base_path of this UpdateLogSettingReq.
        :rtype: str
        """
        return self._log_base_path

    @log_base_path.setter
    def log_base_path(self, log_base_path):
        """Sets the log_base_path of this UpdateLogSettingReq.

        日志在OBS桶中的备份路径。

        :param log_base_path: The log_base_path of this UpdateLogSettingReq.
        :type log_base_path: str
        """
        self._log_base_path = log_base_path

    @property
    def log_bucket(self):
        """Gets the log_bucket of this UpdateLogSettingReq.

        用于存储日志的OBS桶的桶名。

        :return: The log_bucket of this UpdateLogSettingReq.
        :rtype: str
        """
        return self._log_bucket

    @log_bucket.setter
    def log_bucket(self, log_bucket):
        """Sets the log_bucket of this UpdateLogSettingReq.

        用于存储日志的OBS桶的桶名。

        :param log_bucket: The log_bucket of this UpdateLogSettingReq.
        :type log_bucket: str
        """
        self._log_bucket = log_bucket

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
        if not isinstance(other, UpdateLogSettingReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
