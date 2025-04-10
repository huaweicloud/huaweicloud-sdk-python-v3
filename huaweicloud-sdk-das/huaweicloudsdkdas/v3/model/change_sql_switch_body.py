# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeSqlSwitchBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'status': 'int',
        'datastore_type': 'str',
        'retention_days': 'int'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'datastore_type': 'datastore_type',
        'retention_days': 'retention_days'
    }

    def __init__(self, type=None, status=None, datastore_type=None, retention_days=None):
        r"""ChangeSqlSwitchBody

        The model defined in huaweicloud sdk

        :param type: 开关类型。取值DAS SQL Explorer和DAS Slow Query Log，分别表示DAS收集全量SQL开关和DAS收集慢SQL开关。
        :type type: str
        :param status: 开关状态，取值0和1，分别代表要关闭和开启。
        :type status: int
        :param datastore_type: 数据库类型。当前全量SQL支持的数据库类型包括MySQL和GaussDB(for MySQL)，慢SQL支持的类型：MySQL、GaussDB(for MySQL)、PostgreSQL。
        :type datastore_type: str
        :param retention_days: SQL数据保存时长（天）。默认为7天，最长可保留30天，到期后数据自动删除。如果要保留30天以上，请到DAS页面进行操作。
        :type retention_days: int
        """
        
        

        self._type = None
        self._status = None
        self._datastore_type = None
        self._retention_days = None
        self.discriminator = None

        self.type = type
        self.status = status
        self.datastore_type = datastore_type
        if retention_days is not None:
            self.retention_days = retention_days

    @property
    def type(self):
        r"""Gets the type of this ChangeSqlSwitchBody.

        开关类型。取值DAS SQL Explorer和DAS Slow Query Log，分别表示DAS收集全量SQL开关和DAS收集慢SQL开关。

        :return: The type of this ChangeSqlSwitchBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ChangeSqlSwitchBody.

        开关类型。取值DAS SQL Explorer和DAS Slow Query Log，分别表示DAS收集全量SQL开关和DAS收集慢SQL开关。

        :param type: The type of this ChangeSqlSwitchBody.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ChangeSqlSwitchBody.

        开关状态，取值0和1，分别代表要关闭和开启。

        :return: The status of this ChangeSqlSwitchBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ChangeSqlSwitchBody.

        开关状态，取值0和1，分别代表要关闭和开启。

        :param status: The status of this ChangeSqlSwitchBody.
        :type status: int
        """
        self._status = status

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ChangeSqlSwitchBody.

        数据库类型。当前全量SQL支持的数据库类型包括MySQL和GaussDB(for MySQL)，慢SQL支持的类型：MySQL、GaussDB(for MySQL)、PostgreSQL。

        :return: The datastore_type of this ChangeSqlSwitchBody.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ChangeSqlSwitchBody.

        数据库类型。当前全量SQL支持的数据库类型包括MySQL和GaussDB(for MySQL)，慢SQL支持的类型：MySQL、GaussDB(for MySQL)、PostgreSQL。

        :param datastore_type: The datastore_type of this ChangeSqlSwitchBody.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def retention_days(self):
        r"""Gets the retention_days of this ChangeSqlSwitchBody.

        SQL数据保存时长（天）。默认为7天，最长可保留30天，到期后数据自动删除。如果要保留30天以上，请到DAS页面进行操作。

        :return: The retention_days of this ChangeSqlSwitchBody.
        :rtype: int
        """
        return self._retention_days

    @retention_days.setter
    def retention_days(self, retention_days):
        r"""Sets the retention_days of this ChangeSqlSwitchBody.

        SQL数据保存时长（天）。默认为7天，最长可保留30天，到期后数据自动删除。如果要保留30天以上，请到DAS页面进行操作。

        :param retention_days: The retention_days of this ChangeSqlSwitchBody.
        :type retention_days: int
        """
        self._retention_days = retention_days

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
        if not isinstance(other, ChangeSqlSwitchBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
