# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataConnectorRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connector_id': 'str',
        'source_type': 'str',
        'connector_name': 'str',
        'limit': 'int',
        'offset': 'int',
        'available': 'bool'
    }

    attribute_map = {
        'connector_id': 'connector_id',
        'source_type': 'source_type',
        'connector_name': 'connector_name',
        'limit': 'limit',
        'offset': 'offset',
        'available': 'available'
    }

    def __init__(self, connector_id=None, source_type=None, connector_name=None, limit=None, offset=None, available=None):
        """ListDataConnectorRequest

        The model defined in huaweicloud sdk

        :param connector_id: 连接id
        :type connector_id: str
        :param source_type: 数据源类别
        :type source_type: str
        :param connector_name: 数据连接名称
        :type connector_name: str
        :param limit: 每页返回的资源个数
        :type limit: int
        :param offset: 分页查询起始偏移量
        :type offset: int
        :param available: 数据连接是否有效
        :type available: bool
        """
        
        

        self._connector_id = None
        self._source_type = None
        self._connector_name = None
        self._limit = None
        self._offset = None
        self._available = None
        self.discriminator = None

        if connector_id is not None:
            self.connector_id = connector_id
        if source_type is not None:
            self.source_type = source_type
        if connector_name is not None:
            self.connector_name = connector_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if available is not None:
            self.available = available

    @property
    def connector_id(self):
        """Gets the connector_id of this ListDataConnectorRequest.

        连接id

        :return: The connector_id of this ListDataConnectorRequest.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """Sets the connector_id of this ListDataConnectorRequest.

        连接id

        :param connector_id: The connector_id of this ListDataConnectorRequest.
        :type connector_id: str
        """
        self._connector_id = connector_id

    @property
    def source_type(self):
        """Gets the source_type of this ListDataConnectorRequest.

        数据源类别

        :return: The source_type of this ListDataConnectorRequest.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this ListDataConnectorRequest.

        数据源类别

        :param source_type: The source_type of this ListDataConnectorRequest.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def connector_name(self):
        """Gets the connector_name of this ListDataConnectorRequest.

        数据连接名称

        :return: The connector_name of this ListDataConnectorRequest.
        :rtype: str
        """
        return self._connector_name

    @connector_name.setter
    def connector_name(self, connector_name):
        """Sets the connector_name of this ListDataConnectorRequest.

        数据连接名称

        :param connector_name: The connector_name of this ListDataConnectorRequest.
        :type connector_name: str
        """
        self._connector_name = connector_name

    @property
    def limit(self):
        """Gets the limit of this ListDataConnectorRequest.

        每页返回的资源个数

        :return: The limit of this ListDataConnectorRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDataConnectorRequest.

        每页返回的资源个数

        :param limit: The limit of this ListDataConnectorRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListDataConnectorRequest.

        分页查询起始偏移量

        :return: The offset of this ListDataConnectorRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDataConnectorRequest.

        分页查询起始偏移量

        :param offset: The offset of this ListDataConnectorRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def available(self):
        """Gets the available of this ListDataConnectorRequest.

        数据连接是否有效

        :return: The available of this ListDataConnectorRequest.
        :rtype: bool
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this ListDataConnectorRequest.

        数据连接是否有效

        :param available: The available of this ListDataConnectorRequest.
        :type available: bool
        """
        self._available = available

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
        if not isinstance(other, ListDataConnectorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
