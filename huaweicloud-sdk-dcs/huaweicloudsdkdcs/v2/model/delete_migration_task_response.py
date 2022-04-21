# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteMigrationTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'task_id_list': 'list[str]'
    }

    attribute_map = {
        'task_id_list': 'task_id_list'
    }

    def __init__(self, task_id_list=None):
        """DeleteMigrationTaskResponse

        The model defined in huaweicloud sdk

        :param task_id_list: 删除的迁移任务ID列表。
        :type task_id_list: list[str]
        """
        
        super(DeleteMigrationTaskResponse, self).__init__()

        self._task_id_list = None
        self.discriminator = None

        if task_id_list is not None:
            self.task_id_list = task_id_list

    @property
    def task_id_list(self):
        """Gets the task_id_list of this DeleteMigrationTaskResponse.

        删除的迁移任务ID列表。

        :return: The task_id_list of this DeleteMigrationTaskResponse.
        :rtype: list[str]
        """
        return self._task_id_list

    @task_id_list.setter
    def task_id_list(self, task_id_list):
        """Sets the task_id_list of this DeleteMigrationTaskResponse.

        删除的迁移任务ID列表。

        :param task_id_list: The task_id_list of this DeleteMigrationTaskResponse.
        :type task_id_list: list[str]
        """
        self._task_id_list = task_id_list

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
        if not isinstance(other, DeleteMigrationTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
