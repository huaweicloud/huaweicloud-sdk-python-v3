# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNacosNamespacesRequest:

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
        'namespace': 'str',
        'namespace_show_name': 'str',
        'namespace_desc': 'str'
    }

    attribute_map = {
        'x_engine_id': 'x-engine-id',
        'x_enterprise_project_id': 'X-Enterprise-Project-ID',
        'namespace': 'namespace',
        'namespace_show_name': 'namespaceShowName',
        'namespace_desc': 'namespaceDesc'
    }

    def __init__(self, x_engine_id=None, x_enterprise_project_id=None, namespace=None, namespace_show_name=None, namespace_desc=None):
        r"""UpdateNacosNamespacesRequest

        The model defined in huaweicloud sdk

        :param x_engine_id: 微服务引擎的实例ID
        :type x_engine_id: str
        :param x_enterprise_project_id: 企业项目ID
        :type x_enterprise_project_id: str
        :param namespace: 命名空间ID
        :type namespace: str
        :param namespace_show_name: 命名空间名，支持非@、#、$、%、^、&amp;、*，不超过128个字符。
        :type namespace_show_name: str
        :param namespace_desc: 命名空间描述，不超过256个字符。
        :type namespace_desc: str
        """
        
        

        self._x_engine_id = None
        self._x_enterprise_project_id = None
        self._namespace = None
        self._namespace_show_name = None
        self._namespace_desc = None
        self.discriminator = None

        self.x_engine_id = x_engine_id
        self.x_enterprise_project_id = x_enterprise_project_id
        self.namespace = namespace
        self.namespace_show_name = namespace_show_name
        self.namespace_desc = namespace_desc

    @property
    def x_engine_id(self):
        r"""Gets the x_engine_id of this UpdateNacosNamespacesRequest.

        微服务引擎的实例ID

        :return: The x_engine_id of this UpdateNacosNamespacesRequest.
        :rtype: str
        """
        return self._x_engine_id

    @x_engine_id.setter
    def x_engine_id(self, x_engine_id):
        r"""Sets the x_engine_id of this UpdateNacosNamespacesRequest.

        微服务引擎的实例ID

        :param x_engine_id: The x_engine_id of this UpdateNacosNamespacesRequest.
        :type x_engine_id: str
        """
        self._x_engine_id = x_engine_id

    @property
    def x_enterprise_project_id(self):
        r"""Gets the x_enterprise_project_id of this UpdateNacosNamespacesRequest.

        企业项目ID

        :return: The x_enterprise_project_id of this UpdateNacosNamespacesRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        r"""Sets the x_enterprise_project_id of this UpdateNacosNamespacesRequest.

        企业项目ID

        :param x_enterprise_project_id: The x_enterprise_project_id of this UpdateNacosNamespacesRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

    @property
    def namespace(self):
        r"""Gets the namespace of this UpdateNacosNamespacesRequest.

        命名空间ID

        :return: The namespace of this UpdateNacosNamespacesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this UpdateNacosNamespacesRequest.

        命名空间ID

        :param namespace: The namespace of this UpdateNacosNamespacesRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def namespace_show_name(self):
        r"""Gets the namespace_show_name of this UpdateNacosNamespacesRequest.

        命名空间名，支持非@、#、$、%、^、&、*，不超过128个字符。

        :return: The namespace_show_name of this UpdateNacosNamespacesRequest.
        :rtype: str
        """
        return self._namespace_show_name

    @namespace_show_name.setter
    def namespace_show_name(self, namespace_show_name):
        r"""Sets the namespace_show_name of this UpdateNacosNamespacesRequest.

        命名空间名，支持非@、#、$、%、^、&、*，不超过128个字符。

        :param namespace_show_name: The namespace_show_name of this UpdateNacosNamespacesRequest.
        :type namespace_show_name: str
        """
        self._namespace_show_name = namespace_show_name

    @property
    def namespace_desc(self):
        r"""Gets the namespace_desc of this UpdateNacosNamespacesRequest.

        命名空间描述，不超过256个字符。

        :return: The namespace_desc of this UpdateNacosNamespacesRequest.
        :rtype: str
        """
        return self._namespace_desc

    @namespace_desc.setter
    def namespace_desc(self, namespace_desc):
        r"""Sets the namespace_desc of this UpdateNacosNamespacesRequest.

        命名空间描述，不超过256个字符。

        :param namespace_desc: The namespace_desc of this UpdateNacosNamespacesRequest.
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
        if not isinstance(other, UpdateNacosNamespacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
