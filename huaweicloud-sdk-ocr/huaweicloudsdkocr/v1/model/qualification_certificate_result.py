# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QualificationCertificateResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id_number': 'str',
        'assessment_date': 'str',
        'certificate_number': 'str',
        'file_number': 'str',
        'union_card_number': 'str',
        'continuing_education_info': 'str',
        'sex': 'str',
        'phone_number': 'str',
        'registration_date': 'str',
        'work_unit': 'str',
        'integrity_assessment_info': 'str',
        'nationality': 'str',
        'name': 'str',
        'address': 'str',
        'driving_class': 'str',
        'issuing_authority': 'str',
        'birth_date': 'str',
        'qualification_category_list': 'list[QualificationCategory]',
        'confidence': 'QualificationConfidence'
    }

    attribute_map = {
        'id_number': 'id_number',
        'assessment_date': 'assessment_date',
        'certificate_number': 'certificate_number',
        'file_number': 'file_number',
        'union_card_number': 'union_card_number',
        'continuing_education_info': 'continuing_education_info',
        'sex': 'sex',
        'phone_number': 'phone_number',
        'registration_date': 'registration_date',
        'work_unit': 'work_unit',
        'integrity_assessment_info': 'integrity_assessment_info',
        'nationality': 'nationality',
        'name': 'name',
        'address': 'address',
        'driving_class': 'driving_class',
        'issuing_authority': 'issuing_authority',
        'birth_date': 'birth_date',
        'qualification_category_list': 'qualification_category_list',
        'confidence': 'confidence'
    }

    def __init__(self, id_number=None, assessment_date=None, certificate_number=None, file_number=None, union_card_number=None, continuing_education_info=None, sex=None, phone_number=None, registration_date=None, work_unit=None, integrity_assessment_info=None, nationality=None, name=None, address=None, driving_class=None, issuing_authority=None, birth_date=None, qualification_category_list=None, confidence=None):
        r"""QualificationCertificateResult

        The model defined in huaweicloud sdk

        :param id_number: 身份证号（非必有，依赖对应从业资格证板式）。 
        :type id_number: str
        :param assessment_date: 考核时间（非必有，依赖对应从业资格证板式）。 
        :type assessment_date: str
        :param certificate_number: 从业资格证号。 
        :type certificate_number: str
        :param file_number: 档案号（非必有，依赖对应从业资格证板式）。 
        :type file_number: str
        :param union_card_number: 福路通号（非必有，依赖对应从业资格证板式）。 
        :type union_card_number: str
        :param continuing_education_info: 继续教育信息（非必有，依赖对应从业资格证板式）。 
        :type continuing_education_info: str
        :param sex: 性别（非必有，依赖对应从业资格证板式）。 
        :type sex: str
        :param phone_number: 联系电话（非必有，依赖对应从业资格证板式）。 
        :type phone_number: str
        :param registration_date: 登记时间（非必有，依赖对应从业资格证板式）。 
        :type registration_date: str
        :param work_unit: 单位（非必有，依赖对应从业资格证板式）。 
        :type work_unit: str
        :param integrity_assessment_info: 诚信考核信息（非必有，依赖对应从业资格证板式）。 
        :type integrity_assessment_info: str
        :param nationality: 国籍（非必有，依赖对应从业资格证板式）。 
        :type nationality: str
        :param name: 姓名。 
        :type name: str
        :param address: 住址。 
        :type address: str
        :param driving_class: 准驾车型（非必有，依赖对应从业资格证板式）。 
        :type driving_class: str
        :param issuing_authority: 发证机关（非必有，依赖对应从业资格证板式）。 
        :type issuing_authority: str
        :param birth_date: 出生日期（非必有，依赖对应从业资格证板式）。 
        :type birth_date: str
        :param qualification_category_list: 从业资格列表。 
        :type qualification_category_list: list[:class:`huaweicloudsdkocr.v1.QualificationCategory`]
        :param confidence: 
        :type confidence: :class:`huaweicloudsdkocr.v1.QualificationConfidence`
        """
        
        

        self._id_number = None
        self._assessment_date = None
        self._certificate_number = None
        self._file_number = None
        self._union_card_number = None
        self._continuing_education_info = None
        self._sex = None
        self._phone_number = None
        self._registration_date = None
        self._work_unit = None
        self._integrity_assessment_info = None
        self._nationality = None
        self._name = None
        self._address = None
        self._driving_class = None
        self._issuing_authority = None
        self._birth_date = None
        self._qualification_category_list = None
        self._confidence = None
        self.discriminator = None

        if id_number is not None:
            self.id_number = id_number
        if assessment_date is not None:
            self.assessment_date = assessment_date
        if certificate_number is not None:
            self.certificate_number = certificate_number
        if file_number is not None:
            self.file_number = file_number
        if union_card_number is not None:
            self.union_card_number = union_card_number
        if continuing_education_info is not None:
            self.continuing_education_info = continuing_education_info
        if sex is not None:
            self.sex = sex
        if phone_number is not None:
            self.phone_number = phone_number
        if registration_date is not None:
            self.registration_date = registration_date
        if work_unit is not None:
            self.work_unit = work_unit
        if integrity_assessment_info is not None:
            self.integrity_assessment_info = integrity_assessment_info
        if nationality is not None:
            self.nationality = nationality
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if driving_class is not None:
            self.driving_class = driving_class
        if issuing_authority is not None:
            self.issuing_authority = issuing_authority
        if birth_date is not None:
            self.birth_date = birth_date
        if qualification_category_list is not None:
            self.qualification_category_list = qualification_category_list
        if confidence is not None:
            self.confidence = confidence

    @property
    def id_number(self):
        r"""Gets the id_number of this QualificationCertificateResult.

        身份证号（非必有，依赖对应从业资格证板式）。 

        :return: The id_number of this QualificationCertificateResult.
        :rtype: str
        """
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        r"""Sets the id_number of this QualificationCertificateResult.

        身份证号（非必有，依赖对应从业资格证板式）。 

        :param id_number: The id_number of this QualificationCertificateResult.
        :type id_number: str
        """
        self._id_number = id_number

    @property
    def assessment_date(self):
        r"""Gets the assessment_date of this QualificationCertificateResult.

        考核时间（非必有，依赖对应从业资格证板式）。 

        :return: The assessment_date of this QualificationCertificateResult.
        :rtype: str
        """
        return self._assessment_date

    @assessment_date.setter
    def assessment_date(self, assessment_date):
        r"""Sets the assessment_date of this QualificationCertificateResult.

        考核时间（非必有，依赖对应从业资格证板式）。 

        :param assessment_date: The assessment_date of this QualificationCertificateResult.
        :type assessment_date: str
        """
        self._assessment_date = assessment_date

    @property
    def certificate_number(self):
        r"""Gets the certificate_number of this QualificationCertificateResult.

        从业资格证号。 

        :return: The certificate_number of this QualificationCertificateResult.
        :rtype: str
        """
        return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, certificate_number):
        r"""Sets the certificate_number of this QualificationCertificateResult.

        从业资格证号。 

        :param certificate_number: The certificate_number of this QualificationCertificateResult.
        :type certificate_number: str
        """
        self._certificate_number = certificate_number

    @property
    def file_number(self):
        r"""Gets the file_number of this QualificationCertificateResult.

        档案号（非必有，依赖对应从业资格证板式）。 

        :return: The file_number of this QualificationCertificateResult.
        :rtype: str
        """
        return self._file_number

    @file_number.setter
    def file_number(self, file_number):
        r"""Sets the file_number of this QualificationCertificateResult.

        档案号（非必有，依赖对应从业资格证板式）。 

        :param file_number: The file_number of this QualificationCertificateResult.
        :type file_number: str
        """
        self._file_number = file_number

    @property
    def union_card_number(self):
        r"""Gets the union_card_number of this QualificationCertificateResult.

        福路通号（非必有，依赖对应从业资格证板式）。 

        :return: The union_card_number of this QualificationCertificateResult.
        :rtype: str
        """
        return self._union_card_number

    @union_card_number.setter
    def union_card_number(self, union_card_number):
        r"""Sets the union_card_number of this QualificationCertificateResult.

        福路通号（非必有，依赖对应从业资格证板式）。 

        :param union_card_number: The union_card_number of this QualificationCertificateResult.
        :type union_card_number: str
        """
        self._union_card_number = union_card_number

    @property
    def continuing_education_info(self):
        r"""Gets the continuing_education_info of this QualificationCertificateResult.

        继续教育信息（非必有，依赖对应从业资格证板式）。 

        :return: The continuing_education_info of this QualificationCertificateResult.
        :rtype: str
        """
        return self._continuing_education_info

    @continuing_education_info.setter
    def continuing_education_info(self, continuing_education_info):
        r"""Sets the continuing_education_info of this QualificationCertificateResult.

        继续教育信息（非必有，依赖对应从业资格证板式）。 

        :param continuing_education_info: The continuing_education_info of this QualificationCertificateResult.
        :type continuing_education_info: str
        """
        self._continuing_education_info = continuing_education_info

    @property
    def sex(self):
        r"""Gets the sex of this QualificationCertificateResult.

        性别（非必有，依赖对应从业资格证板式）。 

        :return: The sex of this QualificationCertificateResult.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        r"""Sets the sex of this QualificationCertificateResult.

        性别（非必有，依赖对应从业资格证板式）。 

        :param sex: The sex of this QualificationCertificateResult.
        :type sex: str
        """
        self._sex = sex

    @property
    def phone_number(self):
        r"""Gets the phone_number of this QualificationCertificateResult.

        联系电话（非必有，依赖对应从业资格证板式）。 

        :return: The phone_number of this QualificationCertificateResult.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        r"""Sets the phone_number of this QualificationCertificateResult.

        联系电话（非必有，依赖对应从业资格证板式）。 

        :param phone_number: The phone_number of this QualificationCertificateResult.
        :type phone_number: str
        """
        self._phone_number = phone_number

    @property
    def registration_date(self):
        r"""Gets the registration_date of this QualificationCertificateResult.

        登记时间（非必有，依赖对应从业资格证板式）。 

        :return: The registration_date of this QualificationCertificateResult.
        :rtype: str
        """
        return self._registration_date

    @registration_date.setter
    def registration_date(self, registration_date):
        r"""Sets the registration_date of this QualificationCertificateResult.

        登记时间（非必有，依赖对应从业资格证板式）。 

        :param registration_date: The registration_date of this QualificationCertificateResult.
        :type registration_date: str
        """
        self._registration_date = registration_date

    @property
    def work_unit(self):
        r"""Gets the work_unit of this QualificationCertificateResult.

        单位（非必有，依赖对应从业资格证板式）。 

        :return: The work_unit of this QualificationCertificateResult.
        :rtype: str
        """
        return self._work_unit

    @work_unit.setter
    def work_unit(self, work_unit):
        r"""Sets the work_unit of this QualificationCertificateResult.

        单位（非必有，依赖对应从业资格证板式）。 

        :param work_unit: The work_unit of this QualificationCertificateResult.
        :type work_unit: str
        """
        self._work_unit = work_unit

    @property
    def integrity_assessment_info(self):
        r"""Gets the integrity_assessment_info of this QualificationCertificateResult.

        诚信考核信息（非必有，依赖对应从业资格证板式）。 

        :return: The integrity_assessment_info of this QualificationCertificateResult.
        :rtype: str
        """
        return self._integrity_assessment_info

    @integrity_assessment_info.setter
    def integrity_assessment_info(self, integrity_assessment_info):
        r"""Sets the integrity_assessment_info of this QualificationCertificateResult.

        诚信考核信息（非必有，依赖对应从业资格证板式）。 

        :param integrity_assessment_info: The integrity_assessment_info of this QualificationCertificateResult.
        :type integrity_assessment_info: str
        """
        self._integrity_assessment_info = integrity_assessment_info

    @property
    def nationality(self):
        r"""Gets the nationality of this QualificationCertificateResult.

        国籍（非必有，依赖对应从业资格证板式）。 

        :return: The nationality of this QualificationCertificateResult.
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        r"""Sets the nationality of this QualificationCertificateResult.

        国籍（非必有，依赖对应从业资格证板式）。 

        :param nationality: The nationality of this QualificationCertificateResult.
        :type nationality: str
        """
        self._nationality = nationality

    @property
    def name(self):
        r"""Gets the name of this QualificationCertificateResult.

        姓名。 

        :return: The name of this QualificationCertificateResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this QualificationCertificateResult.

        姓名。 

        :param name: The name of this QualificationCertificateResult.
        :type name: str
        """
        self._name = name

    @property
    def address(self):
        r"""Gets the address of this QualificationCertificateResult.

        住址。 

        :return: The address of this QualificationCertificateResult.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this QualificationCertificateResult.

        住址。 

        :param address: The address of this QualificationCertificateResult.
        :type address: str
        """
        self._address = address

    @property
    def driving_class(self):
        r"""Gets the driving_class of this QualificationCertificateResult.

        准驾车型（非必有，依赖对应从业资格证板式）。 

        :return: The driving_class of this QualificationCertificateResult.
        :rtype: str
        """
        return self._driving_class

    @driving_class.setter
    def driving_class(self, driving_class):
        r"""Sets the driving_class of this QualificationCertificateResult.

        准驾车型（非必有，依赖对应从业资格证板式）。 

        :param driving_class: The driving_class of this QualificationCertificateResult.
        :type driving_class: str
        """
        self._driving_class = driving_class

    @property
    def issuing_authority(self):
        r"""Gets the issuing_authority of this QualificationCertificateResult.

        发证机关（非必有，依赖对应从业资格证板式）。 

        :return: The issuing_authority of this QualificationCertificateResult.
        :rtype: str
        """
        return self._issuing_authority

    @issuing_authority.setter
    def issuing_authority(self, issuing_authority):
        r"""Sets the issuing_authority of this QualificationCertificateResult.

        发证机关（非必有，依赖对应从业资格证板式）。 

        :param issuing_authority: The issuing_authority of this QualificationCertificateResult.
        :type issuing_authority: str
        """
        self._issuing_authority = issuing_authority

    @property
    def birth_date(self):
        r"""Gets the birth_date of this QualificationCertificateResult.

        出生日期（非必有，依赖对应从业资格证板式）。 

        :return: The birth_date of this QualificationCertificateResult.
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        r"""Sets the birth_date of this QualificationCertificateResult.

        出生日期（非必有，依赖对应从业资格证板式）。 

        :param birth_date: The birth_date of this QualificationCertificateResult.
        :type birth_date: str
        """
        self._birth_date = birth_date

    @property
    def qualification_category_list(self):
        r"""Gets the qualification_category_list of this QualificationCertificateResult.

        从业资格列表。 

        :return: The qualification_category_list of this QualificationCertificateResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.QualificationCategory`]
        """
        return self._qualification_category_list

    @qualification_category_list.setter
    def qualification_category_list(self, qualification_category_list):
        r"""Sets the qualification_category_list of this QualificationCertificateResult.

        从业资格列表。 

        :param qualification_category_list: The qualification_category_list of this QualificationCertificateResult.
        :type qualification_category_list: list[:class:`huaweicloudsdkocr.v1.QualificationCategory`]
        """
        self._qualification_category_list = qualification_category_list

    @property
    def confidence(self):
        r"""Gets the confidence of this QualificationCertificateResult.

        :return: The confidence of this QualificationCertificateResult.
        :rtype: :class:`huaweicloudsdkocr.v1.QualificationConfidence`
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this QualificationCertificateResult.

        :param confidence: The confidence of this QualificationCertificateResult.
        :type confidence: :class:`huaweicloudsdkocr.v1.QualificationConfidence`
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
        if not isinstance(other, QualificationCertificateResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
