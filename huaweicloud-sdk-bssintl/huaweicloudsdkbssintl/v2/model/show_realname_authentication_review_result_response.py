# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRealnameAuthenticationReviewResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'review_result': 'int',
        'opinion': 'str'
    }

    attribute_map = {
        'review_result': 'review_result',
        'opinion': 'opinion'
    }

    def __init__(self, review_result=None, opinion=None):
        r"""ShowRealnameAuthenticationReviewResultResponse

        The model defined in huaweicloud sdk

        :param review_result: 实名认证审核结果，只有状态码为200并且已经提交过实名认证请求才返回： 0：审核中1：不通过2：通过
        :type review_result: int
        :param opinion: 审批意见，只有状态码为200并且审核不通过才返回。
        :type opinion: str
        """
        
        super(ShowRealnameAuthenticationReviewResultResponse, self).__init__()

        self._review_result = None
        self._opinion = None
        self.discriminator = None

        if review_result is not None:
            self.review_result = review_result
        if opinion is not None:
            self.opinion = opinion

    @property
    def review_result(self):
        r"""Gets the review_result of this ShowRealnameAuthenticationReviewResultResponse.

        实名认证审核结果，只有状态码为200并且已经提交过实名认证请求才返回： 0：审核中1：不通过2：通过

        :return: The review_result of this ShowRealnameAuthenticationReviewResultResponse.
        :rtype: int
        """
        return self._review_result

    @review_result.setter
    def review_result(self, review_result):
        r"""Sets the review_result of this ShowRealnameAuthenticationReviewResultResponse.

        实名认证审核结果，只有状态码为200并且已经提交过实名认证请求才返回： 0：审核中1：不通过2：通过

        :param review_result: The review_result of this ShowRealnameAuthenticationReviewResultResponse.
        :type review_result: int
        """
        self._review_result = review_result

    @property
    def opinion(self):
        r"""Gets the opinion of this ShowRealnameAuthenticationReviewResultResponse.

        审批意见，只有状态码为200并且审核不通过才返回。

        :return: The opinion of this ShowRealnameAuthenticationReviewResultResponse.
        :rtype: str
        """
        return self._opinion

    @opinion.setter
    def opinion(self, opinion):
        r"""Sets the opinion of this ShowRealnameAuthenticationReviewResultResponse.

        审批意见，只有状态码为200并且审核不通过才返回。

        :param opinion: The opinion of this ShowRealnameAuthenticationReviewResultResponse.
        :type opinion: str
        """
        self._opinion = opinion

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
        if not isinstance(other, ShowRealnameAuthenticationReviewResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
