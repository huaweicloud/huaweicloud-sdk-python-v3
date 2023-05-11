# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreInstanceFromCollectionRequestBodyRestoreCollections:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database': 'str',
        'restore_database_time': 'str',
        'collections': 'list[RestoreInstanceFromCollectionRequestBodyCollections]'
    }

    attribute_map = {
        'database': 'database',
        'restore_database_time': 'restore_database_time',
        'collections': 'collections'
    }

    def __init__(self, database=None, restore_database_time=None, collections=None):
        """RestoreInstanceFromCollectionRequestBodyRestoreCollections

        The model defined in huaweicloud sdk

        :param database: 数据库名称。
        :type database: str
        :param restore_database_time: 数据库恢复时间点。如果是数据库级恢复，该参数必传，UNIX时间戳格式，单位是毫秒，时区是UTC。
        :type restore_database_time: str
        :param collections: 集合信息。
        :type collections: list[:class:`huaweicloudsdkdds.v3.RestoreInstanceFromCollectionRequestBodyCollections`]
        """
        
        

        self._database = None
        self._restore_database_time = None
        self._collections = None
        self.discriminator = None

        self.database = database
        if restore_database_time is not None:
            self.restore_database_time = restore_database_time
        if collections is not None:
            self.collections = collections

    @property
    def database(self):
        """Gets the database of this RestoreInstanceFromCollectionRequestBodyRestoreCollections.

        数据库名称。

        :return: The database of this RestoreInstanceFromCollectionRequestBodyRestoreCollections.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this RestoreInstanceFromCollectionRequestBodyRestoreCollections.

        数据库名称。

        :param database: The database of this RestoreInstanceFromCollectionRequestBodyRestoreCollections.
        :type database: str
        """
        self._database = database

    @property
    def restore_database_time(self):
        """Gets the restore_database_time of this RestoreInstanceFromCollectionRequestBodyRestoreCollections.

        数据库恢复时间点。如果是数据库级恢复，该参数必传，UNIX时间戳格式，单位是毫秒，时区是UTC。

        :return: The restore_database_time of this RestoreInstanceFromCollectionRequestBodyRestoreCollections.
        :rtype: str
        """
        return self._restore_database_time

    @restore_database_time.setter
    def restore_database_time(self, restore_database_time):
        """Sets the restore_database_time of this RestoreInstanceFromCollectionRequestBodyRestoreCollections.

        数据库恢复时间点。如果是数据库级恢复，该参数必传，UNIX时间戳格式，单位是毫秒，时区是UTC。

        :param restore_database_time: The restore_database_time of this RestoreInstanceFromCollectionRequestBodyRestoreCollections.
        :type restore_database_time: str
        """
        self._restore_database_time = restore_database_time

    @property
    def collections(self):
        """Gets the collections of this RestoreInstanceFromCollectionRequestBodyRestoreCollections.

        集合信息。

        :return: The collections of this RestoreInstanceFromCollectionRequestBodyRestoreCollections.
        :rtype: list[:class:`huaweicloudsdkdds.v3.RestoreInstanceFromCollectionRequestBodyCollections`]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this RestoreInstanceFromCollectionRequestBodyRestoreCollections.

        集合信息。

        :param collections: The collections of this RestoreInstanceFromCollectionRequestBodyRestoreCollections.
        :type collections: list[:class:`huaweicloudsdkdds.v3.RestoreInstanceFromCollectionRequestBodyCollections`]
        """
        self._collections = collections

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
        if not isinstance(other, RestoreInstanceFromCollectionRequestBodyRestoreCollections):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
