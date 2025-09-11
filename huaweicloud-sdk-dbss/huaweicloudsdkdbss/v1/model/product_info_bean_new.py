# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductInfoBeanNew:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'all_resource_names': 'list[str]',
        'cloud_service_type': 'str',
        'display_id': 'str',
        'product_id': 'str',
        'product_spec_desc': 'str',
        'resource_name': 'str',
        'resource_spec_code': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'all_resource_names': 'all_resource_names',
        'cloud_service_type': 'cloud_service_type',
        'display_id': 'display_id',
        'product_id': 'product_id',
        'product_spec_desc': 'product_spec_desc',
        'resource_name': 'resource_name',
        'resource_spec_code': 'resource_spec_code',
        'resource_type': 'resource_type'
    }

    def __init__(self, all_resource_names=None, cloud_service_type=None, display_id=None, product_id=None, product_spec_desc=None, resource_name=None, resource_spec_code=None, resource_type=None):
        r"""ProductInfoBeanNew

        The model defined in huaweicloud sdk

        :param all_resource_names: 所有资源名称
        :type all_resource_names: list[str]
        :param cloud_service_type: 云服务类型
        :type cloud_service_type: str
        :param display_id: 显示ID
        :type display_id: str
        :param product_id: 产品ID
        :type product_id: str
        :param product_spec_desc: 产品规格描述
        :type product_spec_desc: str
        :param resource_name: 资源名称
        :type resource_name: str
        :param resource_spec_code: 资源规格
        :type resource_spec_code: str
        :param resource_type: 资源类型
        :type resource_type: str
        """
        
        

        self._all_resource_names = None
        self._cloud_service_type = None
        self._display_id = None
        self._product_id = None
        self._product_spec_desc = None
        self._resource_name = None
        self._resource_spec_code = None
        self._resource_type = None
        self.discriminator = None

        if all_resource_names is not None:
            self.all_resource_names = all_resource_names
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if display_id is not None:
            self.display_id = display_id
        if product_id is not None:
            self.product_id = product_id
        if product_spec_desc is not None:
            self.product_spec_desc = product_spec_desc
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def all_resource_names(self):
        r"""Gets the all_resource_names of this ProductInfoBeanNew.

        所有资源名称

        :return: The all_resource_names of this ProductInfoBeanNew.
        :rtype: list[str]
        """
        return self._all_resource_names

    @all_resource_names.setter
    def all_resource_names(self, all_resource_names):
        r"""Sets the all_resource_names of this ProductInfoBeanNew.

        所有资源名称

        :param all_resource_names: The all_resource_names of this ProductInfoBeanNew.
        :type all_resource_names: list[str]
        """
        self._all_resource_names = all_resource_names

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this ProductInfoBeanNew.

        云服务类型

        :return: The cloud_service_type of this ProductInfoBeanNew.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this ProductInfoBeanNew.

        云服务类型

        :param cloud_service_type: The cloud_service_type of this ProductInfoBeanNew.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def display_id(self):
        r"""Gets the display_id of this ProductInfoBeanNew.

        显示ID

        :return: The display_id of this ProductInfoBeanNew.
        :rtype: str
        """
        return self._display_id

    @display_id.setter
    def display_id(self, display_id):
        r"""Sets the display_id of this ProductInfoBeanNew.

        显示ID

        :param display_id: The display_id of this ProductInfoBeanNew.
        :type display_id: str
        """
        self._display_id = display_id

    @property
    def product_id(self):
        r"""Gets the product_id of this ProductInfoBeanNew.

        产品ID

        :return: The product_id of this ProductInfoBeanNew.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ProductInfoBeanNew.

        产品ID

        :param product_id: The product_id of this ProductInfoBeanNew.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def product_spec_desc(self):
        r"""Gets the product_spec_desc of this ProductInfoBeanNew.

        产品规格描述

        :return: The product_spec_desc of this ProductInfoBeanNew.
        :rtype: str
        """
        return self._product_spec_desc

    @product_spec_desc.setter
    def product_spec_desc(self, product_spec_desc):
        r"""Sets the product_spec_desc of this ProductInfoBeanNew.

        产品规格描述

        :param product_spec_desc: The product_spec_desc of this ProductInfoBeanNew.
        :type product_spec_desc: str
        """
        self._product_spec_desc = product_spec_desc

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ProductInfoBeanNew.

        资源名称

        :return: The resource_name of this ProductInfoBeanNew.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ProductInfoBeanNew.

        资源名称

        :param resource_name: The resource_name of this ProductInfoBeanNew.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this ProductInfoBeanNew.

        资源规格

        :return: The resource_spec_code of this ProductInfoBeanNew.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this ProductInfoBeanNew.

        资源规格

        :param resource_spec_code: The resource_spec_code of this ProductInfoBeanNew.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ProductInfoBeanNew.

        资源类型

        :return: The resource_type of this ProductInfoBeanNew.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ProductInfoBeanNew.

        资源类型

        :param resource_type: The resource_type of this ProductInfoBeanNew.
        :type resource_type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, ProductInfoBeanNew):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
