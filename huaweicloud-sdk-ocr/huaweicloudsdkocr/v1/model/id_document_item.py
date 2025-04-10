# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdDocumentItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'country_region': 'str',
        'id_type': 'str',
        'side': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'sex': 'str',
        'nationality': 'str',
        'birth_date': 'str',
        'issue_date': 'str',
        'expiry_date': 'str',
        'document_number': 'str',
        'address': 'str',
        'issuing_authority': 'str',
        'portrait_image': 'str',
        'confidence': 'object'
    }

    attribute_map = {
        'country_region': 'country_region',
        'id_type': 'id_type',
        'side': 'side',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'sex': 'sex',
        'nationality': 'nationality',
        'birth_date': 'birth_date',
        'issue_date': 'issue_date',
        'expiry_date': 'expiry_date',
        'document_number': 'document_number',
        'address': 'address',
        'issuing_authority': 'issuing_authority',
        'portrait_image': 'portrait_image',
        'confidence': 'confidence'
    }

    def __init__(self, country_region=None, id_type=None, side=None, first_name=None, last_name=None, sex=None, nationality=None, birth_date=None, issue_date=None, expiry_date=None, document_number=None, address=None, issuing_authority=None, portrait_image=None, confidence=None):
        r"""IdDocumentItem

        The model defined in huaweicloud sdk

        :param country_region: 证件签发国家或地区代码，命名遵循ISO-3166 3位代码。当前支持国家列表见表1。 
        :type country_region: str
        :param id_type: 证件类型，可选值如下： - PP: passport，国际护照。 - DL: driving license，驾驶证。 - ID: identification card，各国颁发的身份证类型证件，比如身份证、选民卡、社保卡等。 
        :type id_type: str
        :param side: 证件正面或反面,可选值： - front: 正面，一般是包含人像的那面 - back: 背面 对于只有一面的卡证，返回front 
        :type side: str
        :param first_name: 名 
        :type first_name: str
        :param last_name: 姓氏 
        :type last_name: str
        :param sex: 性别，可选值： M:男性 F:女性 X:中性 
        :type sex: str
        :param nationality: 持有人国籍 
        :type nationality: str
        :param birth_date: 生日，格式为yyyy-mm-dd 
        :type birth_date: str
        :param issue_date: 签发日期，yyyy-mm-dd 
        :type issue_date: str
        :param expiry_date: 有效日期，yyyy-mm-dd 
        :type expiry_date: str
        :param document_number: 证件号码 
        :type document_number: str
        :param address: 持有人通讯地址 
        :type address: str
        :param issuing_authority: 签发机关 
        :type issuing_authority: str
        :param portrait_image: 可选返回，证件头像图像base64编码 
        :type portrait_image: str
        :param confidence: 字段置信度，为0~1之间的小数，值越大，表明识别结果越可靠 
        :type confidence: object
        """
        
        

        self._country_region = None
        self._id_type = None
        self._side = None
        self._first_name = None
        self._last_name = None
        self._sex = None
        self._nationality = None
        self._birth_date = None
        self._issue_date = None
        self._expiry_date = None
        self._document_number = None
        self._address = None
        self._issuing_authority = None
        self._portrait_image = None
        self._confidence = None
        self.discriminator = None

        if country_region is not None:
            self.country_region = country_region
        if id_type is not None:
            self.id_type = id_type
        if side is not None:
            self.side = side
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if sex is not None:
            self.sex = sex
        if nationality is not None:
            self.nationality = nationality
        if birth_date is not None:
            self.birth_date = birth_date
        if issue_date is not None:
            self.issue_date = issue_date
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if document_number is not None:
            self.document_number = document_number
        if address is not None:
            self.address = address
        if issuing_authority is not None:
            self.issuing_authority = issuing_authority
        if portrait_image is not None:
            self.portrait_image = portrait_image
        if confidence is not None:
            self.confidence = confidence

    @property
    def country_region(self):
        r"""Gets the country_region of this IdDocumentItem.

        证件签发国家或地区代码，命名遵循ISO-3166 3位代码。当前支持国家列表见表1。 

        :return: The country_region of this IdDocumentItem.
        :rtype: str
        """
        return self._country_region

    @country_region.setter
    def country_region(self, country_region):
        r"""Sets the country_region of this IdDocumentItem.

        证件签发国家或地区代码，命名遵循ISO-3166 3位代码。当前支持国家列表见表1。 

        :param country_region: The country_region of this IdDocumentItem.
        :type country_region: str
        """
        self._country_region = country_region

    @property
    def id_type(self):
        r"""Gets the id_type of this IdDocumentItem.

        证件类型，可选值如下： - PP: passport，国际护照。 - DL: driving license，驾驶证。 - ID: identification card，各国颁发的身份证类型证件，比如身份证、选民卡、社保卡等。 

        :return: The id_type of this IdDocumentItem.
        :rtype: str
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        r"""Sets the id_type of this IdDocumentItem.

        证件类型，可选值如下： - PP: passport，国际护照。 - DL: driving license，驾驶证。 - ID: identification card，各国颁发的身份证类型证件，比如身份证、选民卡、社保卡等。 

        :param id_type: The id_type of this IdDocumentItem.
        :type id_type: str
        """
        self._id_type = id_type

    @property
    def side(self):
        r"""Gets the side of this IdDocumentItem.

        证件正面或反面,可选值： - front: 正面，一般是包含人像的那面 - back: 背面 对于只有一面的卡证，返回front 

        :return: The side of this IdDocumentItem.
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        r"""Sets the side of this IdDocumentItem.

        证件正面或反面,可选值： - front: 正面，一般是包含人像的那面 - back: 背面 对于只有一面的卡证，返回front 

        :param side: The side of this IdDocumentItem.
        :type side: str
        """
        self._side = side

    @property
    def first_name(self):
        r"""Gets the first_name of this IdDocumentItem.

        名 

        :return: The first_name of this IdDocumentItem.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        r"""Sets the first_name of this IdDocumentItem.

        名 

        :param first_name: The first_name of this IdDocumentItem.
        :type first_name: str
        """
        self._first_name = first_name

    @property
    def last_name(self):
        r"""Gets the last_name of this IdDocumentItem.

        姓氏 

        :return: The last_name of this IdDocumentItem.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        r"""Sets the last_name of this IdDocumentItem.

        姓氏 

        :param last_name: The last_name of this IdDocumentItem.
        :type last_name: str
        """
        self._last_name = last_name

    @property
    def sex(self):
        r"""Gets the sex of this IdDocumentItem.

        性别，可选值： M:男性 F:女性 X:中性 

        :return: The sex of this IdDocumentItem.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        r"""Sets the sex of this IdDocumentItem.

        性别，可选值： M:男性 F:女性 X:中性 

        :param sex: The sex of this IdDocumentItem.
        :type sex: str
        """
        self._sex = sex

    @property
    def nationality(self):
        r"""Gets the nationality of this IdDocumentItem.

        持有人国籍 

        :return: The nationality of this IdDocumentItem.
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        r"""Sets the nationality of this IdDocumentItem.

        持有人国籍 

        :param nationality: The nationality of this IdDocumentItem.
        :type nationality: str
        """
        self._nationality = nationality

    @property
    def birth_date(self):
        r"""Gets the birth_date of this IdDocumentItem.

        生日，格式为yyyy-mm-dd 

        :return: The birth_date of this IdDocumentItem.
        :rtype: str
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        r"""Sets the birth_date of this IdDocumentItem.

        生日，格式为yyyy-mm-dd 

        :param birth_date: The birth_date of this IdDocumentItem.
        :type birth_date: str
        """
        self._birth_date = birth_date

    @property
    def issue_date(self):
        r"""Gets the issue_date of this IdDocumentItem.

        签发日期，yyyy-mm-dd 

        :return: The issue_date of this IdDocumentItem.
        :rtype: str
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        r"""Sets the issue_date of this IdDocumentItem.

        签发日期，yyyy-mm-dd 

        :param issue_date: The issue_date of this IdDocumentItem.
        :type issue_date: str
        """
        self._issue_date = issue_date

    @property
    def expiry_date(self):
        r"""Gets the expiry_date of this IdDocumentItem.

        有效日期，yyyy-mm-dd 

        :return: The expiry_date of this IdDocumentItem.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        r"""Sets the expiry_date of this IdDocumentItem.

        有效日期，yyyy-mm-dd 

        :param expiry_date: The expiry_date of this IdDocumentItem.
        :type expiry_date: str
        """
        self._expiry_date = expiry_date

    @property
    def document_number(self):
        r"""Gets the document_number of this IdDocumentItem.

        证件号码 

        :return: The document_number of this IdDocumentItem.
        :rtype: str
        """
        return self._document_number

    @document_number.setter
    def document_number(self, document_number):
        r"""Sets the document_number of this IdDocumentItem.

        证件号码 

        :param document_number: The document_number of this IdDocumentItem.
        :type document_number: str
        """
        self._document_number = document_number

    @property
    def address(self):
        r"""Gets the address of this IdDocumentItem.

        持有人通讯地址 

        :return: The address of this IdDocumentItem.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this IdDocumentItem.

        持有人通讯地址 

        :param address: The address of this IdDocumentItem.
        :type address: str
        """
        self._address = address

    @property
    def issuing_authority(self):
        r"""Gets the issuing_authority of this IdDocumentItem.

        签发机关 

        :return: The issuing_authority of this IdDocumentItem.
        :rtype: str
        """
        return self._issuing_authority

    @issuing_authority.setter
    def issuing_authority(self, issuing_authority):
        r"""Sets the issuing_authority of this IdDocumentItem.

        签发机关 

        :param issuing_authority: The issuing_authority of this IdDocumentItem.
        :type issuing_authority: str
        """
        self._issuing_authority = issuing_authority

    @property
    def portrait_image(self):
        r"""Gets the portrait_image of this IdDocumentItem.

        可选返回，证件头像图像base64编码 

        :return: The portrait_image of this IdDocumentItem.
        :rtype: str
        """
        return self._portrait_image

    @portrait_image.setter
    def portrait_image(self, portrait_image):
        r"""Sets the portrait_image of this IdDocumentItem.

        可选返回，证件头像图像base64编码 

        :param portrait_image: The portrait_image of this IdDocumentItem.
        :type portrait_image: str
        """
        self._portrait_image = portrait_image

    @property
    def confidence(self):
        r"""Gets the confidence of this IdDocumentItem.

        字段置信度，为0~1之间的小数，值越大，表明识别结果越可靠 

        :return: The confidence of this IdDocumentItem.
        :rtype: object
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this IdDocumentItem.

        字段置信度，为0~1之间的小数，值越大，表明识别结果越可靠 

        :param confidence: The confidence of this IdDocumentItem.
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
        if not isinstance(other, IdDocumentItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
