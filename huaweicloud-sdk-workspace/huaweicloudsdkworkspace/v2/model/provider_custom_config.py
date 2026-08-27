# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProviderCustomConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'model_list_api': 'str',
        'auth_header': 'str',
        'auth_prefix': 'str',
        'model_id_field': 'str',
        'model_name_field': 'str',
        'headers': 'dict(str, str)'
    }

    attribute_map = {
        'model_list_api': 'model_list_api',
        'auth_header': 'auth_header',
        'auth_prefix': 'auth_prefix',
        'model_id_field': 'model_id_field',
        'model_name_field': 'model_name_field',
        'headers': 'headers'
    }

    def __init__(self, model_list_api=None, auth_header=None, auth_prefix=None, model_id_field=None, model_name_field=None, headers=None):
        r"""ProviderCustomConfig

        The model defined in huaweicloud sdk

        :param model_list_api: 模型列表接口地址，用于查询供应商远程模型。
        :type model_list_api: str
        :param auth_header: 认证请求头名称。
        :type auth_header: str
        :param auth_prefix: 认证前缀（如Bearer）。
        :type auth_prefix: str
        :param model_id_field: 供应商模型列表中模型ID字段名。
        :type model_id_field: str
        :param model_name_field: 供应商模型列表中模型名称字段名。
        :type model_name_field: str
        :param headers: 自定义HTTP请求头，调用供应商API时附加。
        :type headers: dict(str, str)
        """
        
        

        self._model_list_api = None
        self._auth_header = None
        self._auth_prefix = None
        self._model_id_field = None
        self._model_name_field = None
        self._headers = None
        self.discriminator = None

        if model_list_api is not None:
            self.model_list_api = model_list_api
        if auth_header is not None:
            self.auth_header = auth_header
        if auth_prefix is not None:
            self.auth_prefix = auth_prefix
        if model_id_field is not None:
            self.model_id_field = model_id_field
        if model_name_field is not None:
            self.model_name_field = model_name_field
        if headers is not None:
            self.headers = headers

    @property
    def model_list_api(self):
        r"""Gets the model_list_api of this ProviderCustomConfig.

        模型列表接口地址，用于查询供应商远程模型。

        :return: The model_list_api of this ProviderCustomConfig.
        :rtype: str
        """
        return self._model_list_api

    @model_list_api.setter
    def model_list_api(self, model_list_api):
        r"""Sets the model_list_api of this ProviderCustomConfig.

        模型列表接口地址，用于查询供应商远程模型。

        :param model_list_api: The model_list_api of this ProviderCustomConfig.
        :type model_list_api: str
        """
        self._model_list_api = model_list_api

    @property
    def auth_header(self):
        r"""Gets the auth_header of this ProviderCustomConfig.

        认证请求头名称。

        :return: The auth_header of this ProviderCustomConfig.
        :rtype: str
        """
        return self._auth_header

    @auth_header.setter
    def auth_header(self, auth_header):
        r"""Sets the auth_header of this ProviderCustomConfig.

        认证请求头名称。

        :param auth_header: The auth_header of this ProviderCustomConfig.
        :type auth_header: str
        """
        self._auth_header = auth_header

    @property
    def auth_prefix(self):
        r"""Gets the auth_prefix of this ProviderCustomConfig.

        认证前缀（如Bearer）。

        :return: The auth_prefix of this ProviderCustomConfig.
        :rtype: str
        """
        return self._auth_prefix

    @auth_prefix.setter
    def auth_prefix(self, auth_prefix):
        r"""Sets the auth_prefix of this ProviderCustomConfig.

        认证前缀（如Bearer）。

        :param auth_prefix: The auth_prefix of this ProviderCustomConfig.
        :type auth_prefix: str
        """
        self._auth_prefix = auth_prefix

    @property
    def model_id_field(self):
        r"""Gets the model_id_field of this ProviderCustomConfig.

        供应商模型列表中模型ID字段名。

        :return: The model_id_field of this ProviderCustomConfig.
        :rtype: str
        """
        return self._model_id_field

    @model_id_field.setter
    def model_id_field(self, model_id_field):
        r"""Sets the model_id_field of this ProviderCustomConfig.

        供应商模型列表中模型ID字段名。

        :param model_id_field: The model_id_field of this ProviderCustomConfig.
        :type model_id_field: str
        """
        self._model_id_field = model_id_field

    @property
    def model_name_field(self):
        r"""Gets the model_name_field of this ProviderCustomConfig.

        供应商模型列表中模型名称字段名。

        :return: The model_name_field of this ProviderCustomConfig.
        :rtype: str
        """
        return self._model_name_field

    @model_name_field.setter
    def model_name_field(self, model_name_field):
        r"""Sets the model_name_field of this ProviderCustomConfig.

        供应商模型列表中模型名称字段名。

        :param model_name_field: The model_name_field of this ProviderCustomConfig.
        :type model_name_field: str
        """
        self._model_name_field = model_name_field

    @property
    def headers(self):
        r"""Gets the headers of this ProviderCustomConfig.

        自定义HTTP请求头，调用供应商API时附加。

        :return: The headers of this ProviderCustomConfig.
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        r"""Sets the headers of this ProviderCustomConfig.

        自定义HTTP请求头，调用供应商API时附加。

        :param headers: The headers of this ProviderCustomConfig.
        :type headers: dict(str, str)
        """
        self._headers = headers

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
        if not isinstance(other, ProviderCustomConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
