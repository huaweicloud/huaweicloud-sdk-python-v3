# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecretTaskResponse(SdkResponse):

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
        'tasks': 'list[SecretTask]',
        'next_marker': 'str'
    }

    attribute_map = {
        'total': 'total',
        'tasks': 'tasks',
        'next_marker': 'next_marker'
    }

    def __init__(self, total=None, tasks=None, next_marker=None):
        r"""ListSecretTaskResponse

        The model defined in huaweicloud sdk

        :param total: 任务数量
        :type total: int
        :param tasks: 凭据任务列表。
        :type tasks: list[:class:`huaweicloudsdkcsms.v1.SecretTask`]
        :param next_marker: 下一页查询地址（本页的末尾任务ID）。
        :type next_marker: str
        """
        
        super(ListSecretTaskResponse, self).__init__()

        self._total = None
        self._tasks = None
        self._next_marker = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if tasks is not None:
            self.tasks = tasks
        if next_marker is not None:
            self.next_marker = next_marker

    @property
    def total(self):
        r"""Gets the total of this ListSecretTaskResponse.

        任务数量

        :return: The total of this ListSecretTaskResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSecretTaskResponse.

        任务数量

        :param total: The total of this ListSecretTaskResponse.
        :type total: int
        """
        self._total = total

    @property
    def tasks(self):
        r"""Gets the tasks of this ListSecretTaskResponse.

        凭据任务列表。

        :return: The tasks of this ListSecretTaskResponse.
        :rtype: list[:class:`huaweicloudsdkcsms.v1.SecretTask`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ListSecretTaskResponse.

        凭据任务列表。

        :param tasks: The tasks of this ListSecretTaskResponse.
        :type tasks: list[:class:`huaweicloudsdkcsms.v1.SecretTask`]
        """
        self._tasks = tasks

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ListSecretTaskResponse.

        下一页查询地址（本页的末尾任务ID）。

        :return: The next_marker of this ListSecretTaskResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ListSecretTaskResponse.

        下一页查询地址（本页的末尾任务ID）。

        :param next_marker: The next_marker of this ListSecretTaskResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

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
        if not isinstance(other, ListSecretTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
