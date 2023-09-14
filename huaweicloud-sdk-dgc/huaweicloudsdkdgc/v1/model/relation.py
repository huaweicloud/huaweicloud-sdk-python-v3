# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Relation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'relation_type': 'str',
        'task_name': 'str',
        'task_id': 'int',
        'script_name': 'str',
        'script_id': 'str',
        'user_name': 'str',
        'version': 'int',
        'relation_id': 'str',
        'deleted': 'bool'
    }

    attribute_map = {
        'relation_type': 'relationType',
        'task_name': 'taskName',
        'task_id': 'taskId',
        'script_name': 'scriptName',
        'script_id': 'scriptId',
        'user_name': 'userName',
        'version': 'version',
        'relation_id': 'relationId',
        'deleted': 'deleted'
    }

    def __init__(self, relation_type=None, task_name=None, task_id=None, script_name=None, script_id=None, user_name=None, version=None, relation_id=None, deleted=None):
        """Relation

        The model defined in huaweicloud sdk

        :param relation_type: 依赖类型
        :type relation_type: str
        :param task_name: 作业名称
        :type task_name: str
        :param task_id: 作业ID
        :type task_id: int
        :param script_name: 脚本名称
        :type script_name: str
        :param script_id: 脚本ID
        :type script_id: str
        :param user_name: 用户名
        :type user_name: str
        :param version: 版本号
        :type version: int
        :param relation_id: 依赖类型ID
        :type relation_id: str
        :param deleted: 
        :type deleted: bool
        """
        
        

        self._relation_type = None
        self._task_name = None
        self._task_id = None
        self._script_name = None
        self._script_id = None
        self._user_name = None
        self._version = None
        self._relation_id = None
        self._deleted = None
        self.discriminator = None

        if relation_type is not None:
            self.relation_type = relation_type
        if task_name is not None:
            self.task_name = task_name
        if task_id is not None:
            self.task_id = task_id
        if script_name is not None:
            self.script_name = script_name
        if script_id is not None:
            self.script_id = script_id
        if user_name is not None:
            self.user_name = user_name
        if version is not None:
            self.version = version
        if relation_id is not None:
            self.relation_id = relation_id
        if deleted is not None:
            self.deleted = deleted

    @property
    def relation_type(self):
        """Gets the relation_type of this Relation.

        依赖类型

        :return: The relation_type of this Relation.
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """Sets the relation_type of this Relation.

        依赖类型

        :param relation_type: The relation_type of this Relation.
        :type relation_type: str
        """
        self._relation_type = relation_type

    @property
    def task_name(self):
        """Gets the task_name of this Relation.

        作业名称

        :return: The task_name of this Relation.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this Relation.

        作业名称

        :param task_name: The task_name of this Relation.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_id(self):
        """Gets the task_id of this Relation.

        作业ID

        :return: The task_id of this Relation.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this Relation.

        作业ID

        :param task_id: The task_id of this Relation.
        :type task_id: int
        """
        self._task_id = task_id

    @property
    def script_name(self):
        """Gets the script_name of this Relation.

        脚本名称

        :return: The script_name of this Relation.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        """Sets the script_name of this Relation.

        脚本名称

        :param script_name: The script_name of this Relation.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def script_id(self):
        """Gets the script_id of this Relation.

        脚本ID

        :return: The script_id of this Relation.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """Sets the script_id of this Relation.

        脚本ID

        :param script_id: The script_id of this Relation.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def user_name(self):
        """Gets the user_name of this Relation.

        用户名

        :return: The user_name of this Relation.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this Relation.

        用户名

        :param user_name: The user_name of this Relation.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def version(self):
        """Gets the version of this Relation.

        版本号

        :return: The version of this Relation.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Relation.

        版本号

        :param version: The version of this Relation.
        :type version: int
        """
        self._version = version

    @property
    def relation_id(self):
        """Gets the relation_id of this Relation.

        依赖类型ID

        :return: The relation_id of this Relation.
        :rtype: str
        """
        return self._relation_id

    @relation_id.setter
    def relation_id(self, relation_id):
        """Sets the relation_id of this Relation.

        依赖类型ID

        :param relation_id: The relation_id of this Relation.
        :type relation_id: str
        """
        self._relation_id = relation_id

    @property
    def deleted(self):
        """Gets the deleted of this Relation.

        :return: The deleted of this Relation.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Relation.

        :param deleted: The deleted of this Relation.
        :type deleted: bool
        """
        self._deleted = deleted

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
        if not isinstance(other, Relation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
