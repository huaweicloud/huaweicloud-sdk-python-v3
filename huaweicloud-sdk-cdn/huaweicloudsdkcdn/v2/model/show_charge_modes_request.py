# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowChargeModesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'product_type': 'str',
        'status': 'str',
        'service_area': 'str'
    }

    attribute_map = {
        'product_type': 'product_type',
        'status': 'status',
        'service_area': 'service_area'
    }

    def __init__(self, product_type=None, status=None, service_area=None):
        """ShowChargeModesRequest

        The model defined in huaweicloud sdk

        :param product_type: 加速类型，base（基础加速）
        :type product_type: str
        :param status: 查询计费模式状态，active（已生效），upcoming（待生效），不传默认为active(已生效)
        :type status: str
        :param service_area: 服务区域，mainland_china（国内），outside_mainland_china（海外），不传默认为mainland_china(国内)
        :type service_area: str
        """
        
        

        self._product_type = None
        self._status = None
        self._service_area = None
        self.discriminator = None

        self.product_type = product_type
        if status is not None:
            self.status = status
        if service_area is not None:
            self.service_area = service_area

    @property
    def product_type(self):
        """Gets the product_type of this ShowChargeModesRequest.

        加速类型，base（基础加速）

        :return: The product_type of this ShowChargeModesRequest.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this ShowChargeModesRequest.

        加速类型，base（基础加速）

        :param product_type: The product_type of this ShowChargeModesRequest.
        :type product_type: str
        """
        self._product_type = product_type

    @property
    def status(self):
        """Gets the status of this ShowChargeModesRequest.

        查询计费模式状态，active（已生效），upcoming（待生效），不传默认为active(已生效)

        :return: The status of this ShowChargeModesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowChargeModesRequest.

        查询计费模式状态，active（已生效），upcoming（待生效），不传默认为active(已生效)

        :param status: The status of this ShowChargeModesRequest.
        :type status: str
        """
        self._status = status

    @property
    def service_area(self):
        """Gets the service_area of this ShowChargeModesRequest.

        服务区域，mainland_china（国内），outside_mainland_china（海外），不传默认为mainland_china(国内)

        :return: The service_area of this ShowChargeModesRequest.
        :rtype: str
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this ShowChargeModesRequest.

        服务区域，mainland_china（国内），outside_mainland_china（海外），不传默认为mainland_china(国内)

        :param service_area: The service_area of this ShowChargeModesRequest.
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
        if not isinstance(other, ShowChargeModesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
