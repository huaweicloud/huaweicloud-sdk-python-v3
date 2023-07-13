# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchStopMigrationTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'migration_tasks': 'list[StopMigrationTaskResult]'
    }

    attribute_map = {
        'migration_tasks': 'migration_tasks'
    }

    def __init__(self, migration_tasks=None):
        """BatchStopMigrationTasksResponse

        The model defined in huaweicloud sdk

        :param migration_tasks: 数据迁移任务列表。
        :type migration_tasks: list[:class:`huaweicloudsdkdcs.v2.StopMigrationTaskResult`]
        """
        
        super(BatchStopMigrationTasksResponse, self).__init__()

        self._migration_tasks = None
        self.discriminator = None

        if migration_tasks is not None:
            self.migration_tasks = migration_tasks

    @property
    def migration_tasks(self):
        """Gets the migration_tasks of this BatchStopMigrationTasksResponse.

        数据迁移任务列表。

        :return: The migration_tasks of this BatchStopMigrationTasksResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.StopMigrationTaskResult`]
        """
        return self._migration_tasks

    @migration_tasks.setter
    def migration_tasks(self, migration_tasks):
        """Sets the migration_tasks of this BatchStopMigrationTasksResponse.

        数据迁移任务列表。

        :param migration_tasks: The migration_tasks of this BatchStopMigrationTasksResponse.
        :type migration_tasks: list[:class:`huaweicloudsdkdcs.v2.StopMigrationTaskResult`]
        """
        self._migration_tasks = migration_tasks

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
        if not isinstance(other, BatchStopMigrationTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
