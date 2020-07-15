# coding: utf-8

import pprint
import re

import six





class QueryDeviceResultDTO:


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
        'type': 'str',
        'model': 'str',
        'sn': 'str',
        'account': 'str',
        'number': 'str',
        'prj_code_mode': 'int',
        'dept_code': 'str',
        'dept_name': 'str',
        'dept_name_path': 'str',
        'phone': 'str',
        'country': 'str',
        'email': 'str',
        'description': 'str',
        'status': 'int'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'model': 'model',
        'sn': 'sn',
        'account': 'account',
        'number': 'number',
        'prj_code_mode': 'prjCodeMode',
        'dept_code': 'deptCode',
        'dept_name': 'deptName',
        'dept_name_path': 'deptNamePath',
        'phone': 'phone',
        'country': 'country',
        'email': 'email',
        'description': 'description',
        'status': 'status'
    }

    def __init__(self, name=None, type=None, model=None, sn=None, account=None, number=None, prj_code_mode=None, dept_code=None, dept_name=None, dept_name_path=None, phone=None, country=None, email=None, description=None, status=None):
        """QueryDeviceResultDTO - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._type = None
        self._model = None
        self._sn = None
        self._account = None
        self._number = None
        self._prj_code_mode = None
        self._dept_code = None
        self._dept_name = None
        self._dept_name_path = None
        self._phone = None
        self._country = None
        self._email = None
        self._description = None
        self._status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if model is not None:
            self.model = model
        if sn is not None:
            self.sn = sn
        if account is not None:
            self.account = account
        if number is not None:
            self.number = number
        if prj_code_mode is not None:
            self.prj_code_mode = prj_code_mode
        if dept_code is not None:
            self.dept_code = dept_code
        if dept_name is not None:
            self.dept_name = dept_name
        if dept_name_path is not None:
            self.dept_name_path = dept_name_path
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

    @property
    def name(self):
        """Gets the name of this QueryDeviceResultDTO.

        终端名称。

        :return: The name of this QueryDeviceResultDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueryDeviceResultDTO.

        终端名称。

        :param name: The name of this QueryDeviceResultDTO.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this QueryDeviceResultDTO.

        终端类型，区分自研和第三方终端。

        :return: The type of this QueryDeviceResultDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QueryDeviceResultDTO.

        终端类型，区分自研和第三方终端。

        :param type: The type of this QueryDeviceResultDTO.
        :type: str
        """
        self._type = type

    @property
    def model(self):
        """Gets the model of this QueryDeviceResultDTO.

        终端型号，枚举类型。当前支持TE系列硬件终端，具体的终端类型可以通过获取所有终端类型接口查询。

        :return: The model of this QueryDeviceResultDTO.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this QueryDeviceResultDTO.

        终端型号，枚举类型。当前支持TE系列硬件终端，具体的终端类型可以通过获取所有终端类型接口查询。

        :param model: The model of this QueryDeviceResultDTO.
        :type: str
        """
        self._model = model

    @property
    def sn(self):
        """Gets the sn of this QueryDeviceResultDTO.

        终端SN号，仅可包含数字、字母和下划线。

        :return: The sn of this QueryDeviceResultDTO.
        :rtype: str
        """
        return self._sn

    @sn.setter
    def sn(self, sn):
        """Sets the sn of this QueryDeviceResultDTO.

        终端SN号，仅可包含数字、字母和下划线。

        :param sn: The sn of this QueryDeviceResultDTO.
        :type: str
        """
        self._sn = sn

    @property
    def account(self):
        """Gets the account of this QueryDeviceResultDTO.

        硬终端对应的内置账号。

        :return: The account of this QueryDeviceResultDTO.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this QueryDeviceResultDTO.

        硬终端对应的内置账号。

        :param account: The account of this QueryDeviceResultDTO.
        :type: str
        """
        self._account = account

    @property
    def number(self):
        """Gets the number of this QueryDeviceResultDTO.

        终端绑定的号码

        :return: The number of this QueryDeviceResultDTO.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this QueryDeviceResultDTO.

        终端绑定的号码

        :param number: The number of this QueryDeviceResultDTO.
        :type: str
        """
        self._number = number

    @property
    def prj_code_mode(self):
        """Gets the prj_code_mode of this QueryDeviceResultDTO.

        投影码生成模式 * 0、自动(该模式下根据消息上报的IP地址内部控制复杂度：私网地址配置成简单模式；公网地址配置成复杂模式) * 1、简单 * 2、复杂 

        :return: The prj_code_mode of this QueryDeviceResultDTO.
        :rtype: int
        """
        return self._prj_code_mode

    @prj_code_mode.setter
    def prj_code_mode(self, prj_code_mode):
        """Sets the prj_code_mode of this QueryDeviceResultDTO.

        投影码生成模式 * 0、自动(该模式下根据消息上报的IP地址内部控制复杂度：私网地址配置成简单模式；公网地址配置成复杂模式) * 1、简单 * 2、复杂 

        :param prj_code_mode: The prj_code_mode of this QueryDeviceResultDTO.
        :type: int
        """
        self._prj_code_mode = prj_code_mode

    @property
    def dept_code(self):
        """Gets the dept_code of this QueryDeviceResultDTO.

        部门编号

        :return: The dept_code of this QueryDeviceResultDTO.
        :rtype: str
        """
        return self._dept_code

    @dept_code.setter
    def dept_code(self, dept_code):
        """Sets the dept_code of this QueryDeviceResultDTO.

        部门编号

        :param dept_code: The dept_code of this QueryDeviceResultDTO.
        :type: str
        """
        self._dept_code = dept_code

    @property
    def dept_name(self):
        """Gets the dept_name of this QueryDeviceResultDTO.

        部门名称

        :return: The dept_name of this QueryDeviceResultDTO.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this QueryDeviceResultDTO.

        部门名称

        :param dept_name: The dept_name of this QueryDeviceResultDTO.
        :type: str
        """
        self._dept_name = dept_name

    @property
    def dept_name_path(self):
        """Gets the dept_name_path of this QueryDeviceResultDTO.

        部门名称路径

        :return: The dept_name_path of this QueryDeviceResultDTO.
        :rtype: str
        """
        return self._dept_name_path

    @dept_name_path.setter
    def dept_name_path(self, dept_name_path):
        """Sets the dept_name_path of this QueryDeviceResultDTO.

        部门名称路径

        :param dept_name_path: The dept_name_path of this QueryDeviceResultDTO.
        :type: str
        """
        self._dept_name_path = dept_name_path

    @property
    def phone(self):
        """Gets the phone of this QueryDeviceResultDTO.

        手机号

        :return: The phone of this QueryDeviceResultDTO.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this QueryDeviceResultDTO.

        手机号

        :param phone: The phone of this QueryDeviceResultDTO.
        :type: str
        """
        self._phone = phone

    @property
    def country(self):
        """Gets the country of this QueryDeviceResultDTO.

        手机号所属的国家

        :return: The country of this QueryDeviceResultDTO.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this QueryDeviceResultDTO.

        手机号所属的国家

        :param country: The country of this QueryDeviceResultDTO.
        :type: str
        """
        self._country = country

    @property
    def email(self):
        """Gets the email of this QueryDeviceResultDTO.

        邮箱

        :return: The email of this QueryDeviceResultDTO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this QueryDeviceResultDTO.

        邮箱

        :param email: The email of this QueryDeviceResultDTO.
        :type: str
        """
        self._email = email

    @property
    def description(self):
        """Gets the description of this QueryDeviceResultDTO.

        终端描述

        :return: The description of this QueryDeviceResultDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueryDeviceResultDTO.

        终端描述

        :param description: The description of this QueryDeviceResultDTO.
        :type: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this QueryDeviceResultDTO.

        终端状态 * 0、正常 * 1、停用\" 

        :return: The status of this QueryDeviceResultDTO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueryDeviceResultDTO.

        终端状态 * 0、正常 * 1、停用\" 

        :param status: The status of this QueryDeviceResultDTO.
        :type: int
        """
        self._status = status

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QueryDeviceResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
