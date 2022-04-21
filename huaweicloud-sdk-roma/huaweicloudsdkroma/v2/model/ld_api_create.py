# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LdApiCreate:

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
        'parameters': 'list[LdApiParameter]'
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
        'parameters': 'parameters'
    }

    def __init__(self, name=None, path=None, method=None, description=None, version=None, content_type=None, api_signature_id=None, roma_app_id=None, return_format=None, parameters=None):
        """LdApiCreate

        The model defined in huaweicloud sdk

        :param name: 后端API名称。  支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头。
        :type name: str
        :param path: 后端API请求路径。  支持英文、数字、中划线、下划线、点等，且以斜杠（/）开头。
        :type path: str
        :param method: 后端API请求方法。  支持GET、PUT、POST、DELETE
        :type method: str
        :param description: 后端API描述。  不支持&lt;，&gt;字符
        :type description: str
        :param version: 后端API版本  支持英文，数字，下划线，中划线，点。
        :type version: str
        :param content_type: 后端API返回类型
        :type content_type: str
        :param api_signature_id: 后端API为签名认证时绑定的签名密钥编号
        :type api_signature_id: str
        :param roma_app_id: 后端API归属的集成应用编号
        :type roma_app_id: str
        :param return_format: API响应信息是否格式化  true： 对响应信息进行格式化  false：对响应信息格式化不进行格式化 
        :type return_format: bool
        :param parameters: 后端API的请求参数列表
        :type parameters: list[:class:`huaweicloudsdkroma.v2.LdApiParameter`]
        """
        
        

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

    @property
    def name(self):
        """Gets the name of this LdApiCreate.

        后端API名称。  支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头。

        :return: The name of this LdApiCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LdApiCreate.

        后端API名称。  支持汉字、英文、数字、中划线、下划线、点、斜杠、中英文格式下的小括号和冒号、中文格式下的顿号，且只能以英文、汉字和数字开头。

        :param name: The name of this LdApiCreate.
        :type name: str
        """
        self._name = name

    @property
    def path(self):
        """Gets the path of this LdApiCreate.

        后端API请求路径。  支持英文、数字、中划线、下划线、点等，且以斜杠（/）开头。

        :return: The path of this LdApiCreate.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this LdApiCreate.

        后端API请求路径。  支持英文、数字、中划线、下划线、点等，且以斜杠（/）开头。

        :param path: The path of this LdApiCreate.
        :type path: str
        """
        self._path = path

    @property
    def method(self):
        """Gets the method of this LdApiCreate.

        后端API请求方法。  支持GET、PUT、POST、DELETE

        :return: The method of this LdApiCreate.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this LdApiCreate.

        后端API请求方法。  支持GET、PUT、POST、DELETE

        :param method: The method of this LdApiCreate.
        :type method: str
        """
        self._method = method

    @property
    def description(self):
        """Gets the description of this LdApiCreate.

        后端API描述。  不支持<，>字符

        :return: The description of this LdApiCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LdApiCreate.

        后端API描述。  不支持<，>字符

        :param description: The description of this LdApiCreate.
        :type description: str
        """
        self._description = description

    @property
    def version(self):
        """Gets the version of this LdApiCreate.

        后端API版本  支持英文，数字，下划线，中划线，点。

        :return: The version of this LdApiCreate.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this LdApiCreate.

        后端API版本  支持英文，数字，下划线，中划线，点。

        :param version: The version of this LdApiCreate.
        :type version: str
        """
        self._version = version

    @property
    def content_type(self):
        """Gets the content_type of this LdApiCreate.

        后端API返回类型

        :return: The content_type of this LdApiCreate.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this LdApiCreate.

        后端API返回类型

        :param content_type: The content_type of this LdApiCreate.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def api_signature_id(self):
        """Gets the api_signature_id of this LdApiCreate.

        后端API为签名认证时绑定的签名密钥编号

        :return: The api_signature_id of this LdApiCreate.
        :rtype: str
        """
        return self._api_signature_id

    @api_signature_id.setter
    def api_signature_id(self, api_signature_id):
        """Sets the api_signature_id of this LdApiCreate.

        后端API为签名认证时绑定的签名密钥编号

        :param api_signature_id: The api_signature_id of this LdApiCreate.
        :type api_signature_id: str
        """
        self._api_signature_id = api_signature_id

    @property
    def roma_app_id(self):
        """Gets the roma_app_id of this LdApiCreate.

        后端API归属的集成应用编号

        :return: The roma_app_id of this LdApiCreate.
        :rtype: str
        """
        return self._roma_app_id

    @roma_app_id.setter
    def roma_app_id(self, roma_app_id):
        """Sets the roma_app_id of this LdApiCreate.

        后端API归属的集成应用编号

        :param roma_app_id: The roma_app_id of this LdApiCreate.
        :type roma_app_id: str
        """
        self._roma_app_id = roma_app_id

    @property
    def return_format(self):
        """Gets the return_format of this LdApiCreate.

        API响应信息是否格式化  true： 对响应信息进行格式化  false：对响应信息格式化不进行格式化 

        :return: The return_format of this LdApiCreate.
        :rtype: bool
        """
        return self._return_format

    @return_format.setter
    def return_format(self, return_format):
        """Sets the return_format of this LdApiCreate.

        API响应信息是否格式化  true： 对响应信息进行格式化  false：对响应信息格式化不进行格式化 

        :param return_format: The return_format of this LdApiCreate.
        :type return_format: bool
        """
        self._return_format = return_format

    @property
    def parameters(self):
        """Gets the parameters of this LdApiCreate.

        后端API的请求参数列表

        :return: The parameters of this LdApiCreate.
        :rtype: list[:class:`huaweicloudsdkroma.v2.LdApiParameter`]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this LdApiCreate.

        后端API的请求参数列表

        :param parameters: The parameters of this LdApiCreate.
        :type parameters: list[:class:`huaweicloudsdkroma.v2.LdApiParameter`]
        """
        self._parameters = parameters

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
        if not isinstance(other, LdApiCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
