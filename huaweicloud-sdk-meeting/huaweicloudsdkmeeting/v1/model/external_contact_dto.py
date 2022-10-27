# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalContactDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'other_number': 'str',
        'other_number_country': 'str',
        'country': 'str',
        'phone': 'str',
        'email': 'str',
        'corp_name': 'str',
        'dept_name': 'str',
        'position': 'str',
        'address': 'str',
        'remarks': 'str',
        'id': 'str',
        'name': 'str',
        'custom_number': 'str',
        'update_time': 'float',
        'type': 'str'
    }

    attribute_map = {
        'other_number': 'otherNumber',
        'other_number_country': 'otherNumberCountry',
        'country': 'country',
        'phone': 'phone',
        'email': 'email',
        'corp_name': 'corpName',
        'dept_name': 'deptName',
        'position': 'position',
        'address': 'address',
        'remarks': 'remarks',
        'id': 'id',
        'name': 'name',
        'custom_number': 'customNumber',
        'update_time': 'updateTime',
        'type': 'type'
    }

    def __init__(self, other_number=None, other_number_country=None, country=None, phone=None, email=None, corp_name=None, dept_name=None, position=None, address=None, remarks=None, id=None, name=None, custom_number=None, update_time=None, type=None):
        """ExternalContactDTO

        The model defined in huaweicloud sdk

        :param other_number: 其他号码。 &gt; * 其他号码必须以国家码作为前缀 &gt; * otherNumber填写时，otherNumberCountry也必须填写 &gt; * 如果要清空手机号配置，则otherNumberCountry和otherNumber都要置为\&quot;\&quot; 
        :type other_number: str
        :param other_number_country: [[其他号码所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 
        :type other_number_country: str
        :param country: [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 
        :type country: str
        :param phone: 手机号。 &gt; * 手机号必须以国家码作为前缀 &gt; * phone填写时，country也必须填写 &gt; * 如果要清空手机号配置，则country和phone都要置为\&quot;\&quot; 
        :type phone: str
        :param email: 邮箱。
        :type email: str
        :param corp_name: 公司名称。
        :type corp_name: str
        :param dept_name: 部门。
        :type dept_name: str
        :param position: 职务。
        :type position: str
        :param address: 个人地址。
        :type address: str
        :param remarks: 备注。
        :type remarks: str
        :param id: 外部联系人UUID。
        :type id: str
        :param name: 姓名。
        :type name: str
        :param custom_number: 外部联系人自定义号码。 &gt; 仅VDC场景下使用。 
        :type custom_number: str
        :param update_time: 用户信息最后更新时间戳。
        :type update_time: float
        :param type: 外部联系人类型。 * PERSONAL：个人外部联系人 * CORP：企业外部联系人 
        :type type: str
        """
        
        

        self._other_number = None
        self._other_number_country = None
        self._country = None
        self._phone = None
        self._email = None
        self._corp_name = None
        self._dept_name = None
        self._position = None
        self._address = None
        self._remarks = None
        self._id = None
        self._name = None
        self._custom_number = None
        self._update_time = None
        self._type = None
        self.discriminator = None

        if other_number is not None:
            self.other_number = other_number
        if other_number_country is not None:
            self.other_number_country = other_number_country
        if country is not None:
            self.country = country
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email
        if corp_name is not None:
            self.corp_name = corp_name
        if dept_name is not None:
            self.dept_name = dept_name
        if position is not None:
            self.position = position
        if address is not None:
            self.address = address
        if remarks is not None:
            self.remarks = remarks
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if custom_number is not None:
            self.custom_number = custom_number
        if update_time is not None:
            self.update_time = update_time
        if type is not None:
            self.type = type

    @property
    def other_number(self):
        """Gets the other_number of this ExternalContactDTO.

        其他号码。 > * 其他号码必须以国家码作为前缀 > * otherNumber填写时，otherNumberCountry也必须填写 > * 如果要清空手机号配置，则otherNumberCountry和otherNumber都要置为\"\" 

        :return: The other_number of this ExternalContactDTO.
        :rtype: str
        """
        return self._other_number

    @other_number.setter
    def other_number(self, other_number):
        """Sets the other_number of this ExternalContactDTO.

        其他号码。 > * 其他号码必须以国家码作为前缀 > * otherNumber填写时，otherNumberCountry也必须填写 > * 如果要清空手机号配置，则otherNumberCountry和otherNumber都要置为\"\" 

        :param other_number: The other_number of this ExternalContactDTO.
        :type other_number: str
        """
        self._other_number = other_number

    @property
    def other_number_country(self):
        """Gets the other_number_country of this ExternalContactDTO.

        [[其他号码所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :return: The other_number_country of this ExternalContactDTO.
        :rtype: str
        """
        return self._other_number_country

    @other_number_country.setter
    def other_number_country(self, other_number_country):
        """Sets the other_number_country of this ExternalContactDTO.

        [[其他号码所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :param other_number_country: The other_number_country of this ExternalContactDTO.
        :type other_number_country: str
        """
        self._other_number_country = other_number_country

    @property
    def country(self):
        """Gets the country of this ExternalContactDTO.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :return: The country of this ExternalContactDTO.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ExternalContactDTO.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :param country: The country of this ExternalContactDTO.
        :type country: str
        """
        self._country = country

    @property
    def phone(self):
        """Gets the phone of this ExternalContactDTO.

        手机号。 > * 手机号必须以国家码作为前缀 > * phone填写时，country也必须填写 > * 如果要清空手机号配置，则country和phone都要置为\"\" 

        :return: The phone of this ExternalContactDTO.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ExternalContactDTO.

        手机号。 > * 手机号必须以国家码作为前缀 > * phone填写时，country也必须填写 > * 如果要清空手机号配置，则country和phone都要置为\"\" 

        :param phone: The phone of this ExternalContactDTO.
        :type phone: str
        """
        self._phone = phone

    @property
    def email(self):
        """Gets the email of this ExternalContactDTO.

        邮箱。

        :return: The email of this ExternalContactDTO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ExternalContactDTO.

        邮箱。

        :param email: The email of this ExternalContactDTO.
        :type email: str
        """
        self._email = email

    @property
    def corp_name(self):
        """Gets the corp_name of this ExternalContactDTO.

        公司名称。

        :return: The corp_name of this ExternalContactDTO.
        :rtype: str
        """
        return self._corp_name

    @corp_name.setter
    def corp_name(self, corp_name):
        """Sets the corp_name of this ExternalContactDTO.

        公司名称。

        :param corp_name: The corp_name of this ExternalContactDTO.
        :type corp_name: str
        """
        self._corp_name = corp_name

    @property
    def dept_name(self):
        """Gets the dept_name of this ExternalContactDTO.

        部门。

        :return: The dept_name of this ExternalContactDTO.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this ExternalContactDTO.

        部门。

        :param dept_name: The dept_name of this ExternalContactDTO.
        :type dept_name: str
        """
        self._dept_name = dept_name

    @property
    def position(self):
        """Gets the position of this ExternalContactDTO.

        职务。

        :return: The position of this ExternalContactDTO.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this ExternalContactDTO.

        职务。

        :param position: The position of this ExternalContactDTO.
        :type position: str
        """
        self._position = position

    @property
    def address(self):
        """Gets the address of this ExternalContactDTO.

        个人地址。

        :return: The address of this ExternalContactDTO.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ExternalContactDTO.

        个人地址。

        :param address: The address of this ExternalContactDTO.
        :type address: str
        """
        self._address = address

    @property
    def remarks(self):
        """Gets the remarks of this ExternalContactDTO.

        备注。

        :return: The remarks of this ExternalContactDTO.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this ExternalContactDTO.

        备注。

        :param remarks: The remarks of this ExternalContactDTO.
        :type remarks: str
        """
        self._remarks = remarks

    @property
    def id(self):
        """Gets the id of this ExternalContactDTO.

        外部联系人UUID。

        :return: The id of this ExternalContactDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalContactDTO.

        外部联系人UUID。

        :param id: The id of this ExternalContactDTO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ExternalContactDTO.

        姓名。

        :return: The name of this ExternalContactDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExternalContactDTO.

        姓名。

        :param name: The name of this ExternalContactDTO.
        :type name: str
        """
        self._name = name

    @property
    def custom_number(self):
        """Gets the custom_number of this ExternalContactDTO.

        外部联系人自定义号码。 > 仅VDC场景下使用。 

        :return: The custom_number of this ExternalContactDTO.
        :rtype: str
        """
        return self._custom_number

    @custom_number.setter
    def custom_number(self, custom_number):
        """Sets the custom_number of this ExternalContactDTO.

        外部联系人自定义号码。 > 仅VDC场景下使用。 

        :param custom_number: The custom_number of this ExternalContactDTO.
        :type custom_number: str
        """
        self._custom_number = custom_number

    @property
    def update_time(self):
        """Gets the update_time of this ExternalContactDTO.

        用户信息最后更新时间戳。

        :return: The update_time of this ExternalContactDTO.
        :rtype: float
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ExternalContactDTO.

        用户信息最后更新时间戳。

        :param update_time: The update_time of this ExternalContactDTO.
        :type update_time: float
        """
        self._update_time = update_time

    @property
    def type(self):
        """Gets the type of this ExternalContactDTO.

        外部联系人类型。 * PERSONAL：个人外部联系人 * CORP：企业外部联系人 

        :return: The type of this ExternalContactDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExternalContactDTO.

        外部联系人类型。 * PERSONAL：个人外部联系人 * CORP：企业外部联系人 

        :param type: The type of this ExternalContactDTO.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ExternalContactDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
