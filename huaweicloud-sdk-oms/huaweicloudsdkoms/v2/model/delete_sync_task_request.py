# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteSyncTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sync_task_id': 'str'
    }

    attribute_map = {
        'sync_task_id': 'sync_task_id'
    }

    def __init__(self, sync_task_id=None):
        r"""DeleteSyncTaskRequest

        The model defined in huaweicloud sdk

        :param sync_task_id: 同步任务ID。
        :type sync_task_id: str
        """
        
        

        self._sync_task_id = None
        self.discriminator = None

        self.sync_task_id = sync_task_id

    @property
    def sync_task_id(self):
        r"""Gets the sync_task_id of this DeleteSyncTaskRequest.

        同步任务ID。

        :return: The sync_task_id of this DeleteSyncTaskRequest.
        :rtype: str
        """
        return self._sync_task_id

    @sync_task_id.setter
    def sync_task_id(self, sync_task_id):
        r"""Sets the sync_task_id of this DeleteSyncTaskRequest.

        同步任务ID。

        :param sync_task_id: The sync_task_id of this DeleteSyncTaskRequest.
        :type sync_task_id: str
        """
        self._sync_task_id = sync_task_id

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
        if not isinstance(other, DeleteSyncTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
