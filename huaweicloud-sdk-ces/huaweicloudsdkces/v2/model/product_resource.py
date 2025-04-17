# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_name': 'str',
        'namespace': 'str',
        'product_instances': 'list[ProductInstance]'
    }

    attribute_map = {
        'product_name': 'product_name',
        'namespace': 'namespace',
        'product_instances': 'product_instances'
    }

    def __init__(self, product_name=None, namespace=None, product_instances=None):
        r"""ProductResource

        The model defined in huaweicloud sdk

        :param product_name: 资源所属的云产品，一般由\&quot;服务命名空间,服务首层维度名称\&quot;组成，如\&quot;SYS.ECS,instance_id\&quot;
        :type product_name: str
        :param namespace: 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”
        :type namespace: str
        :param product_instances: 产品实例详情
        :type product_instances: list[:class:`huaweicloudsdkces.v2.ProductInstance`]
        """
        
        

        self._product_name = None
        self._namespace = None
        self._product_instances = None
        self.discriminator = None

        self.product_name = product_name
        self.namespace = namespace
        self.product_instances = product_instances

    @property
    def product_name(self):
        r"""Gets the product_name of this ProductResource.

        资源所属的云产品，一般由\"服务命名空间,服务首层维度名称\"组成，如\"SYS.ECS,instance_id\"

        :return: The product_name of this ProductResource.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this ProductResource.

        资源所属的云产品，一般由\"服务命名空间,服务首层维度名称\"组成，如\"SYS.ECS,instance_id\"

        :param product_name: The product_name of this ProductResource.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def namespace(self):
        r"""Gets the namespace of this ProductResource.

        查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”

        :return: The namespace of this ProductResource.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ProductResource.

        查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”

        :param namespace: The namespace of this ProductResource.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def product_instances(self):
        r"""Gets the product_instances of this ProductResource.

        产品实例详情

        :return: The product_instances of this ProductResource.
        :rtype: list[:class:`huaweicloudsdkces.v2.ProductInstance`]
        """
        return self._product_instances

    @product_instances.setter
    def product_instances(self, product_instances):
        r"""Sets the product_instances of this ProductResource.

        产品实例详情

        :param product_instances: The product_instances of this ProductResource.
        :type product_instances: list[:class:`huaweicloudsdkces.v2.ProductInstance`]
        """
        self._product_instances = product_instances

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
        if not isinstance(other, ProductResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
