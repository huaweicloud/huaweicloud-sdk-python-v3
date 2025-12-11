# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RdsDbRequestDatabases:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type'
    }

    def __init__(self, id=None, type=None):
        r"""RdsDbRequestDatabases

        The model defined in huaweicloud sdk

        :param id: rds数据库id，可在查询rds数据库列表接口的ID字段获取。
        :type id: str
        :param type: 数据库类型 - MYSQL: MySQL - ORACLE: Oracle - POSTGRESQL: PostgreSQL - SQLSERVER: SQL Server - DAMENG:  DAMENG - TAURUS: Taurus DB - DWS: GaussDB(DWS) - KINGBASE: Kingbase - MARIADB: MariaDB - GAUSSDBOPENGAUSS: GaussDB/openGauss
        :type type: str
        """
        
        

        self._id = None
        self._type = None
        self.discriminator = None

        self.id = id
        self.type = type

    @property
    def id(self):
        r"""Gets the id of this RdsDbRequestDatabases.

        rds数据库id，可在查询rds数据库列表接口的ID字段获取。

        :return: The id of this RdsDbRequestDatabases.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RdsDbRequestDatabases.

        rds数据库id，可在查询rds数据库列表接口的ID字段获取。

        :param id: The id of this RdsDbRequestDatabases.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this RdsDbRequestDatabases.

        数据库类型 - MYSQL: MySQL - ORACLE: Oracle - POSTGRESQL: PostgreSQL - SQLSERVER: SQL Server - DAMENG:  DAMENG - TAURUS: Taurus DB - DWS: GaussDB(DWS) - KINGBASE: Kingbase - MARIADB: MariaDB - GAUSSDBOPENGAUSS: GaussDB/openGauss

        :return: The type of this RdsDbRequestDatabases.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RdsDbRequestDatabases.

        数据库类型 - MYSQL: MySQL - ORACLE: Oracle - POSTGRESQL: PostgreSQL - SQLSERVER: SQL Server - DAMENG:  DAMENG - TAURUS: Taurus DB - DWS: GaussDB(DWS) - KINGBASE: Kingbase - MARIADB: MariaDB - GAUSSDBOPENGAUSS: GaussDB/openGauss

        :param type: The type of this RdsDbRequestDatabases.
        :type type: str
        """
        self._type = type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RdsDbRequestDatabases):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
