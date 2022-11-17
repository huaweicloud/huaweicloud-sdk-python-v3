# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Metadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'annotations': 'dict(str, str)',
        'created_at': 'datetime',
        'id': 'str',
        'jod_id': 'str',
        'name': 'str',
        'status': 'str',
        'type': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'annotations': 'annotations',
        'created_at': 'created_at',
        'id': 'id',
        'jod_id': 'jod_id',
        'name': 'name',
        'status': 'status',
        'type': 'type',
        'updated_at': 'updated_at'
    }

    def __init__(self, annotations=None, created_at=None, id=None, jod_id=None, name=None, status=None, type=None, updated_at=None):
        """Metadata

        The model defined in huaweicloud sdk

        :param annotations: 属性信息。
        :type annotations: dict(str, str)
        :param created_at: 创建时间。
        :type created_at: datetime
        :param id: 组件id。
        :type id: str
        :param jod_id: 任务id。
        :type jod_id: str
        :param name: 名称。
        :type name: str
        :param status: 状态。
        :type status: str
        :param type: 组件类型。
        :type type: str
        :param updated_at: 更新时间。
        :type updated_at: datetime
        """
        
        

        self._annotations = None
        self._created_at = None
        self._id = None
        self._jod_id = None
        self._name = None
        self._status = None
        self._type = None
        self._updated_at = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        if jod_id is not None:
            self.jod_id = jod_id
        self.name = name
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def annotations(self):
        """Gets the annotations of this Metadata.

        属性信息。

        :return: The annotations of this Metadata.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this Metadata.

        属性信息。

        :param annotations: The annotations of this Metadata.
        :type annotations: dict(str, str)
        """
        self._annotations = annotations

    @property
    def created_at(self):
        """Gets the created_at of this Metadata.

        创建时间。

        :return: The created_at of this Metadata.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Metadata.

        创建时间。

        :param created_at: The created_at of this Metadata.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this Metadata.

        组件id。

        :return: The id of this Metadata.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Metadata.

        组件id。

        :param id: The id of this Metadata.
        :type id: str
        """
        self._id = id

    @property
    def jod_id(self):
        """Gets the jod_id of this Metadata.

        任务id。

        :return: The jod_id of this Metadata.
        :rtype: str
        """
        return self._jod_id

    @jod_id.setter
    def jod_id(self, jod_id):
        """Sets the jod_id of this Metadata.

        任务id。

        :param jod_id: The jod_id of this Metadata.
        :type jod_id: str
        """
        self._jod_id = jod_id

    @property
    def name(self):
        """Gets the name of this Metadata.

        名称。

        :return: The name of this Metadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Metadata.

        名称。

        :param name: The name of this Metadata.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this Metadata.

        状态。

        :return: The status of this Metadata.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Metadata.

        状态。

        :param status: The status of this Metadata.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this Metadata.

        组件类型。

        :return: The type of this Metadata.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Metadata.

        组件类型。

        :param type: The type of this Metadata.
        :type type: str
        """
        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this Metadata.

        更新时间。

        :return: The updated_at of this Metadata.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Metadata.

        更新时间。

        :param updated_at: The updated_at of this Metadata.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, Metadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
