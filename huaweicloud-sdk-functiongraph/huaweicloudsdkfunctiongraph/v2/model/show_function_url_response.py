# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFunctionUrlResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_type': 'str',
        'cors': 'CorsConfig',
        'function_url': 'str',
        'create_time': 'str',
        'last_modified_time': 'str'
    }

    attribute_map = {
        'auth_type': 'auth_type',
        'cors': 'cors',
        'function_url': 'function_url',
        'create_time': 'create_time',
        'last_modified_time': 'last_modified_time'
    }

    def __init__(self, auth_type=None, cors=None, function_url=None, create_time=None, last_modified_time=None):
        """ShowFunctionUrlResponse

        The model defined in huaweicloud sdk

        :param auth_type: 函数URL鉴权方式
        :type auth_type: str
        :param cors: 
        :type cors: :class:`huaweicloudsdkfunctiongraph.v2.CorsConfig`
        :param function_url: 函数URL地址
        :type function_url: str
        :param create_time: 函数URL创建时间
        :type create_time: str
        :param last_modified_time: 函数URL上次修改时间
        :type last_modified_time: str
        """
        
        super(ShowFunctionUrlResponse, self).__init__()

        self._auth_type = None
        self._cors = None
        self._function_url = None
        self._create_time = None
        self._last_modified_time = None
        self.discriminator = None

        if auth_type is not None:
            self.auth_type = auth_type
        if cors is not None:
            self.cors = cors
        if function_url is not None:
            self.function_url = function_url
        if create_time is not None:
            self.create_time = create_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time

    @property
    def auth_type(self):
        """Gets the auth_type of this ShowFunctionUrlResponse.

        函数URL鉴权方式

        :return: The auth_type of this ShowFunctionUrlResponse.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this ShowFunctionUrlResponse.

        函数URL鉴权方式

        :param auth_type: The auth_type of this ShowFunctionUrlResponse.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def cors(self):
        """Gets the cors of this ShowFunctionUrlResponse.

        :return: The cors of this ShowFunctionUrlResponse.
        :rtype: :class:`huaweicloudsdkfunctiongraph.v2.CorsConfig`
        """
        return self._cors

    @cors.setter
    def cors(self, cors):
        """Sets the cors of this ShowFunctionUrlResponse.

        :param cors: The cors of this ShowFunctionUrlResponse.
        :type cors: :class:`huaweicloudsdkfunctiongraph.v2.CorsConfig`
        """
        self._cors = cors

    @property
    def function_url(self):
        """Gets the function_url of this ShowFunctionUrlResponse.

        函数URL地址

        :return: The function_url of this ShowFunctionUrlResponse.
        :rtype: str
        """
        return self._function_url

    @function_url.setter
    def function_url(self, function_url):
        """Sets the function_url of this ShowFunctionUrlResponse.

        函数URL地址

        :param function_url: The function_url of this ShowFunctionUrlResponse.
        :type function_url: str
        """
        self._function_url = function_url

    @property
    def create_time(self):
        """Gets the create_time of this ShowFunctionUrlResponse.

        函数URL创建时间

        :return: The create_time of this ShowFunctionUrlResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowFunctionUrlResponse.

        函数URL创建时间

        :param create_time: The create_time of this ShowFunctionUrlResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def last_modified_time(self):
        """Gets the last_modified_time of this ShowFunctionUrlResponse.

        函数URL上次修改时间

        :return: The last_modified_time of this ShowFunctionUrlResponse.
        :rtype: str
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        """Sets the last_modified_time of this ShowFunctionUrlResponse.

        函数URL上次修改时间

        :param last_modified_time: The last_modified_time of this ShowFunctionUrlResponse.
        :type last_modified_time: str
        """
        self._last_modified_time = last_modified_time

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
        if not isinstance(other, ShowFunctionUrlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
