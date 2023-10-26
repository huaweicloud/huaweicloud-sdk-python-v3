# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHpcCacheTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'share_id': 'str',
        'type': 'str',
        'status': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'share_id': 'share_id',
        'type': 'type',
        'status': 'status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, share_id=None, type=None, status=None, offset=None, limit=None):
        """ListHpcCacheTasksRequest

        The model defined in huaweicloud sdk

        :param share_id: 文件系统ID
        :type share_id: str
        :param type: 操作类型
        :type type: str
        :param status: 任务状态
        :type status: str
        :param offset: offset，默认值为 0
        :type offset: int
        :param limit: limit，默认值为 20
        :type limit: int
        """
        
        

        self._share_id = None
        self._type = None
        self._status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.share_id = share_id
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def share_id(self):
        """Gets the share_id of this ListHpcCacheTasksRequest.

        文件系统ID

        :return: The share_id of this ListHpcCacheTasksRequest.
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        """Sets the share_id of this ListHpcCacheTasksRequest.

        文件系统ID

        :param share_id: The share_id of this ListHpcCacheTasksRequest.
        :type share_id: str
        """
        self._share_id = share_id

    @property
    def type(self):
        """Gets the type of this ListHpcCacheTasksRequest.

        操作类型

        :return: The type of this ListHpcCacheTasksRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListHpcCacheTasksRequest.

        操作类型

        :param type: The type of this ListHpcCacheTasksRequest.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this ListHpcCacheTasksRequest.

        任务状态

        :return: The status of this ListHpcCacheTasksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListHpcCacheTasksRequest.

        任务状态

        :param status: The status of this ListHpcCacheTasksRequest.
        :type status: str
        """
        self._status = status

    @property
    def offset(self):
        """Gets the offset of this ListHpcCacheTasksRequest.

        offset，默认值为 0

        :return: The offset of this ListHpcCacheTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListHpcCacheTasksRequest.

        offset，默认值为 0

        :param offset: The offset of this ListHpcCacheTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListHpcCacheTasksRequest.

        limit，默认值为 20

        :return: The limit of this ListHpcCacheTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListHpcCacheTasksRequest.

        limit，默认值为 20

        :param limit: The limit of this ListHpcCacheTasksRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListHpcCacheTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
