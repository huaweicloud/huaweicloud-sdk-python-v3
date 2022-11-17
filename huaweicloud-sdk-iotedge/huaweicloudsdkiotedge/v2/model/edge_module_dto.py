# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgeModuleDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edge_app_id': 'str',
        'app_version': 'str',
        'state': 'str',
        'control_status': 'str',
        'node_id': 'str',
        'module_name': 'str',
        'module_id': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'app_type': 'str',
        'function_type': 'str'
    }

    attribute_map = {
        'edge_app_id': 'edge_app_id',
        'app_version': 'app_version',
        'state': 'state',
        'control_status': 'control_status',
        'node_id': 'node_id',
        'module_name': 'module_name',
        'module_id': 'module_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'app_type': 'app_type',
        'function_type': 'function_type'
    }

    def __init__(self, edge_app_id=None, app_version=None, state=None, control_status=None, node_id=None, module_name=None, module_id=None, create_time=None, update_time=None, app_type=None, function_type=None):
        """EdgeModuleDTO

        The model defined in huaweicloud sdk

        :param edge_app_id: 应用ID
        :type edge_app_id: str
        :param app_version: 应用版本
        :type app_version: str
        :param state: 模块运行状态
        :type state: str
        :param control_status: 模块管控状态
        :type control_status: str
        :param node_id: 边缘节点（同deviceID）ID
        :type node_id: str
        :param module_name: 模块名称
        :type module_name: str
        :param module_id: 模块ID
        :type module_id: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 最后一次修改时间
        :type update_time: str
        :param app_type: 应用类型
        :type app_type: str
        :param function_type: 功能类型
        :type function_type: str
        """
        
        

        self._edge_app_id = None
        self._app_version = None
        self._state = None
        self._control_status = None
        self._node_id = None
        self._module_name = None
        self._module_id = None
        self._create_time = None
        self._update_time = None
        self._app_type = None
        self._function_type = None
        self.discriminator = None

        if edge_app_id is not None:
            self.edge_app_id = edge_app_id
        if app_version is not None:
            self.app_version = app_version
        if state is not None:
            self.state = state
        if control_status is not None:
            self.control_status = control_status
        if node_id is not None:
            self.node_id = node_id
        if module_name is not None:
            self.module_name = module_name
        if module_id is not None:
            self.module_id = module_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if app_type is not None:
            self.app_type = app_type
        if function_type is not None:
            self.function_type = function_type

    @property
    def edge_app_id(self):
        """Gets the edge_app_id of this EdgeModuleDTO.

        应用ID

        :return: The edge_app_id of this EdgeModuleDTO.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        """Sets the edge_app_id of this EdgeModuleDTO.

        应用ID

        :param edge_app_id: The edge_app_id of this EdgeModuleDTO.
        :type edge_app_id: str
        """
        self._edge_app_id = edge_app_id

    @property
    def app_version(self):
        """Gets the app_version of this EdgeModuleDTO.

        应用版本

        :return: The app_version of this EdgeModuleDTO.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this EdgeModuleDTO.

        应用版本

        :param app_version: The app_version of this EdgeModuleDTO.
        :type app_version: str
        """
        self._app_version = app_version

    @property
    def state(self):
        """Gets the state of this EdgeModuleDTO.

        模块运行状态

        :return: The state of this EdgeModuleDTO.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this EdgeModuleDTO.

        模块运行状态

        :param state: The state of this EdgeModuleDTO.
        :type state: str
        """
        self._state = state

    @property
    def control_status(self):
        """Gets the control_status of this EdgeModuleDTO.

        模块管控状态

        :return: The control_status of this EdgeModuleDTO.
        :rtype: str
        """
        return self._control_status

    @control_status.setter
    def control_status(self, control_status):
        """Sets the control_status of this EdgeModuleDTO.

        模块管控状态

        :param control_status: The control_status of this EdgeModuleDTO.
        :type control_status: str
        """
        self._control_status = control_status

    @property
    def node_id(self):
        """Gets the node_id of this EdgeModuleDTO.

        边缘节点（同deviceID）ID

        :return: The node_id of this EdgeModuleDTO.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this EdgeModuleDTO.

        边缘节点（同deviceID）ID

        :param node_id: The node_id of this EdgeModuleDTO.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def module_name(self):
        """Gets the module_name of this EdgeModuleDTO.

        模块名称

        :return: The module_name of this EdgeModuleDTO.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """Sets the module_name of this EdgeModuleDTO.

        模块名称

        :param module_name: The module_name of this EdgeModuleDTO.
        :type module_name: str
        """
        self._module_name = module_name

    @property
    def module_id(self):
        """Gets the module_id of this EdgeModuleDTO.

        模块ID

        :return: The module_id of this EdgeModuleDTO.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        """Sets the module_id of this EdgeModuleDTO.

        模块ID

        :param module_id: The module_id of this EdgeModuleDTO.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def create_time(self):
        """Gets the create_time of this EdgeModuleDTO.

        创建时间

        :return: The create_time of this EdgeModuleDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this EdgeModuleDTO.

        创建时间

        :param create_time: The create_time of this EdgeModuleDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this EdgeModuleDTO.

        最后一次修改时间

        :return: The update_time of this EdgeModuleDTO.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this EdgeModuleDTO.

        最后一次修改时间

        :param update_time: The update_time of this EdgeModuleDTO.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def app_type(self):
        """Gets the app_type of this EdgeModuleDTO.

        应用类型

        :return: The app_type of this EdgeModuleDTO.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this EdgeModuleDTO.

        应用类型

        :param app_type: The app_type of this EdgeModuleDTO.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def function_type(self):
        """Gets the function_type of this EdgeModuleDTO.

        功能类型

        :return: The function_type of this EdgeModuleDTO.
        :rtype: str
        """
        return self._function_type

    @function_type.setter
    def function_type(self, function_type):
        """Sets the function_type of this EdgeModuleDTO.

        功能类型

        :param function_type: The function_type of this EdgeModuleDTO.
        :type function_type: str
        """
        self._function_type = function_type

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
        if not isinstance(other, EdgeModuleDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
