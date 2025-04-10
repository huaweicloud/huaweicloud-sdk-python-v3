# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'status': 'int'
    }

    attribute_map = {
        'group_id': 'group_id',
        'limit': 'limit',
        'offset': 'offset',
        'status': 'status'
    }

    def __init__(self, group_id=None, limit=None, offset=None, status=None):
        r"""ListTasksRequest

        The model defined in huaweicloud sdk

        :param group_id: 迁移任务组group_id
        :type group_id: str
        :param limit: 查询返回迁移任务列表当前页面的数量，默认查询10条。 最多返回100条迁移任务信息。
        :type limit: int
        :param offset: 起始的任务序号，默认为0。 取值大于等于0，取值为0时从第一条开始查询。
        :type offset: int
        :param status: 迁移任务状态（无该参数时代表查询所有状态的任务）： 1：等待调度 2：正在执行 3：停止 4：失败 5：成功 7: 暂停中
        :type status: int
        """
        
        

        self._group_id = None
        self._limit = None
        self._offset = None
        self._status = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if status is not None:
            self.status = status

    @property
    def group_id(self):
        r"""Gets the group_id of this ListTasksRequest.

        迁移任务组group_id

        :return: The group_id of this ListTasksRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListTasksRequest.

        迁移任务组group_id

        :param group_id: The group_id of this ListTasksRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def limit(self):
        r"""Gets the limit of this ListTasksRequest.

        查询返回迁移任务列表当前页面的数量，默认查询10条。 最多返回100条迁移任务信息。

        :return: The limit of this ListTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTasksRequest.

        查询返回迁移任务列表当前页面的数量，默认查询10条。 最多返回100条迁移任务信息。

        :param limit: The limit of this ListTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListTasksRequest.

        起始的任务序号，默认为0。 取值大于等于0，取值为0时从第一条开始查询。

        :return: The offset of this ListTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTasksRequest.

        起始的任务序号，默认为0。 取值大于等于0，取值为0时从第一条开始查询。

        :param offset: The offset of this ListTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def status(self):
        r"""Gets the status of this ListTasksRequest.

        迁移任务状态（无该参数时代表查询所有状态的任务）： 1：等待调度 2：正在执行 3：停止 4：失败 5：成功 7: 暂停中

        :return: The status of this ListTasksRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListTasksRequest.

        迁移任务状态（无该参数时代表查询所有状态的任务）： 1：等待调度 2：正在执行 3：停止 4：失败 5：成功 7: 暂停中

        :param status: The status of this ListTasksRequest.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, ListTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
