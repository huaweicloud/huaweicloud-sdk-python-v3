# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContactWayInfoV2:

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
        'mobile': 'str',
        'mail': 'str',
        'area': 'str',
        'address': 'str',
        'id_type': 'int',
        'company_name': 'str',
        'id_files': 'list[str]',
        'other_way': 'str'
    }

    attribute_map = {
        'name': 'name',
        'mobile': 'mobile',
        'mail': 'mail',
        'area': 'area',
        'address': 'address',
        'id_type': 'id_type',
        'company_name': 'company_name',
        'id_files': 'id_files',
        'other_way': 'other_way'
    }

    def __init__(self, name=None, mobile=None, mail=None, area=None, address=None, id_type=None, company_name=None, id_files=None, other_way=None):
        """ContactWayInfoV2

        The model defined in huaweicloud sdk

        :param name: 姓名或名称
        :type name: str
        :param mobile: 联系电话
        :type mobile: str
        :param mail: 联系邮箱
        :type mail: str
        :param area: 国家/地区
        :type area: str
        :param address: 地址
        :type address: str
        :param id_type: 身份。企业 10；个人 20；授权代理人 21；律师 22；知识产权所有人 23
        :type id_type: int
        :param company_name: 公司名称
        :type company_name: str
        :param id_files: 身份证明附件列表，至少1个，最多3个
        :type id_files: list[str]
        :param other_way: 其他联系方式
        :type other_way: str
        """
        
        

        self._name = None
        self._mobile = None
        self._mail = None
        self._area = None
        self._address = None
        self._id_type = None
        self._company_name = None
        self._id_files = None
        self._other_way = None
        self.discriminator = None

        self.name = name
        self.mobile = mobile
        if mail is not None:
            self.mail = mail
        if area is not None:
            self.area = area
        if address is not None:
            self.address = address
        self.id_type = id_type
        if company_name is not None:
            self.company_name = company_name
        self.id_files = id_files
        if other_way is not None:
            self.other_way = other_way

    @property
    def name(self):
        """Gets the name of this ContactWayInfoV2.

        姓名或名称

        :return: The name of this ContactWayInfoV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContactWayInfoV2.

        姓名或名称

        :param name: The name of this ContactWayInfoV2.
        :type name: str
        """
        self._name = name

    @property
    def mobile(self):
        """Gets the mobile of this ContactWayInfoV2.

        联系电话

        :return: The mobile of this ContactWayInfoV2.
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this ContactWayInfoV2.

        联系电话

        :param mobile: The mobile of this ContactWayInfoV2.
        :type mobile: str
        """
        self._mobile = mobile

    @property
    def mail(self):
        """Gets the mail of this ContactWayInfoV2.

        联系邮箱

        :return: The mail of this ContactWayInfoV2.
        :rtype: str
        """
        return self._mail

    @mail.setter
    def mail(self, mail):
        """Sets the mail of this ContactWayInfoV2.

        联系邮箱

        :param mail: The mail of this ContactWayInfoV2.
        :type mail: str
        """
        self._mail = mail

    @property
    def area(self):
        """Gets the area of this ContactWayInfoV2.

        国家/地区

        :return: The area of this ContactWayInfoV2.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this ContactWayInfoV2.

        国家/地区

        :param area: The area of this ContactWayInfoV2.
        :type area: str
        """
        self._area = area

    @property
    def address(self):
        """Gets the address of this ContactWayInfoV2.

        地址

        :return: The address of this ContactWayInfoV2.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ContactWayInfoV2.

        地址

        :param address: The address of this ContactWayInfoV2.
        :type address: str
        """
        self._address = address

    @property
    def id_type(self):
        """Gets the id_type of this ContactWayInfoV2.

        身份。企业 10；个人 20；授权代理人 21；律师 22；知识产权所有人 23

        :return: The id_type of this ContactWayInfoV2.
        :rtype: int
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        """Sets the id_type of this ContactWayInfoV2.

        身份。企业 10；个人 20；授权代理人 21；律师 22；知识产权所有人 23

        :param id_type: The id_type of this ContactWayInfoV2.
        :type id_type: int
        """
        self._id_type = id_type

    @property
    def company_name(self):
        """Gets the company_name of this ContactWayInfoV2.

        公司名称

        :return: The company_name of this ContactWayInfoV2.
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ContactWayInfoV2.

        公司名称

        :param company_name: The company_name of this ContactWayInfoV2.
        :type company_name: str
        """
        self._company_name = company_name

    @property
    def id_files(self):
        """Gets the id_files of this ContactWayInfoV2.

        身份证明附件列表，至少1个，最多3个

        :return: The id_files of this ContactWayInfoV2.
        :rtype: list[str]
        """
        return self._id_files

    @id_files.setter
    def id_files(self, id_files):
        """Sets the id_files of this ContactWayInfoV2.

        身份证明附件列表，至少1个，最多3个

        :param id_files: The id_files of this ContactWayInfoV2.
        :type id_files: list[str]
        """
        self._id_files = id_files

    @property
    def other_way(self):
        """Gets the other_way of this ContactWayInfoV2.

        其他联系方式

        :return: The other_way of this ContactWayInfoV2.
        :rtype: str
        """
        return self._other_way

    @other_way.setter
    def other_way(self, other_way):
        """Sets the other_way of this ContactWayInfoV2.

        其他联系方式

        :param other_way: The other_way of this ContactWayInfoV2.
        :type other_way: str
        """
        self._other_way = other_way

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
        if not isinstance(other, ContactWayInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
