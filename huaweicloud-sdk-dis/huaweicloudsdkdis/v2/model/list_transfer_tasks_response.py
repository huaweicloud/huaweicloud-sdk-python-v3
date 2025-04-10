# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTransferTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_number': 'int',
        'quota': 'int',
        'tasks': 'list[TransferTask]'
    }

    attribute_map = {
        'total_number': 'total_number',
        'quota': 'quota',
        'tasks': 'tasks'
    }

    def __init__(self, total_number=None, quota=None, tasks=None):
        r"""ListTransferTasksResponse

        The model defined in huaweicloud sdk

        :param total_number: 转储任务总数。
        :type total_number: int
        :param quota: 可创建的转储任务配额。
        :type quota: int
        :param tasks: 转储任务列表。
        :type tasks: list[:class:`huaweicloudsdkdis.v2.TransferTask`]
        """
        
        super(ListTransferTasksResponse, self).__init__()

        self._total_number = None
        self._quota = None
        self._tasks = None
        self.discriminator = None

        if total_number is not None:
            self.total_number = total_number
        if quota is not None:
            self.quota = quota
        if tasks is not None:
            self.tasks = tasks

    @property
    def total_number(self):
        r"""Gets the total_number of this ListTransferTasksResponse.

        转储任务总数。

        :return: The total_number of this ListTransferTasksResponse.
        :rtype: int
        """
        return self._total_number

    @total_number.setter
    def total_number(self, total_number):
        r"""Sets the total_number of this ListTransferTasksResponse.

        转储任务总数。

        :param total_number: The total_number of this ListTransferTasksResponse.
        :type total_number: int
        """
        self._total_number = total_number

    @property
    def quota(self):
        r"""Gets the quota of this ListTransferTasksResponse.

        可创建的转储任务配额。

        :return: The quota of this ListTransferTasksResponse.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this ListTransferTasksResponse.

        可创建的转储任务配额。

        :param quota: The quota of this ListTransferTasksResponse.
        :type quota: int
        """
        self._quota = quota

    @property
    def tasks(self):
        r"""Gets the tasks of this ListTransferTasksResponse.

        转储任务列表。

        :return: The tasks of this ListTransferTasksResponse.
        :rtype: list[:class:`huaweicloudsdkdis.v2.TransferTask`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ListTransferTasksResponse.

        转储任务列表。

        :param tasks: The tasks of this ListTransferTasksResponse.
        :type tasks: list[:class:`huaweicloudsdkdis.v2.TransferTask`]
        """
        self._tasks = tasks

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
        if not isinstance(other, ListTransferTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
