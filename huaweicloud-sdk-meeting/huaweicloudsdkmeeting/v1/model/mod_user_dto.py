# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModUserDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'english_name': 'str',
        'phone': 'str',
        'country': 'str',
        'email': 'str',
        'vmr_id': 'str',
        'dept_code': 'str',
        'signature': 'str',
        'title': 'str',
        'desc': 'str',
        'status': 'int',
        'sort_level': 'int',
        'hide_phone': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'english_name': 'englishName',
        'phone': 'phone',
        'country': 'country',
        'email': 'email',
        'vmr_id': 'vmrId',
        'dept_code': 'deptCode',
        'signature': 'signature',
        'title': 'title',
        'desc': 'desc',
        'status': 'status',
        'sort_level': 'sortLevel',
        'hide_phone': 'hidePhone'
    }

    def __init__(self, name=None, english_name=None, phone=None, country=None, email=None, vmr_id=None, dept_code=None, signature=None, title=None, desc=None, status=None, sort_level=None, hide_phone=None):
        """ModUserDTO - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._english_name = None
        self._phone = None
        self._country = None
        self._email = None
        self._vmr_id = None
        self._dept_code = None
        self._signature = None
        self._title = None
        self._desc = None
        self._status = None
        self._sort_level = None
        self._hide_phone = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if english_name is not None:
            self.english_name = english_name
        if phone is not None:
            self.phone = phone
        if country is not None:
            self.country = country
        if email is not None:
            self.email = email
        if vmr_id is not None:
            self.vmr_id = vmr_id
        if dept_code is not None:
            self.dept_code = dept_code
        if signature is not None:
            self.signature = signature
        if title is not None:
            self.title = title
        if desc is not None:
            self.desc = desc
        if status is not None:
            self.status = status
        if sort_level is not None:
            self.sort_level = sort_level
        if hide_phone is not None:
            self.hide_phone = hide_phone

    @property
    def name(self):
        """Gets the name of this ModUserDTO.

        企业用户姓名。 maxLength：64 minLength：1

        :return: The name of this ModUserDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModUserDTO.

        企业用户姓名。 maxLength：64 minLength：1

        :param name: The name of this ModUserDTO.
        :type: str
        """
        self._name = name

    @property
    def english_name(self):
        """Gets the english_name of this ModUserDTO.

        企业用户的英文姓名。 maxLength：64 minLength：0

        :return: The english_name of this ModUserDTO.
        :rtype: str
        """
        return self._english_name

    @english_name.setter
    def english_name(self, english_name):
        """Sets the english_name of this ModUserDTO.

        企业用户的英文姓名。 maxLength：64 minLength：0

        :param english_name: The english_name of this ModUserDTO.
        :type: str
        """
        self._english_name = english_name

    @property
    def phone(self):
        """Gets the phone of this ModUserDTO.

        手机号，必须加上国家码。 例如中国大陆手机为“+86xxxxxxxxxxx”。当填写手机号时 “country”参数必填。 手机号只允许输入纯数字。 说明：手机号或者邮箱至少填写一个。 maxLength：32 minLength：0

        :return: The phone of this ModUserDTO.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ModUserDTO.

        手机号，必须加上国家码。 例如中国大陆手机为“+86xxxxxxxxxxx”。当填写手机号时 “country”参数必填。 手机号只允许输入纯数字。 说明：手机号或者邮箱至少填写一个。 maxLength：32 minLength：0

        :param phone: The phone of this ModUserDTO.
        :type: str
        """
        self._phone = phone

    @property
    def country(self):
        """Gets the country of this ModUserDTO.

        若smsNumber为手机号,则需带上手机号所属的国家。 例如国家为中国大陆则country参数取值为chinaPR 国家和国家码的对应关系请参考：https://support.huaweicloud.com/api-meeting/meeting_21_0109.html 

        :return: The country of this ModUserDTO.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ModUserDTO.

        若smsNumber为手机号,则需带上手机号所属的国家。 例如国家为中国大陆则country参数取值为chinaPR 国家和国家码的对应关系请参考：https://support.huaweicloud.com/api-meeting/meeting_21_0109.html 

        :param country: The country of this ModUserDTO.
        :type: str
        """
        self._country = country

    @property
    def email(self):
        """Gets the email of this ModUserDTO.

        邮箱 maxLength：255 minLength：0

        :return: The email of this ModUserDTO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ModUserDTO.

        邮箱 maxLength：255 minLength：0

        :param email: The email of this ModUserDTO.
        :type: str
        """
        self._email = email

    @property
    def vmr_id(self):
        """Gets the vmr_id of this ModUserDTO.

        虚拟会议室ID，若不携带则后台默认生成。 maxLength：32 minLength：0

        :return: The vmr_id of this ModUserDTO.
        :rtype: str
        """
        return self._vmr_id

    @vmr_id.setter
    def vmr_id(self, vmr_id):
        """Sets the vmr_id of this ModUserDTO.

        虚拟会议室ID，若不携带则后台默认生成。 maxLength：32 minLength：0

        :param vmr_id: The vmr_id of this ModUserDTO.
        :type: str
        """
        self._vmr_id = vmr_id

    @property
    def dept_code(self):
        """Gets the dept_code of this ModUserDTO.

        部门编号，若不携带则默认根部门 默认值：1 maxLength：32 minLength：0

        :return: The dept_code of this ModUserDTO.
        :rtype: str
        """
        return self._dept_code

    @dept_code.setter
    def dept_code(self, dept_code):
        """Sets the dept_code of this ModUserDTO.

        部门编号，若不携带则默认根部门 默认值：1 maxLength：32 minLength：0

        :param dept_code: The dept_code of this ModUserDTO.
        :type: str
        """
        self._dept_code = dept_code

    @property
    def signature(self):
        """Gets the signature of this ModUserDTO.

        签名 maxLength：512 minLength：0

        :return: The signature of this ModUserDTO.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this ModUserDTO.

        签名 maxLength：512 minLength：0

        :param signature: The signature of this ModUserDTO.
        :type: str
        """
        self._signature = signature

    @property
    def title(self):
        """Gets the title of this ModUserDTO.

        职位 maxLength：32 minLength：0

        :return: The title of this ModUserDTO.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ModUserDTO.

        职位 maxLength：32 minLength：0

        :param title: The title of this ModUserDTO.
        :type: str
        """
        self._title = title

    @property
    def desc(self):
        """Gets the desc of this ModUserDTO.

        备注 maxLength：128 minLength：0

        :return: The desc of this ModUserDTO.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this ModUserDTO.

        备注 maxLength：128 minLength：0

        :param desc: The desc of this ModUserDTO.
        :type: str
        """
        self._desc = desc

    @property
    def status(self):
        """Gets the status of this ModUserDTO.

        用户状态 * 0、正常 * 1、停用 默认值：0

        :return: The status of this ModUserDTO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ModUserDTO.

        用户状态 * 0、正常 * 1、停用 默认值：0

        :param status: The status of this ModUserDTO.
        :type: int
        """
        self._status = status

    @property
    def sort_level(self):
        """Gets the sort_level of this ModUserDTO.

        通讯录排序等级，序号越低优先级越高。 默认值：10000 maximum：10000 minimum：1

        :return: The sort_level of this ModUserDTO.
        :rtype: int
        """
        return self._sort_level

    @sort_level.setter
    def sort_level(self, sort_level):
        """Sets the sort_level of this ModUserDTO.

        通讯录排序等级，序号越低优先级越高。 默认值：10000 maximum：10000 minimum：1

        :param sort_level: The sort_level of this ModUserDTO.
        :type: int
        """
        self._sort_level = sort_level

    @property
    def hide_phone(self):
        """Gets the hide_phone of this ModUserDTO.

        是否隐藏手机号码 默认值：false 

        :return: The hide_phone of this ModUserDTO.
        :rtype: bool
        """
        return self._hide_phone

    @hide_phone.setter
    def hide_phone(self, hide_phone):
        """Sets the hide_phone of this ModUserDTO.

        是否隐藏手机号码 默认值：false 

        :param hide_phone: The hide_phone of this ModUserDTO.
        :type: bool
        """
        self._hide_phone = hide_phone

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
        if not isinstance(other, ModUserDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
