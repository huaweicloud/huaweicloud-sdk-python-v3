# coding: utf-8

import pprint
import re

import six





class ListBackupsResult:


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
        'datastore': 'ListBackupsDatastoreResult',
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
        """ListBackupsResult - a model defined in huaweicloud sdk"""
        
        

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
        """Gets the id of this ListBackupsResult.

        备份ID。

        :return: The id of this ListBackupsResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListBackupsResult.

        备份ID。

        :param id: The id of this ListBackupsResult.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListBackupsResult.

        备份名称。

        :return: The name of this ListBackupsResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListBackupsResult.

        备份名称。

        :param name: The name of this ListBackupsResult.
        :type: str
        """
        self._name = name

    @property
    def instance_id(self):
        """Gets the instance_id of this ListBackupsResult.

        备份所属的实例ID。

        :return: The instance_id of this ListBackupsResult.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListBackupsResult.

        备份所属的实例ID。

        :param instance_id: The instance_id of this ListBackupsResult.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this ListBackupsResult.

        备份所属的实例名称。

        :return: The instance_name of this ListBackupsResult.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this ListBackupsResult.

        备份所属的实例名称。

        :param instance_name: The instance_name of this ListBackupsResult.
        :type: str
        """
        self._instance_name = instance_name

    @property
    def datastore(self):
        """Gets the datastore of this ListBackupsResult.


        :return: The datastore of this ListBackupsResult.
        :rtype: ListBackupsDatastoreResult
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this ListBackupsResult.


        :param datastore: The datastore of this ListBackupsResult.
        :type: ListBackupsDatastoreResult
        """
        self._datastore = datastore

    @property
    def type(self):
        """Gets the type of this ListBackupsResult.

        备份类型。 - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。

        :return: The type of this ListBackupsResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListBackupsResult.

        备份类型。 - 取值为“Auto”，表示自动全量备份。 - 取值为“Manual”，表示手动全量备份。

        :param type: The type of this ListBackupsResult.
        :type: str
        """
        self._type = type

    @property
    def begin_time(self):
        """Gets the begin_time of this ListBackupsResult.

        备份开始时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。

        :return: The begin_time of this ListBackupsResult.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListBackupsResult.

        备份开始时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。

        :param begin_time: The begin_time of this ListBackupsResult.
        :type: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ListBackupsResult.

        备份结束时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。

        :return: The end_time of this ListBackupsResult.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListBackupsResult.

        备份结束时间，格式为“yyyy-mm-dd hh:mm:ss”。该时间为UTC时间。

        :param end_time: The end_time of this ListBackupsResult.
        :type: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this ListBackupsResult.

        备份状态。 取值： - BUILDING：备份中。 - COMPLETED：备份完成。 - FAILED：备份失败。 - DISABLED：备份删除中。

        :return: The status of this ListBackupsResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListBackupsResult.

        备份状态。 取值： - BUILDING：备份中。 - COMPLETED：备份完成。 - FAILED：备份失败。 - DISABLED：备份删除中。

        :param status: The status of this ListBackupsResult.
        :type: str
        """
        self._status = status

    @property
    def size(self):
        """Gets the size of this ListBackupsResult.

        备份大小，单位：KB。

        :return: The size of this ListBackupsResult.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListBackupsResult.

        备份大小，单位：KB。

        :param size: The size of this ListBackupsResult.
        :type: int
        """
        self._size = size

    @property
    def description(self):
        """Gets the description of this ListBackupsResult.

        备份描述。

        :return: The description of this ListBackupsResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListBackupsResult.

        备份描述。

        :param description: The description of this ListBackupsResult.
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListBackupsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
