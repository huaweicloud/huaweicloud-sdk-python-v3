# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VariableRes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'by_order': 'int',
        'category': 'str',
        'create_time': 'str',
        'create_time_stamp': 'int',
        'create_time_string': 'str',
        'create_user': 'str',
        'current_permission': 'str',
        'description': 'str',
        'dynamic_param_flag': 'bool',
        'function_params': 'str',
        'group_id': 'str',
        'id': 'str',
        'is_sensitive_info': 'bool',
        'is_sensitive_modified': 'bool',
        'locked': 'int',
        'name': 'str',
        'node_id': 'str',
        'node_type': 'int',
        'parent_id': 'str',
        'parent_node_id': 'str',
        '_property': 'str',
        'region': 'str',
        'sensitive_info_setter_time': 'str',
        'sensitive_info_setter_user': 'str',
        'source_id': 'str',
        'type': 'str',
        'update_time': 'str',
        'update_time_stamp': 'int',
        'update_time_string': 'str',
        'update_user': 'str',
        'variable_type': 'int'
    }

    attribute_map = {
        'by_order': 'by_order',
        'category': 'category',
        'create_time': 'create_time',
        'create_time_stamp': 'create_time_stamp',
        'create_time_string': 'create_time_string',
        'create_user': 'create_user',
        'current_permission': 'currentPermission',
        'description': 'description',
        'dynamic_param_flag': 'dynamicParamFlag',
        'function_params': 'functionParams',
        'group_id': 'groupId',
        'id': 'id',
        'is_sensitive_info': 'isSensitiveInfo',
        'is_sensitive_modified': 'isSensitiveModified',
        'locked': 'locked',
        'name': 'name',
        'node_id': 'node_id',
        'node_type': 'node_type',
        'parent_id': 'parent_id',
        'parent_node_id': 'parent_node_id',
        '_property': 'property',
        'region': 'region',
        'sensitive_info_setter_time': 'sensitiveInfoSetterTime',
        'sensitive_info_setter_user': 'sensitiveInfoSetterUser',
        'source_id': 'sourceId',
        'type': 'type',
        'update_time': 'update_time',
        'update_time_stamp': 'update_time_stamp',
        'update_time_string': 'update_time_string',
        'update_user': 'update_user',
        'variable_type': 'variableType'
    }

    def __init__(self, by_order=None, category=None, create_time=None, create_time_stamp=None, create_time_string=None, create_user=None, current_permission=None, description=None, dynamic_param_flag=None, function_params=None, group_id=None, id=None, is_sensitive_info=None, is_sensitive_modified=None, locked=None, name=None, node_id=None, node_type=None, parent_id=None, parent_node_id=None, _property=None, region=None, sensitive_info_setter_time=None, sensitive_info_setter_user=None, source_id=None, type=None, update_time=None, update_time_stamp=None, update_time_string=None, update_user=None, variable_type=None):
        """VariableRes

        The model defined in huaweicloud sdk

        :param by_order: 
        :type by_order: int
        :param category: 
        :type category: str
        :param create_time: 创建时间
        :type create_time: str
        :param create_time_stamp: 
        :type create_time_stamp: int
        :param create_time_string: 
        :type create_time_string: str
        :param create_user: 创建人
        :type create_user: str
        :param current_permission: 
        :type current_permission: str
        :param description: 
        :type description: str
        :param dynamic_param_flag: 
        :type dynamic_param_flag: bool
        :param function_params: 
        :type function_params: str
        :param group_id: 
        :type group_id: str
        :param id: id
        :type id: str
        :param is_sensitive_info: 
        :type is_sensitive_info: bool
        :param is_sensitive_modified: 
        :type is_sensitive_modified: bool
        :param locked: 
        :type locked: int
        :param name: 
        :type name: str
        :param node_id: 
        :type node_id: str
        :param node_type: 
        :type node_type: int
        :param parent_id: 
        :type parent_id: str
        :param parent_node_id: 
        :type parent_node_id: str
        :param _property: 
        :type _property: str
        :param region: 
        :type region: str
        :param sensitive_info_setter_time: 
        :type sensitive_info_setter_time: str
        :param sensitive_info_setter_user: 
        :type sensitive_info_setter_user: str
        :param source_id: 
        :type source_id: str
        :param type: 
        :type type: str
        :param update_time: 更新时间
        :type update_time: str
        :param update_time_stamp: 
        :type update_time_stamp: int
        :param update_time_string: 
        :type update_time_string: str
        :param update_user: 更新人
        :type update_user: str
        :param variable_type: 
        :type variable_type: int
        """
        
        

        self._by_order = None
        self._category = None
        self._create_time = None
        self._create_time_stamp = None
        self._create_time_string = None
        self._create_user = None
        self._current_permission = None
        self._description = None
        self._dynamic_param_flag = None
        self._function_params = None
        self._group_id = None
        self._id = None
        self._is_sensitive_info = None
        self._is_sensitive_modified = None
        self._locked = None
        self._name = None
        self._node_id = None
        self._node_type = None
        self._parent_id = None
        self._parent_node_id = None
        self.__property = None
        self._region = None
        self._sensitive_info_setter_time = None
        self._sensitive_info_setter_user = None
        self._source_id = None
        self._type = None
        self._update_time = None
        self._update_time_stamp = None
        self._update_time_string = None
        self._update_user = None
        self._variable_type = None
        self.discriminator = None

        if by_order is not None:
            self.by_order = by_order
        if category is not None:
            self.category = category
        if create_time is not None:
            self.create_time = create_time
        if create_time_stamp is not None:
            self.create_time_stamp = create_time_stamp
        if create_time_string is not None:
            self.create_time_string = create_time_string
        if create_user is not None:
            self.create_user = create_user
        if current_permission is not None:
            self.current_permission = current_permission
        if description is not None:
            self.description = description
        if dynamic_param_flag is not None:
            self.dynamic_param_flag = dynamic_param_flag
        if function_params is not None:
            self.function_params = function_params
        if group_id is not None:
            self.group_id = group_id
        if id is not None:
            self.id = id
        if is_sensitive_info is not None:
            self.is_sensitive_info = is_sensitive_info
        if is_sensitive_modified is not None:
            self.is_sensitive_modified = is_sensitive_modified
        if locked is not None:
            self.locked = locked
        if name is not None:
            self.name = name
        if node_id is not None:
            self.node_id = node_id
        if node_type is not None:
            self.node_type = node_type
        if parent_id is not None:
            self.parent_id = parent_id
        if parent_node_id is not None:
            self.parent_node_id = parent_node_id
        if _property is not None:
            self._property = _property
        if region is not None:
            self.region = region
        if sensitive_info_setter_time is not None:
            self.sensitive_info_setter_time = sensitive_info_setter_time
        if sensitive_info_setter_user is not None:
            self.sensitive_info_setter_user = sensitive_info_setter_user
        if source_id is not None:
            self.source_id = source_id
        if type is not None:
            self.type = type
        if update_time is not None:
            self.update_time = update_time
        if update_time_stamp is not None:
            self.update_time_stamp = update_time_stamp
        if update_time_string is not None:
            self.update_time_string = update_time_string
        if update_user is not None:
            self.update_user = update_user
        if variable_type is not None:
            self.variable_type = variable_type

    @property
    def by_order(self):
        """Gets the by_order of this VariableRes.

        :return: The by_order of this VariableRes.
        :rtype: int
        """
        return self._by_order

    @by_order.setter
    def by_order(self, by_order):
        """Sets the by_order of this VariableRes.

        :param by_order: The by_order of this VariableRes.
        :type by_order: int
        """
        self._by_order = by_order

    @property
    def category(self):
        """Gets the category of this VariableRes.

        :return: The category of this VariableRes.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this VariableRes.

        :param category: The category of this VariableRes.
        :type category: str
        """
        self._category = category

    @property
    def create_time(self):
        """Gets the create_time of this VariableRes.

        创建时间

        :return: The create_time of this VariableRes.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this VariableRes.

        创建时间

        :param create_time: The create_time of this VariableRes.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def create_time_stamp(self):
        """Gets the create_time_stamp of this VariableRes.

        :return: The create_time_stamp of this VariableRes.
        :rtype: int
        """
        return self._create_time_stamp

    @create_time_stamp.setter
    def create_time_stamp(self, create_time_stamp):
        """Sets the create_time_stamp of this VariableRes.

        :param create_time_stamp: The create_time_stamp of this VariableRes.
        :type create_time_stamp: int
        """
        self._create_time_stamp = create_time_stamp

    @property
    def create_time_string(self):
        """Gets the create_time_string of this VariableRes.

        :return: The create_time_string of this VariableRes.
        :rtype: str
        """
        return self._create_time_string

    @create_time_string.setter
    def create_time_string(self, create_time_string):
        """Sets the create_time_string of this VariableRes.

        :param create_time_string: The create_time_string of this VariableRes.
        :type create_time_string: str
        """
        self._create_time_string = create_time_string

    @property
    def create_user(self):
        """Gets the create_user of this VariableRes.

        创建人

        :return: The create_user of this VariableRes.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this VariableRes.

        创建人

        :param create_user: The create_user of this VariableRes.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def current_permission(self):
        """Gets the current_permission of this VariableRes.

        :return: The current_permission of this VariableRes.
        :rtype: str
        """
        return self._current_permission

    @current_permission.setter
    def current_permission(self, current_permission):
        """Sets the current_permission of this VariableRes.

        :param current_permission: The current_permission of this VariableRes.
        :type current_permission: str
        """
        self._current_permission = current_permission

    @property
    def description(self):
        """Gets the description of this VariableRes.

        :return: The description of this VariableRes.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VariableRes.

        :param description: The description of this VariableRes.
        :type description: str
        """
        self._description = description

    @property
    def dynamic_param_flag(self):
        """Gets the dynamic_param_flag of this VariableRes.

        :return: The dynamic_param_flag of this VariableRes.
        :rtype: bool
        """
        return self._dynamic_param_flag

    @dynamic_param_flag.setter
    def dynamic_param_flag(self, dynamic_param_flag):
        """Sets the dynamic_param_flag of this VariableRes.

        :param dynamic_param_flag: The dynamic_param_flag of this VariableRes.
        :type dynamic_param_flag: bool
        """
        self._dynamic_param_flag = dynamic_param_flag

    @property
    def function_params(self):
        """Gets the function_params of this VariableRes.

        :return: The function_params of this VariableRes.
        :rtype: str
        """
        return self._function_params

    @function_params.setter
    def function_params(self, function_params):
        """Sets the function_params of this VariableRes.

        :param function_params: The function_params of this VariableRes.
        :type function_params: str
        """
        self._function_params = function_params

    @property
    def group_id(self):
        """Gets the group_id of this VariableRes.

        :return: The group_id of this VariableRes.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this VariableRes.

        :param group_id: The group_id of this VariableRes.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def id(self):
        """Gets the id of this VariableRes.

        id

        :return: The id of this VariableRes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VariableRes.

        id

        :param id: The id of this VariableRes.
        :type id: str
        """
        self._id = id

    @property
    def is_sensitive_info(self):
        """Gets the is_sensitive_info of this VariableRes.

        :return: The is_sensitive_info of this VariableRes.
        :rtype: bool
        """
        return self._is_sensitive_info

    @is_sensitive_info.setter
    def is_sensitive_info(self, is_sensitive_info):
        """Sets the is_sensitive_info of this VariableRes.

        :param is_sensitive_info: The is_sensitive_info of this VariableRes.
        :type is_sensitive_info: bool
        """
        self._is_sensitive_info = is_sensitive_info

    @property
    def is_sensitive_modified(self):
        """Gets the is_sensitive_modified of this VariableRes.

        :return: The is_sensitive_modified of this VariableRes.
        :rtype: bool
        """
        return self._is_sensitive_modified

    @is_sensitive_modified.setter
    def is_sensitive_modified(self, is_sensitive_modified):
        """Sets the is_sensitive_modified of this VariableRes.

        :param is_sensitive_modified: The is_sensitive_modified of this VariableRes.
        :type is_sensitive_modified: bool
        """
        self._is_sensitive_modified = is_sensitive_modified

    @property
    def locked(self):
        """Gets the locked of this VariableRes.

        :return: The locked of this VariableRes.
        :rtype: int
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this VariableRes.

        :param locked: The locked of this VariableRes.
        :type locked: int
        """
        self._locked = locked

    @property
    def name(self):
        """Gets the name of this VariableRes.

        :return: The name of this VariableRes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VariableRes.

        :param name: The name of this VariableRes.
        :type name: str
        """
        self._name = name

    @property
    def node_id(self):
        """Gets the node_id of this VariableRes.

        :return: The node_id of this VariableRes.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this VariableRes.

        :param node_id: The node_id of this VariableRes.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_type(self):
        """Gets the node_type of this VariableRes.

        :return: The node_type of this VariableRes.
        :rtype: int
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this VariableRes.

        :param node_type: The node_type of this VariableRes.
        :type node_type: int
        """
        self._node_type = node_type

    @property
    def parent_id(self):
        """Gets the parent_id of this VariableRes.

        :return: The parent_id of this VariableRes.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this VariableRes.

        :param parent_id: The parent_id of this VariableRes.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def parent_node_id(self):
        """Gets the parent_node_id of this VariableRes.

        :return: The parent_node_id of this VariableRes.
        :rtype: str
        """
        return self._parent_node_id

    @parent_node_id.setter
    def parent_node_id(self, parent_node_id):
        """Sets the parent_node_id of this VariableRes.

        :param parent_node_id: The parent_node_id of this VariableRes.
        :type parent_node_id: str
        """
        self._parent_node_id = parent_node_id

    @property
    def _property(self):
        """Gets the _property of this VariableRes.

        :return: The _property of this VariableRes.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this VariableRes.

        :param _property: The _property of this VariableRes.
        :type _property: str
        """
        self.__property = _property

    @property
    def region(self):
        """Gets the region of this VariableRes.

        :return: The region of this VariableRes.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this VariableRes.

        :param region: The region of this VariableRes.
        :type region: str
        """
        self._region = region

    @property
    def sensitive_info_setter_time(self):
        """Gets the sensitive_info_setter_time of this VariableRes.

        :return: The sensitive_info_setter_time of this VariableRes.
        :rtype: str
        """
        return self._sensitive_info_setter_time

    @sensitive_info_setter_time.setter
    def sensitive_info_setter_time(self, sensitive_info_setter_time):
        """Sets the sensitive_info_setter_time of this VariableRes.

        :param sensitive_info_setter_time: The sensitive_info_setter_time of this VariableRes.
        :type sensitive_info_setter_time: str
        """
        self._sensitive_info_setter_time = sensitive_info_setter_time

    @property
    def sensitive_info_setter_user(self):
        """Gets the sensitive_info_setter_user of this VariableRes.

        :return: The sensitive_info_setter_user of this VariableRes.
        :rtype: str
        """
        return self._sensitive_info_setter_user

    @sensitive_info_setter_user.setter
    def sensitive_info_setter_user(self, sensitive_info_setter_user):
        """Sets the sensitive_info_setter_user of this VariableRes.

        :param sensitive_info_setter_user: The sensitive_info_setter_user of this VariableRes.
        :type sensitive_info_setter_user: str
        """
        self._sensitive_info_setter_user = sensitive_info_setter_user

    @property
    def source_id(self):
        """Gets the source_id of this VariableRes.

        :return: The source_id of this VariableRes.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this VariableRes.

        :param source_id: The source_id of this VariableRes.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def type(self):
        """Gets the type of this VariableRes.

        :return: The type of this VariableRes.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VariableRes.

        :param type: The type of this VariableRes.
        :type type: str
        """
        self._type = type

    @property
    def update_time(self):
        """Gets the update_time of this VariableRes.

        更新时间

        :return: The update_time of this VariableRes.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this VariableRes.

        更新时间

        :param update_time: The update_time of this VariableRes.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def update_time_stamp(self):
        """Gets the update_time_stamp of this VariableRes.

        :return: The update_time_stamp of this VariableRes.
        :rtype: int
        """
        return self._update_time_stamp

    @update_time_stamp.setter
    def update_time_stamp(self, update_time_stamp):
        """Sets the update_time_stamp of this VariableRes.

        :param update_time_stamp: The update_time_stamp of this VariableRes.
        :type update_time_stamp: int
        """
        self._update_time_stamp = update_time_stamp

    @property
    def update_time_string(self):
        """Gets the update_time_string of this VariableRes.

        :return: The update_time_string of this VariableRes.
        :rtype: str
        """
        return self._update_time_string

    @update_time_string.setter
    def update_time_string(self, update_time_string):
        """Sets the update_time_string of this VariableRes.

        :param update_time_string: The update_time_string of this VariableRes.
        :type update_time_string: str
        """
        self._update_time_string = update_time_string

    @property
    def update_user(self):
        """Gets the update_user of this VariableRes.

        更新人

        :return: The update_user of this VariableRes.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this VariableRes.

        更新人

        :param update_user: The update_user of this VariableRes.
        :type update_user: str
        """
        self._update_user = update_user

    @property
    def variable_type(self):
        """Gets the variable_type of this VariableRes.

        :return: The variable_type of this VariableRes.
        :rtype: int
        """
        return self._variable_type

    @variable_type.setter
    def variable_type(self, variable_type):
        """Sets the variable_type of this VariableRes.

        :param variable_type: The variable_type of this VariableRes.
        :type variable_type: int
        """
        self._variable_type = variable_type

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
        if not isinstance(other, VariableRes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
