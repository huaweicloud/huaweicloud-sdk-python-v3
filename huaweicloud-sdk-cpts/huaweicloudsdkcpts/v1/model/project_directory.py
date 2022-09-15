# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectDirectory:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'status': 'int',
        'create_time': 'str',
        'update_time': 'str',
        'parent_id': 'int',
        'type': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'parent_id': 'parent_id',
        'type': 'type'
    }

    def __init__(self, id=None, name=None, status=None, create_time=None, update_time=None, parent_id=None, type=None):
        """ProjectDirectory

        The model defined in huaweicloud sdk

        :param id: id
        :type id: int
        :param name: 名称
        :type name: str
        :param status: 状态(0:已删除,1:启用,2:停用)
        :type status: int
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param parent_id: 父id
        :type parent_id: int
        :param type: 类型(1:目录, 2:用例)
        :type type: int
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self._parent_id = None
        self._type = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.create_time = create_time
        self.update_time = update_time
        self.parent_id = parent_id
        self.type = type

    @property
    def id(self):
        """Gets the id of this ProjectDirectory.

        id

        :return: The id of this ProjectDirectory.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectDirectory.

        id

        :param id: The id of this ProjectDirectory.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ProjectDirectory.

        名称

        :return: The name of this ProjectDirectory.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectDirectory.

        名称

        :param name: The name of this ProjectDirectory.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ProjectDirectory.

        状态(0:已删除,1:启用,2:停用)

        :return: The status of this ProjectDirectory.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProjectDirectory.

        状态(0:已删除,1:启用,2:停用)

        :param status: The status of this ProjectDirectory.
        :type status: int
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this ProjectDirectory.

        创建时间

        :return: The create_time of this ProjectDirectory.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ProjectDirectory.

        创建时间

        :param create_time: The create_time of this ProjectDirectory.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ProjectDirectory.

        更新时间

        :return: The update_time of this ProjectDirectory.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ProjectDirectory.

        更新时间

        :param update_time: The update_time of this ProjectDirectory.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def parent_id(self):
        """Gets the parent_id of this ProjectDirectory.

        父id

        :return: The parent_id of this ProjectDirectory.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ProjectDirectory.

        父id

        :param parent_id: The parent_id of this ProjectDirectory.
        :type parent_id: int
        """
        self._parent_id = parent_id

    @property
    def type(self):
        """Gets the type of this ProjectDirectory.

        类型(1:目录, 2:用例)

        :return: The type of this ProjectDirectory.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProjectDirectory.

        类型(1:目录, 2:用例)

        :param type: The type of this ProjectDirectory.
        :type type: int
        """
        self._type = type

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
        if not isinstance(other, ProjectDirectory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
