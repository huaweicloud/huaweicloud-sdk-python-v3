# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowlogResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'database': 'str',
        'query_sample': 'str',
        'type': 'str',
        'start_time': 'str'
    }

    attribute_map = {
        'time': 'time',
        'database': 'database',
        'query_sample': 'query_sample',
        'type': 'type',
        'start_time': 'start_time'
    }

    def __init__(self, time=None, database=None, query_sample=None, type=None, start_time=None):
        """SlowlogResult

        The model defined in huaweicloud sdk

        :param time: 执行时间。
        :type time: str
        :param database: 所属数据库。
        :type database: str
        :param query_sample: 执行语法。
        :type query_sample: str
        :param type: 语句类型。
        :type type: str
        :param start_time: 发生时间，UTC时间。
        :type start_time: str
        """
        
        

        self._time = None
        self._database = None
        self._query_sample = None
        self._type = None
        self._start_time = None
        self.discriminator = None

        self.time = time
        self.database = database
        self.query_sample = query_sample
        self.type = type
        self.start_time = start_time

    @property
    def time(self):
        """Gets the time of this SlowlogResult.

        执行时间。

        :return: The time of this SlowlogResult.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SlowlogResult.

        执行时间。

        :param time: The time of this SlowlogResult.
        :type time: str
        """
        self._time = time

    @property
    def database(self):
        """Gets the database of this SlowlogResult.

        所属数据库。

        :return: The database of this SlowlogResult.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this SlowlogResult.

        所属数据库。

        :param database: The database of this SlowlogResult.
        :type database: str
        """
        self._database = database

    @property
    def query_sample(self):
        """Gets the query_sample of this SlowlogResult.

        执行语法。

        :return: The query_sample of this SlowlogResult.
        :rtype: str
        """
        return self._query_sample

    @query_sample.setter
    def query_sample(self, query_sample):
        """Sets the query_sample of this SlowlogResult.

        执行语法。

        :param query_sample: The query_sample of this SlowlogResult.
        :type query_sample: str
        """
        self._query_sample = query_sample

    @property
    def type(self):
        """Gets the type of this SlowlogResult.

        语句类型。

        :return: The type of this SlowlogResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SlowlogResult.

        语句类型。

        :param type: The type of this SlowlogResult.
        :type type: str
        """
        self._type = type

    @property
    def start_time(self):
        """Gets the start_time of this SlowlogResult.

        发生时间，UTC时间。

        :return: The start_time of this SlowlogResult.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this SlowlogResult.

        发生时间，UTC时间。

        :param start_time: The start_time of this SlowlogResult.
        :type start_time: str
        """
        self._start_time = start_time

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
        if not isinstance(other, SlowlogResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
