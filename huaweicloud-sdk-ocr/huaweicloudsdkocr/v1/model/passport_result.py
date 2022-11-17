# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PassportResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'passport_type': 'str',
        'country_code': 'str',
        'passport_number': 'str',
        'nationality': 'str',
        'surname': 'str',
        'given_name': 'str',
        'sex': 'str',
        'date_of_birth': 'str',
        'date_of_expiry': 'str',
        'date_of_issue': 'str',
        'place_of_birth': 'str',
        'place_of_issue': 'str',
        'issuing_authority': 'str',
        'confidence': 'object',
        'extra_info': 'object'
    }

    attribute_map = {
        'passport_type': 'passport_type',
        'country_code': 'country_code',
        'passport_number': 'passport_number',
        'nationality': 'nationality',
        'surname': 'surname',
        'given_name': 'given_name',
        'sex': 'sex',
        'date_of_birth': 'date_of_birth',
        'date_of_expiry': 'date_of_expiry',
        'date_of_issue': 'date_of_issue',
        'place_of_birth': 'place_of_birth',
        'place_of_issue': 'place_of_issue',
        'issuing_authority': 'issuing_authority',
        'confidence': 'confidence',
        'extra_info': 'extra_info'
    }

    def __init__(self, passport_type=None, country_code=None, passport_number=None, nationality=None, surname=None, given_name=None, sex=None, date_of_birth=None, date_of_expiry=None, date_of_issue=None, place_of_birth=None, place_of_issue=None, issuing_authority=None, confidence=None, extra_info=None):
        """PassportResult

        The model defined in huaweicloud sdk

        :param passport_type: 护照类型（P:普通因私护照、W:外交护照、G:公务护照）（英文）。 
        :type passport_type: str
        :param country_code: 护照签发国的国家码（英文）。 
        :type country_code: str
        :param passport_number: 护照号码（英文）。 
        :type passport_number: str
        :param nationality: 护照持有人国籍（英文）。 
        :type nationality: str
        :param surname: 姓（英文）。 
        :type surname: str
        :param given_name: 名字（英文）。 
        :type given_name: str
        :param sex: 性别（英文）。 
        :type sex: str
        :param date_of_birth: 出生日期（英文）。 
        :type date_of_birth: str
        :param date_of_expiry: 护照有效期（英文）。 
        :type date_of_expiry: str
        :param date_of_issue: 护照签发日期（英文）。 
        :type date_of_issue: str
        :param place_of_birth: 出生地（英文）。 
        :type place_of_birth: str
        :param place_of_issue: 签发地（英文）。 
        :type place_of_issue: str
        :param issuing_authority: 签发机构（英文），其中对中国的英文简写统一输出为P.R.China。 
        :type issuing_authority: str
        :param confidence: 相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 
        :type confidence: object
        :param extra_info: 默认为空。对于部分常见国家的护照OCR服务，extra_info内会包含护照上由本地官方语言描述的字段信息及其他信息。 如中国护照，里面会包含汉字表达的姓名、出生地等信息。 
        :type extra_info: object
        """
        
        

        self._passport_type = None
        self._country_code = None
        self._passport_number = None
        self._nationality = None
        self._surname = None
        self._given_name = None
        self._sex = None
        self._date_of_birth = None
        self._date_of_expiry = None
        self._date_of_issue = None
        self._place_of_birth = None
        self._place_of_issue = None
        self._issuing_authority = None
        self._confidence = None
        self._extra_info = None
        self.discriminator = None

        if passport_type is not None:
            self.passport_type = passport_type
        if country_code is not None:
            self.country_code = country_code
        if passport_number is not None:
            self.passport_number = passport_number
        if nationality is not None:
            self.nationality = nationality
        if surname is not None:
            self.surname = surname
        if given_name is not None:
            self.given_name = given_name
        if sex is not None:
            self.sex = sex
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if date_of_expiry is not None:
            self.date_of_expiry = date_of_expiry
        if date_of_issue is not None:
            self.date_of_issue = date_of_issue
        if place_of_birth is not None:
            self.place_of_birth = place_of_birth
        if place_of_issue is not None:
            self.place_of_issue = place_of_issue
        if issuing_authority is not None:
            self.issuing_authority = issuing_authority
        if confidence is not None:
            self.confidence = confidence
        if extra_info is not None:
            self.extra_info = extra_info

    @property
    def passport_type(self):
        """Gets the passport_type of this PassportResult.

        护照类型（P:普通因私护照、W:外交护照、G:公务护照）（英文）。 

        :return: The passport_type of this PassportResult.
        :rtype: str
        """
        return self._passport_type

    @passport_type.setter
    def passport_type(self, passport_type):
        """Sets the passport_type of this PassportResult.

        护照类型（P:普通因私护照、W:外交护照、G:公务护照）（英文）。 

        :param passport_type: The passport_type of this PassportResult.
        :type passport_type: str
        """
        self._passport_type = passport_type

    @property
    def country_code(self):
        """Gets the country_code of this PassportResult.

        护照签发国的国家码（英文）。 

        :return: The country_code of this PassportResult.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this PassportResult.

        护照签发国的国家码（英文）。 

        :param country_code: The country_code of this PassportResult.
        :type country_code: str
        """
        self._country_code = country_code

    @property
    def passport_number(self):
        """Gets the passport_number of this PassportResult.

        护照号码（英文）。 

        :return: The passport_number of this PassportResult.
        :rtype: str
        """
        return self._passport_number

    @passport_number.setter
    def passport_number(self, passport_number):
        """Sets the passport_number of this PassportResult.

        护照号码（英文）。 

        :param passport_number: The passport_number of this PassportResult.
        :type passport_number: str
        """
        self._passport_number = passport_number

    @property
    def nationality(self):
        """Gets the nationality of this PassportResult.

        护照持有人国籍（英文）。 

        :return: The nationality of this PassportResult.
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this PassportResult.

        护照持有人国籍（英文）。 

        :param nationality: The nationality of this PassportResult.
        :type nationality: str
        """
        self._nationality = nationality

    @property
    def surname(self):
        """Gets the surname of this PassportResult.

        姓（英文）。 

        :return: The surname of this PassportResult.
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this PassportResult.

        姓（英文）。 

        :param surname: The surname of this PassportResult.
        :type surname: str
        """
        self._surname = surname

    @property
    def given_name(self):
        """Gets the given_name of this PassportResult.

        名字（英文）。 

        :return: The given_name of this PassportResult.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this PassportResult.

        名字（英文）。 

        :param given_name: The given_name of this PassportResult.
        :type given_name: str
        """
        self._given_name = given_name

    @property
    def sex(self):
        """Gets the sex of this PassportResult.

        性别（英文）。 

        :return: The sex of this PassportResult.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this PassportResult.

        性别（英文）。 

        :param sex: The sex of this PassportResult.
        :type sex: str
        """
        self._sex = sex

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this PassportResult.

        出生日期（英文）。 

        :return: The date_of_birth of this PassportResult.
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this PassportResult.

        出生日期（英文）。 

        :param date_of_birth: The date_of_birth of this PassportResult.
        :type date_of_birth: str
        """
        self._date_of_birth = date_of_birth

    @property
    def date_of_expiry(self):
        """Gets the date_of_expiry of this PassportResult.

        护照有效期（英文）。 

        :return: The date_of_expiry of this PassportResult.
        :rtype: str
        """
        return self._date_of_expiry

    @date_of_expiry.setter
    def date_of_expiry(self, date_of_expiry):
        """Sets the date_of_expiry of this PassportResult.

        护照有效期（英文）。 

        :param date_of_expiry: The date_of_expiry of this PassportResult.
        :type date_of_expiry: str
        """
        self._date_of_expiry = date_of_expiry

    @property
    def date_of_issue(self):
        """Gets the date_of_issue of this PassportResult.

        护照签发日期（英文）。 

        :return: The date_of_issue of this PassportResult.
        :rtype: str
        """
        return self._date_of_issue

    @date_of_issue.setter
    def date_of_issue(self, date_of_issue):
        """Sets the date_of_issue of this PassportResult.

        护照签发日期（英文）。 

        :param date_of_issue: The date_of_issue of this PassportResult.
        :type date_of_issue: str
        """
        self._date_of_issue = date_of_issue

    @property
    def place_of_birth(self):
        """Gets the place_of_birth of this PassportResult.

        出生地（英文）。 

        :return: The place_of_birth of this PassportResult.
        :rtype: str
        """
        return self._place_of_birth

    @place_of_birth.setter
    def place_of_birth(self, place_of_birth):
        """Sets the place_of_birth of this PassportResult.

        出生地（英文）。 

        :param place_of_birth: The place_of_birth of this PassportResult.
        :type place_of_birth: str
        """
        self._place_of_birth = place_of_birth

    @property
    def place_of_issue(self):
        """Gets the place_of_issue of this PassportResult.

        签发地（英文）。 

        :return: The place_of_issue of this PassportResult.
        :rtype: str
        """
        return self._place_of_issue

    @place_of_issue.setter
    def place_of_issue(self, place_of_issue):
        """Sets the place_of_issue of this PassportResult.

        签发地（英文）。 

        :param place_of_issue: The place_of_issue of this PassportResult.
        :type place_of_issue: str
        """
        self._place_of_issue = place_of_issue

    @property
    def issuing_authority(self):
        """Gets the issuing_authority of this PassportResult.

        签发机构（英文），其中对中国的英文简写统一输出为P.R.China。 

        :return: The issuing_authority of this PassportResult.
        :rtype: str
        """
        return self._issuing_authority

    @issuing_authority.setter
    def issuing_authority(self, issuing_authority):
        """Sets the issuing_authority of this PassportResult.

        签发机构（英文），其中对中国的英文简写统一输出为P.R.China。 

        :param issuing_authority: The issuing_authority of this PassportResult.
        :type issuing_authority: str
        """
        self._issuing_authority = issuing_authority

    @property
    def confidence(self):
        """Gets the confidence of this PassportResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :return: The confidence of this PassportResult.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this PassportResult.

        相关字段的置信度信息，置信度越大，表示本次识别的对应字段的可靠性越高，在统计意义上，置信度越大，准确率越高。 置信度由算法给出，不直接等价于对应字段的准确率。 

        :param confidence: The confidence of this PassportResult.
        :type confidence: object
        """
        self._confidence = confidence

    @property
    def extra_info(self):
        """Gets the extra_info of this PassportResult.

        默认为空。对于部分常见国家的护照OCR服务，extra_info内会包含护照上由本地官方语言描述的字段信息及其他信息。 如中国护照，里面会包含汉字表达的姓名、出生地等信息。 

        :return: The extra_info of this PassportResult.
        :rtype: object
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this PassportResult.

        默认为空。对于部分常见国家的护照OCR服务，extra_info内会包含护照上由本地官方语言描述的字段信息及其他信息。 如中国护照，里面会包含汉字表达的姓名、出生地等信息。 

        :param extra_info: The extra_info of this PassportResult.
        :type extra_info: object
        """
        self._extra_info = extra_info

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
        if not isinstance(other, PassportResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
