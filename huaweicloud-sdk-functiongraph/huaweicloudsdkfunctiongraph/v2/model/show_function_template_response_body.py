# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFunctionTemplateResponseBody:

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
        'type': 'int',
        'title': 'str',
        'template_name': 'str',
        'description': 'str',
        'runtime': 'str',
        'handler': 'str',
        'code_type': 'str',
        'code': 'str',
        'timeout': 'int',
        'memory_size': 'int',
        'trigger_metadata_list': 'list[TriggerMetadataList]',
        'temp_detail': 'TempDetail',
        'user_data': 'str',
        'encrypted_user_data': 'str',
        'dependencies': 'list[str]',
        'scene': 'str',
        'service': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'title': 'title',
        'template_name': 'template_name',
        'description': 'description',
        'runtime': 'runtime',
        'handler': 'handler',
        'code_type': 'code_type',
        'code': 'code',
        'timeout': 'timeout',
        'memory_size': 'memory_size',
        'trigger_metadata_list': 'trigger_metadata_list',
        'temp_detail': 'temp_detail',
        'user_data': 'user_data',
        'encrypted_user_data': 'encrypted_user_data',
        'dependencies': 'dependencies',
        'scene': 'scene',
        'service': 'service'
    }

    def __init__(self, id=None, type=None, title=None, template_name=None, description=None, runtime=None, handler=None, code_type=None, code=None, timeout=None, memory_size=None, trigger_metadata_list=None, temp_detail=None, user_data=None, encrypted_user_data=None, dependencies=None, scene=None, service=None):
        """ShowFunctionTemplateResponseBody

        The model defined in huaweicloud sdk

        :param id: 模板id
        :type id: str
        :param type: 模板类型
        :type type: int
        :param title: 模板标题
        :type title: str
        :param template_name: 模板名称
        :type template_name: str
        :param description: 模板描述
        :type description: str
        :param runtime: 模板执行运行时
        :type runtime: str
        :param handler: 模板函数执行入口
        :type handler: str
        :param code_type: 代码类型
        :type code_type: str
        :param code: 代码文件
        :type code: str
        :param timeout: 函数执行超时时间，超时函数将被强行停止，范围3～259200秒。
        :type timeout: int
        :param memory_size: 内存大小
        :type memory_size: int
        :param trigger_metadata_list: 触发信息列表
        :type trigger_metadata_list: list[:class:`huaweicloudsdkfunctiongraph.v2.TriggerMetadataList`]
        :param temp_detail: 
        :type temp_detail: :class:`huaweicloudsdkfunctiongraph.v2.TempDetail`
        :param user_data: 用户数据
        :type user_data: str
        :param encrypted_user_data: 加密用户数据
        :type encrypted_user_data: str
        :param dependencies: 模板所需依赖列表
        :type dependencies: list[str]
        :param scene: 模板使用场景
        :type scene: str
        :param service: 模板关联云服务
        :type service: str
        """
        
        

        self._id = None
        self._type = None
        self._title = None
        self._template_name = None
        self._description = None
        self._runtime = None
        self._handler = None
        self._code_type = None
        self._code = None
        self._timeout = None
        self._memory_size = None
        self._trigger_metadata_list = None
        self._temp_detail = None
        self._user_data = None
        self._encrypted_user_data = None
        self._dependencies = None
        self._scene = None
        self._service = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if title is not None:
            self.title = title
        if template_name is not None:
            self.template_name = template_name
        if description is not None:
            self.description = description
        if runtime is not None:
            self.runtime = runtime
        if handler is not None:
            self.handler = handler
        if code_type is not None:
            self.code_type = code_type
        if code is not None:
            self.code = code
        if timeout is not None:
            self.timeout = timeout
        if memory_size is not None:
            self.memory_size = memory_size
        if trigger_metadata_list is not None:
            self.trigger_metadata_list = trigger_metadata_list
        if temp_detail is not None:
            self.temp_detail = temp_detail
        if user_data is not None:
            self.user_data = user_data
        if encrypted_user_data is not None:
            self.encrypted_user_data = encrypted_user_data
        if dependencies is not None:
            self.dependencies = dependencies
        if scene is not None:
            self.scene = scene
        if service is not None:
            self.service = service

    @property
    def id(self):
        """Gets the id of this ShowFunctionTemplateResponseBody.

        模板id

        :return: The id of this ShowFunctionTemplateResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowFunctionTemplateResponseBody.

        模板id

        :param id: The id of this ShowFunctionTemplateResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this ShowFunctionTemplateResponseBody.

        模板类型

        :return: The type of this ShowFunctionTemplateResponseBody.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowFunctionTemplateResponseBody.

        模板类型

        :param type: The type of this ShowFunctionTemplateResponseBody.
        :type type: int
        """
        self._type = type

    @property
    def title(self):
        """Gets the title of this ShowFunctionTemplateResponseBody.

        模板标题

        :return: The title of this ShowFunctionTemplateResponseBody.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ShowFunctionTemplateResponseBody.

        模板标题

        :param title: The title of this ShowFunctionTemplateResponseBody.
        :type title: str
        """
        self._title = title

    @property
    def template_name(self):
        """Gets the template_name of this ShowFunctionTemplateResponseBody.

        模板名称

        :return: The template_name of this ShowFunctionTemplateResponseBody.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this ShowFunctionTemplateResponseBody.

        模板名称

        :param template_name: The template_name of this ShowFunctionTemplateResponseBody.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def description(self):
        """Gets the description of this ShowFunctionTemplateResponseBody.

        模板描述

        :return: The description of this ShowFunctionTemplateResponseBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowFunctionTemplateResponseBody.

        模板描述

        :param description: The description of this ShowFunctionTemplateResponseBody.
        :type description: str
        """
        self._description = description

    @property
    def runtime(self):
        """Gets the runtime of this ShowFunctionTemplateResponseBody.

        模板执行运行时

        :return: The runtime of this ShowFunctionTemplateResponseBody.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this ShowFunctionTemplateResponseBody.

        模板执行运行时

        :param runtime: The runtime of this ShowFunctionTemplateResponseBody.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def handler(self):
        """Gets the handler of this ShowFunctionTemplateResponseBody.

        模板函数执行入口

        :return: The handler of this ShowFunctionTemplateResponseBody.
        :rtype: str
        """
        return self._handler

    @handler.setter
    def handler(self, handler):
        """Sets the handler of this ShowFunctionTemplateResponseBody.

        模板函数执行入口

        :param handler: The handler of this ShowFunctionTemplateResponseBody.
        :type handler: str
        """
        self._handler = handler

    @property
    def code_type(self):
        """Gets the code_type of this ShowFunctionTemplateResponseBody.

        代码类型

        :return: The code_type of this ShowFunctionTemplateResponseBody.
        :rtype: str
        """
        return self._code_type

    @code_type.setter
    def code_type(self, code_type):
        """Sets the code_type of this ShowFunctionTemplateResponseBody.

        代码类型

        :param code_type: The code_type of this ShowFunctionTemplateResponseBody.
        :type code_type: str
        """
        self._code_type = code_type

    @property
    def code(self):
        """Gets the code of this ShowFunctionTemplateResponseBody.

        代码文件

        :return: The code of this ShowFunctionTemplateResponseBody.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ShowFunctionTemplateResponseBody.

        代码文件

        :param code: The code of this ShowFunctionTemplateResponseBody.
        :type code: str
        """
        self._code = code

    @property
    def timeout(self):
        """Gets the timeout of this ShowFunctionTemplateResponseBody.

        函数执行超时时间，超时函数将被强行停止，范围3～259200秒。

        :return: The timeout of this ShowFunctionTemplateResponseBody.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ShowFunctionTemplateResponseBody.

        函数执行超时时间，超时函数将被强行停止，范围3～259200秒。

        :param timeout: The timeout of this ShowFunctionTemplateResponseBody.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def memory_size(self):
        """Gets the memory_size of this ShowFunctionTemplateResponseBody.

        内存大小

        :return: The memory_size of this ShowFunctionTemplateResponseBody.
        :rtype: int
        """
        return self._memory_size

    @memory_size.setter
    def memory_size(self, memory_size):
        """Sets the memory_size of this ShowFunctionTemplateResponseBody.

        内存大小

        :param memory_size: The memory_size of this ShowFunctionTemplateResponseBody.
        :type memory_size: int
        """
        self._memory_size = memory_size

    @property
    def trigger_metadata_list(self):
        """Gets the trigger_metadata_list of this ShowFunctionTemplateResponseBody.

        触发信息列表

        :return: The trigger_metadata_list of this ShowFunctionTemplateResponseBody.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.TriggerMetadataList`]
        """
        return self._trigger_metadata_list

    @trigger_metadata_list.setter
    def trigger_metadata_list(self, trigger_metadata_list):
        """Sets the trigger_metadata_list of this ShowFunctionTemplateResponseBody.

        触发信息列表

        :param trigger_metadata_list: The trigger_metadata_list of this ShowFunctionTemplateResponseBody.
        :type trigger_metadata_list: list[:class:`huaweicloudsdkfunctiongraph.v2.TriggerMetadataList`]
        """
        self._trigger_metadata_list = trigger_metadata_list

    @property
    def temp_detail(self):
        """Gets the temp_detail of this ShowFunctionTemplateResponseBody.

        :return: The temp_detail of this ShowFunctionTemplateResponseBody.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.TempDetail`
        """
        return self._temp_detail

    @temp_detail.setter
    def temp_detail(self, temp_detail):
        """Sets the temp_detail of this ShowFunctionTemplateResponseBody.

        :param temp_detail: The temp_detail of this ShowFunctionTemplateResponseBody.
        :type temp_detail: :class:`huaweicloudsdkfunctiongraph.v2.TempDetail`
        """
        self._temp_detail = temp_detail

    @property
    def user_data(self):
        """Gets the user_data of this ShowFunctionTemplateResponseBody.

        用户数据

        :return: The user_data of this ShowFunctionTemplateResponseBody.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this ShowFunctionTemplateResponseBody.

        用户数据

        :param user_data: The user_data of this ShowFunctionTemplateResponseBody.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def encrypted_user_data(self):
        """Gets the encrypted_user_data of this ShowFunctionTemplateResponseBody.

        加密用户数据

        :return: The encrypted_user_data of this ShowFunctionTemplateResponseBody.
        :rtype: str
        """
        return self._encrypted_user_data

    @encrypted_user_data.setter
    def encrypted_user_data(self, encrypted_user_data):
        """Sets the encrypted_user_data of this ShowFunctionTemplateResponseBody.

        加密用户数据

        :param encrypted_user_data: The encrypted_user_data of this ShowFunctionTemplateResponseBody.
        :type encrypted_user_data: str
        """
        self._encrypted_user_data = encrypted_user_data

    @property
    def dependencies(self):
        """Gets the dependencies of this ShowFunctionTemplateResponseBody.

        模板所需依赖列表

        :return: The dependencies of this ShowFunctionTemplateResponseBody.
        :rtype: list[str]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this ShowFunctionTemplateResponseBody.

        模板所需依赖列表

        :param dependencies: The dependencies of this ShowFunctionTemplateResponseBody.
        :type dependencies: list[str]
        """
        self._dependencies = dependencies

    @property
    def scene(self):
        """Gets the scene of this ShowFunctionTemplateResponseBody.

        模板使用场景

        :return: The scene of this ShowFunctionTemplateResponseBody.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        """Sets the scene of this ShowFunctionTemplateResponseBody.

        模板使用场景

        :param scene: The scene of this ShowFunctionTemplateResponseBody.
        :type scene: str
        """
        self._scene = scene

    @property
    def service(self):
        """Gets the service of this ShowFunctionTemplateResponseBody.

        模板关联云服务

        :return: The service of this ShowFunctionTemplateResponseBody.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this ShowFunctionTemplateResponseBody.

        模板关联云服务

        :param service: The service of this ShowFunctionTemplateResponseBody.
        :type service: str
        """
        self._service = service

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
        if not isinstance(other, ShowFunctionTemplateResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
