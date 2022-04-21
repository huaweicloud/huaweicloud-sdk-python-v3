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
        """IdcardVerificationResult

        The model defined in huaweicloud sdk

        :param valid_number: 身份证号规则校验是否通过。“true”表示身份证号规则校验通过，“false”表示身份证号规则校验不通过。当身份证图片是国徽面时，默认是false。仅在输入参数return_verification为true时，返回该字段。 
        :type valid_number: bool
        :param valid_birth: 出生日期与身份证号所表示的出生日期是否一致。“true”表示一致，“false”表示不一致。当身份证图片是国徽面，或者身份证号规则校验不通过时，默认是false。仅在输入参数return_verification为true时，返回该字段。 
        :type valid_birth: bool
        :param valid_sex: 性别与身份证号所表示的性别信息是否一致。“true”表示一致，“false”表示不一致。当身份证图片是国徽面，或者身份证号规则校验不通过时，默认是false。仅在输入参数return_verification为true时，返回该字段。 
        :type valid_sex: bool
        :param valid_date: 当前日期是否在有效期内。“true”表示当前日期在有效期内，“false”表示当前日期不在有效期内。当身份证图片是人像面时，默认是false。仅在输入参数return_verification为true时，返回该字段。 
        :type valid_date: bool
        """
        
        

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

        身份证号规则校验是否通过。“true”表示身份证号规则校验通过，“false”表示身份证号规则校验不通过。当身份证图片是国徽面时，默认是false。仅在输入参数return_verification为true时，返回该字段。 

        :return: The valid_number of this IdcardVerificationResult.
        :rtype: bool
        """
        return self._valid_number

    @valid_number.setter
    def valid_number(self, valid_number):
        """Sets the valid_number of this IdcardVerificationResult.

        身份证号规则校验是否通过。“true”表示身份证号规则校验通过，“false”表示身份证号规则校验不通过。当身份证图片是国徽面时，默认是false。仅在输入参数return_verification为true时，返回该字段。 

        :param valid_number: The valid_number of this IdcardVerificationResult.
        :type valid_number: bool
        """
        self._valid_number = valid_number

    @property
    def valid_birth(self):
        """Gets the valid_birth of this IdcardVerificationResult.

        出生日期与身份证号所表示的出生日期是否一致。“true”表示一致，“false”表示不一致。当身份证图片是国徽面，或者身份证号规则校验不通过时，默认是false。仅在输入参数return_verification为true时，返回该字段。 

        :return: The valid_birth of this IdcardVerificationResult.
        :rtype: bool
        """
        return self._valid_birth

    @valid_birth.setter
    def valid_birth(self, valid_birth):
        """Sets the valid_birth of this IdcardVerificationResult.

        出生日期与身份证号所表示的出生日期是否一致。“true”表示一致，“false”表示不一致。当身份证图片是国徽面，或者身份证号规则校验不通过时，默认是false。仅在输入参数return_verification为true时，返回该字段。 

        :param valid_birth: The valid_birth of this IdcardVerificationResult.
        :type valid_birth: bool
        """
        self._valid_birth = valid_birth

    @property
    def valid_sex(self):
        """Gets the valid_sex of this IdcardVerificationResult.

        性别与身份证号所表示的性别信息是否一致。“true”表示一致，“false”表示不一致。当身份证图片是国徽面，或者身份证号规则校验不通过时，默认是false。仅在输入参数return_verification为true时，返回该字段。 

        :return: The valid_sex of this IdcardVerificationResult.
        :rtype: bool
        """
        return self._valid_sex

    @valid_sex.setter
    def valid_sex(self, valid_sex):
        """Sets the valid_sex of this IdcardVerificationResult.

        性别与身份证号所表示的性别信息是否一致。“true”表示一致，“false”表示不一致。当身份证图片是国徽面，或者身份证号规则校验不通过时，默认是false。仅在输入参数return_verification为true时，返回该字段。 

        :param valid_sex: The valid_sex of this IdcardVerificationResult.
        :type valid_sex: bool
        """
        self._valid_sex = valid_sex

    @property
    def valid_date(self):
        """Gets the valid_date of this IdcardVerificationResult.

        当前日期是否在有效期内。“true”表示当前日期在有效期内，“false”表示当前日期不在有效期内。当身份证图片是人像面时，默认是false。仅在输入参数return_verification为true时，返回该字段。 

        :return: The valid_date of this IdcardVerificationResult.
        :rtype: bool
        """
        return self._valid_date

    @valid_date.setter
    def valid_date(self, valid_date):
        """Sets the valid_date of this IdcardVerificationResult.

        当前日期是否在有效期内。“true”表示当前日期在有效期内，“false”表示当前日期不在有效期内。当身份证图片是人像面时，默认是false。仅在输入参数return_verification为true时，返回该字段。 

        :param valid_date: The valid_date of this IdcardVerificationResult.
        :type valid_date: bool
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
