# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QualificationConfidence:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id_number': 'float',
        'assessment_date': 'float',
        'certificate_number': 'float',
        'file_number': 'float',
        'union_card_number': 'float',
        'continuing_education_info': 'float',
        'sex': 'float',
        'phone_number': 'float',
        'registration_date': 'float',
        'work_unit': 'float',
        'integrity_assessment_info': 'float',
        'nationality': 'float',
        'name': 'float',
        'address': 'float',
        'driving_class': 'float',
        'issuing_authority': 'float',
        'birth_date': 'float',
        'qualification_category_list': 'list[QualificationCategoryConfidence]'
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
        'qualification_category_list': 'qualification_category_list'
    }

    def __init__(self, id_number=None, assessment_date=None, certificate_number=None, file_number=None, union_card_number=None, continuing_education_info=None, sex=None, phone_number=None, registration_date=None, work_unit=None, integrity_assessment_info=None, nationality=None, name=None, address=None, driving_class=None, issuing_authority=None, birth_date=None, qualification_category_list=None):
        """QualificationConfidence

        The model defined in huaweicloud sdk

        :param id_number: 身份证号置信度。 
        :type id_number: float
        :param assessment_date: 考核时间置信度。 
        :type assessment_date: float
        :param certificate_number: 从业资格证号置信度。 
        :type certificate_number: float
        :param file_number: 档案号置信度。 
        :type file_number: float
        :param union_card_number: 福路通号置信度。 
        :type union_card_number: float
        :param continuing_education_info: 继续教育信息置信度。 
        :type continuing_education_info: float
        :param sex: 性别置信度。 
        :type sex: float
        :param phone_number: 联系电话置信度。 
        :type phone_number: float
        :param registration_date: 登记时间置信度。 
        :type registration_date: float
        :param work_unit: 单位置信度。 
        :type work_unit: float
        :param integrity_assessment_info: 诚信考核信息置信度。 
        :type integrity_assessment_info: float
        :param nationality: 国籍置信度。 
        :type nationality: float
        :param name: 姓名置信度。 
        :type name: float
        :param address: 住址置信度。 
        :type address: float
        :param driving_class: 准驾车型置信度。 
        :type driving_class: float
        :param issuing_authority: 发证机关置信度。 
        :type issuing_authority: float
        :param birth_date: 出生日期置信度。 
        :type birth_date: float
        :param qualification_category_list: 从业资格列表置信度。 
        :type qualification_category_list: list[:class:`huaweicloudsdkocr.v1.QualificationCategoryConfidence`]
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

    @property
    def id_number(self):
        """Gets the id_number of this QualificationConfidence.

        身份证号置信度。 

        :return: The id_number of this QualificationConfidence.
        :rtype: float
        """
        return self._id_number

    @id_number.setter
    def id_number(self, id_number):
        """Sets the id_number of this QualificationConfidence.

        身份证号置信度。 

        :param id_number: The id_number of this QualificationConfidence.
        :type id_number: float
        """
        self._id_number = id_number

    @property
    def assessment_date(self):
        """Gets the assessment_date of this QualificationConfidence.

        考核时间置信度。 

        :return: The assessment_date of this QualificationConfidence.
        :rtype: float
        """
        return self._assessment_date

    @assessment_date.setter
    def assessment_date(self, assessment_date):
        """Sets the assessment_date of this QualificationConfidence.

        考核时间置信度。 

        :param assessment_date: The assessment_date of this QualificationConfidence.
        :type assessment_date: float
        """
        self._assessment_date = assessment_date

    @property
    def certificate_number(self):
        """Gets the certificate_number of this QualificationConfidence.

        从业资格证号置信度。 

        :return: The certificate_number of this QualificationConfidence.
        :rtype: float
        """
        return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, certificate_number):
        """Sets the certificate_number of this QualificationConfidence.

        从业资格证号置信度。 

        :param certificate_number: The certificate_number of this QualificationConfidence.
        :type certificate_number: float
        """
        self._certificate_number = certificate_number

    @property
    def file_number(self):
        """Gets the file_number of this QualificationConfidence.

        档案号置信度。 

        :return: The file_number of this QualificationConfidence.
        :rtype: float
        """
        return self._file_number

    @file_number.setter
    def file_number(self, file_number):
        """Sets the file_number of this QualificationConfidence.

        档案号置信度。 

        :param file_number: The file_number of this QualificationConfidence.
        :type file_number: float
        """
        self._file_number = file_number

    @property
    def union_card_number(self):
        """Gets the union_card_number of this QualificationConfidence.

        福路通号置信度。 

        :return: The union_card_number of this QualificationConfidence.
        :rtype: float
        """
        return self._union_card_number

    @union_card_number.setter
    def union_card_number(self, union_card_number):
        """Sets the union_card_number of this QualificationConfidence.

        福路通号置信度。 

        :param union_card_number: The union_card_number of this QualificationConfidence.
        :type union_card_number: float
        """
        self._union_card_number = union_card_number

    @property
    def continuing_education_info(self):
        """Gets the continuing_education_info of this QualificationConfidence.

        继续教育信息置信度。 

        :return: The continuing_education_info of this QualificationConfidence.
        :rtype: float
        """
        return self._continuing_education_info

    @continuing_education_info.setter
    def continuing_education_info(self, continuing_education_info):
        """Sets the continuing_education_info of this QualificationConfidence.

        继续教育信息置信度。 

        :param continuing_education_info: The continuing_education_info of this QualificationConfidence.
        :type continuing_education_info: float
        """
        self._continuing_education_info = continuing_education_info

    @property
    def sex(self):
        """Gets the sex of this QualificationConfidence.

        性别置信度。 

        :return: The sex of this QualificationConfidence.
        :rtype: float
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this QualificationConfidence.

        性别置信度。 

        :param sex: The sex of this QualificationConfidence.
        :type sex: float
        """
        self._sex = sex

    @property
    def phone_number(self):
        """Gets the phone_number of this QualificationConfidence.

        联系电话置信度。 

        :return: The phone_number of this QualificationConfidence.
        :rtype: float
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this QualificationConfidence.

        联系电话置信度。 

        :param phone_number: The phone_number of this QualificationConfidence.
        :type phone_number: float
        """
        self._phone_number = phone_number

    @property
    def registration_date(self):
        """Gets the registration_date of this QualificationConfidence.

        登记时间置信度。 

        :return: The registration_date of this QualificationConfidence.
        :rtype: float
        """
        return self._registration_date

    @registration_date.setter
    def registration_date(self, registration_date):
        """Sets the registration_date of this QualificationConfidence.

        登记时间置信度。 

        :param registration_date: The registration_date of this QualificationConfidence.
        :type registration_date: float
        """
        self._registration_date = registration_date

    @property
    def work_unit(self):
        """Gets the work_unit of this QualificationConfidence.

        单位置信度。 

        :return: The work_unit of this QualificationConfidence.
        :rtype: float
        """
        return self._work_unit

    @work_unit.setter
    def work_unit(self, work_unit):
        """Sets the work_unit of this QualificationConfidence.

        单位置信度。 

        :param work_unit: The work_unit of this QualificationConfidence.
        :type work_unit: float
        """
        self._work_unit = work_unit

    @property
    def integrity_assessment_info(self):
        """Gets the integrity_assessment_info of this QualificationConfidence.

        诚信考核信息置信度。 

        :return: The integrity_assessment_info of this QualificationConfidence.
        :rtype: float
        """
        return self._integrity_assessment_info

    @integrity_assessment_info.setter
    def integrity_assessment_info(self, integrity_assessment_info):
        """Sets the integrity_assessment_info of this QualificationConfidence.

        诚信考核信息置信度。 

        :param integrity_assessment_info: The integrity_assessment_info of this QualificationConfidence.
        :type integrity_assessment_info: float
        """
        self._integrity_assessment_info = integrity_assessment_info

    @property
    def nationality(self):
        """Gets the nationality of this QualificationConfidence.

        国籍置信度。 

        :return: The nationality of this QualificationConfidence.
        :rtype: float
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this QualificationConfidence.

        国籍置信度。 

        :param nationality: The nationality of this QualificationConfidence.
        :type nationality: float
        """
        self._nationality = nationality

    @property
    def name(self):
        """Gets the name of this QualificationConfidence.

        姓名置信度。 

        :return: The name of this QualificationConfidence.
        :rtype: float
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QualificationConfidence.

        姓名置信度。 

        :param name: The name of this QualificationConfidence.
        :type name: float
        """
        self._name = name

    @property
    def address(self):
        """Gets the address of this QualificationConfidence.

        住址置信度。 

        :return: The address of this QualificationConfidence.
        :rtype: float
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this QualificationConfidence.

        住址置信度。 

        :param address: The address of this QualificationConfidence.
        :type address: float
        """
        self._address = address

    @property
    def driving_class(self):
        """Gets the driving_class of this QualificationConfidence.

        准驾车型置信度。 

        :return: The driving_class of this QualificationConfidence.
        :rtype: float
        """
        return self._driving_class

    @driving_class.setter
    def driving_class(self, driving_class):
        """Sets the driving_class of this QualificationConfidence.

        准驾车型置信度。 

        :param driving_class: The driving_class of this QualificationConfidence.
        :type driving_class: float
        """
        self._driving_class = driving_class

    @property
    def issuing_authority(self):
        """Gets the issuing_authority of this QualificationConfidence.

        发证机关置信度。 

        :return: The issuing_authority of this QualificationConfidence.
        :rtype: float
        """
        return self._issuing_authority

    @issuing_authority.setter
    def issuing_authority(self, issuing_authority):
        """Sets the issuing_authority of this QualificationConfidence.

        发证机关置信度。 

        :param issuing_authority: The issuing_authority of this QualificationConfidence.
        :type issuing_authority: float
        """
        self._issuing_authority = issuing_authority

    @property
    def birth_date(self):
        """Gets the birth_date of this QualificationConfidence.

        出生日期置信度。 

        :return: The birth_date of this QualificationConfidence.
        :rtype: float
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this QualificationConfidence.

        出生日期置信度。 

        :param birth_date: The birth_date of this QualificationConfidence.
        :type birth_date: float
        """
        self._birth_date = birth_date

    @property
    def qualification_category_list(self):
        """Gets the qualification_category_list of this QualificationConfidence.

        从业资格列表置信度。 

        :return: The qualification_category_list of this QualificationConfidence.
        :rtype: list[:class:`huaweicloudsdkocr.v1.QualificationCategoryConfidence`]
        """
        return self._qualification_category_list

    @qualification_category_list.setter
    def qualification_category_list(self, qualification_category_list):
        """Sets the qualification_category_list of this QualificationConfidence.

        从业资格列表置信度。 

        :param qualification_category_list: The qualification_category_list of this QualificationConfidence.
        :type qualification_category_list: list[:class:`huaweicloudsdkocr.v1.QualificationCategoryConfidence`]
        """
        self._qualification_category_list = qualification_category_list

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
        if not isinstance(other, QualificationConfidence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
