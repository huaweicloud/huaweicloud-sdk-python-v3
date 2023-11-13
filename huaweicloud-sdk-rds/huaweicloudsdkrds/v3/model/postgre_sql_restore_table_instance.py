# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostgreSQLRestoreTableInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restore_time': 'int',
        'instance_id': 'str',
        'databases': 'list[PostgreSQLRestoreDatabase]'
    }

    attribute_map = {
        'restore_time': 'restore_time',
        'instance_id': 'instance_id',
        'databases': 'databases'
    }

    def __init__(self, restore_time=None, instance_id=None, databases=None):
        """PostgreSQLRestoreTableInstance

        The model defined in huaweicloud sdk

        :param restore_time: 恢复时间
        :type restore_time: int
        :param instance_id: 实例ID
        :type instance_id: str
        :param databases: 数据库信息
        :type databases: list[:class:`huaweicloudsdkrds.v3.PostgreSQLRestoreDatabase`]
        """
        
        

        self._restore_time = None
        self._instance_id = None
        self._databases = None
        self.discriminator = None

        if restore_time is not None:
            self.restore_time = restore_time
        if instance_id is not None:
            self.instance_id = instance_id
        if databases is not None:
            self.databases = databases

    @property
    def restore_time(self):
        """Gets the restore_time of this PostgreSQLRestoreTableInstance.

        恢复时间

        :return: The restore_time of this PostgreSQLRestoreTableInstance.
        :rtype: int
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        """Sets the restore_time of this PostgreSQLRestoreTableInstance.

        恢复时间

        :param restore_time: The restore_time of this PostgreSQLRestoreTableInstance.
        :type restore_time: int
        """
        self._restore_time = restore_time

    @property
    def instance_id(self):
        """Gets the instance_id of this PostgreSQLRestoreTableInstance.

        实例ID

        :return: The instance_id of this PostgreSQLRestoreTableInstance.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this PostgreSQLRestoreTableInstance.

        实例ID

        :param instance_id: The instance_id of this PostgreSQLRestoreTableInstance.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def databases(self):
        """Gets the databases of this PostgreSQLRestoreTableInstance.

        数据库信息

        :return: The databases of this PostgreSQLRestoreTableInstance.
        :rtype: list[:class:`huaweicloudsdkrds.v3.PostgreSQLRestoreDatabase`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this PostgreSQLRestoreTableInstance.

        数据库信息

        :param databases: The databases of this PostgreSQLRestoreTableInstance.
        :type databases: list[:class:`huaweicloudsdkrds.v3.PostgreSQLRestoreDatabase`]
        """
        self._databases = databases

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
        if not isinstance(other, PostgreSQLRestoreTableInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
