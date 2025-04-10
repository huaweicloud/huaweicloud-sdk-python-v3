# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubscriptionUserResponseItemInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'domain_id': 'str',
        'name': 'str',
        'status': 'str',
        'group': 'list[str]',
        'create_time': 'str',
        'update_time': 'str',
        'http': 'ListSubscriptionUserResponseHttpEndpointInfo',
        'https': 'ListSubscriptionUserResponseHttpsEndpointInfo',
        'sms': 'ListSubscriptionUserResponseSmsEndpointInfo',
        'email': 'ListSubscriptionUserResponseEmailEndpointInfo'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domain_id',
        'name': 'name',
        'status': 'status',
        'group': 'group',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'http': 'http',
        'https': 'https',
        'sms': 'sms',
        'email': 'email'
    }

    def __init__(self, id=None, domain_id=None, name=None, status=None, group=None, create_time=None, update_time=None, http=None, https=None, sms=None, email=None):
        r"""ListSubscriptionUserResponseItemInfo

        The model defined in huaweicloud sdk

        :param id: 订阅用户ID。
        :type id: str
        :param domain_id: 租户账号ID。
        :type domain_id: str
        :param name: 订阅用户名称。
        :type name: str
        :param status: 订阅用户状态。 UNCONFIRMED：未确认 CONFIRMED：已确认 CANCELLED：已取消
        :type status: str
        :param group: 订阅用户分组。
        :type group: list[str]
        :param create_time: 创建时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。
        :type create_time: str
        :param update_time: 更新时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。
        :type update_time: str
        :param http: 
        :type http: :class:`huaweicloudsdksmnglobal.v2.ListSubscriptionUserResponseHttpEndpointInfo`
        :param https: 
        :type https: :class:`huaweicloudsdksmnglobal.v2.ListSubscriptionUserResponseHttpsEndpointInfo`
        :param sms: 
        :type sms: :class:`huaweicloudsdksmnglobal.v2.ListSubscriptionUserResponseSmsEndpointInfo`
        :param email: 
        :type email: :class:`huaweicloudsdksmnglobal.v2.ListSubscriptionUserResponseEmailEndpointInfo`
        """
        
        

        self._id = None
        self._domain_id = None
        self._name = None
        self._status = None
        self._group = None
        self._create_time = None
        self._update_time = None
        self._http = None
        self._https = None
        self._sms = None
        self._email = None
        self.discriminator = None

        self.id = id
        self.domain_id = domain_id
        self.name = name
        self.status = status
        self.group = group
        self.create_time = create_time
        self.update_time = update_time
        if http is not None:
            self.http = http
        if https is not None:
            self.https = https
        if sms is not None:
            self.sms = sms
        if email is not None:
            self.email = email

    @property
    def id(self):
        r"""Gets the id of this ListSubscriptionUserResponseItemInfo.

        订阅用户ID。

        :return: The id of this ListSubscriptionUserResponseItemInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSubscriptionUserResponseItemInfo.

        订阅用户ID。

        :param id: The id of this ListSubscriptionUserResponseItemInfo.
        :type id: str
        """
        self._id = id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListSubscriptionUserResponseItemInfo.

        租户账号ID。

        :return: The domain_id of this ListSubscriptionUserResponseItemInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListSubscriptionUserResponseItemInfo.

        租户账号ID。

        :param domain_id: The domain_id of this ListSubscriptionUserResponseItemInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def name(self):
        r"""Gets the name of this ListSubscriptionUserResponseItemInfo.

        订阅用户名称。

        :return: The name of this ListSubscriptionUserResponseItemInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSubscriptionUserResponseItemInfo.

        订阅用户名称。

        :param name: The name of this ListSubscriptionUserResponseItemInfo.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ListSubscriptionUserResponseItemInfo.

        订阅用户状态。 UNCONFIRMED：未确认 CONFIRMED：已确认 CANCELLED：已取消

        :return: The status of this ListSubscriptionUserResponseItemInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListSubscriptionUserResponseItemInfo.

        订阅用户状态。 UNCONFIRMED：未确认 CONFIRMED：已确认 CANCELLED：已取消

        :param status: The status of this ListSubscriptionUserResponseItemInfo.
        :type status: str
        """
        self._status = status

    @property
    def group(self):
        r"""Gets the group of this ListSubscriptionUserResponseItemInfo.

        订阅用户分组。

        :return: The group of this ListSubscriptionUserResponseItemInfo.
        :rtype: list[str]
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this ListSubscriptionUserResponseItemInfo.

        订阅用户分组。

        :param group: The group of this ListSubscriptionUserResponseItemInfo.
        :type group: list[str]
        """
        self._group = group

    @property
    def create_time(self):
        r"""Gets the create_time of this ListSubscriptionUserResponseItemInfo.

        创建时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :return: The create_time of this ListSubscriptionUserResponseItemInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListSubscriptionUserResponseItemInfo.

        创建时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :param create_time: The create_time of this ListSubscriptionUserResponseItemInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ListSubscriptionUserResponseItemInfo.

        更新时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :return: The update_time of this ListSubscriptionUserResponseItemInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ListSubscriptionUserResponseItemInfo.

        更新时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :param update_time: The update_time of this ListSubscriptionUserResponseItemInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def http(self):
        r"""Gets the http of this ListSubscriptionUserResponseItemInfo.

        :return: The http of this ListSubscriptionUserResponseItemInfo.
        :rtype: :class:`huaweicloudsdksmnglobal.v2.ListSubscriptionUserResponseHttpEndpointInfo`
        """
        return self._http

    @http.setter
    def http(self, http):
        r"""Sets the http of this ListSubscriptionUserResponseItemInfo.

        :param http: The http of this ListSubscriptionUserResponseItemInfo.
        :type http: :class:`huaweicloudsdksmnglobal.v2.ListSubscriptionUserResponseHttpEndpointInfo`
        """
        self._http = http

    @property
    def https(self):
        r"""Gets the https of this ListSubscriptionUserResponseItemInfo.

        :return: The https of this ListSubscriptionUserResponseItemInfo.
        :rtype: :class:`huaweicloudsdksmnglobal.v2.ListSubscriptionUserResponseHttpsEndpointInfo`
        """
        return self._https

    @https.setter
    def https(self, https):
        r"""Sets the https of this ListSubscriptionUserResponseItemInfo.

        :param https: The https of this ListSubscriptionUserResponseItemInfo.
        :type https: :class:`huaweicloudsdksmnglobal.v2.ListSubscriptionUserResponseHttpsEndpointInfo`
        """
        self._https = https

    @property
    def sms(self):
        r"""Gets the sms of this ListSubscriptionUserResponseItemInfo.

        :return: The sms of this ListSubscriptionUserResponseItemInfo.
        :rtype: :class:`huaweicloudsdksmnglobal.v2.ListSubscriptionUserResponseSmsEndpointInfo`
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        r"""Sets the sms of this ListSubscriptionUserResponseItemInfo.

        :param sms: The sms of this ListSubscriptionUserResponseItemInfo.
        :type sms: :class:`huaweicloudsdksmnglobal.v2.ListSubscriptionUserResponseSmsEndpointInfo`
        """
        self._sms = sms

    @property
    def email(self):
        r"""Gets the email of this ListSubscriptionUserResponseItemInfo.

        :return: The email of this ListSubscriptionUserResponseItemInfo.
        :rtype: :class:`huaweicloudsdksmnglobal.v2.ListSubscriptionUserResponseEmailEndpointInfo`
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this ListSubscriptionUserResponseItemInfo.

        :param email: The email of this ListSubscriptionUserResponseItemInfo.
        :type email: :class:`huaweicloudsdksmnglobal.v2.ListSubscriptionUserResponseEmailEndpointInfo`
        """
        self._email = email

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
        if not isinstance(other, ListSubscriptionUserResponseItemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
