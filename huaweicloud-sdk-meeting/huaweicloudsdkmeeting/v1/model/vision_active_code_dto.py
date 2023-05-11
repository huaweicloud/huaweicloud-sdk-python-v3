# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VisionActiveCodeDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dev_type': 'str',
        'dept_code': 'str',
        'dev_name': 'str',
        'description': 'str',
        'sms_number': 'str',
        'country': 'str',
        'email_addr': 'str'
    }

    attribute_map = {
        'dev_type': 'devType',
        'dept_code': 'deptCode',
        'dev_name': 'devName',
        'description': 'description',
        'sms_number': 'smsNumber',
        'country': 'country',
        'email_addr': 'emailAddr'
    }

    def __init__(self, dev_type=None, dept_code=None, dev_name=None, description=None, sms_number=None, country=None, email_addr=None):
        """VisionActiveCodeDTO

        The model defined in huaweicloud sdk

        :param dev_type: 终端类型。 - idea-hub：智能协作大屏 - huawei-vision：智慧屏TV - welink-desktop(iwb)：SmartRooms会议版 - smart-rooms：SmartRooms完整版 
        :type dev_type: str
        :param dept_code: 部门编码，若不携带则默认根部门。
        :type dept_code: str
        :param dev_name: 终端的名称。
        :type dev_name: str
        :param description: 描述信息。
        :type description: str
        :param sms_number: 号码信息，如果为手机号，必须加上国家码。 例如中国大陆手机+86xxxxxxx，当填写手机号时 “country”参数必填,手机格式必须满足(^$|^[+]?[0-9]+$) 
        :type sms_number: str
        :param country: [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 
        :type country: str
        :param email_addr: 邮箱地址。 &gt; 如无中国大陆手机号，则邮箱必填。 
        :type email_addr: str
        """
        
        

        self._dev_type = None
        self._dept_code = None
        self._dev_name = None
        self._description = None
        self._sms_number = None
        self._country = None
        self._email_addr = None
        self.discriminator = None

        self.dev_type = dev_type
        if dept_code is not None:
            self.dept_code = dept_code
        self.dev_name = dev_name
        if description is not None:
            self.description = description
        if sms_number is not None:
            self.sms_number = sms_number
        if country is not None:
            self.country = country
        if email_addr is not None:
            self.email_addr = email_addr

    @property
    def dev_type(self):
        """Gets the dev_type of this VisionActiveCodeDTO.

        终端类型。 - idea-hub：智能协作大屏 - huawei-vision：智慧屏TV - welink-desktop(iwb)：SmartRooms会议版 - smart-rooms：SmartRooms完整版 

        :return: The dev_type of this VisionActiveCodeDTO.
        :rtype: str
        """
        return self._dev_type

    @dev_type.setter
    def dev_type(self, dev_type):
        """Sets the dev_type of this VisionActiveCodeDTO.

        终端类型。 - idea-hub：智能协作大屏 - huawei-vision：智慧屏TV - welink-desktop(iwb)：SmartRooms会议版 - smart-rooms：SmartRooms完整版 

        :param dev_type: The dev_type of this VisionActiveCodeDTO.
        :type dev_type: str
        """
        self._dev_type = dev_type

    @property
    def dept_code(self):
        """Gets the dept_code of this VisionActiveCodeDTO.

        部门编码，若不携带则默认根部门。

        :return: The dept_code of this VisionActiveCodeDTO.
        :rtype: str
        """
        return self._dept_code

    @dept_code.setter
    def dept_code(self, dept_code):
        """Sets the dept_code of this VisionActiveCodeDTO.

        部门编码，若不携带则默认根部门。

        :param dept_code: The dept_code of this VisionActiveCodeDTO.
        :type dept_code: str
        """
        self._dept_code = dept_code

    @property
    def dev_name(self):
        """Gets the dev_name of this VisionActiveCodeDTO.

        终端的名称。

        :return: The dev_name of this VisionActiveCodeDTO.
        :rtype: str
        """
        return self._dev_name

    @dev_name.setter
    def dev_name(self, dev_name):
        """Sets the dev_name of this VisionActiveCodeDTO.

        终端的名称。

        :param dev_name: The dev_name of this VisionActiveCodeDTO.
        :type dev_name: str
        """
        self._dev_name = dev_name

    @property
    def description(self):
        """Gets the description of this VisionActiveCodeDTO.

        描述信息。

        :return: The description of this VisionActiveCodeDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VisionActiveCodeDTO.

        描述信息。

        :param description: The description of this VisionActiveCodeDTO.
        :type description: str
        """
        self._description = description

    @property
    def sms_number(self):
        """Gets the sms_number of this VisionActiveCodeDTO.

        号码信息，如果为手机号，必须加上国家码。 例如中国大陆手机+86xxxxxxx，当填写手机号时 “country”参数必填,手机格式必须满足(^$|^[+]?[0-9]+$) 

        :return: The sms_number of this VisionActiveCodeDTO.
        :rtype: str
        """
        return self._sms_number

    @sms_number.setter
    def sms_number(self, sms_number):
        """Sets the sms_number of this VisionActiveCodeDTO.

        号码信息，如果为手机号，必须加上国家码。 例如中国大陆手机+86xxxxxxx，当填写手机号时 “country”参数必填,手机格式必须满足(^$|^[+]?[0-9]+$) 

        :param sms_number: The sms_number of this VisionActiveCodeDTO.
        :type sms_number: str
        """
        self._sms_number = sms_number

    @property
    def country(self):
        """Gets the country of this VisionActiveCodeDTO.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :return: The country of this VisionActiveCodeDTO.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this VisionActiveCodeDTO.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :param country: The country of this VisionActiveCodeDTO.
        :type country: str
        """
        self._country = country

    @property
    def email_addr(self):
        """Gets the email_addr of this VisionActiveCodeDTO.

        邮箱地址。 > 如无中国大陆手机号，则邮箱必填。 

        :return: The email_addr of this VisionActiveCodeDTO.
        :rtype: str
        """
        return self._email_addr

    @email_addr.setter
    def email_addr(self, email_addr):
        """Sets the email_addr of this VisionActiveCodeDTO.

        邮箱地址。 > 如无中国大陆手机号，则邮箱必填。 

        :param email_addr: The email_addr of this VisionActiveCodeDTO.
        :type email_addr: str
        """
        self._email_addr = email_addr

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
        if not isinstance(other, VisionActiveCodeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
