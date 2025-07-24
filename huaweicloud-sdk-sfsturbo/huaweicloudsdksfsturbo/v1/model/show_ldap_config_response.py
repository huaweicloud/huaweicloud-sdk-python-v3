# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLdapConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'base_dn': 'str',
        'user_dn': 'str',
        'filter_condition': 'str',
        'vpc_id': 'str',
        'backup_url': 'str',
        'schema': 'str',
        'search_timeout': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'url': 'url',
        'base_dn': 'base_dn',
        'user_dn': 'user_dn',
        'filter_condition': 'filter_condition',
        'vpc_id': 'vpc_id',
        'backup_url': 'backup_url',
        'schema': 'schema',
        'search_timeout': 'search_timeout',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, url=None, base_dn=None, user_dn=None, filter_condition=None, vpc_id=None, backup_url=None, schema=None, search_timeout=None, x_request_id=None):
        r"""ShowLdapConfigResponse

        The model defined in huaweicloud sdk

        :param url: LDAP服务器的url
        :type url: str
        :param base_dn: 数据库中的域
        :type base_dn: str
        :param user_dn: 用户区别名
        :type user_dn: str
        :param filter_condition: 过滤条件。保留字段，暂不支持
        :type filter_condition: str
        :param vpc_id: 保留字段，暂不支持
        :type vpc_id: str
        :param backup_url: LDAP备节点的url
        :type backup_url: str
        :param schema: LDAP的schema，不填写则默认为RFC2307
        :type schema: str
        :param search_timeout: LDAP搜索的超时时间，单位为秒。不填写则默认为3秒
        :type search_timeout: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowLdapConfigResponse, self).__init__()

        self._url = None
        self._base_dn = None
        self._user_dn = None
        self._filter_condition = None
        self._vpc_id = None
        self._backup_url = None
        self._schema = None
        self._search_timeout = None
        self._x_request_id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if base_dn is not None:
            self.base_dn = base_dn
        if user_dn is not None:
            self.user_dn = user_dn
        if filter_condition is not None:
            self.filter_condition = filter_condition
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if backup_url is not None:
            self.backup_url = backup_url
        if schema is not None:
            self.schema = schema
        if search_timeout is not None:
            self.search_timeout = search_timeout
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def url(self):
        r"""Gets the url of this ShowLdapConfigResponse.

        LDAP服务器的url

        :return: The url of this ShowLdapConfigResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ShowLdapConfigResponse.

        LDAP服务器的url

        :param url: The url of this ShowLdapConfigResponse.
        :type url: str
        """
        self._url = url

    @property
    def base_dn(self):
        r"""Gets the base_dn of this ShowLdapConfigResponse.

        数据库中的域

        :return: The base_dn of this ShowLdapConfigResponse.
        :rtype: str
        """
        return self._base_dn

    @base_dn.setter
    def base_dn(self, base_dn):
        r"""Sets the base_dn of this ShowLdapConfigResponse.

        数据库中的域

        :param base_dn: The base_dn of this ShowLdapConfigResponse.
        :type base_dn: str
        """
        self._base_dn = base_dn

    @property
    def user_dn(self):
        r"""Gets the user_dn of this ShowLdapConfigResponse.

        用户区别名

        :return: The user_dn of this ShowLdapConfigResponse.
        :rtype: str
        """
        return self._user_dn

    @user_dn.setter
    def user_dn(self, user_dn):
        r"""Sets the user_dn of this ShowLdapConfigResponse.

        用户区别名

        :param user_dn: The user_dn of this ShowLdapConfigResponse.
        :type user_dn: str
        """
        self._user_dn = user_dn

    @property
    def filter_condition(self):
        r"""Gets the filter_condition of this ShowLdapConfigResponse.

        过滤条件。保留字段，暂不支持

        :return: The filter_condition of this ShowLdapConfigResponse.
        :rtype: str
        """
        return self._filter_condition

    @filter_condition.setter
    def filter_condition(self, filter_condition):
        r"""Sets the filter_condition of this ShowLdapConfigResponse.

        过滤条件。保留字段，暂不支持

        :param filter_condition: The filter_condition of this ShowLdapConfigResponse.
        :type filter_condition: str
        """
        self._filter_condition = filter_condition

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ShowLdapConfigResponse.

        保留字段，暂不支持

        :return: The vpc_id of this ShowLdapConfigResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ShowLdapConfigResponse.

        保留字段，暂不支持

        :param vpc_id: The vpc_id of this ShowLdapConfigResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def backup_url(self):
        r"""Gets the backup_url of this ShowLdapConfigResponse.

        LDAP备节点的url

        :return: The backup_url of this ShowLdapConfigResponse.
        :rtype: str
        """
        return self._backup_url

    @backup_url.setter
    def backup_url(self, backup_url):
        r"""Sets the backup_url of this ShowLdapConfigResponse.

        LDAP备节点的url

        :param backup_url: The backup_url of this ShowLdapConfigResponse.
        :type backup_url: str
        """
        self._backup_url = backup_url

    @property
    def schema(self):
        r"""Gets the schema of this ShowLdapConfigResponse.

        LDAP的schema，不填写则默认为RFC2307

        :return: The schema of this ShowLdapConfigResponse.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this ShowLdapConfigResponse.

        LDAP的schema，不填写则默认为RFC2307

        :param schema: The schema of this ShowLdapConfigResponse.
        :type schema: str
        """
        self._schema = schema

    @property
    def search_timeout(self):
        r"""Gets the search_timeout of this ShowLdapConfigResponse.

        LDAP搜索的超时时间，单位为秒。不填写则默认为3秒

        :return: The search_timeout of this ShowLdapConfigResponse.
        :rtype: int
        """
        return self._search_timeout

    @search_timeout.setter
    def search_timeout(self, search_timeout):
        r"""Sets the search_timeout of this ShowLdapConfigResponse.

        LDAP搜索的超时时间，单位为秒。不填写则默认为3秒

        :param search_timeout: The search_timeout of this ShowLdapConfigResponse.
        :type search_timeout: int
        """
        self._search_timeout = search_timeout

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowLdapConfigResponse.

        :return: The x_request_id of this ShowLdapConfigResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowLdapConfigResponse.

        :param x_request_id: The x_request_id of this ShowLdapConfigResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowLdapConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
