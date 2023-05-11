# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BusinessCardResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'list[str]',
        'title': 'list[str]',
        'company': 'list[str]',
        'department': 'list[str]',
        'phone': 'list[str]',
        'address': 'list[str]',
        'email': 'list[str]',
        'fax': 'list[str]',
        'postcode': 'list[str]',
        'website': 'list[str]',
        'extra_info_list': 'list[ExtraInfoList]',
        'adjusted_image': 'str'
    }

    attribute_map = {
        'name': 'name',
        'title': 'title',
        'company': 'company',
        'department': 'department',
        'phone': 'phone',
        'address': 'address',
        'email': 'email',
        'fax': 'fax',
        'postcode': 'postcode',
        'website': 'website',
        'extra_info_list': 'extra_info_list',
        'adjusted_image': 'adjusted_image'
    }

    def __init__(self, name=None, title=None, company=None, department=None, phone=None, address=None, email=None, fax=None, postcode=None, website=None, extra_info_list=None, adjusted_image=None):
        """BusinessCardResult

        The model defined in huaweicloud sdk

        :param name: 姓名列表。 
        :type name: list[str]
        :param title: 职位头衔列表。 
        :type title: list[str]
        :param company: 公司列表。 
        :type company: list[str]
        :param department: 部门列表。 
        :type department: list[str]
        :param phone: 联系方式列表。 
        :type phone: list[str]
        :param address: 地址列表。 
        :type address: list[str]
        :param email: 邮箱列表。 
        :type email: list[str]
        :param fax: 传真列表。 
        :type fax: list[str]
        :param postcode: 邮编列表。 
        :type postcode: list[str]
        :param website: 公司网址列表。 
        :type website: list[str]
        :param extra_info_list: 其余信息列表。 
        :type extra_info_list: list[:class:`huaweicloudsdkocr.v1.ExtraInfoList`]
        :param adjusted_image: 返回矫正后的名片图像的BASE64编码。 
        :type adjusted_image: str
        """
        
        

        self._name = None
        self._title = None
        self._company = None
        self._department = None
        self._phone = None
        self._address = None
        self._email = None
        self._fax = None
        self._postcode = None
        self._website = None
        self._extra_info_list = None
        self._adjusted_image = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if title is not None:
            self.title = title
        if company is not None:
            self.company = company
        if department is not None:
            self.department = department
        if phone is not None:
            self.phone = phone
        if address is not None:
            self.address = address
        if email is not None:
            self.email = email
        if fax is not None:
            self.fax = fax
        if postcode is not None:
            self.postcode = postcode
        if website is not None:
            self.website = website
        if extra_info_list is not None:
            self.extra_info_list = extra_info_list
        if adjusted_image is not None:
            self.adjusted_image = adjusted_image

    @property
    def name(self):
        """Gets the name of this BusinessCardResult.

        姓名列表。 

        :return: The name of this BusinessCardResult.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BusinessCardResult.

        姓名列表。 

        :param name: The name of this BusinessCardResult.
        :type name: list[str]
        """
        self._name = name

    @property
    def title(self):
        """Gets the title of this BusinessCardResult.

        职位头衔列表。 

        :return: The title of this BusinessCardResult.
        :rtype: list[str]
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this BusinessCardResult.

        职位头衔列表。 

        :param title: The title of this BusinessCardResult.
        :type title: list[str]
        """
        self._title = title

    @property
    def company(self):
        """Gets the company of this BusinessCardResult.

        公司列表。 

        :return: The company of this BusinessCardResult.
        :rtype: list[str]
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this BusinessCardResult.

        公司列表。 

        :param company: The company of this BusinessCardResult.
        :type company: list[str]
        """
        self._company = company

    @property
    def department(self):
        """Gets the department of this BusinessCardResult.

        部门列表。 

        :return: The department of this BusinessCardResult.
        :rtype: list[str]
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this BusinessCardResult.

        部门列表。 

        :param department: The department of this BusinessCardResult.
        :type department: list[str]
        """
        self._department = department

    @property
    def phone(self):
        """Gets the phone of this BusinessCardResult.

        联系方式列表。 

        :return: The phone of this BusinessCardResult.
        :rtype: list[str]
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this BusinessCardResult.

        联系方式列表。 

        :param phone: The phone of this BusinessCardResult.
        :type phone: list[str]
        """
        self._phone = phone

    @property
    def address(self):
        """Gets the address of this BusinessCardResult.

        地址列表。 

        :return: The address of this BusinessCardResult.
        :rtype: list[str]
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this BusinessCardResult.

        地址列表。 

        :param address: The address of this BusinessCardResult.
        :type address: list[str]
        """
        self._address = address

    @property
    def email(self):
        """Gets the email of this BusinessCardResult.

        邮箱列表。 

        :return: The email of this BusinessCardResult.
        :rtype: list[str]
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BusinessCardResult.

        邮箱列表。 

        :param email: The email of this BusinessCardResult.
        :type email: list[str]
        """
        self._email = email

    @property
    def fax(self):
        """Gets the fax of this BusinessCardResult.

        传真列表。 

        :return: The fax of this BusinessCardResult.
        :rtype: list[str]
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this BusinessCardResult.

        传真列表。 

        :param fax: The fax of this BusinessCardResult.
        :type fax: list[str]
        """
        self._fax = fax

    @property
    def postcode(self):
        """Gets the postcode of this BusinessCardResult.

        邮编列表。 

        :return: The postcode of this BusinessCardResult.
        :rtype: list[str]
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this BusinessCardResult.

        邮编列表。 

        :param postcode: The postcode of this BusinessCardResult.
        :type postcode: list[str]
        """
        self._postcode = postcode

    @property
    def website(self):
        """Gets the website of this BusinessCardResult.

        公司网址列表。 

        :return: The website of this BusinessCardResult.
        :rtype: list[str]
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this BusinessCardResult.

        公司网址列表。 

        :param website: The website of this BusinessCardResult.
        :type website: list[str]
        """
        self._website = website

    @property
    def extra_info_list(self):
        """Gets the extra_info_list of this BusinessCardResult.

        其余信息列表。 

        :return: The extra_info_list of this BusinessCardResult.
        :rtype: list[:class:`huaweicloudsdkocr.v1.ExtraInfoList`]
        """
        return self._extra_info_list

    @extra_info_list.setter
    def extra_info_list(self, extra_info_list):
        """Sets the extra_info_list of this BusinessCardResult.

        其余信息列表。 

        :param extra_info_list: The extra_info_list of this BusinessCardResult.
        :type extra_info_list: list[:class:`huaweicloudsdkocr.v1.ExtraInfoList`]
        """
        self._extra_info_list = extra_info_list

    @property
    def adjusted_image(self):
        """Gets the adjusted_image of this BusinessCardResult.

        返回矫正后的名片图像的BASE64编码。 

        :return: The adjusted_image of this BusinessCardResult.
        :rtype: str
        """
        return self._adjusted_image

    @adjusted_image.setter
    def adjusted_image(self, adjusted_image):
        """Sets the adjusted_image of this BusinessCardResult.

        返回矫正后的名片图像的BASE64编码。 

        :param adjusted_image: The adjusted_image of this BusinessCardResult.
        :type adjusted_image: str
        """
        self._adjusted_image = adjusted_image

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
        if not isinstance(other, BusinessCardResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
