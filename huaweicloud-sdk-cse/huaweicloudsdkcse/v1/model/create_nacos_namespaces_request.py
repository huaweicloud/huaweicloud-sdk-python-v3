# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNacosNamespacesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_engine_id': 'str',
        'x_enterprise_project_id': 'str',
        'custom_namespace_id': 'str',
        'namespace_name': 'str',
        'namespace_desc': 'str'
    }

    attribute_map = {
        'x_engine_id': 'x-engine-id',
        'x_enterprise_project_id': 'X-Enterprise-Project-ID',
        'custom_namespace_id': 'custom_namespace_id',
        'namespace_name': 'namespace_name',
        'namespace_desc': 'namespace_desc'
    }

    def __init__(self, x_engine_id=None, x_enterprise_project_id=None, custom_namespace_id=None, namespace_name=None, namespace_desc=None):
        """CreateNacosNamespacesRequest

        The model defined in huaweicloud sdk

        :param x_engine_id: 微服务引擎专享版的实例ID
        :type x_engine_id: str
        :param x_enterprise_project_id: 企业项目ID
        :type x_enterprise_project_id: str
        :param custom_namespace_id: 命名空间ID，仅支持大小写字母、数字、短划线（-）和下划线（_），不超过128个字符。
        :type custom_namespace_id: str
        :param namespace_name: 命名空间名，支持非@、#、$、%、^、&amp;、*，不超过128个字符。
        :type namespace_name: str
        :param namespace_desc: 命名空间描述，不超过256个字符。
        :type namespace_desc: str
        """
        
        

        self._x_engine_id = None
        self._x_enterprise_project_id = None
        self._custom_namespace_id = None
        self._namespace_name = None
        self._namespace_desc = None
        self.discriminator = None

        self.x_engine_id = x_engine_id
        self.x_enterprise_project_id = x_enterprise_project_id
        self.custom_namespace_id = custom_namespace_id
        self.namespace_name = namespace_name
        if namespace_desc is not None:
            self.namespace_desc = namespace_desc

    @property
    def x_engine_id(self):
        """Gets the x_engine_id of this CreateNacosNamespacesRequest.

        微服务引擎专享版的实例ID

        :return: The x_engine_id of this CreateNacosNamespacesRequest.
        :rtype: str
        """
        return self._x_engine_id

    @x_engine_id.setter
    def x_engine_id(self, x_engine_id):
        """Sets the x_engine_id of this CreateNacosNamespacesRequest.

        微服务引擎专享版的实例ID

        :param x_engine_id: The x_engine_id of this CreateNacosNamespacesRequest.
        :type x_engine_id: str
        """
        self._x_engine_id = x_engine_id

    @property
    def x_enterprise_project_id(self):
        """Gets the x_enterprise_project_id of this CreateNacosNamespacesRequest.

        企业项目ID

        :return: The x_enterprise_project_id of this CreateNacosNamespacesRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        """Sets the x_enterprise_project_id of this CreateNacosNamespacesRequest.

        企业项目ID

        :param x_enterprise_project_id: The x_enterprise_project_id of this CreateNacosNamespacesRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

    @property
    def custom_namespace_id(self):
        """Gets the custom_namespace_id of this CreateNacosNamespacesRequest.

        命名空间ID，仅支持大小写字母、数字、短划线（-）和下划线（_），不超过128个字符。

        :return: The custom_namespace_id of this CreateNacosNamespacesRequest.
        :rtype: str
        """
        return self._custom_namespace_id

    @custom_namespace_id.setter
    def custom_namespace_id(self, custom_namespace_id):
        """Sets the custom_namespace_id of this CreateNacosNamespacesRequest.

        命名空间ID，仅支持大小写字母、数字、短划线（-）和下划线（_），不超过128个字符。

        :param custom_namespace_id: The custom_namespace_id of this CreateNacosNamespacesRequest.
        :type custom_namespace_id: str
        """
        self._custom_namespace_id = custom_namespace_id

    @property
    def namespace_name(self):
        """Gets the namespace_name of this CreateNacosNamespacesRequest.

        命名空间名，支持非@、#、$、%、^、&、*，不超过128个字符。

        :return: The namespace_name of this CreateNacosNamespacesRequest.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """Sets the namespace_name of this CreateNacosNamespacesRequest.

        命名空间名，支持非@、#、$、%、^、&、*，不超过128个字符。

        :param namespace_name: The namespace_name of this CreateNacosNamespacesRequest.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def namespace_desc(self):
        """Gets the namespace_desc of this CreateNacosNamespacesRequest.

        命名空间描述，不超过256个字符。

        :return: The namespace_desc of this CreateNacosNamespacesRequest.
        :rtype: str
        """
        return self._namespace_desc

    @namespace_desc.setter
    def namespace_desc(self, namespace_desc):
        """Sets the namespace_desc of this CreateNacosNamespacesRequest.

        命名空间描述，不超过256个字符。

        :param namespace_desc: The namespace_desc of this CreateNacosNamespacesRequest.
        :type namespace_desc: str
        """
        self._namespace_desc = namespace_desc

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
        if not isinstance(other, CreateNacosNamespacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
