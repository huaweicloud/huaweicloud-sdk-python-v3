# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSlowLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'offset': 'int',
        'limit': 'int',
        'type': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'offset': 'offset',
        'limit': 'limit',
        'type': 'type'
    }

    def __init__(self, x_language=None, instance_id=None, start_date=None, end_date=None, offset=None, limit=None, type=None):
        """ListSlowLogsRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param start_date: 开始日期，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type start_date: str
        :param end_date: 结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。只能查询当前时间前一个月内的慢日志。
        :type end_date: str
        :param offset: 页数偏移量，如1、2、3、4等，不填时默认为1。
        :type offset: int
        :param limit: 每页多少条记录，取值范围是1~100，不填时默认为10。
        :type limit: int
        :param type: 语句类型，取空值，表示查询所有语句类型。
        :type type: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._start_date = None
        self._end_date = None
        self._offset = None
        self._limit = None
        self._type = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.start_date = start_date
        self.end_date = end_date
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if type is not None:
            self.type = type

    @property
    def x_language(self):
        """Gets the x_language of this ListSlowLogsRequest.

        语言

        :return: The x_language of this ListSlowLogsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListSlowLogsRequest.

        语言

        :param x_language: The x_language of this ListSlowLogsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ListSlowLogsRequest.

        实例ID。

        :return: The instance_id of this ListSlowLogsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListSlowLogsRequest.

        实例ID。

        :param instance_id: The instance_id of this ListSlowLogsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_date(self):
        """Gets the start_date of this ListSlowLogsRequest.

        开始日期，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The start_date of this ListSlowLogsRequest.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ListSlowLogsRequest.

        开始日期，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param start_date: The start_date of this ListSlowLogsRequest.
        :type start_date: str
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ListSlowLogsRequest.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。只能查询当前时间前一个月内的慢日志。

        :return: The end_date of this ListSlowLogsRequest.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ListSlowLogsRequest.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。只能查询当前时间前一个月内的慢日志。

        :param end_date: The end_date of this ListSlowLogsRequest.
        :type end_date: str
        """
        self._end_date = end_date

    @property
    def offset(self):
        """Gets the offset of this ListSlowLogsRequest.

        页数偏移量，如1、2、3、4等，不填时默认为1。

        :return: The offset of this ListSlowLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSlowLogsRequest.

        页数偏移量，如1、2、3、4等，不填时默认为1。

        :param offset: The offset of this ListSlowLogsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSlowLogsRequest.

        每页多少条记录，取值范围是1~100，不填时默认为10。

        :return: The limit of this ListSlowLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSlowLogsRequest.

        每页多少条记录，取值范围是1~100，不填时默认为10。

        :param limit: The limit of this ListSlowLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def type(self):
        """Gets the type of this ListSlowLogsRequest.

        语句类型，取空值，表示查询所有语句类型。

        :return: The type of this ListSlowLogsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListSlowLogsRequest.

        语句类型，取空值，表示查询所有语句类型。

        :param type: The type of this ListSlowLogsRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListSlowLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
