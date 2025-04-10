# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductObject:

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
        'product_spec_desc': 'str',
        'category_code': 'str',
        'product_owner_service': 'str',
        'commercial_resource': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'product_spec_desc': 'product_spec_desc',
        'category_code': 'category_code',
        'product_owner_service': 'product_owner_service',
        'commercial_resource': 'commercial_resource'
    }

    def __init__(self, product_id=None, product_spec_desc=None, category_code=None, product_owner_service=None, commercial_resource=None):
        r"""ProductObject

        The model defined in huaweicloud sdk

        :param product_id: 产品ID。
        :type product_id: str
        :param product_spec_desc: 产品规格描述。
        :type product_spec_desc: str
        :param category_code: 产品目录编码。
        :type category_code: str
        :param product_owner_service: 产品归属的云服务类型编码。
        :type product_owner_service: str
        :param commercial_resource: 商务归属的资源类型编码。
        :type commercial_resource: str
        """
        
        

        self._product_id = None
        self._product_spec_desc = None
        self._category_code = None
        self._product_owner_service = None
        self._commercial_resource = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if product_spec_desc is not None:
            self.product_spec_desc = product_spec_desc
        if category_code is not None:
            self.category_code = category_code
        if product_owner_service is not None:
            self.product_owner_service = product_owner_service
        if commercial_resource is not None:
            self.commercial_resource = commercial_resource

    @property
    def product_id(self):
        r"""Gets the product_id of this ProductObject.

        产品ID。

        :return: The product_id of this ProductObject.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ProductObject.

        产品ID。

        :param product_id: The product_id of this ProductObject.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def product_spec_desc(self):
        r"""Gets the product_spec_desc of this ProductObject.

        产品规格描述。

        :return: The product_spec_desc of this ProductObject.
        :rtype: str
        """
        return self._product_spec_desc

    @product_spec_desc.setter
    def product_spec_desc(self, product_spec_desc):
        r"""Sets the product_spec_desc of this ProductObject.

        产品规格描述。

        :param product_spec_desc: The product_spec_desc of this ProductObject.
        :type product_spec_desc: str
        """
        self._product_spec_desc = product_spec_desc

    @property
    def category_code(self):
        r"""Gets the category_code of this ProductObject.

        产品目录编码。

        :return: The category_code of this ProductObject.
        :rtype: str
        """
        return self._category_code

    @category_code.setter
    def category_code(self, category_code):
        r"""Sets the category_code of this ProductObject.

        产品目录编码。

        :param category_code: The category_code of this ProductObject.
        :type category_code: str
        """
        self._category_code = category_code

    @property
    def product_owner_service(self):
        r"""Gets the product_owner_service of this ProductObject.

        产品归属的云服务类型编码。

        :return: The product_owner_service of this ProductObject.
        :rtype: str
        """
        return self._product_owner_service

    @product_owner_service.setter
    def product_owner_service(self, product_owner_service):
        r"""Sets the product_owner_service of this ProductObject.

        产品归属的云服务类型编码。

        :param product_owner_service: The product_owner_service of this ProductObject.
        :type product_owner_service: str
        """
        self._product_owner_service = product_owner_service

    @property
    def commercial_resource(self):
        r"""Gets the commercial_resource of this ProductObject.

        商务归属的资源类型编码。

        :return: The commercial_resource of this ProductObject.
        :rtype: str
        """
        return self._commercial_resource

    @commercial_resource.setter
    def commercial_resource(self, commercial_resource):
        r"""Sets the commercial_resource of this ProductObject.

        商务归属的资源类型编码。

        :param commercial_resource: The commercial_resource of this ProductObject.
        :type commercial_resource: str
        """
        self._commercial_resource = commercial_resource

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
        if not isinstance(other, ProductObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
