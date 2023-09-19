# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEncodeServersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'type': 'int',
        'status': 'int',
        'server_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'type': 'type',
        'status': 'status',
        'server_id': 'server_id'
    }

    def __init__(self, offset=None, limit=None, type=None, status=None, server_id=None):
        """ListEncodeServersRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源数，默认值为0。
        :type offset: int
        :param limit: 每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。
        :type limit: int
        :param type: 编码服务类型。 - 0：服务器 - 1：容器
        :type type: int
        :param status: 状态列表。 - 1：运行中 - 2：异常 - 3：重启中 - 4：冻结 - 5：关机 - 100、1014、0：创建中
        :type status: int
        :param server_id: 云手机服务器的唯一标识。
        :type server_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._type = None
        self._status = None
        self._server_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if server_id is not None:
            self.server_id = server_id

    @property
    def offset(self):
        """Gets the offset of this ListEncodeServersRequest.

        偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源数，默认值为0。

        :return: The offset of this ListEncodeServersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEncodeServersRequest.

        偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源数，默认值为0。

        :param offset: The offset of this ListEncodeServersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListEncodeServersRequest.

        每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。

        :return: The limit of this ListEncodeServersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEncodeServersRequest.

        每页返回的资源个数。取值范围：1~100（默认值为100），一般设置为10、20、50。

        :param limit: The limit of this ListEncodeServersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def type(self):
        """Gets the type of this ListEncodeServersRequest.

        编码服务类型。 - 0：服务器 - 1：容器

        :return: The type of this ListEncodeServersRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListEncodeServersRequest.

        编码服务类型。 - 0：服务器 - 1：容器

        :param type: The type of this ListEncodeServersRequest.
        :type type: int
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this ListEncodeServersRequest.

        状态列表。 - 1：运行中 - 2：异常 - 3：重启中 - 4：冻结 - 5：关机 - 100、1014、0：创建中

        :return: The status of this ListEncodeServersRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListEncodeServersRequest.

        状态列表。 - 1：运行中 - 2：异常 - 3：重启中 - 4：冻结 - 5：关机 - 100、1014、0：创建中

        :param status: The status of this ListEncodeServersRequest.
        :type status: int
        """
        self._status = status

    @property
    def server_id(self):
        """Gets the server_id of this ListEncodeServersRequest.

        云手机服务器的唯一标识。

        :return: The server_id of this ListEncodeServersRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ListEncodeServersRequest.

        云手机服务器的唯一标识。

        :param server_id: The server_id of this ListEncodeServersRequest.
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
        if not isinstance(other, ListEncodeServersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
