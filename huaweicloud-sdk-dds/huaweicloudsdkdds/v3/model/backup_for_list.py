# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupForList:

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
        'instance_id': 'str',
        'instance_name': 'str',
        'datastore': 'BackupDatabase',
        'type': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'size': 'int',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'datastore': 'datastore',
        'type': 'type',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'status': 'status',
        'size': 'size',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, instance_id=None, instance_name=None, datastore=None, type=None, begin_time=None, end_time=None, status=None, size=None, description=None):
        r"""BackupForList

        The model defined in huaweicloud sdk

        :param id: 备份ID。
        :type id: str
        :param name: 备份名称。
        :type name: str
        :param instance_id: 备份所属的实例ID。
        :type instance_id: str
        :param instance_name: 备份所属的实例名称。
        :type instance_name: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkdds.v3.BackupDatabase`
        :param type: 备份类型。 - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。 - 取值为“Incremental”，表示自动增量备份。
        :type type: str
        :param begin_time: 备份开始时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。
        :type begin_time: str
        :param end_time: 备份结束时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。
        :type end_time: str
        :param status: 备份状态。 取值： - BUILDING：备份中。 - COMPLETED：备份完成。 - FAILED：备份失败。 - DISABLED：备份删除中。
        :type status: str
        :param size: 备份大小，单位：KB。
        :type size: int
        :param description: 备份描述。
        :type description: str
        """
        
        

        self._id = None
        self._name = None
        self._instance_id = None
        self._instance_name = None
        self._datastore = None
        self._type = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._size = None
        self._description = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.datastore = datastore
        self.type = type
        self.begin_time = begin_time
        self.end_time = end_time
        self.status = status
        self.size = size
        self.description = description

    @property
    def id(self):
        r"""Gets the id of this BackupForList.

        备份ID。

        :return: The id of this BackupForList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BackupForList.

        备份ID。

        :param id: The id of this BackupForList.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this BackupForList.

        备份名称。

        :return: The name of this BackupForList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BackupForList.

        备份名称。

        :param name: The name of this BackupForList.
        :type name: str
        """
        self._name = name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BackupForList.

        备份所属的实例ID。

        :return: The instance_id of this BackupForList.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BackupForList.

        备份所属的实例ID。

        :param instance_id: The instance_id of this BackupForList.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this BackupForList.

        备份所属的实例名称。

        :return: The instance_name of this BackupForList.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this BackupForList.

        备份所属的实例名称。

        :param instance_name: The instance_name of this BackupForList.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def datastore(self):
        r"""Gets the datastore of this BackupForList.

        :return: The datastore of this BackupForList.
        :rtype: :class:`huaweicloudsdkdds.v3.BackupDatabase`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this BackupForList.

        :param datastore: The datastore of this BackupForList.
        :type datastore: :class:`huaweicloudsdkdds.v3.BackupDatabase`
        """
        self._datastore = datastore

    @property
    def type(self):
        r"""Gets the type of this BackupForList.

        备份类型。 - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。 - 取值为“Incremental”，表示自动增量备份。

        :return: The type of this BackupForList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BackupForList.

        备份类型。 - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。 - 取值为“Incremental”，表示自动增量备份。

        :param type: The type of this BackupForList.
        :type type: str
        """
        self._type = type

    @property
    def begin_time(self):
        r"""Gets the begin_time of this BackupForList.

        备份开始时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。

        :return: The begin_time of this BackupForList.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this BackupForList.

        备份开始时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。

        :param begin_time: The begin_time of this BackupForList.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this BackupForList.

        备份结束时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。

        :return: The end_time of this BackupForList.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this BackupForList.

        备份结束时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。

        :param end_time: The end_time of this BackupForList.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this BackupForList.

        备份状态。 取值： - BUILDING：备份中。 - COMPLETED：备份完成。 - FAILED：备份失败。 - DISABLED：备份删除中。

        :return: The status of this BackupForList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BackupForList.

        备份状态。 取值： - BUILDING：备份中。 - COMPLETED：备份完成。 - FAILED：备份失败。 - DISABLED：备份删除中。

        :param status: The status of this BackupForList.
        :type status: str
        """
        self._status = status

    @property
    def size(self):
        r"""Gets the size of this BackupForList.

        备份大小，单位：KB。

        :return: The size of this BackupForList.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this BackupForList.

        备份大小，单位：KB。

        :param size: The size of this BackupForList.
        :type size: int
        """
        self._size = size

    @property
    def description(self):
        r"""Gets the description of this BackupForList.

        备份描述。

        :return: The description of this BackupForList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BackupForList.

        备份描述。

        :param description: The description of this BackupForList.
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
        if not isinstance(other, BackupForList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
