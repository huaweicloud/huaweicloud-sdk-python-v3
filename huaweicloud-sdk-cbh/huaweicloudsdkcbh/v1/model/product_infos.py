# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductInfos:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_id': 'str',
        'cloud_service_type': 'str',
        'resource_type': 'str',
        'resource_spec_code': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'resource_spec_code': 'resource_spec_code'
    }

    def __init__(self, product_id=None, cloud_service_type=None, resource_type=None, resource_spec_code=None):
        r"""ProductInfos

        The model defined in huaweicloud sdk

        :param product_id: 产品标识，通过订购询价接口获得。
        :type product_id: str
        :param cloud_service_type: 云服务类型，填写“hws.service.type.cbh”。
        :type cloud_service_type: str
        :param resource_type: 云堡垒机资源类型，填写“hws.resource.type.cbh.ins”。
        :type resource_type: str
        :param resource_spec_code: 待创建云堡垒机规格ID，例如： - cbh.basic.50 - cbh.enhance.50 已上线的规格请参见《云堡垒机产品介绍》的[服务版本差异](https://support.huaweicloud.com/productdesc-cbh/cbh_01_0010.html)章节。
        :type resource_spec_code: str
        """
        
        

        self._product_id = None
        self._cloud_service_type = None
        self._resource_type = None
        self._resource_spec_code = None
        self.discriminator = None

        self.product_id = product_id
        self.cloud_service_type = cloud_service_type
        self.resource_type = resource_type
        self.resource_spec_code = resource_spec_code

    @property
    def product_id(self):
        r"""Gets the product_id of this ProductInfos.

        产品标识，通过订购询价接口获得。

        :return: The product_id of this ProductInfos.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ProductInfos.

        产品标识，通过订购询价接口获得。

        :param product_id: The product_id of this ProductInfos.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this ProductInfos.

        云服务类型，填写“hws.service.type.cbh”。

        :return: The cloud_service_type of this ProductInfos.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this ProductInfos.

        云服务类型，填写“hws.service.type.cbh”。

        :param cloud_service_type: The cloud_service_type of this ProductInfos.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ProductInfos.

        云堡垒机资源类型，填写“hws.resource.type.cbh.ins”。

        :return: The resource_type of this ProductInfos.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ProductInfos.

        云堡垒机资源类型，填写“hws.resource.type.cbh.ins”。

        :param resource_type: The resource_type of this ProductInfos.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this ProductInfos.

        待创建云堡垒机规格ID，例如： - cbh.basic.50 - cbh.enhance.50 已上线的规格请参见《云堡垒机产品介绍》的[服务版本差异](https://support.huaweicloud.com/productdesc-cbh/cbh_01_0010.html)章节。

        :return: The resource_spec_code of this ProductInfos.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this ProductInfos.

        待创建云堡垒机规格ID，例如： - cbh.basic.50 - cbh.enhance.50 已上线的规格请参见《云堡垒机产品介绍》的[服务版本差异](https://support.huaweicloud.com/productdesc-cbh/cbh_01_0010.html)章节。

        :param resource_spec_code: The resource_spec_code of this ProductInfos.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

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
        if not isinstance(other, ProductInfos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
