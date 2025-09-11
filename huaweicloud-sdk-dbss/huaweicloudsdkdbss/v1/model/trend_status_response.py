# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrendStatusResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_id': 'str',
        'db_name': 'str',
        'generate_time': 'str',
        'statistics_type': 'str'
    }

    attribute_map = {
        'db_id': 'db_id',
        'db_name': 'db_name',
        'generate_time': 'generate_time',
        'statistics_type': 'statistics_type'
    }

    def __init__(self, db_id=None, db_name=None, generate_time=None, statistics_type=None):
        r"""TrendStatusResponse

        The model defined in huaweicloud sdk

        :param db_id: 数据库ID
        :type db_id: str
        :param db_name: 数据库名称
        :type db_name: str
        :param generate_time: 生成时间
        :type generate_time: str
        :param statistics_type: 统计类型  - RISK: 风险  - SESSION：SESSION  - SQL: SQL  - COUNT: 数量  - INJECTION：注入 - OPERATION: 操作
        :type statistics_type: str
        """
        
        

        self._db_id = None
        self._db_name = None
        self._generate_time = None
        self._statistics_type = None
        self.discriminator = None

        if db_id is not None:
            self.db_id = db_id
        if db_name is not None:
            self.db_name = db_name
        if generate_time is not None:
            self.generate_time = generate_time
        if statistics_type is not None:
            self.statistics_type = statistics_type

    @property
    def db_id(self):
        r"""Gets the db_id of this TrendStatusResponse.

        数据库ID

        :return: The db_id of this TrendStatusResponse.
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        r"""Sets the db_id of this TrendStatusResponse.

        数据库ID

        :param db_id: The db_id of this TrendStatusResponse.
        :type db_id: str
        """
        self._db_id = db_id

    @property
    def db_name(self):
        r"""Gets the db_name of this TrendStatusResponse.

        数据库名称

        :return: The db_name of this TrendStatusResponse.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this TrendStatusResponse.

        数据库名称

        :param db_name: The db_name of this TrendStatusResponse.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def generate_time(self):
        r"""Gets the generate_time of this TrendStatusResponse.

        生成时间

        :return: The generate_time of this TrendStatusResponse.
        :rtype: str
        """
        return self._generate_time

    @generate_time.setter
    def generate_time(self, generate_time):
        r"""Sets the generate_time of this TrendStatusResponse.

        生成时间

        :param generate_time: The generate_time of this TrendStatusResponse.
        :type generate_time: str
        """
        self._generate_time = generate_time

    @property
    def statistics_type(self):
        r"""Gets the statistics_type of this TrendStatusResponse.

        统计类型  - RISK: 风险  - SESSION：SESSION  - SQL: SQL  - COUNT: 数量  - INJECTION：注入 - OPERATION: 操作

        :return: The statistics_type of this TrendStatusResponse.
        :rtype: str
        """
        return self._statistics_type

    @statistics_type.setter
    def statistics_type(self, statistics_type):
        r"""Sets the statistics_type of this TrendStatusResponse.

        统计类型  - RISK: 风险  - SESSION：SESSION  - SQL: SQL  - COUNT: 数量  - INJECTION：注入 - OPERATION: 操作

        :param statistics_type: The statistics_type of this TrendStatusResponse.
        :type statistics_type: str
        """
        self._statistics_type = statistics_type

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
        if not isinstance(other, TrendStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
