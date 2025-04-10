# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IflytekAiuiConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'app_key': 'str',
        'api_secret': 'str',
        'is_production': 'bool'
    }

    attribute_map = {
        'app_id': 'app_id',
        'app_key': 'app_key',
        'api_secret': 'api_secret',
        'is_production': 'is_production'
    }

    def __init__(self, app_id=None, app_key=None, api_secret=None, is_production=None):
        r"""IflytekAiuiConfig

        The model defined in huaweicloud sdk

        :param app_id: AIUI应用ID。
        :type app_id: str
        :param app_key: AIUI应用密钥。
        :type app_key: str
        :param api_secret: AIUI API密钥。
        :type api_secret: str
        :param is_production: 是否为正式环境
        :type is_production: bool
        """
        
        

        self._app_id = None
        self._app_key = None
        self._api_secret = None
        self._is_production = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if app_key is not None:
            self.app_key = app_key
        if api_secret is not None:
            self.api_secret = api_secret
        if is_production is not None:
            self.is_production = is_production

    @property
    def app_id(self):
        r"""Gets the app_id of this IflytekAiuiConfig.

        AIUI应用ID。

        :return: The app_id of this IflytekAiuiConfig.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this IflytekAiuiConfig.

        AIUI应用ID。

        :param app_id: The app_id of this IflytekAiuiConfig.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_key(self):
        r"""Gets the app_key of this IflytekAiuiConfig.

        AIUI应用密钥。

        :return: The app_key of this IflytekAiuiConfig.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        r"""Sets the app_key of this IflytekAiuiConfig.

        AIUI应用密钥。

        :param app_key: The app_key of this IflytekAiuiConfig.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def api_secret(self):
        r"""Gets the api_secret of this IflytekAiuiConfig.

        AIUI API密钥。

        :return: The api_secret of this IflytekAiuiConfig.
        :rtype: str
        """
        return self._api_secret

    @api_secret.setter
    def api_secret(self, api_secret):
        r"""Sets the api_secret of this IflytekAiuiConfig.

        AIUI API密钥。

        :param api_secret: The api_secret of this IflytekAiuiConfig.
        :type api_secret: str
        """
        self._api_secret = api_secret

    @property
    def is_production(self):
        r"""Gets the is_production of this IflytekAiuiConfig.

        是否为正式环境

        :return: The is_production of this IflytekAiuiConfig.
        :rtype: bool
        """
        return self._is_production

    @is_production.setter
    def is_production(self, is_production):
        r"""Sets the is_production of this IflytekAiuiConfig.

        是否为正式环境

        :param is_production: The is_production of this IflytekAiuiConfig.
        :type is_production: bool
        """
        self._is_production = is_production

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
        if not isinstance(other, IflytekAiuiConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
