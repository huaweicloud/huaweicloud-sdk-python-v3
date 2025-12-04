# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VerifyOrderRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'comments': 'str'
    }

    attribute_map = {
        'comments': 'comments'
    }

    def __init__(self, comments=None):
        r"""VerifyOrderRequestBody

        The model defined in huaweicloud sdk

        :param comments: 客户验收意见说明
        :type comments: str
        """
        
        

        self._comments = None
        self.discriminator = None

        if comments is not None:
            self.comments = comments

    @property
    def comments(self):
        r"""Gets the comments of this VerifyOrderRequestBody.

        客户验收意见说明

        :return: The comments of this VerifyOrderRequestBody.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        r"""Sets the comments of this VerifyOrderRequestBody.

        客户验收意见说明

        :param comments: The comments of this VerifyOrderRequestBody.
        :type comments: str
        """
        self._comments = comments

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VerifyOrderRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
