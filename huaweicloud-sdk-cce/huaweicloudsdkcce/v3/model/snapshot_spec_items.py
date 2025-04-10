# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SnapshotSpecItems:

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
        'type': 'str',
        'status': 'str',
        'creation_timestamp': 'str',
        'update_timestamp': 'str',
        'message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'status': 'status',
        'creation_timestamp': 'creationTimestamp',
        'update_timestamp': 'updateTimestamp',
        'message': 'message'
    }

    def __init__(self, id=None, type=None, status=None, creation_timestamp=None, update_timestamp=None, message=None):
        r"""SnapshotSpecItems

        The model defined in huaweicloud sdk

        :param id: 子任务ID
        :type id: str
        :param type: 子任务类型
        :type type: str
        :param status: 状态
        :type status: str
        :param creation_timestamp: 任务创建时间
        :type creation_timestamp: str
        :param update_timestamp: 任务更新时间
        :type update_timestamp: str
        :param message: 信息
        :type message: str
        """
        
        

        self._id = None
        self._type = None
        self._status = None
        self._creation_timestamp = None
        self._update_timestamp = None
        self._message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp
        if message is not None:
            self.message = message

    @property
    def id(self):
        r"""Gets the id of this SnapshotSpecItems.

        子任务ID

        :return: The id of this SnapshotSpecItems.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SnapshotSpecItems.

        子任务ID

        :param id: The id of this SnapshotSpecItems.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this SnapshotSpecItems.

        子任务类型

        :return: The type of this SnapshotSpecItems.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SnapshotSpecItems.

        子任务类型

        :param type: The type of this SnapshotSpecItems.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this SnapshotSpecItems.

        状态

        :return: The status of this SnapshotSpecItems.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SnapshotSpecItems.

        状态

        :param status: The status of this SnapshotSpecItems.
        :type status: str
        """
        self._status = status

    @property
    def creation_timestamp(self):
        r"""Gets the creation_timestamp of this SnapshotSpecItems.

        任务创建时间

        :return: The creation_timestamp of this SnapshotSpecItems.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        r"""Sets the creation_timestamp of this SnapshotSpecItems.

        任务创建时间

        :param creation_timestamp: The creation_timestamp of this SnapshotSpecItems.
        :type creation_timestamp: str
        """
        self._creation_timestamp = creation_timestamp

    @property
    def update_timestamp(self):
        r"""Gets the update_timestamp of this SnapshotSpecItems.

        任务更新时间

        :return: The update_timestamp of this SnapshotSpecItems.
        :rtype: str
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        r"""Sets the update_timestamp of this SnapshotSpecItems.

        任务更新时间

        :param update_timestamp: The update_timestamp of this SnapshotSpecItems.
        :type update_timestamp: str
        """
        self._update_timestamp = update_timestamp

    @property
    def message(self):
        r"""Gets the message of this SnapshotSpecItems.

        信息

        :return: The message of this SnapshotSpecItems.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this SnapshotSpecItems.

        信息

        :param message: The message of this SnapshotSpecItems.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, SnapshotSpecItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
