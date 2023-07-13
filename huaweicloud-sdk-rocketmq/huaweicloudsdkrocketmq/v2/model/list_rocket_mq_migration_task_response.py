# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRocketMqMigrationTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'task': 'list[MetadataTask]'
    }

    attribute_map = {
        'total': 'total',
        'task': 'task'
    }

    def __init__(self, total=None, task=None):
        """ListRocketMqMigrationTaskResponse

        The model defined in huaweicloud sdk

        :param total: 元数据迁移任务总数。
        :type total: int
        :param task: 元数据迁移任务列表。
        :type task: list[:class:`huaweicloudsdkrocketmq.v2.MetadataTask`]
        """
        
        super(ListRocketMqMigrationTaskResponse, self).__init__()

        self._total = None
        self._task = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if task is not None:
            self.task = task

    @property
    def total(self):
        """Gets the total of this ListRocketMqMigrationTaskResponse.

        元数据迁移任务总数。

        :return: The total of this ListRocketMqMigrationTaskResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListRocketMqMigrationTaskResponse.

        元数据迁移任务总数。

        :param total: The total of this ListRocketMqMigrationTaskResponse.
        :type total: int
        """
        self._total = total

    @property
    def task(self):
        """Gets the task of this ListRocketMqMigrationTaskResponse.

        元数据迁移任务列表。

        :return: The task of this ListRocketMqMigrationTaskResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.MetadataTask`]
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this ListRocketMqMigrationTaskResponse.

        元数据迁移任务列表。

        :param task: The task of this ListRocketMqMigrationTaskResponse.
        :type task: list[:class:`huaweicloudsdkrocketmq.v2.MetadataTask`]
        """
        self._task = task

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
        if not isinstance(other, ListRocketMqMigrationTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
