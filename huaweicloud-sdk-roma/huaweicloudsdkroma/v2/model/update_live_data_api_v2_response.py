# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLiveDataApiV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'path': 'str',
        'method': 'str',
        'description': 'str',
        'version': 'str',
        'content_type': 'str',
        'api_signature_id': 'str',
        'roma_app_id': 'str',
        'return_format': 'bool',
        'parameters': 'list[LdApiParameter]',
        'id': 'str',
        'instance': 'str',
        'type': 'str',
        'status': 'int',
        'created_time': 'datetime',
        'modified_time': 'datetime',
        'scripts': 'list[LdApiScript]',
        'roma_app_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'path': 'path',
        'method': 'method',
        'description': 'description',
        'version': 'version',
        'content_type': 'content_type',
        'api_signature_id': 'api_signature_id',
        'roma_app_id': 'roma_app_id',
        'return_format': 'return_format',
        'parameters': 'parameters',
        'id': 'id',
        'instance': 'instance',
        'type': 'type',
        'status': 'status',
        'created_time': 'created_time',
        'modified_time': 'modified_time',
        'scripts': 'scripts',
        'roma_app_name': 'roma_app_name'
    }

    def __init__(self, name=None, path=None, method=None, description=None, version=None, content_type=None, api_signature_id=None, roma_app_id=None, return_format=None, parameters=None, id=None, instance=None, type=None, status=None, created_time=None, modified_time=None, scripts=None, roma_app_name=None):
        """UpdateLiveDataApiV2Response

        The model defined in huaweicloud sdk

        :param name: 后端API名称。  支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头。
        :type name: str
        :param path: 后端API请求路径。  支持英文、数字、中划线、下划线、点等，且以斜杠（/）开头。  更新后端API时，status&#x3D;4为后端API的已部署状态，该状态下后端API请求路径不能修改。
        :type path: str
        :param method: 后端API请求方法。  支持GET、PUT、POST、DELETE  更新后端API时，status&#x3D;4为后端API的已部署状态，该状态下后端API请求方法不能修改。
        :type method: str
        :param description: 后端API描述。  不支持&lt;，&gt;字符
        :type description: str
        :param version: 后端API版本  支持英文，数字，下划线，中划线，点。
        :type version: str
        :param content_type: 后端API返回类型
        :type content_type: str
        :param api_signature_id: 后端API为签名认证时绑定的签名密钥编号
        :type api_signature_id: str
        :param roma_app_id: 后端API归属的集成应用编号  更新后端API时，status&#x3D;4为后端API的已部署状态，该状态下后端API归属的集成应用编号不能修改。
        :type roma_app_id: str
        :param return_format: API响应信息是否格式化  true： 对响应信息进行格式化  false：对响应信息格式化不进行格式化 
        :type return_format: bool
        :param parameters: 后端API的请求参数列表
        :type parameters: list[:class:`huaweicloudsdkroma.v2.LdApiParameter`]
        :param id: 后端API编号
        :type id: str
        :param instance: 后端API所属实例编号
        :type instance: str
        :param type: 后端API类型： - data：数据后端 - function： 函数后端
        :type type: str
        :param status: 后端API状态： - 1：待开发 - 3：开发中 - 4：已部署
        :type status: int
        :param created_time: 后端API创建时间
        :type created_time: datetime
        :param modified_time: 后端API修改时间
        :type modified_time: datetime
        :param scripts: 后端API脚本信息
        :type scripts: list[:class:`huaweicloudsdkroma.v2.LdApiScript`]
        :param roma_app_name: 后端API归属的集成应用名称
        :type roma_app_name: str
        """
        
        super(UpdateLiveDataApiV2Response, self).__init__()

        self._name = None
        self._path = None
        self._method = None
        self._description = None
        self._version = None
        self._content_type = None
        self._api_signature_id = None
        self._roma_app_id = None
        self._return_format = None
        self._parameters = None
        self._id = None
        self._instance = None
        self._type = None
        self._status = None
        self._created_time = None
        self._modified_time = None
        self._scripts = None
        self._roma_app_name = None
        self.discriminator = None

        self.name = name
        self.path = path
        self.method = method
        if description is not None:
            self.description = description
        self.version = version
        self.content_type = content_type
        if api_signature_id is not None:
            self.api_signature_id = api_signature_id
        self.roma_app_id = roma_app_id
        if return_format is not None:
            self.return_format = return_format
        if parameters is not None:
            self.parameters = parameters
        if id is not None:
            self.id = id
        if instance is not None:
            self.instance = instance
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time
        if scripts is not None:
            self.scripts = scripts
        if roma_app_name is not None:
            self.roma_app_name = roma_app_name

    @property
    def name(self):
        """Gets the name of this UpdateLiveDataApiV2Response.

        后端API名称。  支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头。

        :return: The name of this UpdateLiveDataApiV2Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateLiveDataApiV2Response.

        后端API名称。  支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头。

        :param name: The name of this UpdateLiveDataApiV2Response.
        :type name: str
        """
        self._name = name

    @property
    def path(self):
        """Gets the path of this UpdateLiveDataApiV2Response.

        后端API请求路径。  支持英文、数字、中划线、下划线、点等，且以斜杠（/）开头。  更新后端API时，status=4为后端API的已部署状态，该状态下后端API请求路径不能修改。

        :return: The path of this UpdateLiveDataApiV2Response.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this UpdateLiveDataApiV2Response.

        后端API请求路径。  支持英文、数字、中划线、下划线、点等，且以斜杠（/）开头。  更新后端API时，status=4为后端API的已部署状态，该状态下后端API请求路径不能修改。

        :param path: The path of this UpdateLiveDataApiV2Response.
        :type path: str
        """
        self._path = path

    @property
    def method(self):
        """Gets the method of this UpdateLiveDataApiV2Response.

        后端API请求方法。  支持GET、PUT、POST、DELETE  更新后端API时，status=4为后端API的已部署状态，该状态下后端API请求方法不能修改。

        :return: The method of this UpdateLiveDataApiV2Response.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this UpdateLiveDataApiV2Response.

        后端API请求方法。  支持GET、PUT、POST、DELETE  更新后端API时，status=4为后端API的已部署状态，该状态下后端API请求方法不能修改。

        :param method: The method of this UpdateLiveDataApiV2Response.
        :type method: str
        """
        self._method = method

    @property
    def description(self):
        """Gets the description of this UpdateLiveDataApiV2Response.

        后端API描述。  不支持<，>字符

        :return: The description of this UpdateLiveDataApiV2Response.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateLiveDataApiV2Response.

        后端API描述。  不支持<，>字符

        :param description: The description of this UpdateLiveDataApiV2Response.
        :type description: str
        """
        self._description = description

    @property
    def version(self):
        """Gets the version of this UpdateLiveDataApiV2Response.

        后端API版本  支持英文，数字，下划线，中划线，点。

        :return: The version of this UpdateLiveDataApiV2Response.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpdateLiveDataApiV2Response.

        后端API版本  支持英文，数字，下划线，中划线，点。

        :param version: The version of this UpdateLiveDataApiV2Response.
        :type version: str
        """
        self._version = version

    @property
    def content_type(self):
        """Gets the content_type of this UpdateLiveDataApiV2Response.

        后端API返回类型

        :return: The content_type of this UpdateLiveDataApiV2Response.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this UpdateLiveDataApiV2Response.

        后端API返回类型

        :param content_type: The content_type of this UpdateLiveDataApiV2Response.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def api_signature_id(self):
        """Gets the api_signature_id of this UpdateLiveDataApiV2Response.

        后端API为签名认证时绑定的签名密钥编号

        :return: The api_signature_id of this UpdateLiveDataApiV2Response.
        :rtype: str
        """
        return self._api_signature_id

    @api_signature_id.setter
    def api_signature_id(self, api_signature_id):
        """Sets the api_signature_id of this UpdateLiveDataApiV2Response.

        后端API为签名认证时绑定的签名密钥编号

        :param api_signature_id: The api_signature_id of this UpdateLiveDataApiV2Response.
        :type api_signature_id: str
        """
        self._api_signature_id = api_signature_id

    @property
    def roma_app_id(self):
        """Gets the roma_app_id of this UpdateLiveDataApiV2Response.

        后端API归属的集成应用编号  更新后端API时，status=4为后端API的已部署状态，该状态下后端API归属的集成应用编号不能修改。

        :return: The roma_app_id of this UpdateLiveDataApiV2Response.
        :rtype: str
        """
        return self._roma_app_id

    @roma_app_id.setter
    def roma_app_id(self, roma_app_id):
        """Sets the roma_app_id of this UpdateLiveDataApiV2Response.

        后端API归属的集成应用编号  更新后端API时，status=4为后端API的已部署状态，该状态下后端API归属的集成应用编号不能修改。

        :param roma_app_id: The roma_app_id of this UpdateLiveDataApiV2Response.
        :type roma_app_id: str
        """
        self._roma_app_id = roma_app_id

    @property
    def return_format(self):
        """Gets the return_format of this UpdateLiveDataApiV2Response.

        API响应信息是否格式化  true： 对响应信息进行格式化  false：对响应信息格式化不进行格式化 

        :return: The return_format of this UpdateLiveDataApiV2Response.
        :rtype: bool
        """
        return self._return_format

    @return_format.setter
    def return_format(self, return_format):
        """Sets the return_format of this UpdateLiveDataApiV2Response.

        API响应信息是否格式化  true： 对响应信息进行格式化  false：对响应信息格式化不进行格式化 

        :param return_format: The return_format of this UpdateLiveDataApiV2Response.
        :type return_format: bool
        """
        self._return_format = return_format

    @property
    def parameters(self):
        """Gets the parameters of this UpdateLiveDataApiV2Response.

        后端API的请求参数列表

        :return: The parameters of this UpdateLiveDataApiV2Response.
        :rtype: list[:class:`huaweicloudsdkroma.v2.LdApiParameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this UpdateLiveDataApiV2Response.

        后端API的请求参数列表

        :param parameters: The parameters of this UpdateLiveDataApiV2Response.
        :type parameters: list[:class:`huaweicloudsdkroma.v2.LdApiParameter`]
        """
        self._parameters = parameters

    @property
    def id(self):
        """Gets the id of this UpdateLiveDataApiV2Response.

        后端API编号

        :return: The id of this UpdateLiveDataApiV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateLiveDataApiV2Response.

        后端API编号

        :param id: The id of this UpdateLiveDataApiV2Response.
        :type id: str
        """
        self._id = id

    @property
    def instance(self):
        """Gets the instance of this UpdateLiveDataApiV2Response.

        后端API所属实例编号

        :return: The instance of this UpdateLiveDataApiV2Response.
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this UpdateLiveDataApiV2Response.

        后端API所属实例编号

        :param instance: The instance of this UpdateLiveDataApiV2Response.
        :type instance: str
        """
        self._instance = instance

    @property
    def type(self):
        """Gets the type of this UpdateLiveDataApiV2Response.

        后端API类型： - data：数据后端 - function： 函数后端

        :return: The type of this UpdateLiveDataApiV2Response.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateLiveDataApiV2Response.

        后端API类型： - data：数据后端 - function： 函数后端

        :param type: The type of this UpdateLiveDataApiV2Response.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this UpdateLiveDataApiV2Response.

        后端API状态： - 1：待开发 - 3：开发中 - 4：已部署

        :return: The status of this UpdateLiveDataApiV2Response.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateLiveDataApiV2Response.

        后端API状态： - 1：待开发 - 3：开发中 - 4：已部署

        :param status: The status of this UpdateLiveDataApiV2Response.
        :type status: int
        """
        self._status = status

    @property
    def created_time(self):
        """Gets the created_time of this UpdateLiveDataApiV2Response.

        后端API创建时间

        :return: The created_time of this UpdateLiveDataApiV2Response.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this UpdateLiveDataApiV2Response.

        后端API创建时间

        :param created_time: The created_time of this UpdateLiveDataApiV2Response.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        """Gets the modified_time of this UpdateLiveDataApiV2Response.

        后端API修改时间

        :return: The modified_time of this UpdateLiveDataApiV2Response.
        :rtype: datetime
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        """Sets the modified_time of this UpdateLiveDataApiV2Response.

        后端API修改时间

        :param modified_time: The modified_time of this UpdateLiveDataApiV2Response.
        :type modified_time: datetime
        """
        self._modified_time = modified_time

    @property
    def scripts(self):
        """Gets the scripts of this UpdateLiveDataApiV2Response.

        后端API脚本信息

        :return: The scripts of this UpdateLiveDataApiV2Response.
        :rtype: list[:class:`huaweicloudsdkroma.v2.LdApiScript`]
        """
        return self._scripts

    @scripts.setter
    def scripts(self, scripts):
        """Sets the scripts of this UpdateLiveDataApiV2Response.

        后端API脚本信息

        :param scripts: The scripts of this UpdateLiveDataApiV2Response.
        :type scripts: list[:class:`huaweicloudsdkroma.v2.LdApiScript`]
        """
        self._scripts = scripts

    @property
    def roma_app_name(self):
        """Gets the roma_app_name of this UpdateLiveDataApiV2Response.

        后端API归属的集成应用名称

        :return: The roma_app_name of this UpdateLiveDataApiV2Response.
        :rtype: str
        """
        return self._roma_app_name

    @roma_app_name.setter
    def roma_app_name(self, roma_app_name):
        """Sets the roma_app_name of this UpdateLiveDataApiV2Response.

        后端API归属的集成应用名称

        :param roma_app_name: The roma_app_name of this UpdateLiveDataApiV2Response.
        :type roma_app_name: str
        """
        self._roma_app_name = roma_app_name

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
        if not isinstance(other, UpdateLiveDataApiV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
