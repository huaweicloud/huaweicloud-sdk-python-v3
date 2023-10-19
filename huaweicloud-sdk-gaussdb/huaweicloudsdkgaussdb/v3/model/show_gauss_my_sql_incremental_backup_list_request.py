# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGaussMySqlIncrementalBackupListRequest:

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
        'offset': 'str',
        'limit': 'str',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, x_language=None, instance_id=None, offset=None, limit=None, begin_time=None, end_time=None):
        """ShowGaussMySqlIncrementalBackupListRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。默认en-us。 取值范围： - en-us - zh-cn
        :type x_language: str
        :param instance_id: 实例ID，严格匹配UUID规则。
        :type instance_id: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: str
        :param limit: 查询记录数。默认为10，可取范围：10、20、50。
        :type limit: str
        :param begin_time: 查询开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  “begin_time”有值时，“end_time”必选。
        :type begin_time: str
        :param end_time: 查询结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”，且大于查询开始时间。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  “end_time”有值时，“begin_time”必选。
        :type end_time: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._offset = None
        self._limit = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def x_language(self):
        """Gets the x_language of this ShowGaussMySqlIncrementalBackupListRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :return: The x_language of this ShowGaussMySqlIncrementalBackupListRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowGaussMySqlIncrementalBackupListRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :param x_language: The x_language of this ShowGaussMySqlIncrementalBackupListRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowGaussMySqlIncrementalBackupListRequest.

        实例ID，严格匹配UUID规则。

        :return: The instance_id of this ShowGaussMySqlIncrementalBackupListRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowGaussMySqlIncrementalBackupListRequest.

        实例ID，严格匹配UUID规则。

        :param instance_id: The instance_id of this ShowGaussMySqlIncrementalBackupListRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ShowGaussMySqlIncrementalBackupListRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ShowGaussMySqlIncrementalBackupListRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowGaussMySqlIncrementalBackupListRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ShowGaussMySqlIncrementalBackupListRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowGaussMySqlIncrementalBackupListRequest.

        查询记录数。默认为10，可取范围：10、20、50。

        :return: The limit of this ShowGaussMySqlIncrementalBackupListRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowGaussMySqlIncrementalBackupListRequest.

        查询记录数。默认为10，可取范围：10、20、50。

        :param limit: The limit of this ShowGaussMySqlIncrementalBackupListRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def begin_time(self):
        """Gets the begin_time of this ShowGaussMySqlIncrementalBackupListRequest.

        查询开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  “begin_time”有值时，“end_time”必选。

        :return: The begin_time of this ShowGaussMySqlIncrementalBackupListRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ShowGaussMySqlIncrementalBackupListRequest.

        查询开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  “begin_time”有值时，“end_time”必选。

        :param begin_time: The begin_time of this ShowGaussMySqlIncrementalBackupListRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowGaussMySqlIncrementalBackupListRequest.

        查询结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”，且大于查询开始时间。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  “end_time”有值时，“begin_time”必选。

        :return: The end_time of this ShowGaussMySqlIncrementalBackupListRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowGaussMySqlIncrementalBackupListRequest.

        查询结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”，且大于查询开始时间。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。  “end_time”有值时，“begin_time”必选。

        :param end_time: The end_time of this ShowGaussMySqlIncrementalBackupListRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ShowGaussMySqlIncrementalBackupListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
