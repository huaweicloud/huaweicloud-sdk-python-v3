# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShareBackups:

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
        'size': 'float',
        'type': 'str',
        'backup_method': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'instance_status': 'str',
        'datastore': 'object',
        'user_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'status': 'status',
        'size': 'size',
        'type': 'type',
        'backup_method': 'backup_method',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'instance_status': 'instance_status',
        'datastore': 'datastore',
        'user_name': 'user_name'
    }

    def __init__(self, id=None, name=None, begin_time=None, end_time=None, status=None, size=None, type=None, backup_method=None, instance_id=None, instance_name=None, instance_status=None, datastore=None, user_name=None):
        r"""ShareBackups

        The model defined in huaweicloud sdk

        :param id: 备份ID。
        :type id: str
        :param name: 备份名字。
        :type name: str
        :param begin_time: 备份开始时间。
        :type begin_time: str
        :param end_time: 备份结束时间。
        :type end_time: str
        :param status: 备份状态，取值：BUILDING：备份中，COMPLETED：备份完成，FAILED：备份失败，DELETING：备份删除中。
        :type status: str
        :param size: 备份大小，单位：KB。
        :type size: float
        :param type: 备份类型，取值：\&quot;auto\&quot;自动全量备份，“manual”手动全量备份。
        :type type: str
        :param backup_method: 备份方法。
        :type backup_method: str
        :param instance_id: 备份所在实例ID。
        :type instance_id: str
        :param instance_name: 备份所在实例名称。
        :type instance_name: str
        :param instance_status: 备份所在实例状态。
        :type instance_status: str
        :param datastore: 数据库版本信息。
        :type datastore: object
        :param user_name: 共享者用户名称。
        :type user_name: str
        """
        
        

        self._id = None
        self._name = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._size = None
        self._type = None
        self._backup_method = None
        self._instance_id = None
        self._instance_name = None
        self._instance_status = None
        self._datastore = None
        self._user_name = None
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
        if size is not None:
            self.size = size
        if type is not None:
            self.type = type
        if backup_method is not None:
            self.backup_method = backup_method
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_status is not None:
            self.instance_status = instance_status
        if datastore is not None:
            self.datastore = datastore
        if user_name is not None:
            self.user_name = user_name

    @property
    def id(self):
        r"""Gets the id of this ShareBackups.

        备份ID。

        :return: The id of this ShareBackups.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShareBackups.

        备份ID。

        :param id: The id of this ShareBackups.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShareBackups.

        备份名字。

        :return: The name of this ShareBackups.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShareBackups.

        备份名字。

        :param name: The name of this ShareBackups.
        :type name: str
        """
        self._name = name

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ShareBackups.

        备份开始时间。

        :return: The begin_time of this ShareBackups.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ShareBackups.

        备份开始时间。

        :param begin_time: The begin_time of this ShareBackups.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShareBackups.

        备份结束时间。

        :return: The end_time of this ShareBackups.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShareBackups.

        备份结束时间。

        :param end_time: The end_time of this ShareBackups.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this ShareBackups.

        备份状态，取值：BUILDING：备份中，COMPLETED：备份完成，FAILED：备份失败，DELETING：备份删除中。

        :return: The status of this ShareBackups.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShareBackups.

        备份状态，取值：BUILDING：备份中，COMPLETED：备份完成，FAILED：备份失败，DELETING：备份删除中。

        :param status: The status of this ShareBackups.
        :type status: str
        """
        self._status = status

    @property
    def size(self):
        r"""Gets the size of this ShareBackups.

        备份大小，单位：KB。

        :return: The size of this ShareBackups.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShareBackups.

        备份大小，单位：KB。

        :param size: The size of this ShareBackups.
        :type size: float
        """
        self._size = size

    @property
    def type(self):
        r"""Gets the type of this ShareBackups.

        备份类型，取值：\"auto\"自动全量备份，“manual”手动全量备份。

        :return: The type of this ShareBackups.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShareBackups.

        备份类型，取值：\"auto\"自动全量备份，“manual”手动全量备份。

        :param type: The type of this ShareBackups.
        :type type: str
        """
        self._type = type

    @property
    def backup_method(self):
        r"""Gets the backup_method of this ShareBackups.

        备份方法。

        :return: The backup_method of this ShareBackups.
        :rtype: str
        """
        return self._backup_method

    @backup_method.setter
    def backup_method(self, backup_method):
        r"""Sets the backup_method of this ShareBackups.

        备份方法。

        :param backup_method: The backup_method of this ShareBackups.
        :type backup_method: str
        """
        self._backup_method = backup_method

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShareBackups.

        备份所在实例ID。

        :return: The instance_id of this ShareBackups.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShareBackups.

        备份所在实例ID。

        :param instance_id: The instance_id of this ShareBackups.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ShareBackups.

        备份所在实例名称。

        :return: The instance_name of this ShareBackups.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ShareBackups.

        备份所在实例名称。

        :param instance_name: The instance_name of this ShareBackups.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_status(self):
        r"""Gets the instance_status of this ShareBackups.

        备份所在实例状态。

        :return: The instance_status of this ShareBackups.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this ShareBackups.

        备份所在实例状态。

        :param instance_status: The instance_status of this ShareBackups.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def datastore(self):
        r"""Gets the datastore of this ShareBackups.

        数据库版本信息。

        :return: The datastore of this ShareBackups.
        :rtype: object
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this ShareBackups.

        数据库版本信息。

        :param datastore: The datastore of this ShareBackups.
        :type datastore: object
        """
        self._datastore = datastore

    @property
    def user_name(self):
        r"""Gets the user_name of this ShareBackups.

        共享者用户名称。

        :return: The user_name of this ShareBackups.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ShareBackups.

        共享者用户名称。

        :param user_name: The user_name of this ShareBackups.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, ShareBackups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
