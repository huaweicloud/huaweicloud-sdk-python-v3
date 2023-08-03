# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataConnector:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connector_name': 'str',
        'source_type': 'str',
        'source_info': 'str'
    }

    attribute_map = {
        'connector_name': 'connector_name',
        'source_type': 'source_type',
        'source_info': 'source_info'
    }

    def __init__(self, connector_name=None, source_type=None, source_info=None):
        """DataConnector

        The model defined in huaweicloud sdk

        :param connector_name: 数据连接名称。
        :type connector_name: str
        :param source_type: 数据连接类型。 - RDS_POSTGRES：RDS服务PostgreSQL数据库 - RDS_MYSQL：RDS服务MySQL数据库 - gaussdb-mysql：云数据库GaussDB(for MySQL)
        :type source_type: str
        :param source_info: 数据源信息，为json格式，不同数据连接有不同的信息，各数据源的source_info请求内容可参见示例。
        :type source_info: str
        """
        
        

        self._connector_name = None
        self._source_type = None
        self._source_info = None
        self.discriminator = None

        self.connector_name = connector_name
        self.source_type = source_type
        self.source_info = source_info

    @property
    def connector_name(self):
        """Gets the connector_name of this DataConnector.

        数据连接名称。

        :return: The connector_name of this DataConnector.
        :rtype: str
        """
        return self._connector_name

    @connector_name.setter
    def connector_name(self, connector_name):
        """Sets the connector_name of this DataConnector.

        数据连接名称。

        :param connector_name: The connector_name of this DataConnector.
        :type connector_name: str
        """
        self._connector_name = connector_name

    @property
    def source_type(self):
        """Gets the source_type of this DataConnector.

        数据连接类型。 - RDS_POSTGRES：RDS服务PostgreSQL数据库 - RDS_MYSQL：RDS服务MySQL数据库 - gaussdb-mysql：云数据库GaussDB(for MySQL)

        :return: The source_type of this DataConnector.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this DataConnector.

        数据连接类型。 - RDS_POSTGRES：RDS服务PostgreSQL数据库 - RDS_MYSQL：RDS服务MySQL数据库 - gaussdb-mysql：云数据库GaussDB(for MySQL)

        :param source_type: The source_type of this DataConnector.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def source_info(self):
        """Gets the source_info of this DataConnector.

        数据源信息，为json格式，不同数据连接有不同的信息，各数据源的source_info请求内容可参见示例。

        :return: The source_info of this DataConnector.
        :rtype: str
        """
        return self._source_info

    @source_info.setter
    def source_info(self, source_info):
        """Sets the source_info of this DataConnector.

        数据源信息，为json格式，不同数据连接有不同的信息，各数据源的source_info请求内容可参见示例。

        :param source_info: The source_info of this DataConnector.
        :type source_info: str
        """
        self._source_info = source_info

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
        if not isinstance(other, DataConnector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
