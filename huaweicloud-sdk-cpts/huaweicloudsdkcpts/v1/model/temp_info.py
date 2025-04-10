# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TempInfo:

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
        'project_id': 'int',
        'name': 'str',
        'description': 'str',
        'variables': 'str',
        'contents': 'list[object]',
        'temp_type': 'int',
        'for_loop_params': 'list[object]',
        'logic_controller': 'LogicController',
        'enable_pre': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'name': 'name',
        'description': 'description',
        'variables': 'variables',
        'contents': 'contents',
        'temp_type': 'temp_type',
        'for_loop_params': 'for_loop_params',
        'logic_controller': 'logic_controller',
        'enable_pre': 'enable_pre'
    }

    def __init__(self, id=None, project_id=None, name=None, description=None, variables=None, contents=None, temp_type=None, for_loop_params=None, logic_controller=None, enable_pre=None):
        r"""TempInfo

        The model defined in huaweicloud sdk

        :param id: 事务id
        :type id: int
        :param project_id: 工程id
        :type project_id: int
        :param name: 事务名称
        :type name: str
        :param description: 事务描述
        :type description: str
        :param variables: 变量
        :type variables: str
        :param contents: 事务脚本信息
        :type contents: list[object]
        :param temp_type: 事务类型（弃用）
        :type temp_type: int
        :param for_loop_params: 旧版本逻辑控制器字段，当前已未使用
        :type for_loop_params: list[object]
        :param logic_controller: 
        :type logic_controller: :class:`huaweicloudsdkcpts.v1.LogicController`
        :param enable_pre: 是否启用预置事务，当前版本已未使用
        :type enable_pre: bool
        """
        
        

        self._id = None
        self._project_id = None
        self._name = None
        self._description = None
        self._variables = None
        self._contents = None
        self._temp_type = None
        self._for_loop_params = None
        self._logic_controller = None
        self._enable_pre = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if variables is not None:
            self.variables = variables
        if contents is not None:
            self.contents = contents
        if temp_type is not None:
            self.temp_type = temp_type
        if for_loop_params is not None:
            self.for_loop_params = for_loop_params
        if logic_controller is not None:
            self.logic_controller = logic_controller
        if enable_pre is not None:
            self.enable_pre = enable_pre

    @property
    def id(self):
        r"""Gets the id of this TempInfo.

        事务id

        :return: The id of this TempInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TempInfo.

        事务id

        :param id: The id of this TempInfo.
        :type id: int
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this TempInfo.

        工程id

        :return: The project_id of this TempInfo.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TempInfo.

        工程id

        :param project_id: The project_id of this TempInfo.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def name(self):
        r"""Gets the name of this TempInfo.

        事务名称

        :return: The name of this TempInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TempInfo.

        事务名称

        :param name: The name of this TempInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this TempInfo.

        事务描述

        :return: The description of this TempInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TempInfo.

        事务描述

        :param description: The description of this TempInfo.
        :type description: str
        """
        self._description = description

    @property
    def variables(self):
        r"""Gets the variables of this TempInfo.

        变量

        :return: The variables of this TempInfo.
        :rtype: str
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        r"""Sets the variables of this TempInfo.

        变量

        :param variables: The variables of this TempInfo.
        :type variables: str
        """
        self._variables = variables

    @property
    def contents(self):
        r"""Gets the contents of this TempInfo.

        事务脚本信息

        :return: The contents of this TempInfo.
        :rtype: list[object]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this TempInfo.

        事务脚本信息

        :param contents: The contents of this TempInfo.
        :type contents: list[object]
        """
        self._contents = contents

    @property
    def temp_type(self):
        r"""Gets the temp_type of this TempInfo.

        事务类型（弃用）

        :return: The temp_type of this TempInfo.
        :rtype: int
        """
        return self._temp_type

    @temp_type.setter
    def temp_type(self, temp_type):
        r"""Sets the temp_type of this TempInfo.

        事务类型（弃用）

        :param temp_type: The temp_type of this TempInfo.
        :type temp_type: int
        """
        self._temp_type = temp_type

    @property
    def for_loop_params(self):
        r"""Gets the for_loop_params of this TempInfo.

        旧版本逻辑控制器字段，当前已未使用

        :return: The for_loop_params of this TempInfo.
        :rtype: list[object]
        """
        return self._for_loop_params

    @for_loop_params.setter
    def for_loop_params(self, for_loop_params):
        r"""Sets the for_loop_params of this TempInfo.

        旧版本逻辑控制器字段，当前已未使用

        :param for_loop_params: The for_loop_params of this TempInfo.
        :type for_loop_params: list[object]
        """
        self._for_loop_params = for_loop_params

    @property
    def logic_controller(self):
        r"""Gets the logic_controller of this TempInfo.

        :return: The logic_controller of this TempInfo.
        :rtype: :class:`huaweicloudsdkcpts.v1.LogicController`
        """
        return self._logic_controller

    @logic_controller.setter
    def logic_controller(self, logic_controller):
        r"""Sets the logic_controller of this TempInfo.

        :param logic_controller: The logic_controller of this TempInfo.
        :type logic_controller: :class:`huaweicloudsdkcpts.v1.LogicController`
        """
        self._logic_controller = logic_controller

    @property
    def enable_pre(self):
        r"""Gets the enable_pre of this TempInfo.

        是否启用预置事务，当前版本已未使用

        :return: The enable_pre of this TempInfo.
        :rtype: bool
        """
        return self._enable_pre

    @enable_pre.setter
    def enable_pre(self, enable_pre):
        r"""Sets the enable_pre of this TempInfo.

        是否启用预置事务，当前版本已未使用

        :param enable_pre: The enable_pre of this TempInfo.
        :type enable_pre: bool
        """
        self._enable_pre = enable_pre

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
        if not isinstance(other, TempInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
