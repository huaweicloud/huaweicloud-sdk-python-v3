# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProtectableRequest:

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
        'marker': 'str',
        'name': 'str',
        'offset': 'int',
        'protectable_type': 'str',
        'status': 'str',
        'id': 'str',
        'server_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'name': 'name',
        'offset': 'offset',
        'protectable_type': 'protectable_type',
        'status': 'status',
        'id': 'id',
        'server_id': 'server_id'
    }

    def __init__(self, limit=None, marker=None, name=None, offset=None, protectable_type=None, status=None, id=None, server_id=None):
        """ListProtectableRequest

        The model defined in huaweicloud sdk

        :param limit: 每页显示的条目数量，每页最多支持50条
        :type limit: int
        :param marker: 上一次查询最后一条的ID
        :type marker: str
        :param name: 按名称过滤
        :type name: str
        :param offset: 偏移值
        :type offset: int
        :param protectable_type: 对象类型
        :type protectable_type: str
        :param status: 资源的状态，如available，error 等
        :type status: str
        :param id: 根据资源id过滤
        :type id: str
        :param server_id: 根据该id过滤属于该服务器的所有磁盘，支持企业多项目的用户才能传入此参数
        :type server_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._name = None
        self._offset = None
        self._protectable_type = None
        self._status = None
        self._id = None
        self._server_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        self.protectable_type = protectable_type
        if status is not None:
            self.status = status
        if id is not None:
            self.id = id
        if server_id is not None:
            self.server_id = server_id

    @property
    def limit(self):
        """Gets the limit of this ListProtectableRequest.

        每页显示的条目数量，每页最多支持50条

        :return: The limit of this ListProtectableRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProtectableRequest.

        每页显示的条目数量，每页最多支持50条

        :param limit: The limit of this ListProtectableRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListProtectableRequest.

        上一次查询最后一条的ID

        :return: The marker of this ListProtectableRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListProtectableRequest.

        上一次查询最后一条的ID

        :param marker: The marker of this ListProtectableRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def name(self):
        """Gets the name of this ListProtectableRequest.

        按名称过滤

        :return: The name of this ListProtectableRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListProtectableRequest.

        按名称过滤

        :param name: The name of this ListProtectableRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListProtectableRequest.

        偏移值

        :return: The offset of this ListProtectableRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProtectableRequest.

        偏移值

        :param offset: The offset of this ListProtectableRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def protectable_type(self):
        """Gets the protectable_type of this ListProtectableRequest.

        对象类型

        :return: The protectable_type of this ListProtectableRequest.
        :rtype: str
        """
        return self._protectable_type

    @protectable_type.setter
    def protectable_type(self, protectable_type):
        """Sets the protectable_type of this ListProtectableRequest.

        对象类型

        :param protectable_type: The protectable_type of this ListProtectableRequest.
        :type protectable_type: str
        """
        self._protectable_type = protectable_type

    @property
    def status(self):
        """Gets the status of this ListProtectableRequest.

        资源的状态，如available，error 等

        :return: The status of this ListProtectableRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListProtectableRequest.

        资源的状态，如available，error 等

        :param status: The status of this ListProtectableRequest.
        :type status: str
        """
        self._status = status

    @property
    def id(self):
        """Gets the id of this ListProtectableRequest.

        根据资源id过滤

        :return: The id of this ListProtectableRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListProtectableRequest.

        根据资源id过滤

        :param id: The id of this ListProtectableRequest.
        :type id: str
        """
        self._id = id

    @property
    def server_id(self):
        """Gets the server_id of this ListProtectableRequest.

        根据该id过滤属于该服务器的所有磁盘，支持企业多项目的用户才能传入此参数

        :return: The server_id of this ListProtectableRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ListProtectableRequest.

        根据该id过滤属于该服务器的所有磁盘，支持企业多项目的用户才能传入此参数

        :param server_id: The server_id of this ListProtectableRequest.
        :type server_id: str
        """
        self._server_id = server_id

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
        if not isinstance(other, ListProtectableRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
