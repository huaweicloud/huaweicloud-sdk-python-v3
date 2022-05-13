# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupInfo:

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
        'status': 'str',
        'type': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'begin_time': 'begin_time',
        'status': 'status',
        'type': 'type',
        'instance_id': 'instance_id'
    }

    def __init__(self, id=None, name=None, description=None, begin_time=None, status=None, type=None, instance_id=None):
        """BackupInfo

        The model defined in huaweicloud sdk

        :param id: 备份ID。
        :type id: str
        :param name: 备份名称。
        :type name: str
        :param description: 备份描述。
        :type description: str
        :param begin_time: 备份开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type begin_time: str
        :param status: 备份状态，取值：  - BUILDING: 备份中。 - COMPLETED: 备份完成。 - FAILED：备份失败。 - DELETING：备份删除中。
        :type status: str
        :param type: 备份类型，取值： - “manual”: 手动全量备份
        :type type: str
        :param instance_id: 实例ID。
        :type instance_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._begin_time = None
        self._status = None
        self._type = None
        self._instance_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.begin_time = begin_time
        self.status = status
        self.type = type
        self.instance_id = instance_id

    @property
    def id(self):
        """Gets the id of this BackupInfo.

        备份ID。

        :return: The id of this BackupInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BackupInfo.

        备份ID。

        :param id: The id of this BackupInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this BackupInfo.

        备份名称。

        :return: The name of this BackupInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BackupInfo.

        备份名称。

        :param name: The name of this BackupInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this BackupInfo.

        备份描述。

        :return: The description of this BackupInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BackupInfo.

        备份描述。

        :param description: The description of this BackupInfo.
        :type description: str
        """
        self._description = description

    @property
    def begin_time(self):
        """Gets the begin_time of this BackupInfo.

        备份开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The begin_time of this BackupInfo.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this BackupInfo.

        备份开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param begin_time: The begin_time of this BackupInfo.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def status(self):
        """Gets the status of this BackupInfo.

        备份状态，取值：  - BUILDING: 备份中。 - COMPLETED: 备份完成。 - FAILED：备份失败。 - DELETING：备份删除中。

        :return: The status of this BackupInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BackupInfo.

        备份状态，取值：  - BUILDING: 备份中。 - COMPLETED: 备份完成。 - FAILED：备份失败。 - DELETING：备份删除中。

        :param status: The status of this BackupInfo.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this BackupInfo.

        备份类型，取值： - “manual”: 手动全量备份

        :return: The type of this BackupInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BackupInfo.

        备份类型，取值： - “manual”: 手动全量备份

        :param type: The type of this BackupInfo.
        :type type: str
        """
        self._type = type

    @property
    def instance_id(self):
        """Gets the instance_id of this BackupInfo.

        实例ID。

        :return: The instance_id of this BackupInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this BackupInfo.

        实例ID。

        :param instance_id: The instance_id of this BackupInfo.
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
        if not isinstance(other, BackupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
