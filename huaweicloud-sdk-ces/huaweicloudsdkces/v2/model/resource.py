# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Resource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'dimensions': 'list[ResourceDimension]'
    }

    attribute_map = {
        'namespace': 'namespace',
        'dimensions': 'dimensions'
    }

    def __init__(self, namespace=None, dimensions=None):
        r"""Resource

        The model defined in huaweicloud sdk

        :param namespace: 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”
        :type namespace: str
        :param dimensions: 资源的维度信息
        :type dimensions: list[:class:`huaweicloudsdkces.v2.ResourceDimension`]
        """
        
        

        self._namespace = None
        self._dimensions = None
        self.discriminator = None

        self.namespace = namespace
        self.dimensions = dimensions

    @property
    def namespace(self):
        r"""Gets the namespace of this Resource.

        查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”

        :return: The namespace of this Resource.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this Resource.

        查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”

        :param namespace: The namespace of this Resource.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimensions(self):
        r"""Gets the dimensions of this Resource.

        资源的维度信息

        :return: The dimensions of this Resource.
        :rtype: list[:class:`huaweicloudsdkces.v2.ResourceDimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this Resource.

        资源的维度信息

        :param dimensions: The dimensions of this Resource.
        :type dimensions: list[:class:`huaweicloudsdkces.v2.ResourceDimension`]
        """
        self._dimensions = dimensions

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
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
