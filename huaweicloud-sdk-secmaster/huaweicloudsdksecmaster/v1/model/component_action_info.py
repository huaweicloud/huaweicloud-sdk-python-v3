# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentActionInfo:

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
        'action_name': 'str',
        'action_desc': 'str',
        'action_type': 'str',
        'create_time': 'str',
        'creator_name': 'str',
        'can_update': 'bool',
        'action_version_id': 'str',
        'action_version_name': 'str',
        'action_version_number': 'str',
        'action_enable': 'str',
        'action_input': 'str',
        'action_output': 'str',
        'action_versions': 'list[ComponentActionVersionInfo]'
    }

    attribute_map = {
        'id': 'id',
        'action_name': 'action_name',
        'action_desc': 'action_desc',
        'action_type': 'action_type',
        'create_time': 'create_time',
        'creator_name': 'creator_name',
        'can_update': 'can_update',
        'action_version_id': 'action_version_id',
        'action_version_name': 'action_version_name',
        'action_version_number': 'action_version_number',
        'action_enable': 'action_enable',
        'action_input': 'action_input',
        'action_output': 'action_output',
        'action_versions': 'action_versions'
    }

    def __init__(self, id=None, action_name=None, action_desc=None, action_type=None, create_time=None, creator_name=None, can_update=None, action_version_id=None, action_version_name=None, action_version_number=None, action_enable=None, action_input=None, action_output=None, action_versions=None):
        r"""ComponentActionInfo

        The model defined in huaweicloud sdk

        :param id: 插件执行函数id
        :type id: str
        :param action_name: 插件执行函数名称
        :type action_name: str
        :param action_desc: 插件执行函数描述
        :type action_desc: str
        :param action_type: 执行函数类型，可选action/connector/manager
        :type action_type: str
        :param create_time: 创建时间
        :type create_time: str
        :param creator_name: 创建者名称
        :type creator_name: str
        :param can_update: 是否可升级，true/false
        :type can_update: bool
        :param action_version_id: 当前启用的插件执行函数版本id
        :type action_version_id: str
        :param action_version_name: 当前启用的用户自定义执行函数版本别名
        :type action_version_name: str
        :param action_version_number: 当前启用的执行函数版本号
        :type action_version_number: str
        :param action_enable: 启用/禁用状态
        :type action_enable: str
        :param action_input: 当前启用的执行函数版本输入参数列表
        :type action_input: str
        :param action_output: 当前启用的执行函数版本输出参数列表
        :type action_output: str
        :param action_versions: 全量插件执行函数版本列表
        :type action_versions: list[:class:`huaweicloudsdksecmaster.v1.ComponentActionVersionInfo`]
        """
        
        

        self._id = None
        self._action_name = None
        self._action_desc = None
        self._action_type = None
        self._create_time = None
        self._creator_name = None
        self._can_update = None
        self._action_version_id = None
        self._action_version_name = None
        self._action_version_number = None
        self._action_enable = None
        self._action_input = None
        self._action_output = None
        self._action_versions = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if action_name is not None:
            self.action_name = action_name
        if action_desc is not None:
            self.action_desc = action_desc
        if action_type is not None:
            self.action_type = action_type
        if create_time is not None:
            self.create_time = create_time
        if creator_name is not None:
            self.creator_name = creator_name
        if can_update is not None:
            self.can_update = can_update
        if action_version_id is not None:
            self.action_version_id = action_version_id
        if action_version_name is not None:
            self.action_version_name = action_version_name
        if action_version_number is not None:
            self.action_version_number = action_version_number
        if action_enable is not None:
            self.action_enable = action_enable
        if action_input is not None:
            self.action_input = action_input
        if action_output is not None:
            self.action_output = action_output
        if action_versions is not None:
            self.action_versions = action_versions

    @property
    def id(self):
        r"""Gets the id of this ComponentActionInfo.

        插件执行函数id

        :return: The id of this ComponentActionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ComponentActionInfo.

        插件执行函数id

        :param id: The id of this ComponentActionInfo.
        :type id: str
        """
        self._id = id

    @property
    def action_name(self):
        r"""Gets the action_name of this ComponentActionInfo.

        插件执行函数名称

        :return: The action_name of this ComponentActionInfo.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        r"""Sets the action_name of this ComponentActionInfo.

        插件执行函数名称

        :param action_name: The action_name of this ComponentActionInfo.
        :type action_name: str
        """
        self._action_name = action_name

    @property
    def action_desc(self):
        r"""Gets the action_desc of this ComponentActionInfo.

        插件执行函数描述

        :return: The action_desc of this ComponentActionInfo.
        :rtype: str
        """
        return self._action_desc

    @action_desc.setter
    def action_desc(self, action_desc):
        r"""Sets the action_desc of this ComponentActionInfo.

        插件执行函数描述

        :param action_desc: The action_desc of this ComponentActionInfo.
        :type action_desc: str
        """
        self._action_desc = action_desc

    @property
    def action_type(self):
        r"""Gets the action_type of this ComponentActionInfo.

        执行函数类型，可选action/connector/manager

        :return: The action_type of this ComponentActionInfo.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        r"""Sets the action_type of this ComponentActionInfo.

        执行函数类型，可选action/connector/manager

        :param action_type: The action_type of this ComponentActionInfo.
        :type action_type: str
        """
        self._action_type = action_type

    @property
    def create_time(self):
        r"""Gets the create_time of this ComponentActionInfo.

        创建时间

        :return: The create_time of this ComponentActionInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ComponentActionInfo.

        创建时间

        :param create_time: The create_time of this ComponentActionInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator_name(self):
        r"""Gets the creator_name of this ComponentActionInfo.

        创建者名称

        :return: The creator_name of this ComponentActionInfo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this ComponentActionInfo.

        创建者名称

        :param creator_name: The creator_name of this ComponentActionInfo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def can_update(self):
        r"""Gets the can_update of this ComponentActionInfo.

        是否可升级，true/false

        :return: The can_update of this ComponentActionInfo.
        :rtype: bool
        """
        return self._can_update

    @can_update.setter
    def can_update(self, can_update):
        r"""Sets the can_update of this ComponentActionInfo.

        是否可升级，true/false

        :param can_update: The can_update of this ComponentActionInfo.
        :type can_update: bool
        """
        self._can_update = can_update

    @property
    def action_version_id(self):
        r"""Gets the action_version_id of this ComponentActionInfo.

        当前启用的插件执行函数版本id

        :return: The action_version_id of this ComponentActionInfo.
        :rtype: str
        """
        return self._action_version_id

    @action_version_id.setter
    def action_version_id(self, action_version_id):
        r"""Sets the action_version_id of this ComponentActionInfo.

        当前启用的插件执行函数版本id

        :param action_version_id: The action_version_id of this ComponentActionInfo.
        :type action_version_id: str
        """
        self._action_version_id = action_version_id

    @property
    def action_version_name(self):
        r"""Gets the action_version_name of this ComponentActionInfo.

        当前启用的用户自定义执行函数版本别名

        :return: The action_version_name of this ComponentActionInfo.
        :rtype: str
        """
        return self._action_version_name

    @action_version_name.setter
    def action_version_name(self, action_version_name):
        r"""Sets the action_version_name of this ComponentActionInfo.

        当前启用的用户自定义执行函数版本别名

        :param action_version_name: The action_version_name of this ComponentActionInfo.
        :type action_version_name: str
        """
        self._action_version_name = action_version_name

    @property
    def action_version_number(self):
        r"""Gets the action_version_number of this ComponentActionInfo.

        当前启用的执行函数版本号

        :return: The action_version_number of this ComponentActionInfo.
        :rtype: str
        """
        return self._action_version_number

    @action_version_number.setter
    def action_version_number(self, action_version_number):
        r"""Sets the action_version_number of this ComponentActionInfo.

        当前启用的执行函数版本号

        :param action_version_number: The action_version_number of this ComponentActionInfo.
        :type action_version_number: str
        """
        self._action_version_number = action_version_number

    @property
    def action_enable(self):
        r"""Gets the action_enable of this ComponentActionInfo.

        启用/禁用状态

        :return: The action_enable of this ComponentActionInfo.
        :rtype: str
        """
        return self._action_enable

    @action_enable.setter
    def action_enable(self, action_enable):
        r"""Sets the action_enable of this ComponentActionInfo.

        启用/禁用状态

        :param action_enable: The action_enable of this ComponentActionInfo.
        :type action_enable: str
        """
        self._action_enable = action_enable

    @property
    def action_input(self):
        r"""Gets the action_input of this ComponentActionInfo.

        当前启用的执行函数版本输入参数列表

        :return: The action_input of this ComponentActionInfo.
        :rtype: str
        """
        return self._action_input

    @action_input.setter
    def action_input(self, action_input):
        r"""Sets the action_input of this ComponentActionInfo.

        当前启用的执行函数版本输入参数列表

        :param action_input: The action_input of this ComponentActionInfo.
        :type action_input: str
        """
        self._action_input = action_input

    @property
    def action_output(self):
        r"""Gets the action_output of this ComponentActionInfo.

        当前启用的执行函数版本输出参数列表

        :return: The action_output of this ComponentActionInfo.
        :rtype: str
        """
        return self._action_output

    @action_output.setter
    def action_output(self, action_output):
        r"""Sets the action_output of this ComponentActionInfo.

        当前启用的执行函数版本输出参数列表

        :param action_output: The action_output of this ComponentActionInfo.
        :type action_output: str
        """
        self._action_output = action_output

    @property
    def action_versions(self):
        r"""Gets the action_versions of this ComponentActionInfo.

        全量插件执行函数版本列表

        :return: The action_versions of this ComponentActionInfo.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ComponentActionVersionInfo`]
        """
        return self._action_versions

    @action_versions.setter
    def action_versions(self, action_versions):
        r"""Sets the action_versions of this ComponentActionInfo.

        全量插件执行函数版本列表

        :param action_versions: The action_versions of this ComponentActionInfo.
        :type action_versions: list[:class:`huaweicloudsdksecmaster.v1.ComponentActionVersionInfo`]
        """
        self._action_versions = action_versions

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ComponentActionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
