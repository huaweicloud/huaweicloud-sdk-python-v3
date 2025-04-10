# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiAuthCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'env_id': 'str',
        'app_ids': 'list[str]',
        'api_ids': 'list[str]'
    }

    attribute_map = {
        'env_id': 'env_id',
        'app_ids': 'app_ids',
        'api_ids': 'api_ids'
    }

    def __init__(self, env_id=None, app_ids=None, api_ids=None):
        r"""ApiAuthCreate

        The model defined in huaweicloud sdk

        :param env_id: 需要授权的环境编号
        :type env_id: str
        :param app_ids: APP的编号列表
        :type app_ids: list[str]
        :param api_ids: API的编号列表[，可以选择租户自己的API，也可以选择从云商店上购买的API](tag:hws)。
        :type api_ids: list[str]
        """
        
        

        self._env_id = None
        self._app_ids = None
        self._api_ids = None
        self.discriminator = None

        self.env_id = env_id
        self.app_ids = app_ids
        self.api_ids = api_ids

    @property
    def env_id(self):
        r"""Gets the env_id of this ApiAuthCreate.

        需要授权的环境编号

        :return: The env_id of this ApiAuthCreate.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this ApiAuthCreate.

        需要授权的环境编号

        :param env_id: The env_id of this ApiAuthCreate.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def app_ids(self):
        r"""Gets the app_ids of this ApiAuthCreate.

        APP的编号列表

        :return: The app_ids of this ApiAuthCreate.
        :rtype: list[str]
        """
        return self._app_ids

    @app_ids.setter
    def app_ids(self, app_ids):
        r"""Sets the app_ids of this ApiAuthCreate.

        APP的编号列表

        :param app_ids: The app_ids of this ApiAuthCreate.
        :type app_ids: list[str]
        """
        self._app_ids = app_ids

    @property
    def api_ids(self):
        r"""Gets the api_ids of this ApiAuthCreate.

        API的编号列表[，可以选择租户自己的API，也可以选择从云商店上购买的API](tag:hws)。

        :return: The api_ids of this ApiAuthCreate.
        :rtype: list[str]
        """
        return self._api_ids

    @api_ids.setter
    def api_ids(self, api_ids):
        r"""Sets the api_ids of this ApiAuthCreate.

        API的编号列表[，可以选择租户自己的API，也可以选择从云商店上购买的API](tag:hws)。

        :param api_ids: The api_ids of this ApiAuthCreate.
        :type api_ids: list[str]
        """
        self._api_ids = api_ids

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
        if not isinstance(other, ApiAuthCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
