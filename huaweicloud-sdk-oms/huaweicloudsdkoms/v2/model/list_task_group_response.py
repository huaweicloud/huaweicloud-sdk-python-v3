# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTaskGroupResponse(SdkResponse):

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
        'taskgroups': 'list[TaskGroupResp]'
    }

    attribute_map = {
        'count': 'count',
        'taskgroups': 'taskgroups'
    }

    def __init__(self, count=None, taskgroups=None):
        """ListTaskGroupResponse

        The model defined in huaweicloud sdk

        :param count: 满足查询条件的任务组总数
        :type count: int
        :param taskgroups: 查询的迁移任务组详情
        :type taskgroups: list[:class:`huaweicloudsdkoms.v2.TaskGroupResp`]
        """
        
        super(ListTaskGroupResponse, self).__init__()

        self._count = None
        self._taskgroups = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if taskgroups is not None:
            self.taskgroups = taskgroups

    @property
    def count(self):
        """Gets the count of this ListTaskGroupResponse.

        满足查询条件的任务组总数

        :return: The count of this ListTaskGroupResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListTaskGroupResponse.

        满足查询条件的任务组总数

        :param count: The count of this ListTaskGroupResponse.
        :type count: int
        """
        self._count = count

    @property
    def taskgroups(self):
        """Gets the taskgroups of this ListTaskGroupResponse.

        查询的迁移任务组详情

        :return: The taskgroups of this ListTaskGroupResponse.
        :rtype: list[:class:`huaweicloudsdkoms.v2.TaskGroupResp`]
        """
        return self._taskgroups

    @taskgroups.setter
    def taskgroups(self, taskgroups):
        """Sets the taskgroups of this ListTaskGroupResponse.

        查询的迁移任务组详情

        :param taskgroups: The taskgroups of this ListTaskGroupResponse.
        :type taskgroups: list[:class:`huaweicloudsdkoms.v2.TaskGroupResp`]
        """
        self._taskgroups = taskgroups

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
        if not isinstance(other, ListTaskGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
