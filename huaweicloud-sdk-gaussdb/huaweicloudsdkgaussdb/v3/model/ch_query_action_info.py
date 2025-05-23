# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChQueryActionInfo:

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
        'action': 'str',
        'object_id': 'str',
        'type': 'str',
        'job_id': 'str',
        'status': 'str',
        'created_at': 'int',
        'updated_at': 'int'
    }

    attribute_map = {
        'id': 'id',
        'action': 'action',
        'object_id': 'object_id',
        'type': 'type',
        'job_id': 'job_id',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, action=None, object_id=None, type=None, job_id=None, status=None, created_at=None, updated_at=None):
        r"""ChQueryActionInfo

        The model defined in huaweicloud sdk

        :param id: 实例动作ID。
        :type id: str
        :param action: 实例动作名称。
        :type action: str
        :param object_id: 实例动作对象ID。
        :type object_id: str
        :param type: 实例动作类型。
        :type type: str
        :param job_id: 实例动作任务ID。
        :type job_id: str
        :param status: 实例动作状态。
        :type status: str
        :param created_at: 实例动作创建时间。
        :type created_at: int
        :param updated_at: 实例动作更新时间。
        :type updated_at: int
        """
        
        

        self._id = None
        self._action = None
        self._object_id = None
        self._type = None
        self._job_id = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if action is not None:
            self.action = action
        if object_id is not None:
            self.object_id = object_id
        if type is not None:
            self.type = type
        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this ChQueryActionInfo.

        实例动作ID。

        :return: The id of this ChQueryActionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ChQueryActionInfo.

        实例动作ID。

        :param id: The id of this ChQueryActionInfo.
        :type id: str
        """
        self._id = id

    @property
    def action(self):
        r"""Gets the action of this ChQueryActionInfo.

        实例动作名称。

        :return: The action of this ChQueryActionInfo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ChQueryActionInfo.

        实例动作名称。

        :param action: The action of this ChQueryActionInfo.
        :type action: str
        """
        self._action = action

    @property
    def object_id(self):
        r"""Gets the object_id of this ChQueryActionInfo.

        实例动作对象ID。

        :return: The object_id of this ChQueryActionInfo.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this ChQueryActionInfo.

        实例动作对象ID。

        :param object_id: The object_id of this ChQueryActionInfo.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def type(self):
        r"""Gets the type of this ChQueryActionInfo.

        实例动作类型。

        :return: The type of this ChQueryActionInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ChQueryActionInfo.

        实例动作类型。

        :param type: The type of this ChQueryActionInfo.
        :type type: str
        """
        self._type = type

    @property
    def job_id(self):
        r"""Gets the job_id of this ChQueryActionInfo.

        实例动作任务ID。

        :return: The job_id of this ChQueryActionInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ChQueryActionInfo.

        实例动作任务ID。

        :param job_id: The job_id of this ChQueryActionInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        r"""Gets the status of this ChQueryActionInfo.

        实例动作状态。

        :return: The status of this ChQueryActionInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ChQueryActionInfo.

        实例动作状态。

        :param status: The status of this ChQueryActionInfo.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this ChQueryActionInfo.

        实例动作创建时间。

        :return: The created_at of this ChQueryActionInfo.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ChQueryActionInfo.

        实例动作创建时间。

        :param created_at: The created_at of this ChQueryActionInfo.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ChQueryActionInfo.

        实例动作更新时间。

        :return: The updated_at of this ChQueryActionInfo.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ChQueryActionInfo.

        实例动作更新时间。

        :param updated_at: The updated_at of this ChQueryActionInfo.
        :type updated_at: int
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
        if not isinstance(other, ChQueryActionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
