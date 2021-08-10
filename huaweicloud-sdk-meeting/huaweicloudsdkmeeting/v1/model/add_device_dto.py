# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDeviceDTO:


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
        'model': 'str',
        'sn': 'str',
        'prj_code_mode': 'int',
        'dept_code': 'str',
        'phone': 'str',
        'country': 'str',
        'email': 'str',
        'description': 'str',
        'status': 'int',
        'send_notify': 'str'
    }

    attribute_map = {
        'name': 'name',
        'model': 'model',
        'sn': 'sn',
        'prj_code_mode': 'prjCodeMode',
        'dept_code': 'deptCode',
        'phone': 'phone',
        'country': 'country',
        'email': 'email',
        'description': 'description',
        'status': 'status',
        'send_notify': 'sendNotify'
    }

    def __init__(self, name=None, model=None, sn=None, prj_code_mode=None, dept_code=None, phone=None, country=None, email=None, description=None, status=None, send_notify=None):
        """AddDeviceDTO - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._model = None
        self._sn = None
        self._prj_code_mode = None
        self._dept_code = None
        self._phone = None
        self._country = None
        self._email = None
        self._description = None
        self._status = None
        self._send_notify = None
        self.discriminator = None

        self.name = name
        self.model = model
        if sn is not None:
            self.sn = sn
        if prj_code_mode is not None:
            self.prj_code_mode = prj_code_mode
        if dept_code is not None:
            self.dept_code = dept_code
        if phone is not None:
            self.phone = phone
        if country is not None:
            self.country = country
        if email is not None:
            self.email = email
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if send_notify is not None:
            self.send_notify = send_notify

    @property
    def name(self):
        """Gets the name of this AddDeviceDTO.

        终端名称，可以自定义，建议为具体位置，方便识别。 maxLength：64 minLength：1

        :return: The name of this AddDeviceDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddDeviceDTO.

        终端名称，可以自定义，建议为具体位置，方便识别。 maxLength：64 minLength：1

        :param name: The name of this AddDeviceDTO.
        :type: str
        """
        self._name = name

    @property
    def model(self):
        """Gets the model of this AddDeviceDTO.

        终端型号，枚举类型。当前支持TE系列和部分第三方硬件终端，具体的终端类型可以通过获取所有终端类型接口查询。 maxLength：128 minLength：1

        :return: The model of this AddDeviceDTO.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this AddDeviceDTO.

        终端型号，枚举类型。当前支持TE系列和部分第三方硬件终端，具体的终端类型可以通过获取所有终端类型接口查询。 maxLength：128 minLength：1

        :param model: The model of this AddDeviceDTO.
        :type: str
        """
        self._model = model

    @property
    def sn(self):
        """Gets the sn of this AddDeviceDTO.

        终端SN码，仅可包含数字、字母和下划线。 maxLength：30 minLength：1

        :return: The sn of this AddDeviceDTO.
        :rtype: str
        """
        return self._sn

    @sn.setter
    def sn(self, sn):
        """Sets the sn of this AddDeviceDTO.

        终端SN码，仅可包含数字、字母和下划线。 maxLength：30 minLength：1

        :param sn: The sn of this AddDeviceDTO.
        :type: str
        """
        self._sn = sn

    @property
    def prj_code_mode(self):
        """Gets the prj_code_mode of this AddDeviceDTO.

        投影码生成模式，默认为自动 - 0、自动(该模式下根据消息上报的IP地址内部控制复杂度：   私网地址配置成简单模式；公网地址配置成复杂模式) - 1、简单 - 2、复杂

        :return: The prj_code_mode of this AddDeviceDTO.
        :rtype: int
        """
        return self._prj_code_mode

    @prj_code_mode.setter
    def prj_code_mode(self, prj_code_mode):
        """Sets the prj_code_mode of this AddDeviceDTO.

        投影码生成模式，默认为自动 - 0、自动(该模式下根据消息上报的IP地址内部控制复杂度：   私网地址配置成简单模式；公网地址配置成复杂模式) - 1、简单 - 2、复杂

        :param prj_code_mode: The prj_code_mode of this AddDeviceDTO.
        :type: int
        """
        self._prj_code_mode = prj_code_mode

    @property
    def dept_code(self):
        """Gets the dept_code of this AddDeviceDTO.

        部门编号，默认为根部门 默认值：1 maxLength：32 minLength：1

        :return: The dept_code of this AddDeviceDTO.
        :rtype: str
        """
        return self._dept_code

    @dept_code.setter
    def dept_code(self, dept_code):
        """Sets the dept_code of this AddDeviceDTO.

        部门编号，默认为根部门 默认值：1 maxLength：32 minLength：1

        :param dept_code: The dept_code of this AddDeviceDTO.
        :type: str
        """
        self._dept_code = dept_code

    @property
    def phone(self):
        """Gets the phone of this AddDeviceDTO.

        手机号，必须加上国家码，例如中国大陆手机为“+86xxxxxxxxxxx”。当填写手机号时 “country”参数必填。 手机号只允许输入纯数字。 maxLength：32 minLength：0 说明： - 手机号或者邮箱至少填写一个。

        :return: The phone of this AddDeviceDTO.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this AddDeviceDTO.

        手机号，必须加上国家码，例如中国大陆手机为“+86xxxxxxxxxxx”。当填写手机号时 “country”参数必填。 手机号只允许输入纯数字。 maxLength：32 minLength：0 说明： - 手机号或者邮箱至少填写一个。

        :param phone: The phone of this AddDeviceDTO.
        :type: str
        """
        self._phone = phone

    @property
    def country(self):
        """Gets the country of this AddDeviceDTO.

        若smsNumber为手机号,则需带上手机号所属的国家。 例如国家为中国大陆则country参数取值为chinaPR 国家和国家码的对应关系请参考：https://support.huaweicloud.com/api-meeting/meeting_21_0109.html 

        :return: The country of this AddDeviceDTO.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AddDeviceDTO.

        若smsNumber为手机号,则需带上手机号所属的国家。 例如国家为中国大陆则country参数取值为chinaPR 国家和国家码的对应关系请参考：https://support.huaweicloud.com/api-meeting/meeting_21_0109.html 

        :param country: The country of this AddDeviceDTO.
        :type: str
        """
        self._country = country

    @property
    def email(self):
        """Gets the email of this AddDeviceDTO.

        统一邮箱格式 maxLength：255 minLength：0

        :return: The email of this AddDeviceDTO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AddDeviceDTO.

        统一邮箱格式 maxLength：255 minLength：0

        :param email: The email of this AddDeviceDTO.
        :type: str
        """
        self._email = email

    @property
    def description(self):
        """Gets the description of this AddDeviceDTO.

        终端描述 maxLength：128 minLength：0

        :return: The description of this AddDeviceDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddDeviceDTO.

        终端描述 maxLength：128 minLength：0

        :param description: The description of this AddDeviceDTO.
        :type: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this AddDeviceDTO.

        终端状态 * 0、正常 * 1、冻结\" 默认值：0。 

        :return: The status of this AddDeviceDTO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AddDeviceDTO.

        终端状态 * 0、正常 * 1、冻结\" 默认值：0。 

        :param status: The status of this AddDeviceDTO.
        :type: int
        """
        self._status = status

    @property
    def send_notify(self):
        """Gets the send_notify of this AddDeviceDTO.

        是否发送邮件和短信通知。 * 0：不发送 * 不填或者其他值就发送

        :return: The send_notify of this AddDeviceDTO.
        :rtype: str
        """
        return self._send_notify

    @send_notify.setter
    def send_notify(self, send_notify):
        """Sets the send_notify of this AddDeviceDTO.

        是否发送邮件和短信通知。 * 0：不发送 * 不填或者其他值就发送

        :param send_notify: The send_notify of this AddDeviceDTO.
        :type: str
        """
        self._send_notify = send_notify

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
        if not isinstance(other, AddDeviceDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
