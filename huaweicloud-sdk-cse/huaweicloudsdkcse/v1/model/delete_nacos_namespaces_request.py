# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteNacosNamespacesRequest:

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
        'namespace_id': 'str'
    }

    attribute_map = {
        'x_engine_id': 'x-engine-id',
        'x_enterprise_project_id': 'X-Enterprise-Project-ID',
        'namespace_id': 'namespaceId'
    }

    def __init__(self, x_engine_id=None, x_enterprise_project_id=None, namespace_id=None):
        r"""DeleteNacosNamespacesRequest

        The model defined in huaweicloud sdk

        :param x_engine_id: 微服务引擎的实例ID
        :type x_engine_id: str
        :param x_enterprise_project_id: 企业项目ID
        :type x_enterprise_project_id: str
        :param namespace_id: 命名空间ID
        :type namespace_id: str
        """
        
        

        self._x_engine_id = None
        self._x_enterprise_project_id = None
        self._namespace_id = None
        self.discriminator = None

        self.x_engine_id = x_engine_id
        self.x_enterprise_project_id = x_enterprise_project_id
        self.namespace_id = namespace_id

    @property
    def x_engine_id(self):
        r"""Gets the x_engine_id of this DeleteNacosNamespacesRequest.

        微服务引擎的实例ID

        :return: The x_engine_id of this DeleteNacosNamespacesRequest.
        :rtype: str
        """
        return self._x_engine_id

    @x_engine_id.setter
    def x_engine_id(self, x_engine_id):
        r"""Sets the x_engine_id of this DeleteNacosNamespacesRequest.

        微服务引擎的实例ID

        :param x_engine_id: The x_engine_id of this DeleteNacosNamespacesRequest.
        :type x_engine_id: str
        """
        self._x_engine_id = x_engine_id

    @property
    def x_enterprise_project_id(self):
        r"""Gets the x_enterprise_project_id of this DeleteNacosNamespacesRequest.

        企业项目ID

        :return: The x_enterprise_project_id of this DeleteNacosNamespacesRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        r"""Sets the x_enterprise_project_id of this DeleteNacosNamespacesRequest.

        企业项目ID

        :param x_enterprise_project_id: The x_enterprise_project_id of this DeleteNacosNamespacesRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

    @property
    def namespace_id(self):
        r"""Gets the namespace_id of this DeleteNacosNamespacesRequest.

        命名空间ID

        :return: The namespace_id of this DeleteNacosNamespacesRequest.
        :rtype: str
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        r"""Sets the namespace_id of this DeleteNacosNamespacesRequest.

        命名空间ID

        :param namespace_id: The namespace_id of this DeleteNacosNamespacesRequest.
        :type namespace_id: str
        """
        self._namespace_id = namespace_id

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
        if not isinstance(other, DeleteNacosNamespacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
