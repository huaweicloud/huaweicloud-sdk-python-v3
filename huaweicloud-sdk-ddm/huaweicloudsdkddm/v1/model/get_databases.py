# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetDatabases:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'dbslot': 'int',
        'name': 'str',
        'status': 'str',
        'created': 'str',
        'updated': 'str',
        'id': 'str',
        'id_name': 'str'
    }

    attribute_map = {
        'dbslot': 'dbslot',
        'name': 'name',
        'status': 'status',
        'created': 'created',
        'updated': 'updated',
        'id': 'id',
        'id_name': 'idName'
    }

    def __init__(self, dbslot=None, name=None, status=None, created=None, updated=None, id=None, id_name=None):
        """GetDatabases

        The model defined in huaweicloud sdk

        :param dbslot: 分片数。
        :type dbslot: int
        :param name: 分片名称.
        :type name: str
        :param status: 状态。
        :type status: str
        :param created: 创建时间。
        :type created: str
        :param updated: 最近更新时间。
        :type updated: str
        :param id: 所在RDS的id。
        :type id: str
        :param id_name: 所在RDS的名称。
        :type id_name: str
        """
        
        

        self._dbslot = None
        self._name = None
        self._status = None
        self._created = None
        self._updated = None
        self._id = None
        self._id_name = None
        self.discriminator = None

        self.dbslot = dbslot
        self.name = name
        self.status = status
        self.created = created
        self.updated = updated
        self.id = id
        self.id_name = id_name

    @property
    def dbslot(self):
        """Gets the dbslot of this GetDatabases.

        分片数。

        :return: The dbslot of this GetDatabases.
        :rtype: int
        """
        return self._dbslot

    @dbslot.setter
    def dbslot(self, dbslot):
        """Sets the dbslot of this GetDatabases.

        分片数。

        :param dbslot: The dbslot of this GetDatabases.
        :type dbslot: int
        """
        self._dbslot = dbslot

    @property
    def name(self):
        """Gets the name of this GetDatabases.

        分片名称.

        :return: The name of this GetDatabases.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetDatabases.

        分片名称.

        :param name: The name of this GetDatabases.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this GetDatabases.

        状态。

        :return: The status of this GetDatabases.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetDatabases.

        状态。

        :param status: The status of this GetDatabases.
        :type status: str
        """
        self._status = status

    @property
    def created(self):
        """Gets the created of this GetDatabases.

        创建时间。

        :return: The created of this GetDatabases.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GetDatabases.

        创建时间。

        :param created: The created of this GetDatabases.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this GetDatabases.

        最近更新时间。

        :return: The updated of this GetDatabases.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this GetDatabases.

        最近更新时间。

        :param updated: The updated of this GetDatabases.
        :type updated: str
        """
        self._updated = updated

    @property
    def id(self):
        """Gets the id of this GetDatabases.

        所在RDS的id。

        :return: The id of this GetDatabases.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetDatabases.

        所在RDS的id。

        :param id: The id of this GetDatabases.
        :type id: str
        """
        self._id = id

    @property
    def id_name(self):
        """Gets the id_name of this GetDatabases.

        所在RDS的名称。

        :return: The id_name of this GetDatabases.
        :rtype: str
        """
        return self._id_name

    @id_name.setter
    def id_name(self, id_name):
        """Sets the id_name of this GetDatabases.

        所在RDS的名称。

        :param id_name: The id_name of this GetDatabases.
        :type id_name: str
        """
        self._id_name = id_name

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
        if not isinstance(other, GetDatabases):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
