# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Hsts:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'max_age': 'int',
        'include_subdomains': 'str'
    }

    attribute_map = {
        'status': 'status',
        'max_age': 'max_age',
        'include_subdomains': 'include_subdomains'
    }

    def __init__(self, status=None, max_age=None, include_subdomains=None):
        """Hsts

        The model defined in huaweicloud sdk

        :param status: 状态，on：打开，off：关闭。
        :type status: str
        :param max_age: 过期时间,即：响应头“Strict-Transport-Security”在客户端的缓存时间。单位:秒,取值范围:0-63072000。  &gt; status参数为on时，必传。
        :type max_age: int
        :param include_subdomains: 包含子域名，on：包含，off：不包含。   &gt; status参数为on时，必传。
        :type include_subdomains: str
        """
        
        

        self._status = None
        self._max_age = None
        self._include_subdomains = None
        self.discriminator = None

        self.status = status
        if max_age is not None:
            self.max_age = max_age
        if include_subdomains is not None:
            self.include_subdomains = include_subdomains

    @property
    def status(self):
        """Gets the status of this Hsts.

        状态，on：打开，off：关闭。

        :return: The status of this Hsts.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Hsts.

        状态，on：打开，off：关闭。

        :param status: The status of this Hsts.
        :type status: str
        """
        self._status = status

    @property
    def max_age(self):
        """Gets the max_age of this Hsts.

        过期时间,即：响应头“Strict-Transport-Security”在客户端的缓存时间。单位:秒,取值范围:0-63072000。  > status参数为on时，必传。

        :return: The max_age of this Hsts.
        :rtype: int
        """
        return self._max_age

    @max_age.setter
    def max_age(self, max_age):
        """Sets the max_age of this Hsts.

        过期时间,即：响应头“Strict-Transport-Security”在客户端的缓存时间。单位:秒,取值范围:0-63072000。  > status参数为on时，必传。

        :param max_age: The max_age of this Hsts.
        :type max_age: int
        """
        self._max_age = max_age

    @property
    def include_subdomains(self):
        """Gets the include_subdomains of this Hsts.

        包含子域名，on：包含，off：不包含。   > status参数为on时，必传。

        :return: The include_subdomains of this Hsts.
        :rtype: str
        """
        return self._include_subdomains

    @include_subdomains.setter
    def include_subdomains(self, include_subdomains):
        """Sets the include_subdomains of this Hsts.

        包含子域名，on：包含，off：不包含。   > status参数为on时，必传。

        :param include_subdomains: The include_subdomains of this Hsts.
        :type include_subdomains: str
        """
        self._include_subdomains = include_subdomains

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
        if not isinstance(other, Hsts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
