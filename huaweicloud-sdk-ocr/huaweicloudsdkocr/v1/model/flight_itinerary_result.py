# coding: utf-8

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
        'tax': 'str',
        'tax_rate': 'str',
        'buyer_name': 'str',
        'buyer_id': 'str',
        'number': 'str',
        'international_flag': 'str',
        'issue_status': 'str',
        'gp_number': 'str',
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
        'tax': 'tax',
        'tax_rate': 'tax_rate',
        'buyer_name': 'buyer_name',
        'buyer_id': 'buyer_id',
        'number': 'number',
        'international_flag': 'international_flag',
        'issue_status': 'issue_status',
        'gp_number': 'gp_number',
        'itinerary_list': 'itinerary_list',
        'confidence': 'confidence'
    }

    def __init__(self, serial_number=None, passenger_name=None, id_number=None, endorsements_restrictions=None, order_number=None, fare=None, caac_development_fund=None, fuel_surcharge=None, other_taxes=None, total=None, e_ticket_number=None, check_code=None, reference_information=None, insurance=None, agent_code=None, issue_organization=None, issue_date=None, tax=None, tax_rate=None, buyer_name=None, buyer_id=None, number=None, international_flag=None, issue_status=None, gp_number=None, itinerary_list=None, confidence=None):
        r"""FlightItineraryResult

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
        :param tax: 增值税税额 
        :type tax: str
        :param tax_rate: 增值税税率 
        :type tax_rate: str
        :param buyer_name: 购买方名称 
        :type buyer_name: str
        :param buyer_id: 购买方纳税人识别号 
        :type buyer_id: str
        :param number: 发票号码 
        :type number: str
        :param international_flag: 国内国际标签 
        :type international_flag: str
        :param issue_status: 开具状态 
        :type issue_status: str
        :param gp_number: gp单号。 
        :type gp_number: str
        :param itinerary_list: 机票行程列表。 
        :type itinerary_list: list[:class:`huaweicloudsdkocr.v1.ItineraryList`]
        :param confidence: 相关字段的置信度信息，取值范围0~1。  置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。  &gt; 说明：  - （1）置信度中的相关字段均与返回值中的相关字段一一对应；  - （2）置信度中的itinerary_list的顺序与返回值中的itinerary_list的顺序是一致的。 
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
        self._tax = None
        self._tax_rate = None
        self._buyer_name = None
        self._buyer_id = None
        self._number = None
        self._international_flag = None
        self._issue_status = None
        self._gp_number = None
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
        if tax is not None:
            self.tax = tax
        if tax_rate is not None:
            self.tax_rate = tax_rate
        if buyer_name is not None:
            self.buyer_name = buyer_name
        if buyer_id is not None:
            self.buyer_id = buyer_id
        if number is not None:
            self.number = number
        if international_flag is not None:
            self.international_flag = international_flag
        if issue_status is not None:
            self.issue_status = issue_status
        if gp_number is not None:
            self.gp_number = gp_number
        if itinerary_list is not None:
            self.itinerary_list = itinerary_list
        if confidence is not None:
            self.confidence = confidence

    @property
    def serial_number(self):
        r"""Gets the serial_number of this FlightItineraryResult.

        印刷序号。 

        :return: The serial_number of this FlightItineraryResult.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        r"""Sets the serial_number of this FlightItineraryResult.

        印刷序号。 

        :param serial_number: The serial_number of this FlightItineraryResult.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def passenger_name(self):
        r"""Gets the passenger_name of this FlightItineraryResult.

        旅客姓名。 

        :return: The passenger_name of this FlightItineraryResult.
        :rtype: str
        """
        return self._passenger_name

    @passenger_name.setter
    def passenger_name(self, passenger_name):
        r"""Sets the passenger_name of this FlightItineraryResult.

        旅客姓名。 

        :param passenger_name: The passenger_name of this FlightItineraryResult.
        :type passenger_name: str
        """
        self._passenger_name = passenger_name

    @property
    def id_number(self):
        r"""Gets the id_number of this FlightItineraryResult.

        有效身份证件号码。 

        :return: The id_number of this FlightItineraryResult.
        :rtype: str
        """
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        r"""Sets the id_number of this FlightItineraryResult.

        有效身份证件号码。 

        :param id_number: The id_number of this FlightItineraryResult.
        :type id_number: str
        """
        self._id_number = id_number

    @property
    def endorsements_restrictions(self):
        r"""Gets the endorsements_restrictions of this FlightItineraryResult.

        备注。 

        :return: The endorsements_restrictions of this FlightItineraryResult.
        :rtype: str
        """
        return self._endorsements_restrictions

    @endorsements_restrictions.setter
    def endorsements_restrictions(self, endorsements_restrictions):
        r"""Sets the endorsements_restrictions of this FlightItineraryResult.

        备注。 

        :param endorsements_restrictions: The endorsements_restrictions of this FlightItineraryResult.
        :type endorsements_restrictions: str
        """
        self._endorsements_restrictions = endorsements_restrictions

    @property
    def order_number(self):
        r"""Gets the order_number of this FlightItineraryResult.

        订单号。 

        :return: The order_number of this FlightItineraryResult.
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        r"""Sets the order_number of this FlightItineraryResult.

        订单号。 

        :param order_number: The order_number of this FlightItineraryResult.
        :type order_number: str
        """
        self._order_number = order_number

    @property
    def fare(self):
        r"""Gets the fare of this FlightItineraryResult.

        票价。 

        :return: The fare of this FlightItineraryResult.
        :rtype: str
        """
        return self._fare

    @fare.setter
    def fare(self, fare):
        r"""Sets the fare of this FlightItineraryResult.

        票价。 

        :param fare: The fare of this FlightItineraryResult.
        :type fare: str
        """
        self._fare = fare

    @property
    def caac_development_fund(self):
        r"""Gets the caac_development_fund of this FlightItineraryResult.

        民航（CAAC)发展基金。 

        :return: The caac_development_fund of this FlightItineraryResult.
        :rtype: str
        """
        return self._caac_development_fund

    @caac_development_fund.setter
    def caac_development_fund(self, caac_development_fund):
        r"""Sets the caac_development_fund of this FlightItineraryResult.

        民航（CAAC)发展基金。 

        :param caac_development_fund: The caac_development_fund of this FlightItineraryResult.
        :type caac_development_fund: str
        """
        self._caac_development_fund = caac_development_fund

    @property
    def fuel_surcharge(self):
        r"""Gets the fuel_surcharge of this FlightItineraryResult.

        燃油附加费。 

        :return: The fuel_surcharge of this FlightItineraryResult.
        :rtype: str
        """
        return self._fuel_surcharge

    @fuel_surcharge.setter
    def fuel_surcharge(self, fuel_surcharge):
        r"""Sets the fuel_surcharge of this FlightItineraryResult.

        燃油附加费。 

        :param fuel_surcharge: The fuel_surcharge of this FlightItineraryResult.
        :type fuel_surcharge: str
        """
        self._fuel_surcharge = fuel_surcharge

    @property
    def other_taxes(self):
        r"""Gets the other_taxes of this FlightItineraryResult.

        其他税费。 

        :return: The other_taxes of this FlightItineraryResult.
        :rtype: str
        """
        return self._other_taxes

    @other_taxes.setter
    def other_taxes(self, other_taxes):
        r"""Sets the other_taxes of this FlightItineraryResult.

        其他税费。 

        :param other_taxes: The other_taxes of this FlightItineraryResult.
        :type other_taxes: str
        """
        self._other_taxes = other_taxes

    @property
    def total(self):
        r"""Gets the total of this FlightItineraryResult.

        合计。 

        :return: The total of this FlightItineraryResult.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this FlightItineraryResult.

        合计。 

        :param total: The total of this FlightItineraryResult.
        :type total: str
        """
        self._total = total

    @property
    def e_ticket_number(self):
        r"""Gets the e_ticket_number of this FlightItineraryResult.

        电子客票号码。 

        :return: The e_ticket_number of this FlightItineraryResult.
        :rtype: str
        """
        return self._e_ticket_number

    @e_ticket_number.setter
    def e_ticket_number(self, e_ticket_number):
        r"""Sets the e_ticket_number of this FlightItineraryResult.

        电子客票号码。 

        :param e_ticket_number: The e_ticket_number of this FlightItineraryResult.
        :type e_ticket_number: str
        """
        self._e_ticket_number = e_ticket_number

    @property
    def check_code(self):
        r"""Gets the check_code of this FlightItineraryResult.

        验证码。 

        :return: The check_code of this FlightItineraryResult.
        :rtype: str
        """
        return self._check_code

    @check_code.setter
    def check_code(self, check_code):
        r"""Sets the check_code of this FlightItineraryResult.

        验证码。 

        :param check_code: The check_code of this FlightItineraryResult.
        :type check_code: str
        """
        self._check_code = check_code

    @property
    def reference_information(self):
        r"""Gets the reference_information of this FlightItineraryResult.

        提示信息。 

        :return: The reference_information of this FlightItineraryResult.
        :rtype: str
        """
        return self._reference_information

    @reference_information.setter
    def reference_information(self, reference_information):
        r"""Sets the reference_information of this FlightItineraryResult.

        提示信息。 

        :param reference_information: The reference_information of this FlightItineraryResult.
        :type reference_information: str
        """
        self._reference_information = reference_information

    @property
    def insurance(self):
        r"""Gets the insurance of this FlightItineraryResult.

        保险费。 

        :return: The insurance of this FlightItineraryResult.
        :rtype: str
        """
        return self._insurance

    @insurance.setter
    def insurance(self, insurance):
        r"""Sets the insurance of this FlightItineraryResult.

        保险费。 

        :param insurance: The insurance of this FlightItineraryResult.
        :type insurance: str
        """
        self._insurance = insurance

    @property
    def agent_code(self):
        r"""Gets the agent_code of this FlightItineraryResult.

        销售单位代号。 

        :return: The agent_code of this FlightItineraryResult.
        :rtype: str
        """
        return self._agent_code

    @agent_code.setter
    def agent_code(self, agent_code):
        r"""Sets the agent_code of this FlightItineraryResult.

        销售单位代号。 

        :param agent_code: The agent_code of this FlightItineraryResult.
        :type agent_code: str
        """
        self._agent_code = agent_code

    @property
    def issue_organization(self):
        r"""Gets the issue_organization of this FlightItineraryResult.

        填开单位。 

        :return: The issue_organization of this FlightItineraryResult.
        :rtype: str
        """
        return self._issue_organization

    @issue_organization.setter
    def issue_organization(self, issue_organization):
        r"""Sets the issue_organization of this FlightItineraryResult.

        填开单位。 

        :param issue_organization: The issue_organization of this FlightItineraryResult.
        :type issue_organization: str
        """
        self._issue_organization = issue_organization

    @property
    def issue_date(self):
        r"""Gets the issue_date of this FlightItineraryResult.

        填开日期。 

        :return: The issue_date of this FlightItineraryResult.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        r"""Sets the issue_date of this FlightItineraryResult.

        填开日期。 

        :param issue_date: The issue_date of this FlightItineraryResult.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def tax(self):
        r"""Gets the tax of this FlightItineraryResult.

        增值税税额 

        :return: The tax of this FlightItineraryResult.
        :rtype: str
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        r"""Sets the tax of this FlightItineraryResult.

        增值税税额 

        :param tax: The tax of this FlightItineraryResult.
        :type tax: str
        """
        self._tax = tax

    @property
    def tax_rate(self):
        r"""Gets the tax_rate of this FlightItineraryResult.

        增值税税率 

        :return: The tax_rate of this FlightItineraryResult.
        :rtype: str
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        r"""Sets the tax_rate of this FlightItineraryResult.

        增值税税率 

        :param tax_rate: The tax_rate of this FlightItineraryResult.
        :type tax_rate: str
        """
        self._tax_rate = tax_rate

    @property
    def buyer_name(self):
        r"""Gets the buyer_name of this FlightItineraryResult.

        购买方名称 

        :return: The buyer_name of this FlightItineraryResult.
        :rtype: str
        """
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, buyer_name):
        r"""Sets the buyer_name of this FlightItineraryResult.

        购买方名称 

        :param buyer_name: The buyer_name of this FlightItineraryResult.
        :type buyer_name: str
        """
        self._buyer_name = buyer_name

    @property
    def buyer_id(self):
        r"""Gets the buyer_id of this FlightItineraryResult.

        购买方纳税人识别号 

        :return: The buyer_id of this FlightItineraryResult.
        :rtype: str
        """
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, buyer_id):
        r"""Sets the buyer_id of this FlightItineraryResult.

        购买方纳税人识别号 

        :param buyer_id: The buyer_id of this FlightItineraryResult.
        :type buyer_id: str
        """
        self._buyer_id = buyer_id

    @property
    def number(self):
        r"""Gets the number of this FlightItineraryResult.

        发票号码 

        :return: The number of this FlightItineraryResult.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this FlightItineraryResult.

        发票号码 

        :param number: The number of this FlightItineraryResult.
        :type number: str
        """
        self._number = number

    @property
    def international_flag(self):
        r"""Gets the international_flag of this FlightItineraryResult.

        国内国际标签 

        :return: The international_flag of this FlightItineraryResult.
        :rtype: str
        """
        return self._international_flag

    @international_flag.setter
    def international_flag(self, international_flag):
        r"""Sets the international_flag of this FlightItineraryResult.

        国内国际标签 

        :param international_flag: The international_flag of this FlightItineraryResult.
        :type international_flag: str
        """
        self._international_flag = international_flag

    @property
    def issue_status(self):
        r"""Gets the issue_status of this FlightItineraryResult.

        开具状态 

        :return: The issue_status of this FlightItineraryResult.
        :rtype: str
        """
        return self._issue_status

    @issue_status.setter
    def issue_status(self, issue_status):
        r"""Sets the issue_status of this FlightItineraryResult.

        开具状态 

        :param issue_status: The issue_status of this FlightItineraryResult.
        :type issue_status: str
        """
        self._issue_status = issue_status

    @property
    def gp_number(self):
        r"""Gets the gp_number of this FlightItineraryResult.

        gp单号。 

        :return: The gp_number of this FlightItineraryResult.
        :rtype: str
        """
        return self._gp_number

    @gp_number.setter
    def gp_number(self, gp_number):
        r"""Sets the gp_number of this FlightItineraryResult.

        gp单号。 

        :param gp_number: The gp_number of this FlightItineraryResult.
        :type gp_number: str
        """
        self._gp_number = gp_number

    @property
    def itinerary_list(self):
        r"""Gets the itinerary_list of this FlightItineraryResult.

        机票行程列表。 

        :return: The itinerary_list of this FlightItineraryResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.ItineraryList`]
        """
        return self._itinerary_list

    @itinerary_list.setter
    def itinerary_list(self, itinerary_list):
        r"""Sets the itinerary_list of this FlightItineraryResult.

        机票行程列表。 

        :param itinerary_list: The itinerary_list of this FlightItineraryResult.
        :type itinerary_list: list[:class:`huaweicloudsdkocr.v1.ItineraryList`]
        """
        self._itinerary_list = itinerary_list

    @property
    def confidence(self):
        r"""Gets the confidence of this FlightItineraryResult.

        相关字段的置信度信息，取值范围0~1。  置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。  > 说明：  - （1）置信度中的相关字段均与返回值中的相关字段一一对应；  - （2）置信度中的itinerary_list的顺序与返回值中的itinerary_list的顺序是一致的。 

        :return: The confidence of this FlightItineraryResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this FlightItineraryResult.

        相关字段的置信度信息，取值范围0~1。  置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。  > 说明：  - （1）置信度中的相关字段均与返回值中的相关字段一一对应；  - （2）置信度中的itinerary_list的顺序与返回值中的itinerary_list的顺序是一致的。 

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
