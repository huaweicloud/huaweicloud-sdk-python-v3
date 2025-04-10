# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Task:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'index': 'int',
        'name': 'str',
        'status': 'str',
        'detail': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'index': 'index',
        'name': 'name',
        'status': 'status',
        'detail': 'detail',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, index=None, name=None, status=None, detail=None, created_at=None, updated_at=None):
        r"""Task

        The model defined in huaweicloud sdk

        :param index: 任务序号。
        :type index: int
        :param name: 任务名称。
        :type name: str
        :param status: 任务状态。
        :type status: str
        :param detail: 任务详情。
        :type detail: str
        :param created_at: 创建时间。
        :type created_at: str
        :param updated_at: 更新时间。
        :type updated_at: str
        """
        
        

        self._index = None
        self._name = None
        self._status = None
        self._detail = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if index is not None:
            self.index = index
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if detail is not None:
            self.detail = detail
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def index(self):
        r"""Gets the index of this Task.

        任务序号。

        :return: The index of this Task.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this Task.

        任务序号。

        :param index: The index of this Task.
        :type index: int
        """
        self._index = index

    @property
    def name(self):
        r"""Gets the name of this Task.

        任务名称。

        :return: The name of this Task.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Task.

        任务名称。

        :param name: The name of this Task.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this Task.

        任务状态。

        :return: The status of this Task.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Task.

        任务状态。

        :param status: The status of this Task.
        :type status: str
        """
        self._status = status

    @property
    def detail(self):
        r"""Gets the detail of this Task.

        任务详情。

        :return: The detail of this Task.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this Task.

        任务详情。

        :param detail: The detail of this Task.
        :type detail: str
        """
        self._detail = detail

    @property
    def created_at(self):
        r"""Gets the created_at of this Task.

        创建时间。

        :return: The created_at of this Task.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Task.

        创建时间。

        :param created_at: The created_at of this Task.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Task.

        更新时间。

        :return: The updated_at of this Task.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Task.

        更新时间。

        :param updated_at: The updated_at of this Task.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, Task):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
