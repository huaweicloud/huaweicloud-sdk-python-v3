# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAnimatedGraphicsTaskResponse(SdkResponse):

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
        'tasks': 'list[AnimatedGraphicsTask]'
    }

    attribute_map = {
        'total': 'total',
        'tasks': 'tasks'
    }

    def __init__(self, total=None, tasks=None):
        r"""ListAnimatedGraphicsTaskResponse

        The model defined in huaweicloud sdk

        :param total: 任务总数
        :type total: int
        :param tasks: 任务列表
        :type tasks: list[:class:`huaweicloudsdkmpc.v1.AnimatedGraphicsTask`]
        """
        
        super(ListAnimatedGraphicsTaskResponse, self).__init__()

        self._total = None
        self._tasks = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if tasks is not None:
            self.tasks = tasks

    @property
    def total(self):
        r"""Gets the total of this ListAnimatedGraphicsTaskResponse.

        任务总数

        :return: The total of this ListAnimatedGraphicsTaskResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListAnimatedGraphicsTaskResponse.

        任务总数

        :param total: The total of this ListAnimatedGraphicsTaskResponse.
        :type total: int
        """
        self._total = total

    @property
    def tasks(self):
        r"""Gets the tasks of this ListAnimatedGraphicsTaskResponse.

        任务列表

        :return: The tasks of this ListAnimatedGraphicsTaskResponse.
        :rtype: list[:class:`huaweicloudsdkmpc.v1.AnimatedGraphicsTask`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ListAnimatedGraphicsTaskResponse.

        任务列表

        :param tasks: The tasks of this ListAnimatedGraphicsTaskResponse.
        :type tasks: list[:class:`huaweicloudsdkmpc.v1.AnimatedGraphicsTask`]
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
        if not isinstance(other, ListAnimatedGraphicsTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
