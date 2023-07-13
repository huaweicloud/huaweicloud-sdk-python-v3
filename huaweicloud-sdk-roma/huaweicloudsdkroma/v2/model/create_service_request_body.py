# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateServiceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_template_id': 'int',
        'product_id': 'int',
        'service_name': 'str',
        'description': 'str',
        'status': 'int'
    }

    attribute_map = {
        'product_template_id': 'product_template_id',
        'product_id': 'product_id',
        'service_name': 'service_name',
        'description': 'description',
        'status': 'status'
    }

    def __init__(self, product_template_id=None, product_id=None, service_name=None, description=None, status=None):
        """CreateServiceRequestBody

        The model defined in huaweicloud sdk

        :param product_template_id: 服务归属的产品模板ID，产品模板ID和产品ID二选一必填，自动向下取整
        :type product_template_id: int
        :param product_id: 服务归属的产品ID，产品模板ID和产品ID二选一必填，自动向下取整
        :type product_id: int
        :param service_name: 服务名称，支持中文,英文大小写，数字，下划线和中划线,长度2-64
        :type service_name: str
        :param description: 服务描述，长度0-200
        :type description: str
        :param status: 服务状态 0-启用 1-停用
        :type status: int
        """
        
        

        self._product_template_id = None
        self._product_id = None
        self._service_name = None
        self._description = None
        self._status = None
        self.discriminator = None

        if product_template_id is not None:
            self.product_template_id = product_template_id
        if product_id is not None:
            self.product_id = product_id
        self.service_name = service_name
        if description is not None:
            self.description = description
        self.status = status

    @property
    def product_template_id(self):
        """Gets the product_template_id of this CreateServiceRequestBody.

        服务归属的产品模板ID，产品模板ID和产品ID二选一必填，自动向下取整

        :return: The product_template_id of this CreateServiceRequestBody.
        :rtype: int
        """
        return self._product_template_id

    @product_template_id.setter
    def product_template_id(self, product_template_id):
        """Sets the product_template_id of this CreateServiceRequestBody.

        服务归属的产品模板ID，产品模板ID和产品ID二选一必填，自动向下取整

        :param product_template_id: The product_template_id of this CreateServiceRequestBody.
        :type product_template_id: int
        """
        self._product_template_id = product_template_id

    @property
    def product_id(self):
        """Gets the product_id of this CreateServiceRequestBody.

        服务归属的产品ID，产品模板ID和产品ID二选一必填，自动向下取整

        :return: The product_id of this CreateServiceRequestBody.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this CreateServiceRequestBody.

        服务归属的产品ID，产品模板ID和产品ID二选一必填，自动向下取整

        :param product_id: The product_id of this CreateServiceRequestBody.
        :type product_id: int
        """
        self._product_id = product_id

    @property
    def service_name(self):
        """Gets the service_name of this CreateServiceRequestBody.

        服务名称，支持中文,英文大小写，数字，下划线和中划线,长度2-64

        :return: The service_name of this CreateServiceRequestBody.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this CreateServiceRequestBody.

        服务名称，支持中文,英文大小写，数字，下划线和中划线,长度2-64

        :param service_name: The service_name of this CreateServiceRequestBody.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def description(self):
        """Gets the description of this CreateServiceRequestBody.

        服务描述，长度0-200

        :return: The description of this CreateServiceRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateServiceRequestBody.

        服务描述，长度0-200

        :param description: The description of this CreateServiceRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this CreateServiceRequestBody.

        服务状态 0-启用 1-停用

        :return: The status of this CreateServiceRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateServiceRequestBody.

        服务状态 0-启用 1-停用

        :param status: The status of this CreateServiceRequestBody.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, CreateServiceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
