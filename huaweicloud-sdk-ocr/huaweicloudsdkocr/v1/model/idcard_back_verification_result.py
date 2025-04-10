# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdcardBackVerificationResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'valid_date': 'bool',
        'valid_validity_period': 'bool'
    }

    attribute_map = {
        'valid_date': 'valid_date',
        'valid_validity_period': 'valid_validity_period'
    }

    def __init__(self, valid_date=None, valid_validity_period=None):
        r"""IdcardBackVerificationResult

        The model defined in huaweicloud sdk

        :param valid_date: 当前日期是否在有效期内。 - true：表示当前日期在有效期内。 - false：表示当前日期不在有效期内。 当识别结果为单页，身份证图片是人像面时，默认是false。输入参数side为double_side时，该字段仅在back字典中存在。 仅在输入参数return_verification为true时，返回该字段。 
        :type valid_date: bool
        :param valid_validity_period: 身份证有效日期是否合法。 - true：表示身份证的有效日期合法 - false：表示身份证有效日期非法 当识别结果为单页，身份证图片是人像面时，默认是false。输入参数side为double_side时，该字段仅在back字典中存在。 仅在输入参数return_verification为true时，返回该字段。 
        :type valid_validity_period: bool
        """
        
        

        self._valid_date = None
        self._valid_validity_period = None
        self.discriminator = None

        if valid_date is not None:
            self.valid_date = valid_date
        if valid_validity_period is not None:
            self.valid_validity_period = valid_validity_period

    @property
    def valid_date(self):
        r"""Gets the valid_date of this IdcardBackVerificationResult.

        当前日期是否在有效期内。 - true：表示当前日期在有效期内。 - false：表示当前日期不在有效期内。 当识别结果为单页，身份证图片是人像面时，默认是false。输入参数side为double_side时，该字段仅在back字典中存在。 仅在输入参数return_verification为true时，返回该字段。 

        :return: The valid_date of this IdcardBackVerificationResult.
        :rtype: bool
        """
        return self._valid_date

    @valid_date.setter
    def valid_date(self, valid_date):
        r"""Sets the valid_date of this IdcardBackVerificationResult.

        当前日期是否在有效期内。 - true：表示当前日期在有效期内。 - false：表示当前日期不在有效期内。 当识别结果为单页，身份证图片是人像面时，默认是false。输入参数side为double_side时，该字段仅在back字典中存在。 仅在输入参数return_verification为true时，返回该字段。 

        :param valid_date: The valid_date of this IdcardBackVerificationResult.
        :type valid_date: bool
        """
        self._valid_date = valid_date

    @property
    def valid_validity_period(self):
        r"""Gets the valid_validity_period of this IdcardBackVerificationResult.

        身份证有效日期是否合法。 - true：表示身份证的有效日期合法 - false：表示身份证有效日期非法 当识别结果为单页，身份证图片是人像面时，默认是false。输入参数side为double_side时，该字段仅在back字典中存在。 仅在输入参数return_verification为true时，返回该字段。 

        :return: The valid_validity_period of this IdcardBackVerificationResult.
        :rtype: bool
        """
        return self._valid_validity_period

    @valid_validity_period.setter
    def valid_validity_period(self, valid_validity_period):
        r"""Sets the valid_validity_period of this IdcardBackVerificationResult.

        身份证有效日期是否合法。 - true：表示身份证的有效日期合法 - false：表示身份证有效日期非法 当识别结果为单页，身份证图片是人像面时，默认是false。输入参数side为double_side时，该字段仅在back字典中存在。 仅在输入参数return_verification为true时，返回该字段。 

        :param valid_validity_period: The valid_validity_period of this IdcardBackVerificationResult.
        :type valid_validity_period: bool
        """
        self._valid_validity_period = valid_validity_period

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
        if not isinstance(other, IdcardBackVerificationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
