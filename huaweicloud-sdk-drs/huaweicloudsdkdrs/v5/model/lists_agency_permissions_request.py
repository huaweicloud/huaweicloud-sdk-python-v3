# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListsAgencyPermissionsRequest:

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
        'source_type': 'str',
        'target_type': 'str',
        'is_non_dbs': 'bool'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'source_type': 'source_type',
        'target_type': 'target_type',
        'is_non_dbs': 'is_non_dbs'
    }

    def __init__(self, x_language=None, source_type=None, target_type=None, is_non_dbs=None):
        """ListsAgencyPermissionsRequest

        The model defined in huaweicloud sdk

        :param x_language: 请求语言类型。
        :type x_language: str
        :param source_type: 源库类型 - mysql - sqlserver - postgresql - hwsql - mongodb - dws - oracle - taurus - tauruslite - ddm - kafka - mrsKafka - gaussdb - gaussdbv5 - gaussdbv5ha - gaussmongodb - cassandra - dmq - gaussdbt - gaussdb300 - gaussdbtha - elasticsearch - db2 - tidb - redis - rediscluster - gaussredis - mariadb - gaussdbv1 - informix - dynamo - gausscassandra - oceanbase
        :type source_type: str
        :param target_type: 目标库类型 - mysql - sqlserver - postgresql - hwsql - mongodb - dws - oracle - taurus - tauruslite - ddm - kafka - mrsKafka - gaussdb - gaussdbv5 - gaussdbv5ha - gaussmongodb - cassandra - dmq - gaussdbt - gaussdb300 - gaussdbtha - elasticsearch - db2 - tidb - redis - rediscluster - gaussredis - mariadb - gaussdbv1 - informix - dynamo - gausscassandra - oceanbase
        :type target_type: str
        :param is_non_dbs: 是否自建。
        :type is_non_dbs: bool
        """
        
        

        self._x_language = None
        self._source_type = None
        self._target_type = None
        self._is_non_dbs = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if source_type is not None:
            self.source_type = source_type
        if target_type is not None:
            self.target_type = target_type
        self.is_non_dbs = is_non_dbs

    @property
    def x_language(self):
        """Gets the x_language of this ListsAgencyPermissionsRequest.

        请求语言类型。

        :return: The x_language of this ListsAgencyPermissionsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListsAgencyPermissionsRequest.

        请求语言类型。

        :param x_language: The x_language of this ListsAgencyPermissionsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def source_type(self):
        """Gets the source_type of this ListsAgencyPermissionsRequest.

        源库类型 - mysql - sqlserver - postgresql - hwsql - mongodb - dws - oracle - taurus - tauruslite - ddm - kafka - mrsKafka - gaussdb - gaussdbv5 - gaussdbv5ha - gaussmongodb - cassandra - dmq - gaussdbt - gaussdb300 - gaussdbtha - elasticsearch - db2 - tidb - redis - rediscluster - gaussredis - mariadb - gaussdbv1 - informix - dynamo - gausscassandra - oceanbase

        :return: The source_type of this ListsAgencyPermissionsRequest.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this ListsAgencyPermissionsRequest.

        源库类型 - mysql - sqlserver - postgresql - hwsql - mongodb - dws - oracle - taurus - tauruslite - ddm - kafka - mrsKafka - gaussdb - gaussdbv5 - gaussdbv5ha - gaussmongodb - cassandra - dmq - gaussdbt - gaussdb300 - gaussdbtha - elasticsearch - db2 - tidb - redis - rediscluster - gaussredis - mariadb - gaussdbv1 - informix - dynamo - gausscassandra - oceanbase

        :param source_type: The source_type of this ListsAgencyPermissionsRequest.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def target_type(self):
        """Gets the target_type of this ListsAgencyPermissionsRequest.

        目标库类型 - mysql - sqlserver - postgresql - hwsql - mongodb - dws - oracle - taurus - tauruslite - ddm - kafka - mrsKafka - gaussdb - gaussdbv5 - gaussdbv5ha - gaussmongodb - cassandra - dmq - gaussdbt - gaussdb300 - gaussdbtha - elasticsearch - db2 - tidb - redis - rediscluster - gaussredis - mariadb - gaussdbv1 - informix - dynamo - gausscassandra - oceanbase

        :return: The target_type of this ListsAgencyPermissionsRequest.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this ListsAgencyPermissionsRequest.

        目标库类型 - mysql - sqlserver - postgresql - hwsql - mongodb - dws - oracle - taurus - tauruslite - ddm - kafka - mrsKafka - gaussdb - gaussdbv5 - gaussdbv5ha - gaussmongodb - cassandra - dmq - gaussdbt - gaussdb300 - gaussdbtha - elasticsearch - db2 - tidb - redis - rediscluster - gaussredis - mariadb - gaussdbv1 - informix - dynamo - gausscassandra - oceanbase

        :param target_type: The target_type of this ListsAgencyPermissionsRequest.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def is_non_dbs(self):
        """Gets the is_non_dbs of this ListsAgencyPermissionsRequest.

        是否自建。

        :return: The is_non_dbs of this ListsAgencyPermissionsRequest.
        :rtype: bool
        """
        return self._is_non_dbs

    @is_non_dbs.setter
    def is_non_dbs(self, is_non_dbs):
        """Sets the is_non_dbs of this ListsAgencyPermissionsRequest.

        是否自建。

        :param is_non_dbs: The is_non_dbs of this ListsAgencyPermissionsRequest.
        :type is_non_dbs: bool
        """
        self._is_non_dbs = is_non_dbs

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
        if not isinstance(other, ListsAgencyPermissionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
