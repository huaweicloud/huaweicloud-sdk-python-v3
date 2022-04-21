# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationEndpointsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []
    sensitive_list.append('token')

    openapi_types = {
        'application_urn': 'str',
        'offset': 'int',
        'limit': 'int',
        'enabled': 'str',
        'token': 'str',
        'user_data': 'str'
    }

    attribute_map = {
        'application_urn': 'application_urn',
        'offset': 'offset',
        'limit': 'limit',
        'enabled': 'enabled',
        'token': 'token',
        'user_data': 'user_data'
    }

    def __init__(self, application_urn=None, offset=None, limit=None, enabled=None, token=None, user_data=None):
        """ListApplicationEndpointsRequest

        The model defined in huaweicloud sdk

        :param application_urn: Application的唯一资源标识，可通过[查询Application](https://support.huaweicloud.com/api-smn/ListApplications.html)获取该标识。
        :type application_urn: str
        :param offset: 偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。
        :type offset: int
        :param limit: 查询的数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。
        :type limit: int
        :param enabled: 设备是否可用，值为true或false字符串。
        :type enabled: str
        :param token: 设备token，最大长度512个字节。
        :type token: str
        :param user_data: 用户数据，最大长度2048个字节。
        :type user_data: str
        """
        
        

        self._application_urn = None
        self._offset = None
        self._limit = None
        self._enabled = None
        self._token = None
        self._user_data = None
        self.discriminator = None

        self.application_urn = application_urn
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if enabled is not None:
            self.enabled = enabled
        if token is not None:
            self.token = token
        if user_data is not None:
            self.user_data = user_data

    @property
    def application_urn(self):
        """Gets the application_urn of this ListApplicationEndpointsRequest.

        Application的唯一资源标识，可通过[查询Application](https://support.huaweicloud.com/api-smn/ListApplications.html)获取该标识。

        :return: The application_urn of this ListApplicationEndpointsRequest.
        :rtype: str
        """
        return self._application_urn

    @application_urn.setter
    def application_urn(self, application_urn):
        """Sets the application_urn of this ListApplicationEndpointsRequest.

        Application的唯一资源标识，可通过[查询Application](https://support.huaweicloud.com/api-smn/ListApplications.html)获取该标识。

        :param application_urn: The application_urn of this ListApplicationEndpointsRequest.
        :type application_urn: str
        """
        self._application_urn = application_urn

    @property
    def offset(self):
        """Gets the offset of this ListApplicationEndpointsRequest.

        偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。

        :return: The offset of this ListApplicationEndpointsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListApplicationEndpointsRequest.

        偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。

        :param offset: The offset of this ListApplicationEndpointsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListApplicationEndpointsRequest.

        查询的数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。

        :return: The limit of this ListApplicationEndpointsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListApplicationEndpointsRequest.

        查询的数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。

        :param limit: The limit of this ListApplicationEndpointsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def enabled(self):
        """Gets the enabled of this ListApplicationEndpointsRequest.

        设备是否可用，值为true或false字符串。

        :return: The enabled of this ListApplicationEndpointsRequest.
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ListApplicationEndpointsRequest.

        设备是否可用，值为true或false字符串。

        :param enabled: The enabled of this ListApplicationEndpointsRequest.
        :type enabled: str
        """
        self._enabled = enabled

    @property
    def token(self):
        """Gets the token of this ListApplicationEndpointsRequest.

        设备token，最大长度512个字节。

        :return: The token of this ListApplicationEndpointsRequest.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ListApplicationEndpointsRequest.

        设备token，最大长度512个字节。

        :param token: The token of this ListApplicationEndpointsRequest.
        :type token: str
        """
        self._token = token

    @property
    def user_data(self):
        """Gets the user_data of this ListApplicationEndpointsRequest.

        用户数据，最大长度2048个字节。

        :return: The user_data of this ListApplicationEndpointsRequest.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this ListApplicationEndpointsRequest.

        用户数据，最大长度2048个字节。

        :param user_data: The user_data of this ListApplicationEndpointsRequest.
        :type user_data: str
        """
        self._user_data = user_data

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
        if not isinstance(other, ListApplicationEndpointsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
