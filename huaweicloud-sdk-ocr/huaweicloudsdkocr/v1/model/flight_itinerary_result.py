# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlightItineraryResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'serial_number': 'str',
        'passenger_name': 'str',
        'id_number': 'str',
        'endorsements_restrictions': 'str',
        'order_number': 'str',
        'fare': 'str',
        'caac_development_fund': 'str',
        'fuel_surcharge': 'str',
        'other_taxes': 'str',
        'total': 'str',
        'e_ticket_number': 'str',
        'check_code': 'str',
        'reference_information': 'str',
        'insurance': 'str',
        'agent_code': 'str',
        'issue_organization': 'str',
        'issue_date': 'str',
        'itinerary_list': 'list[ItineraryList]',
        'confidence': 'object'
    }

    attribute_map = {
        'serial_number': 'serial_number',
        'passenger_name': 'passenger_name',
        'id_number': 'id_number',
        'endorsements_restrictions': 'endorsements_restrictions',
        'order_number': 'order_number',
        'fare': 'fare',
        'caac_development_fund': 'caac_development_fund',
        'fuel_surcharge': 'fuel_surcharge',
        'other_taxes': 'other_taxes',
        'total': 'total',
        'e_ticket_number': 'e_ticket_number',
        'check_code': 'check_code',
        'reference_information': 'reference_information',
        'insurance': 'insurance',
        'agent_code': 'agent_code',
        'issue_organization': 'issue_organization',
        'issue_date': 'issue_date',
        'itinerary_list': 'itinerary_list',
        'confidence': 'confidence'
    }

    def __init__(self, serial_number=None, passenger_name=None, id_number=None, endorsements_restrictions=None, order_number=None, fare=None, caac_development_fund=None, fuel_surcharge=None, other_taxes=None, total=None, e_ticket_number=None, check_code=None, reference_information=None, insurance=None, agent_code=None, issue_organization=None, issue_date=None, itinerary_list=None, confidence=None):
        """FlightItineraryResult

        The model defined in huaweicloud sdk

        :param serial_number: 印刷序号。 
        :type serial_number: str
        :param passenger_name: 旅客姓名。 
        :type passenger_name: str
        :param id_number: 有效身份证件号码。 
        :type id_number: str
        :param endorsements_restrictions: 备注。 
        :type endorsements_restrictions: str
        :param order_number: 订单号。 
        :type order_number: str
        :param fare: 票价。 
        :type fare: str
        :param caac_development_fund: 民航（CAAC)发展基金。 
        :type caac_development_fund: str
        :param fuel_surcharge: 燃油附加费。 
        :type fuel_surcharge: str
        :param other_taxes: 其他税费。 
        :type other_taxes: str
        :param total: 合计。 
        :type total: str
        :param e_ticket_number: 电子客票号码。 
        :type e_ticket_number: str
        :param check_code: 验证码。 
        :type check_code: str
        :param reference_information: 提示信息。 
        :type reference_information: str
        :param insurance: 保险费。 
        :type insurance: str
        :param agent_code: 销售单位代号。 
        :type agent_code: str
        :param issue_organization: 填开单位。 
        :type issue_organization: str
        :param issue_date: 填开日期。 
        :type issue_date: str
        :param itinerary_list: 机票行程列表。 
        :type itinerary_list: list[:class:`huaweicloudsdkocr.v1.ItineraryList`]
        :param confidence: 相关字段的置信度信息，取值范围0~1。  置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。  置信度由算法给出，不直接等价于对应字段的准确率。  &gt; 说明：  - （1）置信度中的相关字段均与返回值中的相关字段一一对应；  - （2）置信度中的itinerary_list的顺序与返回值中的itinerary_list的顺序是一致的。 
        :type confidence: object
        """
        
        

        self._serial_number = None
        self._passenger_name = None
        self._id_number = None
        self._endorsements_restrictions = None
        self._order_number = None
        self._fare = None
        self._caac_development_fund = None
        self._fuel_surcharge = None
        self._other_taxes = None
        self._total = None
        self._e_ticket_number = None
        self._check_code = None
        self._reference_information = None
        self._insurance = None
        self._agent_code = None
        self._issue_organization = None
        self._issue_date = None
        self._itinerary_list = None
        self._confidence = None
        self.discriminator = None

        if serial_number is not None:
            self.serial_number = serial_number
        if passenger_name is not None:
            self.passenger_name = passenger_name
        if id_number is not None:
            self.id_number = id_number
        if endorsements_restrictions is not None:
            self.endorsements_restrictions = endorsements_restrictions
        if order_number is not None:
            self.order_number = order_number
        if fare is not None:
            self.fare = fare
        if caac_development_fund is not None:
            self.caac_development_fund = caac_development_fund
        if fuel_surcharge is not None:
            self.fuel_surcharge = fuel_surcharge
        if other_taxes is not None:
            self.other_taxes = other_taxes
        if total is not None:
            self.total = total
        if e_ticket_number is not None:
            self.e_ticket_number = e_ticket_number
        if check_code is not None:
            self.check_code = check_code
        if reference_information is not None:
            self.reference_information = reference_information
        if insurance is not None:
            self.insurance = insurance
        if agent_code is not None:
            self.agent_code = agent_code
        if issue_organization is not None:
            self.issue_organization = issue_organization
        if issue_date is not None:
            self.issue_date = issue_date
        if itinerary_list is not None:
            self.itinerary_list = itinerary_list
        if confidence is not None:
            self.confidence = confidence

    @property
    def serial_number(self):
        """Gets the serial_number of this FlightItineraryResult.

        印刷序号。 

        :return: The serial_number of this FlightItineraryResult.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this FlightItineraryResult.

        印刷序号。 

        :param serial_number: The serial_number of this FlightItineraryResult.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def passenger_name(self):
        """Gets the passenger_name of this FlightItineraryResult.

        旅客姓名。 

        :return: The passenger_name of this FlightItineraryResult.
        :rtype: str
        """
        return self._passenger_name

    @passenger_name.setter
    def passenger_name(self, passenger_name):
        """Sets the passenger_name of this FlightItineraryResult.

        旅客姓名。 

        :param passenger_name: The passenger_name of this FlightItineraryResult.
        :type passenger_name: str
        """
        self._passenger_name = passenger_name

    @property
    def id_number(self):
        """Gets the id_number of this FlightItineraryResult.

        有效身份证件号码。 

        :return: The id_number of this FlightItineraryResult.
        :rtype: str
        """
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        """Sets the id_number of this FlightItineraryResult.

        有效身份证件号码。 

        :param id_number: The id_number of this FlightItineraryResult.
        :type id_number: str
        """
        self._id_number = id_number

    @property
    def endorsements_restrictions(self):
        """Gets the endorsements_restrictions of this FlightItineraryResult.

        备注。 

        :return: The endorsements_restrictions of this FlightItineraryResult.
        :rtype: str
        """
        return self._endorsements_restrictions

    @endorsements_restrictions.setter
    def endorsements_restrictions(self, endorsements_restrictions):
        """Sets the endorsements_restrictions of this FlightItineraryResult.

        备注。 

        :param endorsements_restrictions: The endorsements_restrictions of this FlightItineraryResult.
        :type endorsements_restrictions: str
        """
        self._endorsements_restrictions = endorsements_restrictions

    @property
    def order_number(self):
        """Gets the order_number of this FlightItineraryResult.

        订单号。 

        :return: The order_number of this FlightItineraryResult.
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this FlightItineraryResult.

        订单号。 

        :param order_number: The order_number of this FlightItineraryResult.
        :type order_number: str
        """
        self._order_number = order_number

    @property
    def fare(self):
        """Gets the fare of this FlightItineraryResult.

        票价。 

        :return: The fare of this FlightItineraryResult.
        :rtype: str
        """
        return self._fare

    @fare.setter
    def fare(self, fare):
        """Sets the fare of this FlightItineraryResult.

        票价。 

        :param fare: The fare of this FlightItineraryResult.
        :type fare: str
        """
        self._fare = fare

    @property
    def caac_development_fund(self):
        """Gets the caac_development_fund of this FlightItineraryResult.

        民航（CAAC)发展基金。 

        :return: The caac_development_fund of this FlightItineraryResult.
        :rtype: str
        """
        return self._caac_development_fund

    @caac_development_fund.setter
    def caac_development_fund(self, caac_development_fund):
        """Sets the caac_development_fund of this FlightItineraryResult.

        民航（CAAC)发展基金。 

        :param caac_development_fund: The caac_development_fund of this FlightItineraryResult.
        :type caac_development_fund: str
        """
        self._caac_development_fund = caac_development_fund

    @property
    def fuel_surcharge(self):
        """Gets the fuel_surcharge of this FlightItineraryResult.

        燃油附加费。 

        :return: The fuel_surcharge of this FlightItineraryResult.
        :rtype: str
        """
        return self._fuel_surcharge

    @fuel_surcharge.setter
    def fuel_surcharge(self, fuel_surcharge):
        """Sets the fuel_surcharge of this FlightItineraryResult.

        燃油附加费。 

        :param fuel_surcharge: The fuel_surcharge of this FlightItineraryResult.
        :type fuel_surcharge: str
        """
        self._fuel_surcharge = fuel_surcharge

    @property
    def other_taxes(self):
        """Gets the other_taxes of this FlightItineraryResult.

        其他税费。 

        :return: The other_taxes of this FlightItineraryResult.
        :rtype: str
        """
        return self._other_taxes

    @other_taxes.setter
    def other_taxes(self, other_taxes):
        """Sets the other_taxes of this FlightItineraryResult.

        其他税费。 

        :param other_taxes: The other_taxes of this FlightItineraryResult.
        :type other_taxes: str
        """
        self._other_taxes = other_taxes

    @property
    def total(self):
        """Gets the total of this FlightItineraryResult.

        合计。 

        :return: The total of this FlightItineraryResult.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this FlightItineraryResult.

        合计。 

        :param total: The total of this FlightItineraryResult.
        :type total: str
        """
        self._total = total

    @property
    def e_ticket_number(self):
        """Gets the e_ticket_number of this FlightItineraryResult.

        电子客票号码。 

        :return: The e_ticket_number of this FlightItineraryResult.
        :rtype: str
        """
        return self._e_ticket_number

    @e_ticket_number.setter
    def e_ticket_number(self, e_ticket_number):
        """Sets the e_ticket_number of this FlightItineraryResult.

        电子客票号码。 

        :param e_ticket_number: The e_ticket_number of this FlightItineraryResult.
        :type e_ticket_number: str
        """
        self._e_ticket_number = e_ticket_number

    @property
    def check_code(self):
        """Gets the check_code of this FlightItineraryResult.

        验证码。 

        :return: The check_code of this FlightItineraryResult.
        :rtype: str
        """
        return self._check_code

    @check_code.setter
    def check_code(self, check_code):
        """Sets the check_code of this FlightItineraryResult.

        验证码。 

        :param check_code: The check_code of this FlightItineraryResult.
        :type check_code: str
        """
        self._check_code = check_code

    @property
    def reference_information(self):
        """Gets the reference_information of this FlightItineraryResult.

        提示信息。 

        :return: The reference_information of this FlightItineraryResult.
        :rtype: str
        """
        return self._reference_information

    @reference_information.setter
    def reference_information(self, reference_information):
        """Sets the reference_information of this FlightItineraryResult.

        提示信息。 

        :param reference_information: The reference_information of this FlightItineraryResult.
        :type reference_information: str
        """
        self._reference_information = reference_information

    @property
    def insurance(self):
        """Gets the insurance of this FlightItineraryResult.

        保险费。 

        :return: The insurance of this FlightItineraryResult.
        :rtype: str
        """
        return self._insurance

    @insurance.setter
    def insurance(self, insurance):
        """Sets the insurance of this FlightItineraryResult.

        保险费。 

        :param insurance: The insurance of this FlightItineraryResult.
        :type insurance: str
        """
        self._insurance = insurance

    @property
    def agent_code(self):
        """Gets the agent_code of this FlightItineraryResult.

        销售单位代号。 

        :return: The agent_code of this FlightItineraryResult.
        :rtype: str
        """
        return self._agent_code

    @agent_code.setter
    def agent_code(self, agent_code):
        """Sets the agent_code of this FlightItineraryResult.

        销售单位代号。 

        :param agent_code: The agent_code of this FlightItineraryResult.
        :type agent_code: str
        """
        self._agent_code = agent_code

    @property
    def issue_organization(self):
        """Gets the issue_organization of this FlightItineraryResult.

        填开单位。 

        :return: The issue_organization of this FlightItineraryResult.
        :rtype: str
        """
        return self._issue_organization

    @issue_organization.setter
    def issue_organization(self, issue_organization):
        """Sets the issue_organization of this FlightItineraryResult.

        填开单位。 

        :param issue_organization: The issue_organization of this FlightItineraryResult.
        :type issue_organization: str
        """
        self._issue_organization = issue_organization

    @property
    def issue_date(self):
        """Gets the issue_date of this FlightItineraryResult.

        填开日期。 

        :return: The issue_date of this FlightItineraryResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this FlightItineraryResult.

        填开日期。 

        :param issue_date: The issue_date of this FlightItineraryResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def itinerary_list(self):
        """Gets the itinerary_list of this FlightItineraryResult.

        机票行程列表。 

        :return: The itinerary_list of this FlightItineraryResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.ItineraryList`]
        """
        return self._itinerary_list

    @itinerary_list.setter
    def itinerary_list(self, itinerary_list):
        """Sets the itinerary_list of this FlightItineraryResult.

        机票行程列表。 

        :param itinerary_list: The itinerary_list of this FlightItineraryResult.
        :type itinerary_list: list[:class:`huaweicloudsdkocr.v1.ItineraryList`]
        """
        self._itinerary_list = itinerary_list

    @property
    def confidence(self):
        """Gets the confidence of this FlightItineraryResult.

        相关字段的置信度信息，取值范围0~1。  置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。  置信度由算法给出，不直接等价于对应字段的准确率。  > 说明：  - （1）置信度中的相关字段均与返回值中的相关字段一一对应；  - （2）置信度中的itinerary_list的顺序与返回值中的itinerary_list的顺序是一致的。 

        :return: The confidence of this FlightItineraryResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this FlightItineraryResult.

        相关字段的置信度信息，取值范围0~1。  置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。  置信度由算法给出，不直接等价于对应字段的准确率。  > 说明：  - （1）置信度中的相关字段均与返回值中的相关字段一一对应；  - （2）置信度中的itinerary_list的顺序与返回值中的itinerary_list的顺序是一致的。 

        :param confidence: The confidence of this FlightItineraryResult.
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
        if not isinstance(other, FlightItineraryResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
