# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'description': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'size': 'float',
        'type': 'str',
        'datastore': 'DatastoreResult',
        'instance_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'status': 'status',
        'size': 'size',
        'type': 'type',
        'datastore': 'datastore',
        'instance_id': 'instance_id'
    }

    def __init__(self, id=None, name=None, description=None, begin_time=None, end_time=None, status=None, size=None, type=None, datastore=None, instance_id=None):
        r"""ListBackupsResult

        The model defined in huaweicloud sdk

        :param id: 备份ID。
        :type id: str
        :param name: 备份名称。
        :type name: str
        :param description: 备份文件描述信息。
        :type description: str
        :param begin_time: 备份开始时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type begin_time: str
        :param end_time: 备份结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type end_time: str
        :param status: 备份状态
        :type status: str
        :param size: 备份大小(单位：MB)
        :type size: float
        :param type: 备份类型
        :type type: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdbforopengauss.v3.DatastoreResult`
        :param instance_id: 实例ID。
        :type instance_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._size = None
        self._type = None
        self._datastore = None
        self._instance_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
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
        if datastore is not None:
            self.datastore = datastore
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def id(self):
        r"""Gets the id of this ListBackupsResult.

        备份ID。

        :return: The id of this ListBackupsResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListBackupsResult.

        备份ID。

        :param id: The id of this ListBackupsResult.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListBackupsResult.

        备份名称。

        :return: The name of this ListBackupsResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListBackupsResult.

        备份名称。

        :param name: The name of this ListBackupsResult.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListBackupsResult.

        备份文件描述信息。

        :return: The description of this ListBackupsResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListBackupsResult.

        备份文件描述信息。

        :param description: The description of this ListBackupsResult.
        :type description: str
        """
        self._description = description

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListBackupsResult.

        备份开始时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The begin_time of this ListBackupsResult.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListBackupsResult.

        备份开始时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param begin_time: The begin_time of this ListBackupsResult.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListBackupsResult.

        备份结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The end_time of this ListBackupsResult.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListBackupsResult.

        备份结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param end_time: The end_time of this ListBackupsResult.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this ListBackupsResult.

        备份状态

        :return: The status of this ListBackupsResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListBackupsResult.

        备份状态

        :param status: The status of this ListBackupsResult.
        :type status: str
        """
        self._status = status

    @property
    def size(self):
        r"""Gets the size of this ListBackupsResult.

        备份大小(单位：MB)

        :return: The size of this ListBackupsResult.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListBackupsResult.

        备份大小(单位：MB)

        :param size: The size of this ListBackupsResult.
        :type size: float
        """
        self._size = size

    @property
    def type(self):
        r"""Gets the type of this ListBackupsResult.

        备份类型

        :return: The type of this ListBackupsResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListBackupsResult.

        备份类型

        :param type: The type of this ListBackupsResult.
        :type type: str
        """
        self._type = type

    @property
    def datastore(self):
        r"""Gets the datastore of this ListBackupsResult.

        :return: The datastore of this ListBackupsResult.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.DatastoreResult`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this ListBackupsResult.

        :param datastore: The datastore of this ListBackupsResult.
        :type datastore: :class:`huaweicloudsdkgaussdbforopengauss.v3.DatastoreResult`
        """
        self._datastore = datastore

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListBackupsResult.

        实例ID。

        :return: The instance_id of this ListBackupsResult.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListBackupsResult.

        实例ID。

        :param instance_id: The instance_id of this ListBackupsResult.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, ListBackupsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
