# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportSlowQueryLogsRequest:

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
        'datastore_type': 'str',
        'start_at': 'int',
        'end_at': 'int',
        'limit': 'int',
        'marker': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'datastore_type': 'datastore_type',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'limit': 'limit',
        'marker': 'marker',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, datastore_type=None, start_at=None, end_at=None, limit=None, marker=None, x_language=None):
        r"""ExportSlowQueryLogsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param datastore_type: 数据库类型。支持MySQL、GaussDB(for MySQL)、PostgreSQL。
        :type datastore_type: str
        :param start_at: 开始时间（Unix timestamp），单位：毫秒。
        :type start_at: int
        :param end_at: 结束时间（Unix timestamp），单位：毫秒。
        :type end_at: int
        :param limit: 每页记录数。最大为2000。
        :type limit: int
        :param marker: 指定一个标识符。获取第一页时不用赋值，获取下一页时取上页查询结果的返回值。
        :type marker: str
        :param x_language: 请求语言类型。
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._datastore_type = None
        self._start_at = None
        self._end_at = None
        self._limit = None
        self._marker = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        self.datastore_type = datastore_type
        self.start_at = start_at
        self.end_at = end_at
        self.limit = limit
        if marker is not None:
            self.marker = marker
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ExportSlowQueryLogsRequest.

        实例ID。

        :return: The instance_id of this ExportSlowQueryLogsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ExportSlowQueryLogsRequest.

        实例ID。

        :param instance_id: The instance_id of this ExportSlowQueryLogsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ExportSlowQueryLogsRequest.

        数据库类型。支持MySQL、GaussDB(for MySQL)、PostgreSQL。

        :return: The datastore_type of this ExportSlowQueryLogsRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ExportSlowQueryLogsRequest.

        数据库类型。支持MySQL、GaussDB(for MySQL)、PostgreSQL。

        :param datastore_type: The datastore_type of this ExportSlowQueryLogsRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def start_at(self):
        r"""Gets the start_at of this ExportSlowQueryLogsRequest.

        开始时间（Unix timestamp），单位：毫秒。

        :return: The start_at of this ExportSlowQueryLogsRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ExportSlowQueryLogsRequest.

        开始时间（Unix timestamp），单位：毫秒。

        :param start_at: The start_at of this ExportSlowQueryLogsRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ExportSlowQueryLogsRequest.

        结束时间（Unix timestamp），单位：毫秒。

        :return: The end_at of this ExportSlowQueryLogsRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ExportSlowQueryLogsRequest.

        结束时间（Unix timestamp），单位：毫秒。

        :param end_at: The end_at of this ExportSlowQueryLogsRequest.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def limit(self):
        r"""Gets the limit of this ExportSlowQueryLogsRequest.

        每页记录数。最大为2000。

        :return: The limit of this ExportSlowQueryLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ExportSlowQueryLogsRequest.

        每页记录数。最大为2000。

        :param limit: The limit of this ExportSlowQueryLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ExportSlowQueryLogsRequest.

        指定一个标识符。获取第一页时不用赋值，获取下一页时取上页查询结果的返回值。

        :return: The marker of this ExportSlowQueryLogsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ExportSlowQueryLogsRequest.

        指定一个标识符。获取第一页时不用赋值，获取下一页时取上页查询结果的返回值。

        :param marker: The marker of this ExportSlowQueryLogsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def x_language(self):
        r"""Gets the x_language of this ExportSlowQueryLogsRequest.

        请求语言类型。

        :return: The x_language of this ExportSlowQueryLogsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ExportSlowQueryLogsRequest.

        请求语言类型。

        :param x_language: The x_language of this ExportSlowQueryLogsRequest.
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
        if not isinstance(other, ExportSlowQueryLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
