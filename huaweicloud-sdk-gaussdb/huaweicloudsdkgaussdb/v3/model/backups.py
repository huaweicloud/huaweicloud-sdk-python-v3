# coding: utf-8

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
        'datastore': 'MysqlDatastoreInBackup',
        'instance_id': 'str',
        'instance_name': 'str',
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
        'instance_name': 'instance_name',
        'backup_level': 'backup_level',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, begin_time=None, end_time=None, status=None, take_up_time=None, type=None, size=None, datastore=None, instance_id=None, instance_name=None, backup_level=None, description=None):
        r"""Backups

        The model defined in huaweicloud sdk

        :param id: 备份ID。
        :type id: str
        :param name: 备份名称。
        :type name: str
        :param begin_time: 备份开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type begin_time: str
        :param end_time: 备份结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。
        :type end_time: str
        :param status: 备份状态，取值： - BUILDING：备份中。 - COMPLETED：备份完成。 - FAILED：备份失败。 - AVAILABLE：备份可用。
        :type status: str
        :param take_up_time: 备份花费时间（单位：minutes）
        :type take_up_time: int
        :param type: 备份类型，取值：  - auto：自动全量备份。 - manual：手动全量备份。
        :type type: str
        :param size: 备份大小（单位：MB）。
        :type size: int
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdb.v3.MysqlDatastoreInBackup`
        :param instance_id: 实例ID，严格匹配UUID规则。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param backup_level: 备份级别。当开启一级备份开关时，返回该参数。
        :type backup_level: str
        :param description: 备份文件描述信息。
        :type description: str
        """
        
        

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
        self._instance_name = None
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
        if instance_name is not None:
            self.instance_name = instance_name
        if backup_level is not None:
            self.backup_level = backup_level
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this Backups.

        备份ID。

        :return: The id of this Backups.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Backups.

        备份ID。

        :param id: The id of this Backups.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Backups.

        备份名称。

        :return: The name of this Backups.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Backups.

        备份名称。

        :param name: The name of this Backups.
        :type name: str
        """
        self._name = name

    @property
    def begin_time(self):
        r"""Gets the begin_time of this Backups.

        备份开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The begin_time of this Backups.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this Backups.

        备份开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param begin_time: The begin_time of this Backups.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this Backups.

        备份结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :return: The end_time of this Backups.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this Backups.

        备份结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。

        :param end_time: The end_time of this Backups.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this Backups.

        备份状态，取值： - BUILDING：备份中。 - COMPLETED：备份完成。 - FAILED：备份失败。 - AVAILABLE：备份可用。

        :return: The status of this Backups.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Backups.

        备份状态，取值： - BUILDING：备份中。 - COMPLETED：备份完成。 - FAILED：备份失败。 - AVAILABLE：备份可用。

        :param status: The status of this Backups.
        :type status: str
        """
        self._status = status

    @property
    def take_up_time(self):
        r"""Gets the take_up_time of this Backups.

        备份花费时间（单位：minutes）

        :return: The take_up_time of this Backups.
        :rtype: int
        """
        return self._take_up_time

    @take_up_time.setter
    def take_up_time(self, take_up_time):
        r"""Sets the take_up_time of this Backups.

        备份花费时间（单位：minutes）

        :param take_up_time: The take_up_time of this Backups.
        :type take_up_time: int
        """
        self._take_up_time = take_up_time

    @property
    def type(self):
        r"""Gets the type of this Backups.

        备份类型，取值：  - auto：自动全量备份。 - manual：手动全量备份。

        :return: The type of this Backups.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Backups.

        备份类型，取值：  - auto：自动全量备份。 - manual：手动全量备份。

        :param type: The type of this Backups.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        r"""Gets the size of this Backups.

        备份大小（单位：MB）。

        :return: The size of this Backups.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this Backups.

        备份大小（单位：MB）。

        :param size: The size of this Backups.
        :type size: int
        """
        self._size = size

    @property
    def datastore(self):
        r"""Gets the datastore of this Backups.

        :return: The datastore of this Backups.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlDatastoreInBackup`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this Backups.

        :param datastore: The datastore of this Backups.
        :type datastore: :class:`huaweicloudsdkgaussdb.v3.MysqlDatastoreInBackup`
        """
        self._datastore = datastore

    @property
    def instance_id(self):
        r"""Gets the instance_id of this Backups.

        实例ID，严格匹配UUID规则。

        :return: The instance_id of this Backups.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this Backups.

        实例ID，严格匹配UUID规则。

        :param instance_id: The instance_id of this Backups.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this Backups.

        实例名称。

        :return: The instance_name of this Backups.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this Backups.

        实例名称。

        :param instance_name: The instance_name of this Backups.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def backup_level(self):
        r"""Gets the backup_level of this Backups.

        备份级别。当开启一级备份开关时，返回该参数。

        :return: The backup_level of this Backups.
        :rtype: str
        """
        return self._backup_level

    @backup_level.setter
    def backup_level(self, backup_level):
        r"""Sets the backup_level of this Backups.

        备份级别。当开启一级备份开关时，返回该参数。

        :param backup_level: The backup_level of this Backups.
        :type backup_level: str
        """
        self._backup_level = backup_level

    @property
    def description(self):
        r"""Gets the description of this Backups.

        备份文件描述信息。

        :return: The description of this Backups.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Backups.

        备份文件描述信息。

        :param description: The description of this Backups.
        :type description: str
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
