# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecretFunctionTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'secret_type': 'str',
        'secret_sub_type': 'str',
        'engine': 'str'
    }

    attribute_map = {
        'secret_type': 'secret_type',
        'secret_sub_type': 'secret_sub_type',
        'engine': 'engine'
    }

    def __init__(self, secret_type=None, secret_sub_type=None, engine=None):
        r"""ShowSecretFunctionTemplatesRequest

        The model defined in huaweicloud sdk

        :param secret_type: 凭据类型。
        :type secret_type: str
        :param secret_sub_type: 凭据轮转账号类型。 - SingleUser：单用户模式轮转 - MultiUser：双用户模式轮转
        :type secret_sub_type: str
        :param engine: 数据库类型。凭据类型为RDS-FG时为必填参数，可传入mysql、postgresql、sqlserver。其余凭据类型不支持。
        :type engine: str
        """
        
        

        self._secret_type = None
        self._secret_sub_type = None
        self._engine = None
        self.discriminator = None

        self.secret_type = secret_type
        self.secret_sub_type = secret_sub_type
        if engine is not None:
            self.engine = engine

    @property
    def secret_type(self):
        r"""Gets the secret_type of this ShowSecretFunctionTemplatesRequest.

        凭据类型。

        :return: The secret_type of this ShowSecretFunctionTemplatesRequest.
        :rtype: str
        """
        return self._secret_type

    @secret_type.setter
    def secret_type(self, secret_type):
        r"""Sets the secret_type of this ShowSecretFunctionTemplatesRequest.

        凭据类型。

        :param secret_type: The secret_type of this ShowSecretFunctionTemplatesRequest.
        :type secret_type: str
        """
        self._secret_type = secret_type

    @property
    def secret_sub_type(self):
        r"""Gets the secret_sub_type of this ShowSecretFunctionTemplatesRequest.

        凭据轮转账号类型。 - SingleUser：单用户模式轮转 - MultiUser：双用户模式轮转

        :return: The secret_sub_type of this ShowSecretFunctionTemplatesRequest.
        :rtype: str
        """
        return self._secret_sub_type

    @secret_sub_type.setter
    def secret_sub_type(self, secret_sub_type):
        r"""Sets the secret_sub_type of this ShowSecretFunctionTemplatesRequest.

        凭据轮转账号类型。 - SingleUser：单用户模式轮转 - MultiUser：双用户模式轮转

        :param secret_sub_type: The secret_sub_type of this ShowSecretFunctionTemplatesRequest.
        :type secret_sub_type: str
        """
        self._secret_sub_type = secret_sub_type

    @property
    def engine(self):
        r"""Gets the engine of this ShowSecretFunctionTemplatesRequest.

        数据库类型。凭据类型为RDS-FG时为必填参数，可传入mysql、postgresql、sqlserver。其余凭据类型不支持。

        :return: The engine of this ShowSecretFunctionTemplatesRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ShowSecretFunctionTemplatesRequest.

        数据库类型。凭据类型为RDS-FG时为必填参数，可传入mysql、postgresql、sqlserver。其余凭据类型不支持。

        :param engine: The engine of this ShowSecretFunctionTemplatesRequest.
        :type engine: str
        """
        self._engine = engine

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
        if not isinstance(other, ShowSecretFunctionTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
