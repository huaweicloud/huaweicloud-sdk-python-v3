# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StandardRespDataByVideoAndNameAndId:

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
        'similarity': 'str',
        'video_result': 'VideoResult'
    }

    attribute_map = {
        'verification_result': 'verification_result',
        'verification_message': 'verification_message',
        'verification_code': 'verification_code',
        'similarity': 'similarity',
        'video_result': 'video_result'
    }

    def __init__(self, verification_result=None, verification_message=None, verification_code=None, similarity=None, video_result=None):
        r"""StandardRespDataByVideoAndNameAndId

        The model defined in huaweicloud sdk

        :param verification_result: 审核校验结果： \&quot;valid\&quot;表示身份审核通过； \&quot;invalid\&quot;表示身份审核不通过； \&quot;nonexistent\&quot;表示数据源没有该身份证号码，这种情况一般是被验证人正在办理户籍迁移，或者被验证人是军人或政要。
        :type verification_result: str
        :param verification_message: 审核校验信息，具体参考[校验信息说明](https://support.huaweicloud.com/api-ivs/ivs_02_0017.html)
        :type verification_message: str
        :param verification_code: 审核校验代码，具体参考[校验信息说明](https://support.huaweicloud.com/api-ivs/ivs_02_0017.html)
        :type verification_code: int
        :param similarity: 人像相识度，取值默认范围为[0,100]，当入参detail为true时，取值范围为[0,1000]。
        :type similarity: str
        :param video_result: 
        :type video_result: :class:`huaweicloudsdkivs.v2.VideoResult`
        """
        
        

        self._verification_result = None
        self._verification_message = None
        self._verification_code = None
        self._similarity = None
        self._video_result = None
        self.discriminator = None

        self.verification_result = verification_result
        self.verification_message = verification_message
        self.verification_code = verification_code
        self.similarity = similarity
        self.video_result = video_result

    @property
    def verification_result(self):
        r"""Gets the verification_result of this StandardRespDataByVideoAndNameAndId.

        审核校验结果： \"valid\"表示身份审核通过； \"invalid\"表示身份审核不通过； \"nonexistent\"表示数据源没有该身份证号码，这种情况一般是被验证人正在办理户籍迁移，或者被验证人是军人或政要。

        :return: The verification_result of this StandardRespDataByVideoAndNameAndId.
        :rtype: str
        """
        return self._verification_result

    @verification_result.setter
    def verification_result(self, verification_result):
        r"""Sets the verification_result of this StandardRespDataByVideoAndNameAndId.

        审核校验结果： \"valid\"表示身份审核通过； \"invalid\"表示身份审核不通过； \"nonexistent\"表示数据源没有该身份证号码，这种情况一般是被验证人正在办理户籍迁移，或者被验证人是军人或政要。

        :param verification_result: The verification_result of this StandardRespDataByVideoAndNameAndId.
        :type verification_result: str
        """
        self._verification_result = verification_result

    @property
    def verification_message(self):
        r"""Gets the verification_message of this StandardRespDataByVideoAndNameAndId.

        审核校验信息，具体参考[校验信息说明](https://support.huaweicloud.com/api-ivs/ivs_02_0017.html)

        :return: The verification_message of this StandardRespDataByVideoAndNameAndId.
        :rtype: str
        """
        return self._verification_message

    @verification_message.setter
    def verification_message(self, verification_message):
        r"""Sets the verification_message of this StandardRespDataByVideoAndNameAndId.

        审核校验信息，具体参考[校验信息说明](https://support.huaweicloud.com/api-ivs/ivs_02_0017.html)

        :param verification_message: The verification_message of this StandardRespDataByVideoAndNameAndId.
        :type verification_message: str
        """
        self._verification_message = verification_message

    @property
    def verification_code(self):
        r"""Gets the verification_code of this StandardRespDataByVideoAndNameAndId.

        审核校验代码，具体参考[校验信息说明](https://support.huaweicloud.com/api-ivs/ivs_02_0017.html)

        :return: The verification_code of this StandardRespDataByVideoAndNameAndId.
        :rtype: int
        """
        return self._verification_code

    @verification_code.setter
    def verification_code(self, verification_code):
        r"""Sets the verification_code of this StandardRespDataByVideoAndNameAndId.

        审核校验代码，具体参考[校验信息说明](https://support.huaweicloud.com/api-ivs/ivs_02_0017.html)

        :param verification_code: The verification_code of this StandardRespDataByVideoAndNameAndId.
        :type verification_code: int
        """
        self._verification_code = verification_code

    @property
    def similarity(self):
        r"""Gets the similarity of this StandardRespDataByVideoAndNameAndId.

        人像相识度，取值默认范围为[0,100]，当入参detail为true时，取值范围为[0,1000]。

        :return: The similarity of this StandardRespDataByVideoAndNameAndId.
        :rtype: str
        """
        return self._similarity

    @similarity.setter
    def similarity(self, similarity):
        r"""Sets the similarity of this StandardRespDataByVideoAndNameAndId.

        人像相识度，取值默认范围为[0,100]，当入参detail为true时，取值范围为[0,1000]。

        :param similarity: The similarity of this StandardRespDataByVideoAndNameAndId.
        :type similarity: str
        """
        self._similarity = similarity

    @property
    def video_result(self):
        r"""Gets the video_result of this StandardRespDataByVideoAndNameAndId.

        :return: The video_result of this StandardRespDataByVideoAndNameAndId.
        :rtype: :class:`huaweicloudsdkivs.v2.VideoResult`
        """
        return self._video_result

    @video_result.setter
    def video_result(self, video_result):
        r"""Sets the video_result of this StandardRespDataByVideoAndNameAndId.

        :param video_result: The video_result of this StandardRespDataByVideoAndNameAndId.
        :type video_result: :class:`huaweicloudsdkivs.v2.VideoResult`
        """
        self._video_result = video_result

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
        if not isinstance(other, StandardRespDataByVideoAndNameAndId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
