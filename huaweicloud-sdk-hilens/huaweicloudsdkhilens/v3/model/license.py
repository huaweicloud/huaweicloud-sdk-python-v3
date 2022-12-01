# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class License:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'channel_limit': 'int',
        'charging_model': 'int',
        'cloud_service_type': 'str',
        'hilens_resource_spec_code': 'str',
        'measure_type': 'str',
        'measure_unit': 'str',
        'offline_flag': 'int',
        'order_limit': 'int',
        'product_info': 'list[ProductInfo]',
        'resource_spec_code': 'str',
        'resource_step_size': 'int',
        'resource_type': 'str',
        'validity': 'int'
    }

    attribute_map = {
        'channel_limit': 'channel_limit',
        'charging_model': 'charging_model',
        'cloud_service_type': 'cloud_service_type',
        'hilens_resource_spec_code': 'hilens_resource_spec_code',
        'measure_type': 'measure_type',
        'measure_unit': 'measure_unit',
        'offline_flag': 'offline_flag',
        'order_limit': 'order_limit',
        'product_info': 'product_info',
        'resource_spec_code': 'resource_spec_code',
        'resource_step_size': 'resource_step_size',
        'resource_type': 'resource_type',
        'validity': 'validity'
    }

    def __init__(self, channel_limit=None, charging_model=None, cloud_service_type=None, hilens_resource_spec_code=None, measure_type=None, measure_unit=None, offline_flag=None, order_limit=None, product_info=None, resource_spec_code=None, resource_step_size=None, resource_type=None, validity=None):
        """License

        The model defined in huaweicloud sdk

        :param channel_limit: 
        :type channel_limit: int
        :param charging_model: 
        :type charging_model: int
        :param cloud_service_type: 
        :type cloud_service_type: str
        :param hilens_resource_spec_code: 
        :type hilens_resource_spec_code: str
        :param measure_type: 
        :type measure_type: str
        :param measure_unit: 
        :type measure_unit: str
        :param offline_flag: 
        :type offline_flag: int
        :param order_limit: 
        :type order_limit: int
        :param product_info: 
        :type product_info: list[:class:`huaweicloudsdkhilens.v3.ProductInfo`]
        :param resource_spec_code: 
        :type resource_spec_code: str
        :param resource_step_size: 
        :type resource_step_size: int
        :param resource_type: 
        :type resource_type: str
        :param validity: 
        :type validity: int
        """
        
        

        self._channel_limit = None
        self._charging_model = None
        self._cloud_service_type = None
        self._hilens_resource_spec_code = None
        self._measure_type = None
        self._measure_unit = None
        self._offline_flag = None
        self._order_limit = None
        self._product_info = None
        self._resource_spec_code = None
        self._resource_step_size = None
        self._resource_type = None
        self._validity = None
        self.discriminator = None

        if channel_limit is not None:
            self.channel_limit = channel_limit
        if charging_model is not None:
            self.charging_model = charging_model
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if hilens_resource_spec_code is not None:
            self.hilens_resource_spec_code = hilens_resource_spec_code
        if measure_type is not None:
            self.measure_type = measure_type
        if measure_unit is not None:
            self.measure_unit = measure_unit
        if offline_flag is not None:
            self.offline_flag = offline_flag
        if order_limit is not None:
            self.order_limit = order_limit
        if product_info is not None:
            self.product_info = product_info
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if resource_step_size is not None:
            self.resource_step_size = resource_step_size
        if resource_type is not None:
            self.resource_type = resource_type
        if validity is not None:
            self.validity = validity

    @property
    def channel_limit(self):
        """Gets the channel_limit of this License.

        :return: The channel_limit of this License.
        :rtype: int
        """
        return self._channel_limit

    @channel_limit.setter
    def channel_limit(self, channel_limit):
        """Sets the channel_limit of this License.

        :param channel_limit: The channel_limit of this License.
        :type channel_limit: int
        """
        self._channel_limit = channel_limit

    @property
    def charging_model(self):
        """Gets the charging_model of this License.

        :return: The charging_model of this License.
        :rtype: int
        """
        return self._charging_model

    @charging_model.setter
    def charging_model(self, charging_model):
        """Sets the charging_model of this License.

        :param charging_model: The charging_model of this License.
        :type charging_model: int
        """
        self._charging_model = charging_model

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this License.

        :return: The cloud_service_type of this License.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this License.

        :param cloud_service_type: The cloud_service_type of this License.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def hilens_resource_spec_code(self):
        """Gets the hilens_resource_spec_code of this License.

        :return: The hilens_resource_spec_code of this License.
        :rtype: str
        """
        return self._hilens_resource_spec_code

    @hilens_resource_spec_code.setter
    def hilens_resource_spec_code(self, hilens_resource_spec_code):
        """Sets the hilens_resource_spec_code of this License.

        :param hilens_resource_spec_code: The hilens_resource_spec_code of this License.
        :type hilens_resource_spec_code: str
        """
        self._hilens_resource_spec_code = hilens_resource_spec_code

    @property
    def measure_type(self):
        """Gets the measure_type of this License.

        :return: The measure_type of this License.
        :rtype: str
        """
        return self._measure_type

    @measure_type.setter
    def measure_type(self, measure_type):
        """Sets the measure_type of this License.

        :param measure_type: The measure_type of this License.
        :type measure_type: str
        """
        self._measure_type = measure_type

    @property
    def measure_unit(self):
        """Gets the measure_unit of this License.

        :return: The measure_unit of this License.
        :rtype: str
        """
        return self._measure_unit

    @measure_unit.setter
    def measure_unit(self, measure_unit):
        """Sets the measure_unit of this License.

        :param measure_unit: The measure_unit of this License.
        :type measure_unit: str
        """
        self._measure_unit = measure_unit

    @property
    def offline_flag(self):
        """Gets the offline_flag of this License.

        :return: The offline_flag of this License.
        :rtype: int
        """
        return self._offline_flag

    @offline_flag.setter
    def offline_flag(self, offline_flag):
        """Sets the offline_flag of this License.

        :param offline_flag: The offline_flag of this License.
        :type offline_flag: int
        """
        self._offline_flag = offline_flag

    @property
    def order_limit(self):
        """Gets the order_limit of this License.

        :return: The order_limit of this License.
        :rtype: int
        """
        return self._order_limit

    @order_limit.setter
    def order_limit(self, order_limit):
        """Sets the order_limit of this License.

        :param order_limit: The order_limit of this License.
        :type order_limit: int
        """
        self._order_limit = order_limit

    @property
    def product_info(self):
        """Gets the product_info of this License.

        :return: The product_info of this License.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.ProductInfo`]
        """
        return self._product_info

    @product_info.setter
    def product_info(self, product_info):
        """Sets the product_info of this License.

        :param product_info: The product_info of this License.
        :type product_info: list[:class:`huaweicloudsdkhilens.v3.ProductInfo`]
        """
        self._product_info = product_info

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this License.

        :return: The resource_spec_code of this License.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this License.

        :param resource_spec_code: The resource_spec_code of this License.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def resource_step_size(self):
        """Gets the resource_step_size of this License.

        :return: The resource_step_size of this License.
        :rtype: int
        """
        return self._resource_step_size

    @resource_step_size.setter
    def resource_step_size(self, resource_step_size):
        """Sets the resource_step_size of this License.

        :param resource_step_size: The resource_step_size of this License.
        :type resource_step_size: int
        """
        self._resource_step_size = resource_step_size

    @property
    def resource_type(self):
        """Gets the resource_type of this License.

        :return: The resource_type of this License.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this License.

        :param resource_type: The resource_type of this License.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def validity(self):
        """Gets the validity of this License.

        :return: The validity of this License.
        :rtype: int
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this License.

        :param validity: The validity of this License.
        :type validity: int
        """
        self._validity = validity

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
        if not isinstance(other, License):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
