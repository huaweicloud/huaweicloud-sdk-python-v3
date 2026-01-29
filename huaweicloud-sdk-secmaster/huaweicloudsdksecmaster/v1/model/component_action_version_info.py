# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentActionVersionInfo:

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
        'create_time': 'str',
        'creator_name': 'str',
        'update_time': 'str',
        'action_version_name': 'str',
        'action_version_number': 'str',
        'action_version_desc': 'str',
        'action_input': 'str',
        'action_output': 'str',
        'action_code': 'str',
        'action_status': 'str',
        'action_enable': 'str',
        'debug_result': 'str',
        'debug_output': 'str',
        'debug_log': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'creator_name': 'creator_name',
        'update_time': 'update_time',
        'action_version_name': 'action_version_name',
        'action_version_number': 'action_version_number',
        'action_version_desc': 'action_version_desc',
        'action_input': 'action_input',
        'action_output': 'action_output',
        'action_code': 'action_code',
        'action_status': 'action_status',
        'action_enable': 'action_enable',
        'debug_result': 'debug_result',
        'debug_output': 'debug_output',
        'debug_log': 'debug_log'
    }

    def __init__(self, id=None, create_time=None, creator_name=None, update_time=None, action_version_name=None, action_version_number=None, action_version_desc=None, action_input=None, action_output=None, action_code=None, action_status=None, action_enable=None, debug_result=None, debug_output=None, debug_log=None):
        r"""ComponentActionVersionInfo

        The model defined in huaweicloud sdk

        :param id: 插件执行函数版本id
        :type id: str
        :param create_time: 创建时间
        :type create_time: str
        :param creator_name: 创建者名称
        :type creator_name: str
        :param update_time: 更新时间
        :type update_time: str
        :param action_version_name: 用户自定义执行函数版本别名
        :type action_version_name: str
        :param action_version_number: 内部生成的执行函数版本号，只会递增
        :type action_version_number: str
        :param action_version_desc: 版本描述
        :type action_version_desc: str
        :param action_input: 执行函数版本输入参数列表
        :type action_input: str
        :param action_output: 执行函数版本输出参数列表
        :type action_output: str
        :param action_code: 执行函数代码
        :type action_code: str
        :param action_status: 版本审核状态
        :type action_status: str
        :param action_enable: 启用/禁用状态
        :type action_enable: str
        :param debug_result: 调试结果
        :type debug_result: str
        :param debug_output: 调试输出
        :type debug_output: str
        :param debug_log: 调试日志
        :type debug_log: str
        """
        
        

        self._id = None
        self._create_time = None
        self._creator_name = None
        self._update_time = None
        self._action_version_name = None
        self._action_version_number = None
        self._action_version_desc = None
        self._action_input = None
        self._action_output = None
        self._action_code = None
        self._action_status = None
        self._action_enable = None
        self._debug_result = None
        self._debug_output = None
        self._debug_log = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_time is not None:
            self.create_time = create_time
        if creator_name is not None:
            self.creator_name = creator_name
        if update_time is not None:
            self.update_time = update_time
        if action_version_name is not None:
            self.action_version_name = action_version_name
        if action_version_number is not None:
            self.action_version_number = action_version_number
        if action_version_desc is not None:
            self.action_version_desc = action_version_desc
        if action_input is not None:
            self.action_input = action_input
        if action_output is not None:
            self.action_output = action_output
        if action_code is not None:
            self.action_code = action_code
        if action_status is not None:
            self.action_status = action_status
        if action_enable is not None:
            self.action_enable = action_enable
        if debug_result is not None:
            self.debug_result = debug_result
        if debug_output is not None:
            self.debug_output = debug_output
        if debug_log is not None:
            self.debug_log = debug_log

    @property
    def id(self):
        r"""Gets the id of this ComponentActionVersionInfo.

        插件执行函数版本id

        :return: The id of this ComponentActionVersionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ComponentActionVersionInfo.

        插件执行函数版本id

        :param id: The id of this ComponentActionVersionInfo.
        :type id: str
        """
        self._id = id

    @property
    def create_time(self):
        r"""Gets the create_time of this ComponentActionVersionInfo.

        创建时间

        :return: The create_time of this ComponentActionVersionInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ComponentActionVersionInfo.

        创建时间

        :param create_time: The create_time of this ComponentActionVersionInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator_name(self):
        r"""Gets the creator_name of this ComponentActionVersionInfo.

        创建者名称

        :return: The creator_name of this ComponentActionVersionInfo.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this ComponentActionVersionInfo.

        创建者名称

        :param creator_name: The creator_name of this ComponentActionVersionInfo.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def update_time(self):
        r"""Gets the update_time of this ComponentActionVersionInfo.

        更新时间

        :return: The update_time of this ComponentActionVersionInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ComponentActionVersionInfo.

        更新时间

        :param update_time: The update_time of this ComponentActionVersionInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def action_version_name(self):
        r"""Gets the action_version_name of this ComponentActionVersionInfo.

        用户自定义执行函数版本别名

        :return: The action_version_name of this ComponentActionVersionInfo.
        :rtype: str
        """
        return self._action_version_name

    @action_version_name.setter
    def action_version_name(self, action_version_name):
        r"""Sets the action_version_name of this ComponentActionVersionInfo.

        用户自定义执行函数版本别名

        :param action_version_name: The action_version_name of this ComponentActionVersionInfo.
        :type action_version_name: str
        """
        self._action_version_name = action_version_name

    @property
    def action_version_number(self):
        r"""Gets the action_version_number of this ComponentActionVersionInfo.

        内部生成的执行函数版本号，只会递增

        :return: The action_version_number of this ComponentActionVersionInfo.
        :rtype: str
        """
        return self._action_version_number

    @action_version_number.setter
    def action_version_number(self, action_version_number):
        r"""Sets the action_version_number of this ComponentActionVersionInfo.

        内部生成的执行函数版本号，只会递增

        :param action_version_number: The action_version_number of this ComponentActionVersionInfo.
        :type action_version_number: str
        """
        self._action_version_number = action_version_number

    @property
    def action_version_desc(self):
        r"""Gets the action_version_desc of this ComponentActionVersionInfo.

        版本描述

        :return: The action_version_desc of this ComponentActionVersionInfo.
        :rtype: str
        """
        return self._action_version_desc

    @action_version_desc.setter
    def action_version_desc(self, action_version_desc):
        r"""Sets the action_version_desc of this ComponentActionVersionInfo.

        版本描述

        :param action_version_desc: The action_version_desc of this ComponentActionVersionInfo.
        :type action_version_desc: str
        """
        self._action_version_desc = action_version_desc

    @property
    def action_input(self):
        r"""Gets the action_input of this ComponentActionVersionInfo.

        执行函数版本输入参数列表

        :return: The action_input of this ComponentActionVersionInfo.
        :rtype: str
        """
        return self._action_input

    @action_input.setter
    def action_input(self, action_input):
        r"""Sets the action_input of this ComponentActionVersionInfo.

        执行函数版本输入参数列表

        :param action_input: The action_input of this ComponentActionVersionInfo.
        :type action_input: str
        """
        self._action_input = action_input

    @property
    def action_output(self):
        r"""Gets the action_output of this ComponentActionVersionInfo.

        执行函数版本输出参数列表

        :return: The action_output of this ComponentActionVersionInfo.
        :rtype: str
        """
        return self._action_output

    @action_output.setter
    def action_output(self, action_output):
        r"""Sets the action_output of this ComponentActionVersionInfo.

        执行函数版本输出参数列表

        :param action_output: The action_output of this ComponentActionVersionInfo.
        :type action_output: str
        """
        self._action_output = action_output

    @property
    def action_code(self):
        r"""Gets the action_code of this ComponentActionVersionInfo.

        执行函数代码

        :return: The action_code of this ComponentActionVersionInfo.
        :rtype: str
        """
        return self._action_code

    @action_code.setter
    def action_code(self, action_code):
        r"""Sets the action_code of this ComponentActionVersionInfo.

        执行函数代码

        :param action_code: The action_code of this ComponentActionVersionInfo.
        :type action_code: str
        """
        self._action_code = action_code

    @property
    def action_status(self):
        r"""Gets the action_status of this ComponentActionVersionInfo.

        版本审核状态

        :return: The action_status of this ComponentActionVersionInfo.
        :rtype: str
        """
        return self._action_status

    @action_status.setter
    def action_status(self, action_status):
        r"""Sets the action_status of this ComponentActionVersionInfo.

        版本审核状态

        :param action_status: The action_status of this ComponentActionVersionInfo.
        :type action_status: str
        """
        self._action_status = action_status

    @property
    def action_enable(self):
        r"""Gets the action_enable of this ComponentActionVersionInfo.

        启用/禁用状态

        :return: The action_enable of this ComponentActionVersionInfo.
        :rtype: str
        """
        return self._action_enable

    @action_enable.setter
    def action_enable(self, action_enable):
        r"""Sets the action_enable of this ComponentActionVersionInfo.

        启用/禁用状态

        :param action_enable: The action_enable of this ComponentActionVersionInfo.
        :type action_enable: str
        """
        self._action_enable = action_enable

    @property
    def debug_result(self):
        r"""Gets the debug_result of this ComponentActionVersionInfo.

        调试结果

        :return: The debug_result of this ComponentActionVersionInfo.
        :rtype: str
        """
        return self._debug_result

    @debug_result.setter
    def debug_result(self, debug_result):
        r"""Sets the debug_result of this ComponentActionVersionInfo.

        调试结果

        :param debug_result: The debug_result of this ComponentActionVersionInfo.
        :type debug_result: str
        """
        self._debug_result = debug_result

    @property
    def debug_output(self):
        r"""Gets the debug_output of this ComponentActionVersionInfo.

        调试输出

        :return: The debug_output of this ComponentActionVersionInfo.
        :rtype: str
        """
        return self._debug_output

    @debug_output.setter
    def debug_output(self, debug_output):
        r"""Sets the debug_output of this ComponentActionVersionInfo.

        调试输出

        :param debug_output: The debug_output of this ComponentActionVersionInfo.
        :type debug_output: str
        """
        self._debug_output = debug_output

    @property
    def debug_log(self):
        r"""Gets the debug_log of this ComponentActionVersionInfo.

        调试日志

        :return: The debug_log of this ComponentActionVersionInfo.
        :rtype: str
        """
        return self._debug_log

    @debug_log.setter
    def debug_log(self, debug_log):
        r"""Sets the debug_log of this ComponentActionVersionInfo.

        调试日志

        :param debug_log: The debug_log of this ComponentActionVersionInfo.
        :type debug_log: str
        """
        self._debug_log = debug_log

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
        if not isinstance(other, ComponentActionVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
