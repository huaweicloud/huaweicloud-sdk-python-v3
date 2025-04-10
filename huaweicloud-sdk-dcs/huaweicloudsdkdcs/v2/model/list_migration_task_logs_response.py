# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMigrationTaskLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_num': 'int',
        'migration_logs': 'list[MigrationLog]'
    }

    attribute_map = {
        'log_num': 'log_num',
        'migration_logs': 'migration_logs'
    }

    def __init__(self, log_num=None, migration_logs=None):
        r"""ListMigrationTaskLogsResponse

        The model defined in huaweicloud sdk

        :param log_num: 日志条数
        :type log_num: int
        :param migration_logs: 日志列表
        :type migration_logs: list[:class:`huaweicloudsdkdcs.v2.MigrationLog`]
        """
        
        super(ListMigrationTaskLogsResponse, self).__init__()

        self._log_num = None
        self._migration_logs = None
        self.discriminator = None

        if log_num is not None:
            self.log_num = log_num
        if migration_logs is not None:
            self.migration_logs = migration_logs

    @property
    def log_num(self):
        r"""Gets the log_num of this ListMigrationTaskLogsResponse.

        日志条数

        :return: The log_num of this ListMigrationTaskLogsResponse.
        :rtype: int
        """
        return self._log_num

    @log_num.setter
    def log_num(self, log_num):
        r"""Sets the log_num of this ListMigrationTaskLogsResponse.

        日志条数

        :param log_num: The log_num of this ListMigrationTaskLogsResponse.
        :type log_num: int
        """
        self._log_num = log_num

    @property
    def migration_logs(self):
        r"""Gets the migration_logs of this ListMigrationTaskLogsResponse.

        日志列表

        :return: The migration_logs of this ListMigrationTaskLogsResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.MigrationLog`]
        """
        return self._migration_logs

    @migration_logs.setter
    def migration_logs(self, migration_logs):
        r"""Sets the migration_logs of this ListMigrationTaskLogsResponse.

        日志列表

        :param migration_logs: The migration_logs of this ListMigrationTaskLogsResponse.
        :type migration_logs: list[:class:`huaweicloudsdkdcs.v2.MigrationLog`]
        """
        self._migration_logs = migration_logs

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
        if not isinstance(other, ListMigrationTaskLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
