# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackgroundTasksRespTasks:

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
        'user_name': 'str',
        'user_id': 'str',
        'params': 'str',
        'status': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'user_name': 'user_name',
        'user_id': 'user_id',
        'params': 'params',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, user_name=None, user_id=None, params=None, status=None, created_at=None, updated_at=None):
        """ListBackgroundTasksRespTasks

        The model defined in huaweicloud sdk

        :param id: 任务ID。
        :type id: str
        :param name: 任务名称。
        :type name: str
        :param user_name: 用户名。
        :type user_name: str
        :param user_id: 用户ID。
        :type user_id: str
        :param params: 任务参数。
        :type params: str
        :param status: 任务状态。
        :type status: str
        :param created_at: 启动时间。
        :type created_at: str
        :param updated_at: 结束时间。
        :type updated_at: str
        """
        
        

        self._id = None
        self._name = None
        self._user_name = None
        self._user_id = None
        self._params = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if user_name is not None:
            self.user_name = user_name
        if user_id is not None:
            self.user_id = user_id
        if params is not None:
            self.params = params
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this ListBackgroundTasksRespTasks.

        任务ID。

        :return: The id of this ListBackgroundTasksRespTasks.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListBackgroundTasksRespTasks.

        任务ID。

        :param id: The id of this ListBackgroundTasksRespTasks.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListBackgroundTasksRespTasks.

        任务名称。

        :return: The name of this ListBackgroundTasksRespTasks.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListBackgroundTasksRespTasks.

        任务名称。

        :param name: The name of this ListBackgroundTasksRespTasks.
        :type name: str
        """
        self._name = name

    @property
    def user_name(self):
        """Gets the user_name of this ListBackgroundTasksRespTasks.

        用户名。

        :return: The user_name of this ListBackgroundTasksRespTasks.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListBackgroundTasksRespTasks.

        用户名。

        :param user_name: The user_name of this ListBackgroundTasksRespTasks.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_id(self):
        """Gets the user_id of this ListBackgroundTasksRespTasks.

        用户ID。

        :return: The user_id of this ListBackgroundTasksRespTasks.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ListBackgroundTasksRespTasks.

        用户ID。

        :param user_id: The user_id of this ListBackgroundTasksRespTasks.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def params(self):
        """Gets the params of this ListBackgroundTasksRespTasks.

        任务参数。

        :return: The params of this ListBackgroundTasksRespTasks.
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ListBackgroundTasksRespTasks.

        任务参数。

        :param params: The params of this ListBackgroundTasksRespTasks.
        :type params: str
        """
        self._params = params

    @property
    def status(self):
        """Gets the status of this ListBackgroundTasksRespTasks.

        任务状态。

        :return: The status of this ListBackgroundTasksRespTasks.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListBackgroundTasksRespTasks.

        任务状态。

        :param status: The status of this ListBackgroundTasksRespTasks.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this ListBackgroundTasksRespTasks.

        启动时间。

        :return: The created_at of this ListBackgroundTasksRespTasks.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ListBackgroundTasksRespTasks.

        启动时间。

        :param created_at: The created_at of this ListBackgroundTasksRespTasks.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ListBackgroundTasksRespTasks.

        结束时间。

        :return: The updated_at of this ListBackgroundTasksRespTasks.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ListBackgroundTasksRespTasks.

        结束时间。

        :param updated_at: The updated_at of this ListBackgroundTasksRespTasks.
        :type updated_at: str
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
        if not isinstance(other, ListBackgroundTasksRespTasks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
