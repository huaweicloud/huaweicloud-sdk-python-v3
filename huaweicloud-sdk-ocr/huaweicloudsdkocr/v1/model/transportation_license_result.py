# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransportationLicenseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'owner_name': 'str',
        'license_number': 'str',
        'vehicle_number': 'str',
        'vehicle_type': 'str',
        'maximum_capacity': 'str',
        'vehicle_size': 'str',
        'issuing_authority': 'str',
        'issue_date': 'str',
        'owner_address': 'str',
        'economic_type': 'str',
        'business_certificate': 'str',
        'business_scope': 'str',
        'confidence': 'object'
    }

    attribute_map = {
        'owner_name': 'owner_name',
        'license_number': 'license_number',
        'vehicle_number': 'vehicle_number',
        'vehicle_type': 'vehicle_type',
        'maximum_capacity': 'maximum_capacity',
        'vehicle_size': 'vehicle_size',
        'issuing_authority': 'issuing_authority',
        'issue_date': 'issue_date',
        'owner_address': 'owner_address',
        'economic_type': 'economic_type',
        'business_certificate': 'business_certificate',
        'business_scope': 'business_scope',
        'confidence': 'confidence'
    }

    def __init__(self, owner_name=None, license_number=None, vehicle_number=None, vehicle_type=None, maximum_capacity=None, vehicle_size=None, issuing_authority=None, issue_date=None, owner_address=None, economic_type=None, business_certificate=None, business_scope=None, confidence=None):
        """TransportationLicenseResult

        The model defined in huaweicloud sdk

        :param owner_name: 业户名称。 
        :type owner_name: str
        :param license_number: 道路运输证号。 
        :type license_number: str
        :param vehicle_number: 车辆号牌。 
        :type vehicle_number: str
        :param vehicle_type: 车辆类型。 
        :type vehicle_type: str
        :param maximum_capacity: 吨(座)位。 
        :type maximum_capacity: str
        :param vehicle_size: 车辆尺寸。 
        :type vehicle_size: str
        :param issuing_authority: 核发机关（非必有，依赖对应运输证板式）。 
        :type issuing_authority: str
        :param issue_date: 签发日期（非必有，依赖对应运输证板式）。 
        :type issue_date: str
        :param owner_address: 业户地址（非必有，依赖对应运输证板式）。 
        :type owner_address: str
        :param economic_type: 经济类型（非必有，依赖对应运输证板式）。 
        :type economic_type: str
        :param business_certificate: 经营许可证号（非必有，依赖对应运输证板式）。 
        :type business_certificate: str
        :param business_scope: 道路普通货物运输（非必有，依赖对应运输证板式）。 
        :type business_scope: str
        :param confidence: 相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 
        :type confidence: object
        """
        
        

        self._owner_name = None
        self._license_number = None
        self._vehicle_number = None
        self._vehicle_type = None
        self._maximum_capacity = None
        self._vehicle_size = None
        self._issuing_authority = None
        self._issue_date = None
        self._owner_address = None
        self._economic_type = None
        self._business_certificate = None
        self._business_scope = None
        self._confidence = None
        self.discriminator = None

        if owner_name is not None:
            self.owner_name = owner_name
        if license_number is not None:
            self.license_number = license_number
        if vehicle_number is not None:
            self.vehicle_number = vehicle_number
        if vehicle_type is not None:
            self.vehicle_type = vehicle_type
        if maximum_capacity is not None:
            self.maximum_capacity = maximum_capacity
        if vehicle_size is not None:
            self.vehicle_size = vehicle_size
        if issuing_authority is not None:
            self.issuing_authority = issuing_authority
        if issue_date is not None:
            self.issue_date = issue_date
        if owner_address is not None:
            self.owner_address = owner_address
        if economic_type is not None:
            self.economic_type = economic_type
        if business_certificate is not None:
            self.business_certificate = business_certificate
        if business_scope is not None:
            self.business_scope = business_scope
        if confidence is not None:
            self.confidence = confidence

    @property
    def owner_name(self):
        """Gets the owner_name of this TransportationLicenseResult.

        业户名称。 

        :return: The owner_name of this TransportationLicenseResult.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this TransportationLicenseResult.

        业户名称。 

        :param owner_name: The owner_name of this TransportationLicenseResult.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def license_number(self):
        """Gets the license_number of this TransportationLicenseResult.

        道路运输证号。 

        :return: The license_number of this TransportationLicenseResult.
        :rtype: str
        """
        return self._license_number

    @license_number.setter
    def license_number(self, license_number):
        """Sets the license_number of this TransportationLicenseResult.

        道路运输证号。 

        :param license_number: The license_number of this TransportationLicenseResult.
        :type license_number: str
        """
        self._license_number = license_number

    @property
    def vehicle_number(self):
        """Gets the vehicle_number of this TransportationLicenseResult.

        车辆号牌。 

        :return: The vehicle_number of this TransportationLicenseResult.
        :rtype: str
        """
        return self._vehicle_number

    @vehicle_number.setter
    def vehicle_number(self, vehicle_number):
        """Sets the vehicle_number of this TransportationLicenseResult.

        车辆号牌。 

        :param vehicle_number: The vehicle_number of this TransportationLicenseResult.
        :type vehicle_number: str
        """
        self._vehicle_number = vehicle_number

    @property
    def vehicle_type(self):
        """Gets the vehicle_type of this TransportationLicenseResult.

        车辆类型。 

        :return: The vehicle_type of this TransportationLicenseResult.
        :rtype: str
        """
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        """Sets the vehicle_type of this TransportationLicenseResult.

        车辆类型。 

        :param vehicle_type: The vehicle_type of this TransportationLicenseResult.
        :type vehicle_type: str
        """
        self._vehicle_type = vehicle_type

    @property
    def maximum_capacity(self):
        """Gets the maximum_capacity of this TransportationLicenseResult.

        吨(座)位。 

        :return: The maximum_capacity of this TransportationLicenseResult.
        :rtype: str
        """
        return self._maximum_capacity

    @maximum_capacity.setter
    def maximum_capacity(self, maximum_capacity):
        """Sets the maximum_capacity of this TransportationLicenseResult.

        吨(座)位。 

        :param maximum_capacity: The maximum_capacity of this TransportationLicenseResult.
        :type maximum_capacity: str
        """
        self._maximum_capacity = maximum_capacity

    @property
    def vehicle_size(self):
        """Gets the vehicle_size of this TransportationLicenseResult.

        车辆尺寸。 

        :return: The vehicle_size of this TransportationLicenseResult.
        :rtype: str
        """
        return self._vehicle_size

    @vehicle_size.setter
    def vehicle_size(self, vehicle_size):
        """Sets the vehicle_size of this TransportationLicenseResult.

        车辆尺寸。 

        :param vehicle_size: The vehicle_size of this TransportationLicenseResult.
        :type vehicle_size: str
        """
        self._vehicle_size = vehicle_size

    @property
    def issuing_authority(self):
        """Gets the issuing_authority of this TransportationLicenseResult.

        核发机关（非必有，依赖对应运输证板式）。 

        :return: The issuing_authority of this TransportationLicenseResult.
        :rtype: str
        """
        return self._issuing_authority

    @issuing_authority.setter
    def issuing_authority(self, issuing_authority):
        """Sets the issuing_authority of this TransportationLicenseResult.

        核发机关（非必有，依赖对应运输证板式）。 

        :param issuing_authority: The issuing_authority of this TransportationLicenseResult.
        :type issuing_authority: str
        """
        self._issuing_authority = issuing_authority

    @property
    def issue_date(self):
        """Gets the issue_date of this TransportationLicenseResult.

        签发日期（非必有，依赖对应运输证板式）。 

        :return: The issue_date of this TransportationLicenseResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this TransportationLicenseResult.

        签发日期（非必有，依赖对应运输证板式）。 

        :param issue_date: The issue_date of this TransportationLicenseResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def owner_address(self):
        """Gets the owner_address of this TransportationLicenseResult.

        业户地址（非必有，依赖对应运输证板式）。 

        :return: The owner_address of this TransportationLicenseResult.
        :rtype: str
        """
        return self._owner_address

    @owner_address.setter
    def owner_address(self, owner_address):
        """Sets the owner_address of this TransportationLicenseResult.

        业户地址（非必有，依赖对应运输证板式）。 

        :param owner_address: The owner_address of this TransportationLicenseResult.
        :type owner_address: str
        """
        self._owner_address = owner_address

    @property
    def economic_type(self):
        """Gets the economic_type of this TransportationLicenseResult.

        经济类型（非必有，依赖对应运输证板式）。 

        :return: The economic_type of this TransportationLicenseResult.
        :rtype: str
        """
        return self._economic_type

    @economic_type.setter
    def economic_type(self, economic_type):
        """Sets the economic_type of this TransportationLicenseResult.

        经济类型（非必有，依赖对应运输证板式）。 

        :param economic_type: The economic_type of this TransportationLicenseResult.
        :type economic_type: str
        """
        self._economic_type = economic_type

    @property
    def business_certificate(self):
        """Gets the business_certificate of this TransportationLicenseResult.

        经营许可证号（非必有，依赖对应运输证板式）。 

        :return: The business_certificate of this TransportationLicenseResult.
        :rtype: str
        """
        return self._business_certificate

    @business_certificate.setter
    def business_certificate(self, business_certificate):
        """Sets the business_certificate of this TransportationLicenseResult.

        经营许可证号（非必有，依赖对应运输证板式）。 

        :param business_certificate: The business_certificate of this TransportationLicenseResult.
        :type business_certificate: str
        """
        self._business_certificate = business_certificate

    @property
    def business_scope(self):
        """Gets the business_scope of this TransportationLicenseResult.

        道路普通货物运输（非必有，依赖对应运输证板式）。 

        :return: The business_scope of this TransportationLicenseResult.
        :rtype: str
        """
        return self._business_scope

    @business_scope.setter
    def business_scope(self, business_scope):
        """Sets the business_scope of this TransportationLicenseResult.

        道路普通货物运输（非必有，依赖对应运输证板式）。 

        :param business_scope: The business_scope of this TransportationLicenseResult.
        :type business_scope: str
        """
        self._business_scope = business_scope

    @property
    def confidence(self):
        """Gets the confidence of this TransportationLicenseResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The confidence of this TransportationLicenseResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this TransportationLicenseResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :param confidence: The confidence of this TransportationLicenseResult.
        :type confidence: object
        """
        self._confidence = confidence

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
        if not isinstance(other, TransportationLicenseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
