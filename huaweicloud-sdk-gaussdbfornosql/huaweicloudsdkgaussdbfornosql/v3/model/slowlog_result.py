# coding: utf-8

import pprint
import re

import six





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
        'node_name': 'str',
        'database': 'str',
        'query_sample': 'str',
        'type': 'str',
        'start_time': 'str'
    }

    attribute_map = {
        'node_name': 'node_name',
        'database': 'database',
        'query_sample': 'query_sample',
        'type': 'type',
        'start_time': 'start_time'
    }

    def __init__(self, node_name=None, database=None, query_sample=None, type=None, start_time=None):
        """SlowlogResult - a model defined in huaweicloud sdk"""
        
        

        self._node_name = None
        self._database = None
        self._query_sample = None
        self._type = None
        self._start_time = None
        self.discriminator = None

        if node_name is not None:
            self.node_name = node_name
        self.database = database
        self.query_sample = query_sample
        self.type = type
        self.start_time = start_time

    @property
    def node_name(self):
        """Gets the node_name of this SlowlogResult.

        节点名称。

        :return: The node_name of this SlowlogResult.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this SlowlogResult.

        节点名称。

        :param node_name: The node_name of this SlowlogResult.
        :type: str
        """
        self._node_name = node_name

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
        :type: str
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
        :type: str
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
        :type: str
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
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SlowlogResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
