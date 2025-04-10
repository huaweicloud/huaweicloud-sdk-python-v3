# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduledTaskResponse(SdkResponse):

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
        'next_maker': 'str',
        'scheduled_tasks': 'list[ScheduledTaskBasicInfo]'
    }

    attribute_map = {
        'count': 'count',
        'next_maker': 'next_maker',
        'scheduled_tasks': 'scheduled_tasks'
    }

    def __init__(self, count=None, next_maker=None, scheduled_tasks=None):
        r"""ListScheduledTaskResponse

        The model defined in huaweicloud sdk

        :param count: 定时运维总数量
        :type count: int
        :param next_maker: 下次起始点
        :type next_maker: str
        :param scheduled_tasks: 定时运维列表
        :type scheduled_tasks: list[:class:`huaweicloudsdkcoc.v1.ScheduledTaskBasicInfo`]
        """
        
        super(ListScheduledTaskResponse, self).__init__()

        self._count = None
        self._next_maker = None
        self._scheduled_tasks = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if next_maker is not None:
            self.next_maker = next_maker
        if scheduled_tasks is not None:
            self.scheduled_tasks = scheduled_tasks

    @property
    def count(self):
        r"""Gets the count of this ListScheduledTaskResponse.

        定时运维总数量

        :return: The count of this ListScheduledTaskResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListScheduledTaskResponse.

        定时运维总数量

        :param count: The count of this ListScheduledTaskResponse.
        :type count: int
        """
        self._count = count

    @property
    def next_maker(self):
        r"""Gets the next_maker of this ListScheduledTaskResponse.

        下次起始点

        :return: The next_maker of this ListScheduledTaskResponse.
        :rtype: str
        """
        return self._next_maker

    @next_maker.setter
    def next_maker(self, next_maker):
        r"""Sets the next_maker of this ListScheduledTaskResponse.

        下次起始点

        :param next_maker: The next_maker of this ListScheduledTaskResponse.
        :type next_maker: str
        """
        self._next_maker = next_maker

    @property
    def scheduled_tasks(self):
        r"""Gets the scheduled_tasks of this ListScheduledTaskResponse.

        定时运维列表

        :return: The scheduled_tasks of this ListScheduledTaskResponse.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ScheduledTaskBasicInfo`]
        """
        return self._scheduled_tasks

    @scheduled_tasks.setter
    def scheduled_tasks(self, scheduled_tasks):
        r"""Sets the scheduled_tasks of this ListScheduledTaskResponse.

        定时运维列表

        :param scheduled_tasks: The scheduled_tasks of this ListScheduledTaskResponse.
        :type scheduled_tasks: list[:class:`huaweicloudsdkcoc.v1.ScheduledTaskBasicInfo`]
        """
        self._scheduled_tasks = scheduled_tasks

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
        if not isinstance(other, ListScheduledTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
