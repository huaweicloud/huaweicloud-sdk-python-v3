# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdcardFrontVerificationResult:

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
        'valid_sex': 'bool'
    }

    attribute_map = {
        'valid_number': 'valid_number',
        'valid_birth': 'valid_birth',
        'valid_sex': 'valid_sex'
    }

    def __init__(self, valid_number=None, valid_birth=None, valid_sex=None):
        r"""IdcardFrontVerificationResult

        The model defined in huaweicloud sdk

        :param valid_number: 身份证号规则校验是否通过。 - true：表示身份证号规则校验通过。 - false：表示身份证号规则校验不通过。 当识别结果为单页，身份证图片是国徽面时，默认是false。输入参数side为double_side时，该字典仅在front字段中存在。 仅在输入参数return_verification为true时，返回该字段。 
        :type valid_number: bool
        :param valid_birth: 出生日期与身份证号所表示的出生日期是否一致。 - true：出生日期与身份证号所表示的出生日期一致。 - false：出生日期与身份证号所表示的出生日期不一致。 当识别结果为单页，身份证图片是国徽面，或者身份证号规则校验不通过时，默认是false。输入参数side为double_side时，该字段仅在front字典中存在。 仅在输入参数return_verification为true时，返回该字段。 
        :type valid_birth: bool
        :param valid_sex: 性别与身份证号所表示的性别信息是否一致。 -true：性别与身份证号所表示的性别信息一致 -false：性别与身份证号所表示的性别信息不一致。 当识别结果为单页，身份证图片是国徽面，或者身份证号规则校验不通过时，默认是false。输入参数side为double_side时，该字段仅在front字典中存在。 仅在输入参数return_verification为true时，返回该字段。 
        :type valid_sex: bool
        """
        
        

        self._valid_number = None
        self._valid_birth = None
        self._valid_sex = None
        self.discriminator = None

        if valid_number is not None:
            self.valid_number = valid_number
        if valid_birth is not None:
            self.valid_birth = valid_birth
        if valid_sex is not None:
            self.valid_sex = valid_sex

    @property
    def valid_number(self):
        r"""Gets the valid_number of this IdcardFrontVerificationResult.

        身份证号规则校验是否通过。 - true：表示身份证号规则校验通过。 - false：表示身份证号规则校验不通过。 当识别结果为单页，身份证图片是国徽面时，默认是false。输入参数side为double_side时，该字典仅在front字段中存在。 仅在输入参数return_verification为true时，返回该字段。 

        :return: The valid_number of this IdcardFrontVerificationResult.
        :rtype: bool
        """
        return self._valid_number

    @valid_number.setter
    def valid_number(self, valid_number):
        r"""Sets the valid_number of this IdcardFrontVerificationResult.

        身份证号规则校验是否通过。 - true：表示身份证号规则校验通过。 - false：表示身份证号规则校验不通过。 当识别结果为单页，身份证图片是国徽面时，默认是false。输入参数side为double_side时，该字典仅在front字段中存在。 仅在输入参数return_verification为true时，返回该字段。 

        :param valid_number: The valid_number of this IdcardFrontVerificationResult.
        :type valid_number: bool
        """
        self._valid_number = valid_number

    @property
    def valid_birth(self):
        r"""Gets the valid_birth of this IdcardFrontVerificationResult.

        出生日期与身份证号所表示的出生日期是否一致。 - true：出生日期与身份证号所表示的出生日期一致。 - false：出生日期与身份证号所表示的出生日期不一致。 当识别结果为单页，身份证图片是国徽面，或者身份证号规则校验不通过时，默认是false。输入参数side为double_side时，该字段仅在front字典中存在。 仅在输入参数return_verification为true时，返回该字段。 

        :return: The valid_birth of this IdcardFrontVerificationResult.
        :rtype: bool
        """
        return self._valid_birth

    @valid_birth.setter
    def valid_birth(self, valid_birth):
        r"""Sets the valid_birth of this IdcardFrontVerificationResult.

        出生日期与身份证号所表示的出生日期是否一致。 - true：出生日期与身份证号所表示的出生日期一致。 - false：出生日期与身份证号所表示的出生日期不一致。 当识别结果为单页，身份证图片是国徽面，或者身份证号规则校验不通过时，默认是false。输入参数side为double_side时，该字段仅在front字典中存在。 仅在输入参数return_verification为true时，返回该字段。 

        :param valid_birth: The valid_birth of this IdcardFrontVerificationResult.
        :type valid_birth: bool
        """
        self._valid_birth = valid_birth

    @property
    def valid_sex(self):
        r"""Gets the valid_sex of this IdcardFrontVerificationResult.

        性别与身份证号所表示的性别信息是否一致。 -true：性别与身份证号所表示的性别信息一致 -false：性别与身份证号所表示的性别信息不一致。 当识别结果为单页，身份证图片是国徽面，或者身份证号规则校验不通过时，默认是false。输入参数side为double_side时，该字段仅在front字典中存在。 仅在输入参数return_verification为true时，返回该字段。 

        :return: The valid_sex of this IdcardFrontVerificationResult.
        :rtype: bool
        """
        return self._valid_sex

    @valid_sex.setter
    def valid_sex(self, valid_sex):
        r"""Sets the valid_sex of this IdcardFrontVerificationResult.

        性别与身份证号所表示的性别信息是否一致。 -true：性别与身份证号所表示的性别信息一致 -false：性别与身份证号所表示的性别信息不一致。 当识别结果为单页，身份证图片是国徽面，或者身份证号规则校验不通过时，默认是false。输入参数side为double_side时，该字段仅在front字典中存在。 仅在输入参数return_verification为true时，返回该字段。 

        :param valid_sex: The valid_sex of this IdcardFrontVerificationResult.
        :type valid_sex: bool
        """
        self._valid_sex = valid_sex

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
        if not isinstance(other, IdcardFrontVerificationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
