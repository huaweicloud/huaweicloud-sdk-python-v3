# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdcardVerificationResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'valid_number': 'bool',
        'valid_birth': 'bool',
        'valid_sex': 'bool',
        'valid_date': 'bool'
    }

    attribute_map = {
        'valid_number': 'valid_number',
        'valid_birth': 'valid_birth',
        'valid_sex': 'valid_sex',
        'valid_date': 'valid_date'
    }

    def __init__(self, valid_number=None, valid_birth=None, valid_sex=None, valid_date=None):
        """IdcardVerificationResult - a model defined in huaweicloud sdk"""
        
        

        self._valid_number = None
        self._valid_birth = None
        self._valid_sex = None
        self._valid_date = None
        self.discriminator = None

        if valid_number is not None:
            self.valid_number = valid_number
        if valid_birth is not None:
            self.valid_birth = valid_birth
        if valid_sex is not None:
            self.valid_sex = valid_sex
        if valid_date is not None:
            self.valid_date = valid_date

    @property
    def valid_number(self):
        """Gets the valid_number of this IdcardVerificationResult.

        身份证号合法。校验规则为：将身份证号前17位数字分别乘以7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2，再求和，求和结果对11取模，取模结果作为数组[1,0,X,9,8,7,6,5,4,3,2]的下标，从里面取出一位结果，例如取模结果为0，则从数组里取出来的结果是1，最后判断从数组里面取出来的结果是否和身份证号最后一位是否一致。如果一致，代表身份证号合法，返回true，否则代表身份证号不合法，返回false。  当身份证图片是背面时，默认是false。 

        :return: The valid_number of this IdcardVerificationResult.
        :rtype: bool
        """
        return self._valid_number

    @valid_number.setter
    def valid_number(self, valid_number):
        """Sets the valid_number of this IdcardVerificationResult.

        身份证号合法。校验规则为：将身份证号前17位数字分别乘以7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2，再求和，求和结果对11取模，取模结果作为数组[1,0,X,9,8,7,6,5,4,3,2]的下标，从里面取出一位结果，例如取模结果为0，则从数组里取出来的结果是1，最后判断从数组里面取出来的结果是否和身份证号最后一位是否一致。如果一致，代表身份证号合法，返回true，否则代表身份证号不合法，返回false。  当身份证图片是背面时，默认是false。 

        :param valid_number: The valid_number of this IdcardVerificationResult.
        :type: bool
        """
        self._valid_number = valid_number

    @property
    def valid_birth(self):
        """Gets the valid_birth of this IdcardVerificationResult.

        身份证号与出生日期一致。出生日期和身份证号的第7位和第14位之间表示的出生日期是否一致。一致返回true，否则返回false。  当身份证图片是背面时，默认是false。 

        :return: The valid_birth of this IdcardVerificationResult.
        :rtype: bool
        """
        return self._valid_birth

    @valid_birth.setter
    def valid_birth(self, valid_birth):
        """Sets the valid_birth of this IdcardVerificationResult.

        身份证号与出生日期一致。出生日期和身份证号的第7位和第14位之间表示的出生日期是否一致。一致返回true，否则返回false。  当身份证图片是背面时，默认是false。 

        :param valid_birth: The valid_birth of this IdcardVerificationResult.
        :type: bool
        """
        self._valid_birth = valid_birth

    @property
    def valid_sex(self):
        """Gets the valid_sex of this IdcardVerificationResult.

        身份证号与性别一致。性别和身份证号的第17位表示的性别信息是否一致。身份证号的第17位如果为奇数表示男性，偶数表示女性。一致返回true，否则返回false。  当身份证图片是背面时，默认是false。 

        :return: The valid_sex of this IdcardVerificationResult.
        :rtype: bool
        """
        return self._valid_sex

    @valid_sex.setter
    def valid_sex(self, valid_sex):
        """Sets the valid_sex of this IdcardVerificationResult.

        身份证号与性别一致。性别和身份证号的第17位表示的性别信息是否一致。身份证号的第17位如果为奇数表示男性，偶数表示女性。一致返回true，否则返回false。  当身份证图片是背面时，默认是false。 

        :param valid_sex: The valid_sex of this IdcardVerificationResult.
        :type: bool
        """
        self._valid_sex = valid_sex

    @property
    def valid_date(self):
        """Gets the valid_date of this IdcardVerificationResult.

        当前日期在有效期内。当前日期在身份证有效期内返回true，否则返回false。  当身份证图片是正面时，默认是false。 

        :return: The valid_date of this IdcardVerificationResult.
        :rtype: bool
        """
        return self._valid_date

    @valid_date.setter
    def valid_date(self, valid_date):
        """Sets the valid_date of this IdcardVerificationResult.

        当前日期在有效期内。当前日期在身份证有效期内返回true，否则返回false。  当身份证图片是正面时，默认是false。 

        :param valid_date: The valid_date of this IdcardVerificationResult.
        :type: bool
        """
        self._valid_date = valid_date

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
        if not isinstance(other, IdcardVerificationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
