# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourcesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resources': 'list[Resource]',
        'product_resources': 'list[ProductResource]'
    }

    attribute_map = {
        'resources': 'resources',
        'product_resources': 'product_resources'
    }

    def __init__(self, resources=None, product_resources=None):
        r"""ResourcesReq

        The model defined in huaweicloud sdk

        :param resources: 资源信息
        :type resources: list[:class:`huaweicloudsdkces.v2.Resource`]
        :param product_resources: 手动创建，选择资源层级为云产品时的资源详情
        :type product_resources: list[:class:`huaweicloudsdkces.v2.ProductResource`]
        """
        
        

        self._resources = None
        self._product_resources = None
        self.discriminator = None

        if resources is not None:
            self.resources = resources
        if product_resources is not None:
            self.product_resources = product_resources

    @property
    def resources(self):
        r"""Gets the resources of this ResourcesReq.

        资源信息

        :return: The resources of this ResourcesReq.
        :rtype: list[:class:`huaweicloudsdkces.v2.Resource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ResourcesReq.

        资源信息

        :param resources: The resources of this ResourcesReq.
        :type resources: list[:class:`huaweicloudsdkces.v2.Resource`]
        """
        self._resources = resources

    @property
    def product_resources(self):
        r"""Gets the product_resources of this ResourcesReq.

        手动创建，选择资源层级为云产品时的资源详情

        :return: The product_resources of this ResourcesReq.
        :rtype: list[:class:`huaweicloudsdkces.v2.ProductResource`]
        """
        return self._product_resources

    @product_resources.setter
    def product_resources(self, product_resources):
        r"""Sets the product_resources of this ResourcesReq.

        手动创建，选择资源层级为云产品时的资源详情

        :param product_resources: The product_resources of this ResourcesReq.
        :type product_resources: list[:class:`huaweicloudsdkces.v2.ProductResource`]
        """
        self._product_resources = product_resources

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
        if not isinstance(other, ResourcesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
