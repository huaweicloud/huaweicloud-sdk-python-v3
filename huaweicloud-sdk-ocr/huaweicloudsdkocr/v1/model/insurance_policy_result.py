# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InsurancePolicyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bank_name': 'str',
        'bill_number': 'InsurancePolicyDetail',
        'company': 'InsurancePolicyDetail',
        'effective_date': 'InsurancePolicyDetail',
        'applicant_name': 'InsurancePolicyDetail',
        'applicant_sex': 'InsurancePolicyDetail',
        'applicant_birthday': 'InsurancePolicyDetail',
        'applicant_id_type': 'InsurancePolicyDetail',
        'applicant_id_number': 'InsurancePolicyDetail',
        'insurant_list': 'list[InsurantItem]',
        'beneficiary_list': 'list[BeneficiaryItem]',
        'insurance_list': 'list[InsuranceItem]'
    }

    attribute_map = {
        'bank_name': 'bank_name',
        'bill_number': 'bill_number',
        'company': 'company',
        'effective_date': 'effective_date',
        'applicant_name': 'applicant_name',
        'applicant_sex': 'applicant_sex',
        'applicant_birthday': 'applicant_birthday',
        'applicant_id_type': 'applicant_id_type',
        'applicant_id_number': 'applicant_id_number',
        'insurant_list': 'insurant_list',
        'beneficiary_list': 'beneficiary_list',
        'insurance_list': 'insurance_list'
    }

    def __init__(self, bank_name=None, bill_number=None, company=None, effective_date=None, applicant_name=None, applicant_sex=None, applicant_birthday=None, applicant_id_type=None, applicant_id_number=None, insurant_list=None, beneficiary_list=None, insurance_list=None):
        """InsurancePolicyResult

        The model defined in huaweicloud sdk

        :param bank_name: 发卡行。 
        :type bank_name: str
        :param bill_number: 
        :type bill_number: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param company: 
        :type company: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param effective_date: 
        :type effective_date: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param applicant_name: 
        :type applicant_name: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param applicant_sex: 
        :type applicant_sex: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param applicant_birthday: 
        :type applicant_birthday: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param applicant_id_type: 
        :type applicant_id_type: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param applicant_id_number: 
        :type applicant_id_number: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        :param insurant_list: 被保人列表（第一个默认为主被保人）。 
        :type insurant_list: list[:class:`huaweicloudsdkocr.v1.InsurantItem`]
        :param beneficiary_list: 受益人列表。 
        :type beneficiary_list: list[:class:`huaweicloudsdkocr.v1.BeneficiaryItem`]
        :param insurance_list: 保险项目信息列表。 
        :type insurance_list: list[:class:`huaweicloudsdkocr.v1.InsuranceItem`]
        """
        
        

        self._bank_name = None
        self._bill_number = None
        self._company = None
        self._effective_date = None
        self._applicant_name = None
        self._applicant_sex = None
        self._applicant_birthday = None
        self._applicant_id_type = None
        self._applicant_id_number = None
        self._insurant_list = None
        self._beneficiary_list = None
        self._insurance_list = None
        self.discriminator = None

        if bank_name is not None:
            self.bank_name = bank_name
        if bill_number is not None:
            self.bill_number = bill_number
        if company is not None:
            self.company = company
        if effective_date is not None:
            self.effective_date = effective_date
        if applicant_name is not None:
            self.applicant_name = applicant_name
        if applicant_sex is not None:
            self.applicant_sex = applicant_sex
        if applicant_birthday is not None:
            self.applicant_birthday = applicant_birthday
        if applicant_id_type is not None:
            self.applicant_id_type = applicant_id_type
        if applicant_id_number is not None:
            self.applicant_id_number = applicant_id_number
        if insurant_list is not None:
            self.insurant_list = insurant_list
        if beneficiary_list is not None:
            self.beneficiary_list = beneficiary_list
        if insurance_list is not None:
            self.insurance_list = insurance_list

    @property
    def bank_name(self):
        """Gets the bank_name of this InsurancePolicyResult.

        发卡行。 

        :return: The bank_name of this InsurancePolicyResult.
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """Sets the bank_name of this InsurancePolicyResult.

        发卡行。 

        :param bank_name: The bank_name of this InsurancePolicyResult.
        :type bank_name: str
        """
        self._bank_name = bank_name

    @property
    def bill_number(self):
        """Gets the bill_number of this InsurancePolicyResult.


        :return: The bill_number of this InsurancePolicyResult.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._bill_number

    @bill_number.setter
    def bill_number(self, bill_number):
        """Sets the bill_number of this InsurancePolicyResult.


        :param bill_number: The bill_number of this InsurancePolicyResult.
        :type bill_number: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._bill_number = bill_number

    @property
    def company(self):
        """Gets the company of this InsurancePolicyResult.


        :return: The company of this InsurancePolicyResult.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this InsurancePolicyResult.


        :param company: The company of this InsurancePolicyResult.
        :type company: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._company = company

    @property
    def effective_date(self):
        """Gets the effective_date of this InsurancePolicyResult.


        :return: The effective_date of this InsurancePolicyResult.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this InsurancePolicyResult.


        :param effective_date: The effective_date of this InsurancePolicyResult.
        :type effective_date: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._effective_date = effective_date

    @property
    def applicant_name(self):
        """Gets the applicant_name of this InsurancePolicyResult.


        :return: The applicant_name of this InsurancePolicyResult.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._applicant_name

    @applicant_name.setter
    def applicant_name(self, applicant_name):
        """Sets the applicant_name of this InsurancePolicyResult.


        :param applicant_name: The applicant_name of this InsurancePolicyResult.
        :type applicant_name: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._applicant_name = applicant_name

    @property
    def applicant_sex(self):
        """Gets the applicant_sex of this InsurancePolicyResult.


        :return: The applicant_sex of this InsurancePolicyResult.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._applicant_sex

    @applicant_sex.setter
    def applicant_sex(self, applicant_sex):
        """Sets the applicant_sex of this InsurancePolicyResult.


        :param applicant_sex: The applicant_sex of this InsurancePolicyResult.
        :type applicant_sex: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._applicant_sex = applicant_sex

    @property
    def applicant_birthday(self):
        """Gets the applicant_birthday of this InsurancePolicyResult.


        :return: The applicant_birthday of this InsurancePolicyResult.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._applicant_birthday

    @applicant_birthday.setter
    def applicant_birthday(self, applicant_birthday):
        """Sets the applicant_birthday of this InsurancePolicyResult.


        :param applicant_birthday: The applicant_birthday of this InsurancePolicyResult.
        :type applicant_birthday: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._applicant_birthday = applicant_birthday

    @property
    def applicant_id_type(self):
        """Gets the applicant_id_type of this InsurancePolicyResult.


        :return: The applicant_id_type of this InsurancePolicyResult.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._applicant_id_type

    @applicant_id_type.setter
    def applicant_id_type(self, applicant_id_type):
        """Sets the applicant_id_type of this InsurancePolicyResult.


        :param applicant_id_type: The applicant_id_type of this InsurancePolicyResult.
        :type applicant_id_type: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._applicant_id_type = applicant_id_type

    @property
    def applicant_id_number(self):
        """Gets the applicant_id_number of this InsurancePolicyResult.


        :return: The applicant_id_number of this InsurancePolicyResult.
        :rtype: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        return self._applicant_id_number

    @applicant_id_number.setter
    def applicant_id_number(self, applicant_id_number):
        """Sets the applicant_id_number of this InsurancePolicyResult.


        :param applicant_id_number: The applicant_id_number of this InsurancePolicyResult.
        :type applicant_id_number: :class:`huaweicloudsdkocr.v1.InsurancePolicyDetail`
        """
        self._applicant_id_number = applicant_id_number

    @property
    def insurant_list(self):
        """Gets the insurant_list of this InsurancePolicyResult.

        被保人列表（第一个默认为主被保人）。 

        :return: The insurant_list of this InsurancePolicyResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.InsurantItem`]
        """
        return self._insurant_list

    @insurant_list.setter
    def insurant_list(self, insurant_list):
        """Sets the insurant_list of this InsurancePolicyResult.

        被保人列表（第一个默认为主被保人）。 

        :param insurant_list: The insurant_list of this InsurancePolicyResult.
        :type insurant_list: list[:class:`huaweicloudsdkocr.v1.InsurantItem`]
        """
        self._insurant_list = insurant_list

    @property
    def beneficiary_list(self):
        """Gets the beneficiary_list of this InsurancePolicyResult.

        受益人列表。 

        :return: The beneficiary_list of this InsurancePolicyResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.BeneficiaryItem`]
        """
        return self._beneficiary_list

    @beneficiary_list.setter
    def beneficiary_list(self, beneficiary_list):
        """Sets the beneficiary_list of this InsurancePolicyResult.

        受益人列表。 

        :param beneficiary_list: The beneficiary_list of this InsurancePolicyResult.
        :type beneficiary_list: list[:class:`huaweicloudsdkocr.v1.BeneficiaryItem`]
        """
        self._beneficiary_list = beneficiary_list

    @property
    def insurance_list(self):
        """Gets the insurance_list of this InsurancePolicyResult.

        保险项目信息列表。 

        :return: The insurance_list of this InsurancePolicyResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.InsuranceItem`]
        """
        return self._insurance_list

    @insurance_list.setter
    def insurance_list(self, insurance_list):
        """Sets the insurance_list of this InsurancePolicyResult.

        保险项目信息列表。 

        :param insurance_list: The insurance_list of this InsurancePolicyResult.
        :type insurance_list: list[:class:`huaweicloudsdkocr.v1.InsuranceItem`]
        """
        self._insurance_list = insurance_list

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
        if not isinstance(other, InsurancePolicyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
