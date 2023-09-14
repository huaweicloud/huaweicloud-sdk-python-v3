# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecretVersionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'secret_binary': 'str',
        'secret_string': 'str',
        'version_stages': 'list[str]',
        'expire_time': 'int'
    }

    attribute_map = {
        'secret_binary': 'secret_binary',
        'secret_string': 'secret_string',
        'version_stages': 'version_stages',
        'expire_time': 'expire_time'
    }

    def __init__(self, secret_binary=None, secret_string=None, version_stages=None, expire_time=None):
        """CreateSecretVersionRequestBody

        The model defined in huaweicloud sdk

        :param secret_binary: 新创建凭据的凭据值，将其加密后，存入初始版本中。  类型：base64编码的二进制数据对象。  约束：secret_binary和secret_string必须且只能设置一个，最大32K。 
        :type secret_binary: str
        :param secret_string: 新创建凭据的凭据值，将其加密后，存入初始版本中。  约束：secret_binary和 secret_string必须且只能设置一个，最大32K。 
        :type secret_string: str
        :param version_stages: 凭据版本在存入时需要被同时标记的版本状态。如果您不指定此参数，凭据管家默认为新版本标记SYSCURRENT  约束：数组大小：最小1，最大12。stage长度：最小1字节，最大64字节。 
        :type version_stages: list[str]
        :param expire_time: 凭据版本过期时间，时间戳，即从1970年1月1日至该时间的总秒数。默认为空，凭据订阅“版本过期”事件类型时，有效期判断所依据的值。 
        :type expire_time: int
        """
        
        

        self._secret_binary = None
        self._secret_string = None
        self._version_stages = None
        self._expire_time = None
        self.discriminator = None

        if secret_binary is not None:
            self.secret_binary = secret_binary
        if secret_string is not None:
            self.secret_string = secret_string
        if version_stages is not None:
            self.version_stages = version_stages
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def secret_binary(self):
        """Gets the secret_binary of this CreateSecretVersionRequestBody.

        新创建凭据的凭据值，将其加密后，存入初始版本中。  类型：base64编码的二进制数据对象。  约束：secret_binary和secret_string必须且只能设置一个，最大32K。 

        :return: The secret_binary of this CreateSecretVersionRequestBody.
        :rtype: str
        """
        return self._secret_binary

    @secret_binary.setter
    def secret_binary(self, secret_binary):
        """Sets the secret_binary of this CreateSecretVersionRequestBody.

        新创建凭据的凭据值，将其加密后，存入初始版本中。  类型：base64编码的二进制数据对象。  约束：secret_binary和secret_string必须且只能设置一个，最大32K。 

        :param secret_binary: The secret_binary of this CreateSecretVersionRequestBody.
        :type secret_binary: str
        """
        self._secret_binary = secret_binary

    @property
    def secret_string(self):
        """Gets the secret_string of this CreateSecretVersionRequestBody.

        新创建凭据的凭据值，将其加密后，存入初始版本中。  约束：secret_binary和 secret_string必须且只能设置一个，最大32K。 

        :return: The secret_string of this CreateSecretVersionRequestBody.
        :rtype: str
        """
        return self._secret_string

    @secret_string.setter
    def secret_string(self, secret_string):
        """Sets the secret_string of this CreateSecretVersionRequestBody.

        新创建凭据的凭据值，将其加密后，存入初始版本中。  约束：secret_binary和 secret_string必须且只能设置一个，最大32K。 

        :param secret_string: The secret_string of this CreateSecretVersionRequestBody.
        :type secret_string: str
        """
        self._secret_string = secret_string

    @property
    def version_stages(self):
        """Gets the version_stages of this CreateSecretVersionRequestBody.

        凭据版本在存入时需要被同时标记的版本状态。如果您不指定此参数，凭据管家默认为新版本标记SYSCURRENT  约束：数组大小：最小1，最大12。stage长度：最小1字节，最大64字节。 

        :return: The version_stages of this CreateSecretVersionRequestBody.
        :rtype: list[str]
        """
        return self._version_stages

    @version_stages.setter
    def version_stages(self, version_stages):
        """Sets the version_stages of this CreateSecretVersionRequestBody.

        凭据版本在存入时需要被同时标记的版本状态。如果您不指定此参数，凭据管家默认为新版本标记SYSCURRENT  约束：数组大小：最小1，最大12。stage长度：最小1字节，最大64字节。 

        :param version_stages: The version_stages of this CreateSecretVersionRequestBody.
        :type version_stages: list[str]
        """
        self._version_stages = version_stages

    @property
    def expire_time(self):
        """Gets the expire_time of this CreateSecretVersionRequestBody.

        凭据版本过期时间，时间戳，即从1970年1月1日至该时间的总秒数。默认为空，凭据订阅“版本过期”事件类型时，有效期判断所依据的值。 

        :return: The expire_time of this CreateSecretVersionRequestBody.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this CreateSecretVersionRequestBody.

        凭据版本过期时间，时间戳，即从1970年1月1日至该时间的总秒数。默认为空，凭据订阅“版本过期”事件类型时，有效期判断所依据的值。 

        :param expire_time: The expire_time of this CreateSecretVersionRequestBody.
        :type expire_time: int
        """
        self._expire_time = expire_time

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
        if not isinstance(other, CreateSecretVersionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
