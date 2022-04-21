# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StandardRespDataByNameAndId:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'verification_result': 'str',
        'verification_message': 'str',
        'verification_code': 'int',
        'similarity': 'str'
    }

    attribute_map = {
        'verification_result': 'verification_result',
        'verification_message': 'verification_message',
        'verification_code': 'verification_code',
        'similarity': 'similarity'
    }

    def __init__(self, verification_result=None, verification_message=None, verification_code=None, similarity=None):
        """StandardRespDataByNameAndId

        The model defined in huaweicloud sdk

        :param verification_result: 审核校验结果： \&quot;valid\&quot;表示身份审核通过； \&quot;invalid\&quot;表示身份审核不通过； \&quot;nonexistent\&quot;表示数据源没有该身份证号码，这种情况一般是被验证人正在办理户籍迁移，或者被验证人是军人或政要。
        :type verification_result: str
        :param verification_message: 审核校验信息，具体参[考校验信息说明](https://support.huaweicloud.com/api-ivs/ivs_02_0017.html)
        :type verification_message: str
        :param verification_code: 审核校验代码，具体参[考校验信息说明](https://support.huaweicloud.com/api-ivs/ivs_02_0017.html)
        :type verification_code: int
        :param similarity: 人像相识度。取值范围[0,100]
        :type similarity: str
        """
        
        

        self._verification_result = None
        self._verification_message = None
        self._verification_code = None
        self._similarity = None
        self.discriminator = None

        if verification_result is not None:
            self.verification_result = verification_result
        if verification_message is not None:
            self.verification_message = verification_message
        if verification_code is not None:
            self.verification_code = verification_code
        if similarity is not None:
            self.similarity = similarity

    @property
    def verification_result(self):
        """Gets the verification_result of this StandardRespDataByNameAndId.

        审核校验结果： \"valid\"表示身份审核通过； \"invalid\"表示身份审核不通过； \"nonexistent\"表示数据源没有该身份证号码，这种情况一般是被验证人正在办理户籍迁移，或者被验证人是军人或政要。

        :return: The verification_result of this StandardRespDataByNameAndId.
        :rtype: str
        """
        return self._verification_result

    @verification_result.setter
    def verification_result(self, verification_result):
        """Sets the verification_result of this StandardRespDataByNameAndId.

        审核校验结果： \"valid\"表示身份审核通过； \"invalid\"表示身份审核不通过； \"nonexistent\"表示数据源没有该身份证号码，这种情况一般是被验证人正在办理户籍迁移，或者被验证人是军人或政要。

        :param verification_result: The verification_result of this StandardRespDataByNameAndId.
        :type verification_result: str
        """
        self._verification_result = verification_result

    @property
    def verification_message(self):
        """Gets the verification_message of this StandardRespDataByNameAndId.

        审核校验信息，具体参[考校验信息说明](https://support.huaweicloud.com/api-ivs/ivs_02_0017.html)

        :return: The verification_message of this StandardRespDataByNameAndId.
        :rtype: str
        """
        return self._verification_message

    @verification_message.setter
    def verification_message(self, verification_message):
        """Sets the verification_message of this StandardRespDataByNameAndId.

        审核校验信息，具体参[考校验信息说明](https://support.huaweicloud.com/api-ivs/ivs_02_0017.html)

        :param verification_message: The verification_message of this StandardRespDataByNameAndId.
        :type verification_message: str
        """
        self._verification_message = verification_message

    @property
    def verification_code(self):
        """Gets the verification_code of this StandardRespDataByNameAndId.

        审核校验代码，具体参[考校验信息说明](https://support.huaweicloud.com/api-ivs/ivs_02_0017.html)

        :return: The verification_code of this StandardRespDataByNameAndId.
        :rtype: int
        """
        return self._verification_code

    @verification_code.setter
    def verification_code(self, verification_code):
        """Sets the verification_code of this StandardRespDataByNameAndId.

        审核校验代码，具体参[考校验信息说明](https://support.huaweicloud.com/api-ivs/ivs_02_0017.html)

        :param verification_code: The verification_code of this StandardRespDataByNameAndId.
        :type verification_code: int
        """
        self._verification_code = verification_code

    @property
    def similarity(self):
        """Gets the similarity of this StandardRespDataByNameAndId.

        人像相识度。取值范围[0,100]

        :return: The similarity of this StandardRespDataByNameAndId.
        :rtype: str
        """
        return self._similarity

    @similarity.setter
    def similarity(self, similarity):
        """Sets the similarity of this StandardRespDataByNameAndId.

        人像相识度。取值范围[0,100]

        :param similarity: The similarity of this StandardRespDataByNameAndId.
        :type similarity: str
        """
        self._similarity = similarity

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
        if not isinstance(other, StandardRespDataByNameAndId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
