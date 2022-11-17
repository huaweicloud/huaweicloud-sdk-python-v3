# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetChargeModesBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'charge_mode': 'str',
        'product_type': 'str',
        'service_area': 'str'
    }

    attribute_map = {
        'charge_mode': 'charge_mode',
        'product_type': 'product_type',
        'service_area': 'service_area'
    }

    def __init__(self, charge_mode=None, product_type=None, service_area=None):
        """SetChargeModesBody

        The model defined in huaweicloud sdk

        :param charge_mode: 计费模式，支持flux（流量），bw（带宽）
        :type charge_mode: str
        :param product_type: 产品模式，仅支持base（基础加速）
        :type product_type: str
        :param service_area: 服务区域，仅支持mainland_china（国内）
        :type service_area: str
        """
        
        

        self._charge_mode = None
        self._product_type = None
        self._service_area = None
        self.discriminator = None

        self.charge_mode = charge_mode
        self.product_type = product_type
        self.service_area = service_area

    @property
    def charge_mode(self):
        """Gets the charge_mode of this SetChargeModesBody.

        计费模式，支持flux（流量），bw（带宽）

        :return: The charge_mode of this SetChargeModesBody.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this SetChargeModesBody.

        计费模式，支持flux（流量），bw（带宽）

        :param charge_mode: The charge_mode of this SetChargeModesBody.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def product_type(self):
        """Gets the product_type of this SetChargeModesBody.

        产品模式，仅支持base（基础加速）

        :return: The product_type of this SetChargeModesBody.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this SetChargeModesBody.

        产品模式，仅支持base（基础加速）

        :param product_type: The product_type of this SetChargeModesBody.
        :type product_type: str
        """
        self._product_type = product_type

    @property
    def service_area(self):
        """Gets the service_area of this SetChargeModesBody.

        服务区域，仅支持mainland_china（国内）

        :return: The service_area of this SetChargeModesBody.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this SetChargeModesBody.

        服务区域，仅支持mainland_china（国内）

        :param service_area: The service_area of this SetChargeModesBody.
        :type service_area: str
        """
        self._service_area = service_area

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
        if not isinstance(other, SetChargeModesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
