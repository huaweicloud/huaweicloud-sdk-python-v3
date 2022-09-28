# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobLogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'logs': 'list[LogContentDto]',
        'log_storage_link': 'str'
    }

    attribute_map = {
        'count': 'count',
        'logs': 'logs',
        'log_storage_link': 'log_storage_link'
    }

    def __init__(self, count=None, logs=None, log_storage_link=None):
        """ShowJobLogResponse

        The model defined in huaweicloud sdk

        :param count: 作业日志条数
        :type count: int
        :param logs: 作业日志内容列表
        :type logs: list[:class:`huaweicloudsdkeihealth.v1.LogContentDto`]
        :param log_storage_link: 作业日志存储链接
        :type log_storage_link: str
        """
        
        super(ShowJobLogResponse, self).__init__()

        self._count = None
        self._logs = None
        self._log_storage_link = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if logs is not None:
            self.logs = logs
        if log_storage_link is not None:
            self.log_storage_link = log_storage_link

    @property
    def count(self):
        """Gets the count of this ShowJobLogResponse.

        作业日志条数

        :return: The count of this ShowJobLogResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShowJobLogResponse.

        作业日志条数

        :param count: The count of this ShowJobLogResponse.
        :type count: int
        """
        self._count = count

    @property
    def logs(self):
        """Gets the logs of this ShowJobLogResponse.

        作业日志内容列表

        :return: The logs of this ShowJobLogResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.LogContentDto`]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this ShowJobLogResponse.

        作业日志内容列表

        :param logs: The logs of this ShowJobLogResponse.
        :type logs: list[:class:`huaweicloudsdkeihealth.v1.LogContentDto`]
        """
        self._logs = logs

    @property
    def log_storage_link(self):
        """Gets the log_storage_link of this ShowJobLogResponse.

        作业日志存储链接

        :return: The log_storage_link of this ShowJobLogResponse.
        :rtype: str
        """
        return self._log_storage_link

    @log_storage_link.setter
    def log_storage_link(self, log_storage_link):
        """Sets the log_storage_link of this ShowJobLogResponse.

        作业日志存储链接

        :param log_storage_link: The log_storage_link of this ShowJobLogResponse.
        :type log_storage_link: str
        """
        self._log_storage_link = log_storage_link

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
        if not isinstance(other, ShowJobLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
