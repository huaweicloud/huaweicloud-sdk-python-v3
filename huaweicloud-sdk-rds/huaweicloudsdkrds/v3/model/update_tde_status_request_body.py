# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTdeStatusRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rotate_day': 'int',
        'secret_id': 'str',
        'secret_name': 'str',
        'secret_version': 'str'
    }

    attribute_map = {
        'rotate_day': 'rotate_day',
        'secret_id': 'secret_id',
        'secret_name': 'secret_name',
        'secret_version': 'secret_version'
    }

    def __init__(self, rotate_day=None, secret_id=None, secret_name=None, secret_version=None):
        r"""UpdateTdeStatusRequestBody

        The model defined in huaweicloud sdk

        :param rotate_day: 轮转天数
        :type rotate_day: int
        :param secret_id: 密钥ID
        :type secret_id: str
        :param secret_name: 密钥名称
        :type secret_name: str
        :param secret_version: 密钥版本
        :type secret_version: str
        """
        
        

        self._rotate_day = None
        self._secret_id = None
        self._secret_name = None
        self._secret_version = None
        self.discriminator = None

        if rotate_day is not None:
            self.rotate_day = rotate_day
        if secret_id is not None:
            self.secret_id = secret_id
        if secret_name is not None:
            self.secret_name = secret_name
        if secret_version is not None:
            self.secret_version = secret_version

    @property
    def rotate_day(self):
        r"""Gets the rotate_day of this UpdateTdeStatusRequestBody.

        轮转天数

        :return: The rotate_day of this UpdateTdeStatusRequestBody.
        :rtype: int
        """
        return self._rotate_day

    @rotate_day.setter
    def rotate_day(self, rotate_day):
        r"""Sets the rotate_day of this UpdateTdeStatusRequestBody.

        轮转天数

        :param rotate_day: The rotate_day of this UpdateTdeStatusRequestBody.
        :type rotate_day: int
        """
        self._rotate_day = rotate_day

    @property
    def secret_id(self):
        r"""Gets the secret_id of this UpdateTdeStatusRequestBody.

        密钥ID

        :return: The secret_id of this UpdateTdeStatusRequestBody.
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        r"""Sets the secret_id of this UpdateTdeStatusRequestBody.

        密钥ID

        :param secret_id: The secret_id of this UpdateTdeStatusRequestBody.
        :type secret_id: str
        """
        self._secret_id = secret_id

    @property
    def secret_name(self):
        r"""Gets the secret_name of this UpdateTdeStatusRequestBody.

        密钥名称

        :return: The secret_name of this UpdateTdeStatusRequestBody.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        r"""Sets the secret_name of this UpdateTdeStatusRequestBody.

        密钥名称

        :param secret_name: The secret_name of this UpdateTdeStatusRequestBody.
        :type secret_name: str
        """
        self._secret_name = secret_name

    @property
    def secret_version(self):
        r"""Gets the secret_version of this UpdateTdeStatusRequestBody.

        密钥版本

        :return: The secret_version of this UpdateTdeStatusRequestBody.
        :rtype: str
        """
        return self._secret_version

    @secret_version.setter
    def secret_version(self, secret_version):
        r"""Sets the secret_version of this UpdateTdeStatusRequestBody.

        密钥版本

        :param secret_version: The secret_version of this UpdateTdeStatusRequestBody.
        :type secret_version: str
        """
        self._secret_version = secret_version

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
        if not isinstance(other, UpdateTdeStatusRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
