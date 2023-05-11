# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAllInstancesBackupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'datastore_type': 'str',
        'instance_id': 'str',
        'backup_id': 'str',
        'backup_type': 'str',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'datastore_type': 'datastore_type',
        'instance_id': 'instance_id',
        'backup_id': 'backup_id',
        'backup_type': 'backup_type',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, offset=None, limit=None, datastore_type=None, instance_id=None, backup_id=None, backup_type=None, begin_time=None, end_time=None):
        """ShowAllInstancesBackupsRequest

        The model defined in huaweicloud sdk

        :param offset: 分页页码。
        :type offset: int
        :param limit: 每页条数。
        :type limit: int
        :param datastore_type: 引擎类型 不传该参数则查询所有的引擎。
        :type datastore_type: str
        :param instance_id: 实例ID 不传该参数则查询所有备份列表。
        :type instance_id: str
        :param backup_id: 备份ID。
        :type backup_id: str
        :param backup_type: 备份类型。
        :type backup_type: str
        :param begin_time: 查询备份开始的时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。
        :type begin_time: str
        :param end_time: 查询备份开始的结束时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。
        :type end_time: str
        """
        
        

        self._offset = None
        self._limit = None
        self._datastore_type = None
        self._instance_id = None
        self._backup_id = None
        self._backup_type = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit
        if datastore_type is not None:
            self.datastore_type = datastore_type
        if instance_id is not None:
            self.instance_id = instance_id
        if backup_id is not None:
            self.backup_id = backup_id
        if backup_type is not None:
            self.backup_type = backup_type
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def offset(self):
        """Gets the offset of this ShowAllInstancesBackupsRequest.

        分页页码。

        :return: The offset of this ShowAllInstancesBackupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowAllInstancesBackupsRequest.

        分页页码。

        :param offset: The offset of this ShowAllInstancesBackupsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowAllInstancesBackupsRequest.

        每页条数。

        :return: The limit of this ShowAllInstancesBackupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowAllInstancesBackupsRequest.

        每页条数。

        :param limit: The limit of this ShowAllInstancesBackupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def datastore_type(self):
        """Gets the datastore_type of this ShowAllInstancesBackupsRequest.

        引擎类型 不传该参数则查询所有的引擎。

        :return: The datastore_type of this ShowAllInstancesBackupsRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        """Sets the datastore_type of this ShowAllInstancesBackupsRequest.

        引擎类型 不传该参数则查询所有的引擎。

        :param datastore_type: The datastore_type of this ShowAllInstancesBackupsRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowAllInstancesBackupsRequest.

        实例ID 不传该参数则查询所有备份列表。

        :return: The instance_id of this ShowAllInstancesBackupsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowAllInstancesBackupsRequest.

        实例ID 不传该参数则查询所有备份列表。

        :param instance_id: The instance_id of this ShowAllInstancesBackupsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def backup_id(self):
        """Gets the backup_id of this ShowAllInstancesBackupsRequest.

        备份ID。

        :return: The backup_id of this ShowAllInstancesBackupsRequest.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this ShowAllInstancesBackupsRequest.

        备份ID。

        :param backup_id: The backup_id of this ShowAllInstancesBackupsRequest.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def backup_type(self):
        """Gets the backup_type of this ShowAllInstancesBackupsRequest.

        备份类型。

        :return: The backup_type of this ShowAllInstancesBackupsRequest.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """Sets the backup_type of this ShowAllInstancesBackupsRequest.

        备份类型。

        :param backup_type: The backup_type of this ShowAllInstancesBackupsRequest.
        :type backup_type: str
        """
        self._backup_type = backup_type

    @property
    def begin_time(self):
        """Gets the begin_time of this ShowAllInstancesBackupsRequest.

        查询备份开始的时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。

        :return: The begin_time of this ShowAllInstancesBackupsRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ShowAllInstancesBackupsRequest.

        查询备份开始的时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。

        :param begin_time: The begin_time of this ShowAllInstancesBackupsRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowAllInstancesBackupsRequest.

        查询备份开始的结束时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。

        :return: The end_time of this ShowAllInstancesBackupsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowAllInstancesBackupsRequest.

        查询备份开始的结束时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。

        :param end_time: The end_time of this ShowAllInstancesBackupsRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ShowAllInstancesBackupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
