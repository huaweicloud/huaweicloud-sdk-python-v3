# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PartnersServiceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_id': 'str',
        'customer_name': 'str',
        'service_time_zone': 'str',
        'service_time_day': 'str',
        'service_time_hour': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'customer_name': 'customer_name',
        'service_time_zone': 'service_time_zone',
        'service_time_day': 'service_time_day',
        'service_time_hour': 'service_time_hour'
    }

    def __init__(self, customer_id=None, customer_name=None, service_time_zone=None, service_time_day=None, service_time_hour=None):
        """PartnersServiceInfo

        The model defined in huaweicloud sdk

        :param customer_id: 客户id
        :type customer_id: str
        :param customer_name: 客户名称
        :type customer_name: str
        :param service_time_zone: 服务时区，GMT+08:00
        :type service_time_zone: str
        :param service_time_day: 每周服务天数
        :type service_time_day: str
        :param service_time_hour: 每天服务小时
        :type service_time_hour: str
        """
        
        

        self._customer_id = None
        self._customer_name = None
        self._service_time_zone = None
        self._service_time_day = None
        self._service_time_hour = None
        self.discriminator = None

        if customer_id is not None:
            self.customer_id = customer_id
        if customer_name is not None:
            self.customer_name = customer_name
        if service_time_zone is not None:
            self.service_time_zone = service_time_zone
        if service_time_day is not None:
            self.service_time_day = service_time_day
        if service_time_hour is not None:
            self.service_time_hour = service_time_hour

    @property
    def customer_id(self):
        """Gets the customer_id of this PartnersServiceInfo.

        客户id

        :return: The customer_id of this PartnersServiceInfo.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this PartnersServiceInfo.

        客户id

        :param customer_id: The customer_id of this PartnersServiceInfo.
        :type customer_id: str
        """
        self._customer_id = customer_id

    @property
    def customer_name(self):
        """Gets the customer_name of this PartnersServiceInfo.

        客户名称

        :return: The customer_name of this PartnersServiceInfo.
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this PartnersServiceInfo.

        客户名称

        :param customer_name: The customer_name of this PartnersServiceInfo.
        :type customer_name: str
        """
        self._customer_name = customer_name

    @property
    def service_time_zone(self):
        """Gets the service_time_zone of this PartnersServiceInfo.

        服务时区，GMT+08:00

        :return: The service_time_zone of this PartnersServiceInfo.
        :rtype: str
        """
        return self._service_time_zone

    @service_time_zone.setter
    def service_time_zone(self, service_time_zone):
        """Sets the service_time_zone of this PartnersServiceInfo.

        服务时区，GMT+08:00

        :param service_time_zone: The service_time_zone of this PartnersServiceInfo.
        :type service_time_zone: str
        """
        self._service_time_zone = service_time_zone

    @property
    def service_time_day(self):
        """Gets the service_time_day of this PartnersServiceInfo.

        每周服务天数

        :return: The service_time_day of this PartnersServiceInfo.
        :rtype: str
        """
        return self._service_time_day

    @service_time_day.setter
    def service_time_day(self, service_time_day):
        """Sets the service_time_day of this PartnersServiceInfo.

        每周服务天数

        :param service_time_day: The service_time_day of this PartnersServiceInfo.
        :type service_time_day: str
        """
        self._service_time_day = service_time_day

    @property
    def service_time_hour(self):
        """Gets the service_time_hour of this PartnersServiceInfo.

        每天服务小时

        :return: The service_time_hour of this PartnersServiceInfo.
        :rtype: str
        """
        return self._service_time_hour

    @service_time_hour.setter
    def service_time_hour(self, service_time_hour):
        """Sets the service_time_hour of this PartnersServiceInfo.

        每天服务小时

        :param service_time_hour: The service_time_hour of this PartnersServiceInfo.
        :type service_time_hour: str
        """
        self._service_time_hour = service_time_hour

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
        if not isinstance(other, PartnersServiceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
