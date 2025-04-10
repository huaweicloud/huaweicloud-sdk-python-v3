# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtentionReqDataByNameAndId:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'verification_name': 'str',
        'verification_id': 'str'
    }

    attribute_map = {
        'verification_name': 'verification_name',
        'verification_id': 'verification_id'
    }

    def __init__(self, verification_name=None, verification_id=None):
        r"""ExtentionReqDataByNameAndId

        The model defined in huaweicloud sdk

        :param verification_name: 被验证人的姓名。
        :type verification_name: str
        :param verification_id: 被验证人的身份证号码。
        :type verification_id: str
        """
        
        

        self._verification_name = None
        self._verification_id = None
        self.discriminator = None

        self.verification_name = verification_name
        self.verification_id = verification_id

    @property
    def verification_name(self):
        r"""Gets the verification_name of this ExtentionReqDataByNameAndId.

        被验证人的姓名。

        :return: The verification_name of this ExtentionReqDataByNameAndId.
        :rtype: str
        """
        return self._verification_name

    @verification_name.setter
    def verification_name(self, verification_name):
        r"""Sets the verification_name of this ExtentionReqDataByNameAndId.

        被验证人的姓名。

        :param verification_name: The verification_name of this ExtentionReqDataByNameAndId.
        :type verification_name: str
        """
        self._verification_name = verification_name

    @property
    def verification_id(self):
        r"""Gets the verification_id of this ExtentionReqDataByNameAndId.

        被验证人的身份证号码。

        :return: The verification_id of this ExtentionReqDataByNameAndId.
        :rtype: str
        """
        return self._verification_id

    @verification_id.setter
    def verification_id(self, verification_id):
        r"""Sets the verification_id of this ExtentionReqDataByNameAndId.

        被验证人的身份证号码。

        :param verification_id: The verification_id of this ExtentionReqDataByNameAndId.
        :type verification_id: str
        """
        self._verification_id = verification_id

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
        if not isinstance(other, ExtentionReqDataByNameAndId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
