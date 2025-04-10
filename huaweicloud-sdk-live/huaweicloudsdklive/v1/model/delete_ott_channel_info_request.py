# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteOttChannelInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_control_allow_internal': 'str',
        'access_control_allow_external': 'str',
        'domain': 'str',
        'app_name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'access_control_allow_internal': 'Access-Control-Allow-Internal',
        'access_control_allow_external': 'Access-Control-Allow-External',
        'domain': 'domain',
        'app_name': 'app_name',
        'id': 'id'
    }

    def __init__(self, access_control_allow_internal=None, access_control_allow_external=None, domain=None, app_name=None, id=None):
        r"""DeleteOttChannelInfoRequest

        The model defined in huaweicloud sdk

        :param access_control_allow_internal: 服务鉴权Token，服务开启鉴权，必须携带Access-Control-Allow-Internal访问服务。
        :type access_control_allow_internal: str
        :param access_control_allow_external: 服务鉴权Token，服务开启鉴权，必须携带Access-Control-Allow-External访问服务。
        :type access_control_allow_external: str
        :param domain: 推流域名
        :type domain: str
        :param app_name: 组名或应用名
        :type app_name: str
        :param id: 频道ID
        :type id: str
        """
        
        

        self._access_control_allow_internal = None
        self._access_control_allow_external = None
        self._domain = None
        self._app_name = None
        self._id = None
        self.discriminator = None

        if access_control_allow_internal is not None:
            self.access_control_allow_internal = access_control_allow_internal
        if access_control_allow_external is not None:
            self.access_control_allow_external = access_control_allow_external
        self.domain = domain
        self.app_name = app_name
        self.id = id

    @property
    def access_control_allow_internal(self):
        r"""Gets the access_control_allow_internal of this DeleteOttChannelInfoRequest.

        服务鉴权Token，服务开启鉴权，必须携带Access-Control-Allow-Internal访问服务。

        :return: The access_control_allow_internal of this DeleteOttChannelInfoRequest.
        :rtype: str
        """
        return self._access_control_allow_internal

    @access_control_allow_internal.setter
    def access_control_allow_internal(self, access_control_allow_internal):
        r"""Sets the access_control_allow_internal of this DeleteOttChannelInfoRequest.

        服务鉴权Token，服务开启鉴权，必须携带Access-Control-Allow-Internal访问服务。

        :param access_control_allow_internal: The access_control_allow_internal of this DeleteOttChannelInfoRequest.
        :type access_control_allow_internal: str
        """
        self._access_control_allow_internal = access_control_allow_internal

    @property
    def access_control_allow_external(self):
        r"""Gets the access_control_allow_external of this DeleteOttChannelInfoRequest.

        服务鉴权Token，服务开启鉴权，必须携带Access-Control-Allow-External访问服务。

        :return: The access_control_allow_external of this DeleteOttChannelInfoRequest.
        :rtype: str
        """
        return self._access_control_allow_external

    @access_control_allow_external.setter
    def access_control_allow_external(self, access_control_allow_external):
        r"""Sets the access_control_allow_external of this DeleteOttChannelInfoRequest.

        服务鉴权Token，服务开启鉴权，必须携带Access-Control-Allow-External访问服务。

        :param access_control_allow_external: The access_control_allow_external of this DeleteOttChannelInfoRequest.
        :type access_control_allow_external: str
        """
        self._access_control_allow_external = access_control_allow_external

    @property
    def domain(self):
        r"""Gets the domain of this DeleteOttChannelInfoRequest.

        推流域名

        :return: The domain of this DeleteOttChannelInfoRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this DeleteOttChannelInfoRequest.

        推流域名

        :param domain: The domain of this DeleteOttChannelInfoRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def app_name(self):
        r"""Gets the app_name of this DeleteOttChannelInfoRequest.

        组名或应用名

        :return: The app_name of this DeleteOttChannelInfoRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this DeleteOttChannelInfoRequest.

        组名或应用名

        :param app_name: The app_name of this DeleteOttChannelInfoRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def id(self):
        r"""Gets the id of this DeleteOttChannelInfoRequest.

        频道ID

        :return: The id of this DeleteOttChannelInfoRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DeleteOttChannelInfoRequest.

        频道ID

        :param id: The id of this DeleteOttChannelInfoRequest.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, DeleteOttChannelInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
