# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Backups:


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
        'name': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'take_up_time': 'int',
        'type': 'str',
        'size': 'int',
        'datastore': 'MysqlDatastore',
        'instance_id': 'str',
        'backup_level': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'status': 'status',
        'take_up_time': 'take_up_time',
        'type': 'type',
        'size': 'size',
        'datastore': 'datastore',
        'instance_id': 'instance_id',
        'backup_level': 'backup_level',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, begin_time=None, end_time=None, status=None, take_up_time=None, type=None, size=None, datastore=None, instance_id=None, backup_level=None, description=None):
        """Backups - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._take_up_time = None
        self._type = None
        self._size = None
        self._datastore = None
        self._instance_id = None
        self._backup_level = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if take_up_time is not None:
            self.take_up_time = take_up_time
        if type is not None:
            self.type = type
        if size is not None:
            self.size = size
        if datastore is not None:
            self.datastore = datastore
        if instance_id is not None:
            self.instance_id = instance_id
        if backup_level is not None:
            self.backup_level = backup_level
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this Backups.

        备份ID。

        :return: The id of this Backups.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Backups.

        备份ID。

        :param id: The id of this Backups.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Backups.

        备份名称。

        :return: The name of this Backups.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Backups.

        备份名称。

        :param name: The name of this Backups.
        :type: str
        """
        self._name = name

    @property
    def begin_time(self):
        """Gets the begin_time of this Backups.

        备份开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The begin_time of this Backups.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this Backups.

        备份开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param begin_time: The begin_time of this Backups.
        :type: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this Backups.

        备份结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The end_time of this Backups.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Backups.

        备份结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param end_time: The end_time of this Backups.
        :type: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this Backups.

        备份状态

        :return: The status of this Backups.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Backups.

        备份状态

        :param status: The status of this Backups.
        :type: str
        """
        self._status = status

    @property
    def take_up_time(self):
        """Gets the take_up_time of this Backups.

        备份花费时间(单位：minutes)

        :return: The take_up_time of this Backups.
        :rtype: int
        """
        return self._take_up_time

    @take_up_time.setter
    def take_up_time(self, take_up_time):
        """Sets the take_up_time of this Backups.

        备份花费时间(单位：minutes)

        :param take_up_time: The take_up_time of this Backups.
        :type: int
        """
        self._take_up_time = take_up_time

    @property
    def type(self):
        """Gets the type of this Backups.

        备份类型

        :return: The type of this Backups.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Backups.

        备份类型

        :param type: The type of this Backups.
        :type: str
        """
        self._type = type

    @property
    def size(self):
        """Gets the size of this Backups.

        备份大小，(单位：MB)

        :return: The size of this Backups.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Backups.

        备份大小，(单位：MB)

        :param size: The size of this Backups.
        :type: int
        """
        self._size = size

    @property
    def datastore(self):
        """Gets the datastore of this Backups.


        :return: The datastore of this Backups.
        :rtype: MysqlDatastore
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this Backups.


        :param datastore: The datastore of this Backups.
        :type: MysqlDatastore
        """
        self._datastore = datastore

    @property
    def instance_id(self):
        """Gets the instance_id of this Backups.

        实例ID。

        :return: The instance_id of this Backups.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this Backups.

        实例ID。

        :param instance_id: The instance_id of this Backups.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def backup_level(self):
        """Gets the backup_level of this Backups.

        备份级别。当开启一级备份开关时，返回该参数。

        :return: The backup_level of this Backups.
        :rtype: str
        """
        return self._backup_level

    @backup_level.setter
    def backup_level(self, backup_level):
        """Sets the backup_level of this Backups.

        备份级别。当开启一级备份开关时，返回该参数。

        :param backup_level: The backup_level of this Backups.
        :type: str
        """
        self._backup_level = backup_level

    @property
    def description(self):
        """Gets the description of this Backups.

        备份文件描述信息

        :return: The description of this Backups.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Backups.

        备份文件描述信息

        :param description: The description of this Backups.
        :type: str
        """
        self._description = description

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
        if not isinstance(other, Backups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
