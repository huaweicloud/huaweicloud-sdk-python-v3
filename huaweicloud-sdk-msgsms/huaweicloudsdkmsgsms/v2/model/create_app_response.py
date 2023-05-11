# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAppResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_key': 'str',
        'app_name': 'str',
        'id': 'str',
        'app_secret': 'str'
    }

    attribute_map = {
        'app_key': 'app_key',
        'app_name': 'app_name',
        'id': 'id',
        'app_secret': 'app_secret'
    }

    def __init__(self, app_key=None, app_name=None, id=None, app_secret=None):
        """CreateAppResponse

        The model defined in huaweicloud sdk

        :param app_key: 应用KEY
        :type app_key: str
        :param app_name: 应用名称
        :type app_name: str
        :param id: 应用主键ID
        :type id: str
        :param app_secret: Application Secret，应用密钥
        :type app_secret: str
        """
        
        super(CreateAppResponse, self).__init__()

        self._app_key = None
        self._app_name = None
        self._id = None
        self._app_secret = None
        self.discriminator = None

        if app_key is not None:
            self.app_key = app_key
        if app_name is not None:
            self.app_name = app_name
        if id is not None:
            self.id = id
        if app_secret is not None:
            self.app_secret = app_secret

    @property
    def app_key(self):
        """Gets the app_key of this CreateAppResponse.

        应用KEY

        :return: The app_key of this CreateAppResponse.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        """Sets the app_key of this CreateAppResponse.

        应用KEY

        :param app_key: The app_key of this CreateAppResponse.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def app_name(self):
        """Gets the app_name of this CreateAppResponse.

        应用名称

        :return: The app_name of this CreateAppResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this CreateAppResponse.

        应用名称

        :param app_name: The app_name of this CreateAppResponse.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def id(self):
        """Gets the id of this CreateAppResponse.

        应用主键ID

        :return: The id of this CreateAppResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateAppResponse.

        应用主键ID

        :param id: The id of this CreateAppResponse.
        :type id: str
        """
        self._id = id

    @property
    def app_secret(self):
        """Gets the app_secret of this CreateAppResponse.

        Application Secret，应用密钥

        :return: The app_secret of this CreateAppResponse.
        :rtype: str
        """
        return self._app_secret

    @app_secret.setter
    def app_secret(self, app_secret):
        """Sets the app_secret of this CreateAppResponse.

        Application Secret，应用密钥

        :param app_secret: The app_secret of this CreateAppResponse.
        :type app_secret: str
        """
        self._app_secret = app_secret

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
        if not isinstance(other, CreateAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
