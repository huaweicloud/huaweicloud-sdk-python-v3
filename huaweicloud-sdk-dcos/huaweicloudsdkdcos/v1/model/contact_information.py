# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContactInformation:

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
        'certificate_no_top': 'str',
        'certificate_no_last': 'str',
        'country_code': 'str',
        'phone': 'str',
        'work_unit': 'str',
        'remarks': 'str'
    }

    attribute_map = {
        'name': 'name',
        'certificate_no_top': 'certificate_no_top',
        'certificate_no_last': 'certificate_no_last',
        'country_code': 'country_code',
        'phone': 'phone',
        'work_unit': 'work_unit',
        'remarks': 'remarks'
    }

    def __init__(self, name=None, certificate_no_top=None, certificate_no_last=None, country_code=None, phone=None, work_unit=None, remarks=None):
        r"""ContactInformation

        The model defined in huaweicloud sdk

        :param name: 人员姓名
        :type name: str
        :param certificate_no_top: 证件号前三位
        :type certificate_no_top: str
        :param certificate_no_last: 证件号后四位
        :type certificate_no_last: str
        :param country_code: 手机国际码
        :type country_code: str
        :param phone: 电话
        :type phone: str
        :param work_unit: 单位
        :type work_unit: str
        :param remarks: 备注
        :type remarks: str
        """
        
        

        self._name = None
        self._certificate_no_top = None
        self._certificate_no_last = None
        self._country_code = None
        self._phone = None
        self._work_unit = None
        self._remarks = None
        self.discriminator = None

        self.name = name
        if certificate_no_top is not None:
            self.certificate_no_top = certificate_no_top
        if certificate_no_last is not None:
            self.certificate_no_last = certificate_no_last
        if country_code is not None:
            self.country_code = country_code
        if phone is not None:
            self.phone = phone
        if work_unit is not None:
            self.work_unit = work_unit
        if remarks is not None:
            self.remarks = remarks

    @property
    def name(self):
        r"""Gets the name of this ContactInformation.

        人员姓名

        :return: The name of this ContactInformation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ContactInformation.

        人员姓名

        :param name: The name of this ContactInformation.
        :type name: str
        """
        self._name = name

    @property
    def certificate_no_top(self):
        r"""Gets the certificate_no_top of this ContactInformation.

        证件号前三位

        :return: The certificate_no_top of this ContactInformation.
        :rtype: str
        """
        return self._certificate_no_top

    @certificate_no_top.setter
    def certificate_no_top(self, certificate_no_top):
        r"""Sets the certificate_no_top of this ContactInformation.

        证件号前三位

        :param certificate_no_top: The certificate_no_top of this ContactInformation.
        :type certificate_no_top: str
        """
        self._certificate_no_top = certificate_no_top

    @property
    def certificate_no_last(self):
        r"""Gets the certificate_no_last of this ContactInformation.

        证件号后四位

        :return: The certificate_no_last of this ContactInformation.
        :rtype: str
        """
        return self._certificate_no_last

    @certificate_no_last.setter
    def certificate_no_last(self, certificate_no_last):
        r"""Sets the certificate_no_last of this ContactInformation.

        证件号后四位

        :param certificate_no_last: The certificate_no_last of this ContactInformation.
        :type certificate_no_last: str
        """
        self._certificate_no_last = certificate_no_last

    @property
    def country_code(self):
        r"""Gets the country_code of this ContactInformation.

        手机国际码

        :return: The country_code of this ContactInformation.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        r"""Sets the country_code of this ContactInformation.

        手机国际码

        :param country_code: The country_code of this ContactInformation.
        :type country_code: str
        """
        self._country_code = country_code

    @property
    def phone(self):
        r"""Gets the phone of this ContactInformation.

        电话

        :return: The phone of this ContactInformation.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        r"""Sets the phone of this ContactInformation.

        电话

        :param phone: The phone of this ContactInformation.
        :type phone: str
        """
        self._phone = phone

    @property
    def work_unit(self):
        r"""Gets the work_unit of this ContactInformation.

        单位

        :return: The work_unit of this ContactInformation.
        :rtype: str
        """
        return self._work_unit

    @work_unit.setter
    def work_unit(self, work_unit):
        r"""Sets the work_unit of this ContactInformation.

        单位

        :param work_unit: The work_unit of this ContactInformation.
        :type work_unit: str
        """
        self._work_unit = work_unit

    @property
    def remarks(self):
        r"""Gets the remarks of this ContactInformation.

        备注

        :return: The remarks of this ContactInformation.
        :rtype: str
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        r"""Sets the remarks of this ContactInformation.

        备注

        :param remarks: The remarks of this ContactInformation.
        :type remarks: str
        """
        self._remarks = remarks

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
        if not isinstance(other, ContactInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
