# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstancePeriodRequestProductInfos:

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
        'resource_spec_code': 'str',
        'product_spec_desc': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'cloud_service_type': 'cloud_service_type',
        'resource_type': 'resource_type',
        'resource_spec_code': 'resource_spec_code',
        'product_spec_desc': 'product_spec_desc'
    }

    def __init__(self, product_id=None, cloud_service_type=None, resource_type=None, resource_spec_code=None, product_spec_desc=None):
        """CreateInstancePeriodRequestProductInfos

        The model defined in huaweicloud sdk

        :param product_id: 产品ID
        :type product_id: str
        :param cloud_service_type: 服务类型： 默认hws.service.type.dbss
        :type cloud_service_type: str
        :param resource_type: 资源类型: 默认hws.resource.type.dbss
        :type resource_type: str
        :param resource_spec_code: 资源规格： dbss.bypassaudit.low、dbss.bypassaudit.medium、dbss.bypassaudit.high
        :type resource_spec_code: str
        :param product_spec_desc: 产品规格描述
        :type product_spec_desc: str
        """
        
        

        self._product_id = None
        self._cloud_service_type = None
        self._resource_type = None
        self._resource_spec_code = None
        self._product_spec_desc = None
        self.discriminator = None

        self.product_id = product_id
        self.cloud_service_type = cloud_service_type
        self.resource_type = resource_type
        self.resource_spec_code = resource_spec_code
        self.product_spec_desc = product_spec_desc

    @property
    def product_id(self):
        """Gets the product_id of this CreateInstancePeriodRequestProductInfos.

        产品ID

        :return: The product_id of this CreateInstancePeriodRequestProductInfos.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this CreateInstancePeriodRequestProductInfos.

        产品ID

        :param product_id: The product_id of this CreateInstancePeriodRequestProductInfos.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this CreateInstancePeriodRequestProductInfos.

        服务类型： 默认hws.service.type.dbss

        :return: The cloud_service_type of this CreateInstancePeriodRequestProductInfos.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this CreateInstancePeriodRequestProductInfos.

        服务类型： 默认hws.service.type.dbss

        :param cloud_service_type: The cloud_service_type of this CreateInstancePeriodRequestProductInfos.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        """Gets the resource_type of this CreateInstancePeriodRequestProductInfos.

        资源类型: 默认hws.resource.type.dbss

        :return: The resource_type of this CreateInstancePeriodRequestProductInfos.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this CreateInstancePeriodRequestProductInfos.

        资源类型: 默认hws.resource.type.dbss

        :param resource_type: The resource_type of this CreateInstancePeriodRequestProductInfos.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this CreateInstancePeriodRequestProductInfos.

        资源规格： dbss.bypassaudit.low、dbss.bypassaudit.medium、dbss.bypassaudit.high

        :return: The resource_spec_code of this CreateInstancePeriodRequestProductInfos.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this CreateInstancePeriodRequestProductInfos.

        资源规格： dbss.bypassaudit.low、dbss.bypassaudit.medium、dbss.bypassaudit.high

        :param resource_spec_code: The resource_spec_code of this CreateInstancePeriodRequestProductInfos.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def product_spec_desc(self):
        """Gets the product_spec_desc of this CreateInstancePeriodRequestProductInfos.

        产品规格描述

        :return: The product_spec_desc of this CreateInstancePeriodRequestProductInfos.
        :rtype: str
        """
        return self._product_spec_desc

    @product_spec_desc.setter
    def product_spec_desc(self, product_spec_desc):
        """Sets the product_spec_desc of this CreateInstancePeriodRequestProductInfos.

        产品规格描述

        :param product_spec_desc: The product_spec_desc of this CreateInstancePeriodRequestProductInfos.
        :type product_spec_desc: str
        """
        self._product_spec_desc = product_spec_desc

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
        if not isinstance(other, CreateInstancePeriodRequestProductInfos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
