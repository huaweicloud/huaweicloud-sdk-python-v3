# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportTopSqlTrendDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'start_at': 'int',
        'end_at': 'int',
        'datastore_type': 'str',
        'node_id': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'datastore_type': 'datastore_type',
        'node_id': 'node_id',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, start_at=None, end_at=None, datastore_type=None, node_id=None, x_language=None):
        """ExportTopSqlTrendDetailsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param start_at: 开始时间（Unix timestamp），单位：毫秒。
        :type start_at: int
        :param end_at: 结束时间（Unix timestamp），单位：毫秒。
        :type end_at: int
        :param datastore_type: 数据库类型。支持MySQL和GaussDB(for MySQL)。
        :type datastore_type: str
        :param node_id: 节点ID。
        :type node_id: str
        :param x_language: 请求语言类型。
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._start_at = None
        self._end_at = None
        self._datastore_type = None
        self._node_id = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        self.start_at = start_at
        self.end_at = end_at
        self.datastore_type = datastore_type
        if node_id is not None:
            self.node_id = node_id
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ExportTopSqlTrendDetailsRequest.

        实例ID。

        :return: The instance_id of this ExportTopSqlTrendDetailsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ExportTopSqlTrendDetailsRequest.

        实例ID。

        :param instance_id: The instance_id of this ExportTopSqlTrendDetailsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_at(self):
        """Gets the start_at of this ExportTopSqlTrendDetailsRequest.

        开始时间（Unix timestamp），单位：毫秒。

        :return: The start_at of this ExportTopSqlTrendDetailsRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """Sets the start_at of this ExportTopSqlTrendDetailsRequest.

        开始时间（Unix timestamp），单位：毫秒。

        :param start_at: The start_at of this ExportTopSqlTrendDetailsRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        """Gets the end_at of this ExportTopSqlTrendDetailsRequest.

        结束时间（Unix timestamp），单位：毫秒。

        :return: The end_at of this ExportTopSqlTrendDetailsRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        """Sets the end_at of this ExportTopSqlTrendDetailsRequest.

        结束时间（Unix timestamp），单位：毫秒。

        :param end_at: The end_at of this ExportTopSqlTrendDetailsRequest.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def datastore_type(self):
        """Gets the datastore_type of this ExportTopSqlTrendDetailsRequest.

        数据库类型。支持MySQL和GaussDB(for MySQL)。

        :return: The datastore_type of this ExportTopSqlTrendDetailsRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        """Sets the datastore_type of this ExportTopSqlTrendDetailsRequest.

        数据库类型。支持MySQL和GaussDB(for MySQL)。

        :param datastore_type: The datastore_type of this ExportTopSqlTrendDetailsRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def node_id(self):
        """Gets the node_id of this ExportTopSqlTrendDetailsRequest.

        节点ID。

        :return: The node_id of this ExportTopSqlTrendDetailsRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ExportTopSqlTrendDetailsRequest.

        节点ID。

        :param node_id: The node_id of this ExportTopSqlTrendDetailsRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def x_language(self):
        """Gets the x_language of this ExportTopSqlTrendDetailsRequest.

        请求语言类型。

        :return: The x_language of this ExportTopSqlTrendDetailsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ExportTopSqlTrendDetailsRequest.

        请求语言类型。

        :param x_language: The x_language of this ExportTopSqlTrendDetailsRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ExportTopSqlTrendDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
