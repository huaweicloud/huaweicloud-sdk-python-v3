# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateStarRocksDatabaseUserPasswordRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'x_language': 'str',
        'body': 'StarRocksDatabaseUserPWinfo'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, instance_id=None, x_language=None, body=None):
        r"""UpdateStarRocksDatabaseUserPasswordRequest

        The model defined in huaweicloud sdk

        :param instance_id: StarRocks实例ID，严格匹配UUID规则。
        :type instance_id: str
        :param x_language: 请求语言类型。默认en-us。 取值范围： - en-us - zh-cn
        :type x_language: str
        :param body: Body of the UpdateStarRocksDatabaseUserPasswordRequest
        :type body: :class:`huaweicloudsdkgaussdb.v3.StarRocksDatabaseUserPWinfo`
        """
        
        

        self._instance_id = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        if x_language is not None:
            self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateStarRocksDatabaseUserPasswordRequest.

        StarRocks实例ID，严格匹配UUID规则。

        :return: The instance_id of this UpdateStarRocksDatabaseUserPasswordRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateStarRocksDatabaseUserPasswordRequest.

        StarRocks实例ID，严格匹配UUID规则。

        :param instance_id: The instance_id of this UpdateStarRocksDatabaseUserPasswordRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def x_language(self):
        r"""Gets the x_language of this UpdateStarRocksDatabaseUserPasswordRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :return: The x_language of this UpdateStarRocksDatabaseUserPasswordRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this UpdateStarRocksDatabaseUserPasswordRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :param x_language: The x_language of this UpdateStarRocksDatabaseUserPasswordRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        r"""Gets the body of this UpdateStarRocksDatabaseUserPasswordRequest.

        :return: The body of this UpdateStarRocksDatabaseUserPasswordRequest.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.StarRocksDatabaseUserPWinfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateStarRocksDatabaseUserPasswordRequest.

        :param body: The body of this UpdateStarRocksDatabaseUserPasswordRequest.
        :type body: :class:`huaweicloudsdkgaussdb.v3.StarRocksDatabaseUserPWinfo`
        """
        self._body = body

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
        if not isinstance(other, UpdateStarRocksDatabaseUserPasswordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
