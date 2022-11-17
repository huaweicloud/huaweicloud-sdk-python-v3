# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlSwitchStatusRequest:

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
        'type': 'str',
        'datastore_type': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'type': 'type',
        'datastore_type': 'datastore_type',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, type=None, datastore_type=None, x_language=None):
        """ShowSqlSwitchStatusRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param type: 开关类型。取值DAS SQL Explorer和DAS Slow Query Log，分别表示DAS收集全量SQL开关和DAS收集慢SQL开关。
        :type type: str
        :param datastore_type: 数据库类型。当前全量SQL支持的数据库类型包括MySQL和GaussDB(for MySQL)，慢SQL支持的类型：MySQL、GaussDB(for MySQL)、PostgreSQL。
        :type datastore_type: str
        :param x_language: 请求语言类型。
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._type = None
        self._datastore_type = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        self.type = type
        self.datastore_type = datastore_type
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowSqlSwitchStatusRequest.

        实例ID。

        :return: The instance_id of this ShowSqlSwitchStatusRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowSqlSwitchStatusRequest.

        实例ID。

        :param instance_id: The instance_id of this ShowSqlSwitchStatusRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def type(self):
        """Gets the type of this ShowSqlSwitchStatusRequest.

        开关类型。取值DAS SQL Explorer和DAS Slow Query Log，分别表示DAS收集全量SQL开关和DAS收集慢SQL开关。

        :return: The type of this ShowSqlSwitchStatusRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowSqlSwitchStatusRequest.

        开关类型。取值DAS SQL Explorer和DAS Slow Query Log，分别表示DAS收集全量SQL开关和DAS收集慢SQL开关。

        :param type: The type of this ShowSqlSwitchStatusRequest.
        :type type: str
        """
        self._type = type

    @property
    def datastore_type(self):
        """Gets the datastore_type of this ShowSqlSwitchStatusRequest.

        数据库类型。当前全量SQL支持的数据库类型包括MySQL和GaussDB(for MySQL)，慢SQL支持的类型：MySQL、GaussDB(for MySQL)、PostgreSQL。

        :return: The datastore_type of this ShowSqlSwitchStatusRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        """Sets the datastore_type of this ShowSqlSwitchStatusRequest.

        数据库类型。当前全量SQL支持的数据库类型包括MySQL和GaussDB(for MySQL)，慢SQL支持的类型：MySQL、GaussDB(for MySQL)、PostgreSQL。

        :param datastore_type: The datastore_type of this ShowSqlSwitchStatusRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def x_language(self):
        """Gets the x_language of this ShowSqlSwitchStatusRequest.

        请求语言类型。

        :return: The x_language of this ShowSqlSwitchStatusRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowSqlSwitchStatusRequest.

        请求语言类型。

        :param x_language: The x_language of this ShowSqlSwitchStatusRequest.
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
        if not isinstance(other, ShowSqlSwitchStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
