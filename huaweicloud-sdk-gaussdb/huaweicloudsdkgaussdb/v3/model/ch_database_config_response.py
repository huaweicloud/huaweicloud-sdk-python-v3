# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChDatabaseConfigResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        'db_config_check_results': 'list[ChDatabaseConfigCheckResult]'
    }

    attribute_map = {
        'database_name': 'database_name',
        'db_config_check_results': 'db_config_check_results'
    }

    def __init__(self, database_name=None, db_config_check_results=None):
        r"""ChDatabaseConfigResponse

        The model defined in huaweicloud sdk

        :param database_name: 源数据库名称。
        :type database_name: str
        :param db_config_check_results: 源数据库配置检查结果。
        :type db_config_check_results: list[:class:`huaweicloudsdkgaussdb.v3.ChDatabaseConfigCheckResult`]
        """
        
        

        self._database_name = None
        self._db_config_check_results = None
        self.discriminator = None

        self.database_name = database_name
        self.db_config_check_results = db_config_check_results

    @property
    def database_name(self):
        r"""Gets the database_name of this ChDatabaseConfigResponse.

        源数据库名称。

        :return: The database_name of this ChDatabaseConfigResponse.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ChDatabaseConfigResponse.

        源数据库名称。

        :param database_name: The database_name of this ChDatabaseConfigResponse.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def db_config_check_results(self):
        r"""Gets the db_config_check_results of this ChDatabaseConfigResponse.

        源数据库配置检查结果。

        :return: The db_config_check_results of this ChDatabaseConfigResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ChDatabaseConfigCheckResult`]
        """
        return self._db_config_check_results

    @db_config_check_results.setter
    def db_config_check_results(self, db_config_check_results):
        r"""Sets the db_config_check_results of this ChDatabaseConfigResponse.

        源数据库配置检查结果。

        :param db_config_check_results: The db_config_check_results of this ChDatabaseConfigResponse.
        :type db_config_check_results: list[:class:`huaweicloudsdkgaussdb.v3.ChDatabaseConfigCheckResult`]
        """
        self._db_config_check_results = db_config_check_results

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
        if not isinstance(other, ChDatabaseConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
