# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiOverview:

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
        'group_id': 'str',
        'description': 'str',
        'status': 'str',
        'debug_status': 'str',
        'type': 'str',
        'manager': 'str',
        'create_user': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'group_id': 'group_id',
        'description': 'description',
        'status': 'status',
        'debug_status': 'debug_status',
        'type': 'type',
        'manager': 'manager',
        'create_user': 'create_user',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, name=None, group_id=None, description=None, status=None, debug_status=None, type=None, manager=None, create_user=None, create_time=None):
        """ApiOverview

        The model defined in huaweicloud sdk

        :param id: API ID
        :type id: str
        :param name: API名称
        :type name: str
        :param group_id: API分组ID
        :type group_id: str
        :param description: API描述
        :type description: str
        :param status: API状态
        :type status: str
        :param debug_status: API调试状态
        :type debug_status: str
        :param type: API 类型
        :type type: str
        :param manager: API审核人
        :type manager: str
        :param create_user: API创建者
        :type create_user: str
        :param create_time: API 创建时间
        :type create_time: int
        """
        
        

        self._id = None
        self._name = None
        self._group_id = None
        self._description = None
        self._status = None
        self._debug_status = None
        self._type = None
        self._manager = None
        self._create_user = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if group_id is not None:
            self.group_id = group_id
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if debug_status is not None:
            self.debug_status = debug_status
        if type is not None:
            self.type = type
        if manager is not None:
            self.manager = manager
        if create_user is not None:
            self.create_user = create_user
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        """Gets the id of this ApiOverview.

        API ID

        :return: The id of this ApiOverview.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiOverview.

        API ID

        :param id: The id of this ApiOverview.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ApiOverview.

        API名称

        :return: The name of this ApiOverview.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiOverview.

        API名称

        :param name: The name of this ApiOverview.
        :type name: str
        """
        self._name = name

    @property
    def group_id(self):
        """Gets the group_id of this ApiOverview.

        API分组ID

        :return: The group_id of this ApiOverview.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ApiOverview.

        API分组ID

        :param group_id: The group_id of this ApiOverview.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def description(self):
        """Gets the description of this ApiOverview.

        API描述

        :return: The description of this ApiOverview.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiOverview.

        API描述

        :param description: The description of this ApiOverview.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this ApiOverview.

        API状态

        :return: The status of this ApiOverview.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiOverview.

        API状态

        :param status: The status of this ApiOverview.
        :type status: str
        """
        self._status = status

    @property
    def debug_status(self):
        """Gets the debug_status of this ApiOverview.

        API调试状态

        :return: The debug_status of this ApiOverview.
        :rtype: str
        """
        return self._debug_status

    @debug_status.setter
    def debug_status(self, debug_status):
        """Sets the debug_status of this ApiOverview.

        API调试状态

        :param debug_status: The debug_status of this ApiOverview.
        :type debug_status: str
        """
        self._debug_status = debug_status

    @property
    def type(self):
        """Gets the type of this ApiOverview.

        API 类型

        :return: The type of this ApiOverview.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ApiOverview.

        API 类型

        :param type: The type of this ApiOverview.
        :type type: str
        """
        self._type = type

    @property
    def manager(self):
        """Gets the manager of this ApiOverview.

        API审核人

        :return: The manager of this ApiOverview.
        :rtype: str
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """Sets the manager of this ApiOverview.

        API审核人

        :param manager: The manager of this ApiOverview.
        :type manager: str
        """
        self._manager = manager

    @property
    def create_user(self):
        """Gets the create_user of this ApiOverview.

        API创建者

        :return: The create_user of this ApiOverview.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this ApiOverview.

        API创建者

        :param create_user: The create_user of this ApiOverview.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def create_time(self):
        """Gets the create_time of this ApiOverview.

        API 创建时间

        :return: The create_time of this ApiOverview.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ApiOverview.

        API 创建时间

        :param create_time: The create_time of this ApiOverview.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, ApiOverview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
