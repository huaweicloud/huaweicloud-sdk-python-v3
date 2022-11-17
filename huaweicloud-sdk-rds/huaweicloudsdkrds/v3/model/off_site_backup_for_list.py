# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OffSiteBackupForList:

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
        'instance_id': 'str',
        'name': 'str',
        'databases': 'list[BackupDatabase]',
        'begin_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'type': 'str',
        'size': 'int',
        'datastore': 'ParaGroupDatastore',
        'associated_with_ddm': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'name': 'name',
        'databases': 'databases',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'status': 'status',
        'type': 'type',
        'size': 'size',
        'datastore': 'datastore',
        'associated_with_ddm': 'associated_with_ddm'
    }

    def __init__(self, id=None, instance_id=None, name=None, databases=None, begin_time=None, end_time=None, status=None, type=None, size=None, datastore=None, associated_with_ddm=None):
        """OffSiteBackupForList

        The model defined in huaweicloud sdk

        :param id: 备份ID。
        :type id: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param name: 备份名称。
        :type name: str
        :param databases: 备份的数据库。
        :type databases: list[:class:`huaweicloudsdkrds.v3.BackupDatabase`]
        :param begin_time: 备份开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type begin_time: str
        :param end_time: 备份结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type end_time: str
        :param status: 备份状态，取值：  - BUILDING: 备份中。 - COMPLETED: 备份完成。 - FAILED：备份失败。 - DELETING：备份删除中。
        :type status: str
        :param type: 备份类型，取值：  - “auto”: 自动全量备份 - “incremental”: 自动增量备份
        :type type: str
        :param size: 备份大小，单位为KB。
        :type size: int
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkrds.v3.ParaGroupDatastore`
        :param associated_with_ddm: 是否已被DDM实例关联。
        :type associated_with_ddm: bool
        """
        
        

        self._id = None
        self._instance_id = None
        self._name = None
        self._databases = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._type = None
        self._size = None
        self._datastore = None
        self._associated_with_ddm = None
        self.discriminator = None

        self.id = id
        self.instance_id = instance_id
        self.name = name
        if databases is not None:
            self.databases = databases
        self.begin_time = begin_time
        self.end_time = end_time
        self.status = status
        self.type = type
        self.size = size
        self.datastore = datastore
        if associated_with_ddm is not None:
            self.associated_with_ddm = associated_with_ddm

    @property
    def id(self):
        """Gets the id of this OffSiteBackupForList.

        备份ID。

        :return: The id of this OffSiteBackupForList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OffSiteBackupForList.

        备份ID。

        :param id: The id of this OffSiteBackupForList.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        """Gets the instance_id of this OffSiteBackupForList.

        实例ID。

        :return: The instance_id of this OffSiteBackupForList.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this OffSiteBackupForList.

        实例ID。

        :param instance_id: The instance_id of this OffSiteBackupForList.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        """Gets the name of this OffSiteBackupForList.

        备份名称。

        :return: The name of this OffSiteBackupForList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OffSiteBackupForList.

        备份名称。

        :param name: The name of this OffSiteBackupForList.
        :type name: str
        """
        self._name = name

    @property
    def databases(self):
        """Gets the databases of this OffSiteBackupForList.

        备份的数据库。

        :return: The databases of this OffSiteBackupForList.
        :rtype: list[:class:`huaweicloudsdkrds.v3.BackupDatabase`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this OffSiteBackupForList.

        备份的数据库。

        :param databases: The databases of this OffSiteBackupForList.
        :type databases: list[:class:`huaweicloudsdkrds.v3.BackupDatabase`]
        """
        self._databases = databases

    @property
    def begin_time(self):
        """Gets the begin_time of this OffSiteBackupForList.

        备份开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The begin_time of this OffSiteBackupForList.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this OffSiteBackupForList.

        备份开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param begin_time: The begin_time of this OffSiteBackupForList.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this OffSiteBackupForList.

        备份结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The end_time of this OffSiteBackupForList.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this OffSiteBackupForList.

        备份结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param end_time: The end_time of this OffSiteBackupForList.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this OffSiteBackupForList.

        备份状态，取值：  - BUILDING: 备份中。 - COMPLETED: 备份完成。 - FAILED：备份失败。 - DELETING：备份删除中。

        :return: The status of this OffSiteBackupForList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OffSiteBackupForList.

        备份状态，取值：  - BUILDING: 备份中。 - COMPLETED: 备份完成。 - FAILED：备份失败。 - DELETING：备份删除中。

        :param status: The status of this OffSiteBackupForList.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this OffSiteBackupForList.

        备份类型，取值：  - “auto”: 自动全量备份 - “incremental”: 自动增量备份

        :return: The type of this OffSiteBackupForList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OffSiteBackupForList.

        备份类型，取值：  - “auto”: 自动全量备份 - “incremental”: 自动增量备份

        :param type: The type of this OffSiteBackupForList.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        """Gets the size of this OffSiteBackupForList.

        备份大小，单位为KB。

        :return: The size of this OffSiteBackupForList.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this OffSiteBackupForList.

        备份大小，单位为KB。

        :param size: The size of this OffSiteBackupForList.
        :type size: int
        """
        self._size = size

    @property
    def datastore(self):
        """Gets the datastore of this OffSiteBackupForList.

        :return: The datastore of this OffSiteBackupForList.
        :rtype: :class:`huaweicloudsdkrds.v3.ParaGroupDatastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this OffSiteBackupForList.

        :param datastore: The datastore of this OffSiteBackupForList.
        :type datastore: :class:`huaweicloudsdkrds.v3.ParaGroupDatastore`
        """
        self._datastore = datastore

    @property
    def associated_with_ddm(self):
        """Gets the associated_with_ddm of this OffSiteBackupForList.

        是否已被DDM实例关联。

        :return: The associated_with_ddm of this OffSiteBackupForList.
        :rtype: bool
        """
        return self._associated_with_ddm

    @associated_with_ddm.setter
    def associated_with_ddm(self, associated_with_ddm):
        """Sets the associated_with_ddm of this OffSiteBackupForList.

        是否已被DDM实例关联。

        :param associated_with_ddm: The associated_with_ddm of this OffSiteBackupForList.
        :type associated_with_ddm: bool
        """
        self._associated_with_ddm = associated_with_ddm

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
        if not isinstance(other, OffSiteBackupForList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
