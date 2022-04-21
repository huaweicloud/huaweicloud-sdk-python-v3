# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddApplicationResponse(SdkResponse):

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
        'app_name': 'str',
        'create_time': 'str',
        'default_app': 'bool'
    }

    attribute_map = {
        'app_id': 'app_id',
        'app_name': 'app_name',
        'create_time': 'create_time',
        'default_app': 'default_app'
    }

    def __init__(self, app_id=None, app_name=None, create_time=None, default_app=None):
        """AddApplicationResponse

        The model defined in huaweicloud sdk

        :param app_id: 资源空间ID，唯一标识一个资源空间，由物联网平台在创建资源空间时分配。资源空间对应的是物联网平台原有的应用，在物联网平台的含义与应用一致，只是变更了名称。
        :type app_id: str
        :param app_name: 资源空间名称。
        :type app_name: str
        :param create_time: 资源空间创建时间，格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type create_time: str
        :param default_app: 是否为默认资源空间
        :type default_app: bool
        """
        
        super(AddApplicationResponse, self).__init__()

        self._app_id = None
        self._app_name = None
        self._create_time = None
        self._default_app = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if create_time is not None:
            self.create_time = create_time
        if default_app is not None:
            self.default_app = default_app

    @property
    def app_id(self):
        """Gets the app_id of this AddApplicationResponse.

        资源空间ID，唯一标识一个资源空间，由物联网平台在创建资源空间时分配。资源空间对应的是物联网平台原有的应用，在物联网平台的含义与应用一致，只是变更了名称。

        :return: The app_id of this AddApplicationResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AddApplicationResponse.

        资源空间ID，唯一标识一个资源空间，由物联网平台在创建资源空间时分配。资源空间对应的是物联网平台原有的应用，在物联网平台的含义与应用一致，只是变更了名称。

        :param app_id: The app_id of this AddApplicationResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        """Gets the app_name of this AddApplicationResponse.

        资源空间名称。

        :return: The app_name of this AddApplicationResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this AddApplicationResponse.

        资源空间名称。

        :param app_name: The app_name of this AddApplicationResponse.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def create_time(self):
        """Gets the create_time of this AddApplicationResponse.

        资源空间创建时间，格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The create_time of this AddApplicationResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AddApplicationResponse.

        资源空间创建时间，格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param create_time: The create_time of this AddApplicationResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def default_app(self):
        """Gets the default_app of this AddApplicationResponse.

        是否为默认资源空间

        :return: The default_app of this AddApplicationResponse.
        :rtype: bool
        """
        return self._default_app

    @default_app.setter
    def default_app(self, default_app):
        """Sets the default_app of this AddApplicationResponse.

        是否为默认资源空间

        :param default_app: The default_app of this AddApplicationResponse.
        :type default_app: bool
        """
        self._default_app = default_app

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
        if not isinstance(other, AddApplicationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
