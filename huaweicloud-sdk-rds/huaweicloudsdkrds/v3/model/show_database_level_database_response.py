# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDatabaseLevelDatabaseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'databases': 'list[DatabaseBackupInfo]',
        'database_limit': 'int',
        'bucket_name': 'str'
    }

    attribute_map = {
        'databases': 'databases',
        'database_limit': 'database_limit',
        'bucket_name': 'bucket_name'
    }

    def __init__(self, databases=None, database_limit=None, bucket_name=None):
        r"""ShowDatabaseLevelDatabaseResponse

        The model defined in huaweicloud sdk

        :param databases: 库信息列表
        :type databases: list[:class:`huaweicloudsdkrds.v3.DatabaseBackupInfo`]
        :param database_limit: 可恢复库的个数
        :type database_limit: int
        :param bucket_name: obs桶名
        :type bucket_name: str
        """
        
        super(ShowDatabaseLevelDatabaseResponse, self).__init__()

        self._databases = None
        self._database_limit = None
        self._bucket_name = None
        self.discriminator = None

        if databases is not None:
            self.databases = databases
        if database_limit is not None:
            self.database_limit = database_limit
        if bucket_name is not None:
            self.bucket_name = bucket_name

    @property
    def databases(self):
        r"""Gets the databases of this ShowDatabaseLevelDatabaseResponse.

        库信息列表

        :return: The databases of this ShowDatabaseLevelDatabaseResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.DatabaseBackupInfo`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this ShowDatabaseLevelDatabaseResponse.

        库信息列表

        :param databases: The databases of this ShowDatabaseLevelDatabaseResponse.
        :type databases: list[:class:`huaweicloudsdkrds.v3.DatabaseBackupInfo`]
        """
        self._databases = databases

    @property
    def database_limit(self):
        r"""Gets the database_limit of this ShowDatabaseLevelDatabaseResponse.

        可恢复库的个数

        :return: The database_limit of this ShowDatabaseLevelDatabaseResponse.
        :rtype: int
        """
        return self._database_limit

    @database_limit.setter
    def database_limit(self, database_limit):
        r"""Sets the database_limit of this ShowDatabaseLevelDatabaseResponse.

        可恢复库的个数

        :param database_limit: The database_limit of this ShowDatabaseLevelDatabaseResponse.
        :type database_limit: int
        """
        self._database_limit = database_limit

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this ShowDatabaseLevelDatabaseResponse.

        obs桶名

        :return: The bucket_name of this ShowDatabaseLevelDatabaseResponse.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this ShowDatabaseLevelDatabaseResponse.

        obs桶名

        :param bucket_name: The bucket_name of this ShowDatabaseLevelDatabaseResponse.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

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
        if not isinstance(other, ShowDatabaseLevelDatabaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
