# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTaskGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'status': 'int'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'status': 'status'
    }

    def __init__(self, limit=None, offset=None, status=None):
        """ListTaskGroupRequest

        The model defined in huaweicloud sdk

        :param limit: 查询返回迁移组任务列表当前页面的数量，默认查询10条。 最多返回100条迁移任务信息。
        :type limit: int
        :param offset: 起始的任务序号，默认为0。 取值大于等于0，取值为0时从第一条开始查询。
        :type offset: int
        :param status: 迁移任务组状态（无该参数时代表查询所有状态的任务） 0 – 等待中 1 – 执行中/创建中 2 – 监控任务执行 3 – 暂停 4 – 创建任务失败 5 – 迁移失败 6 – 迁移完成 7 – 暂停中 8 – 等待删除中 9 – 删除
        :type status: int
        """
        
        

        self._limit = None
        self._offset = None
        self._status = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if status is not None:
            self.status = status

    @property
    def limit(self):
        """Gets the limit of this ListTaskGroupRequest.

        查询返回迁移组任务列表当前页面的数量，默认查询10条。 最多返回100条迁移任务信息。

        :return: The limit of this ListTaskGroupRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTaskGroupRequest.

        查询返回迁移组任务列表当前页面的数量，默认查询10条。 最多返回100条迁移任务信息。

        :param limit: The limit of this ListTaskGroupRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListTaskGroupRequest.

        起始的任务序号，默认为0。 取值大于等于0，取值为0时从第一条开始查询。

        :return: The offset of this ListTaskGroupRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTaskGroupRequest.

        起始的任务序号，默认为0。 取值大于等于0，取值为0时从第一条开始查询。

        :param offset: The offset of this ListTaskGroupRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def status(self):
        """Gets the status of this ListTaskGroupRequest.

        迁移任务组状态（无该参数时代表查询所有状态的任务） 0 – 等待中 1 – 执行中/创建中 2 – 监控任务执行 3 – 暂停 4 – 创建任务失败 5 – 迁移失败 6 – 迁移完成 7 – 暂停中 8 – 等待删除中 9 – 删除

        :return: The status of this ListTaskGroupRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListTaskGroupRequest.

        迁移任务组状态（无该参数时代表查询所有状态的任务） 0 – 等待中 1 – 执行中/创建中 2 – 监控任务执行 3 – 暂停 4 – 创建任务失败 5 – 迁移失败 6 – 迁移完成 7 – 暂停中 8 – 等待删除中 9 – 删除

        :param status: The status of this ListTaskGroupRequest.
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
        if not isinstance(other, ListTaskGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
