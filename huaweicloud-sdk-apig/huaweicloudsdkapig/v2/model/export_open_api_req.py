# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportOpenApiReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'env_id': 'str',
        'group_id': 'str',
        'define': 'str',
        'type': 'str',
        'version': 'str',
        'apis': 'list[str]'
    }

    attribute_map = {
        'env_id': 'env_id',
        'group_id': 'group_id',
        'define': 'define',
        'type': 'type',
        'version': 'version',
        'apis': 'apis'
    }

    def __init__(self, env_id=None, group_id=None, define=None, type=None, version=None, apis=None):
        """ExportOpenApiReq

        The model defined in huaweicloud sdk

        :param env_id: API分组发布的环境ID
        :type env_id: str
        :param group_id: API分组ID
        :type group_id: str
        :param define: 导出API的定义范围： - spec：基础定义，只包括api前端定义 - proxy：全量定义，包括api前后端定义 - all：扩展定义，包括api前后端定义以及流控、访问控制、自定义认证等扩展定义 - dev：开发定义，包括未发布的api的前后端定义
        :type define: str
        :param type: 导出的API定义的格式
        :type type: str
        :param version: 导出的API定义版本，默认为当前时间
        :type version: str
        :param apis: 导出的API ID列表
        :type apis: list[str]
        """
        
        

        self._env_id = None
        self._group_id = None
        self._define = None
        self._type = None
        self._version = None
        self._apis = None
        self.discriminator = None

        self.env_id = env_id
        self.group_id = group_id
        if define is not None:
            self.define = define
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if apis is not None:
            self.apis = apis

    @property
    def env_id(self):
        """Gets the env_id of this ExportOpenApiReq.

        API分组发布的环境ID

        :return: The env_id of this ExportOpenApiReq.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this ExportOpenApiReq.

        API分组发布的环境ID

        :param env_id: The env_id of this ExportOpenApiReq.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def group_id(self):
        """Gets the group_id of this ExportOpenApiReq.

        API分组ID

        :return: The group_id of this ExportOpenApiReq.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ExportOpenApiReq.

        API分组ID

        :param group_id: The group_id of this ExportOpenApiReq.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def define(self):
        """Gets the define of this ExportOpenApiReq.

        导出API的定义范围： - spec：基础定义，只包括api前端定义 - proxy：全量定义，包括api前后端定义 - all：扩展定义，包括api前后端定义以及流控、访问控制、自定义认证等扩展定义 - dev：开发定义，包括未发布的api的前后端定义

        :return: The define of this ExportOpenApiReq.
        :rtype: str
        """
        return self._define

    @define.setter
    def define(self, define):
        """Sets the define of this ExportOpenApiReq.

        导出API的定义范围： - spec：基础定义，只包括api前端定义 - proxy：全量定义，包括api前后端定义 - all：扩展定义，包括api前后端定义以及流控、访问控制、自定义认证等扩展定义 - dev：开发定义，包括未发布的api的前后端定义

        :param define: The define of this ExportOpenApiReq.
        :type define: str
        """
        self._define = define

    @property
    def type(self):
        """Gets the type of this ExportOpenApiReq.

        导出的API定义的格式

        :return: The type of this ExportOpenApiReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExportOpenApiReq.

        导出的API定义的格式

        :param type: The type of this ExportOpenApiReq.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this ExportOpenApiReq.

        导出的API定义版本，默认为当前时间

        :return: The version of this ExportOpenApiReq.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ExportOpenApiReq.

        导出的API定义版本，默认为当前时间

        :param version: The version of this ExportOpenApiReq.
        :type version: str
        """
        self._version = version

    @property
    def apis(self):
        """Gets the apis of this ExportOpenApiReq.

        导出的API ID列表

        :return: The apis of this ExportOpenApiReq.
        :rtype: list[str]
        """
        return self._apis

    @apis.setter
    def apis(self, apis):
        """Sets the apis of this ExportOpenApiReq.

        导出的API ID列表

        :param apis: The apis of this ExportOpenApiReq.
        :type apis: list[str]
        """
        self._apis = apis

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
        if not isinstance(other, ExportOpenApiReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
