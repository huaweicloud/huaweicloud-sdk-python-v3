# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdentityAssumerole:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'agency_name': 'str',
        'domain_id': 'str',
        'domain_name': 'str',
        'duration_seconds': 'int',
        'session_user': 'AssumeroleSessionuser'
    }

    attribute_map = {
        'agency_name': 'agency_name',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'duration_seconds': 'duration_seconds',
        'session_user': 'session_user'
    }

    def __init__(self, agency_name=None, domain_id=None, domain_name=None, duration_seconds=None, session_user=None):
        """IdentityAssumerole

        The model defined in huaweicloud sdk

        :param agency_name: 委托名。
        :type agency_name: str
        :param domain_id: 委托方的账号ID。“domain_id”与“domain_name”至少填写一个。
        :type domain_id: str
        :param domain_name: 委托方的账号名。“domain_id”与“domain_name”至少填写一个。
        :type domain_name: str
        :param duration_seconds: AK/SK和securitytoken的有效期，时间单位为秒。取值范围：15min ~ 24h ，默认为15min。
        :type duration_seconds: int
        :param session_user: 
        :type session_user: :class:`huaweicloudsdkiam.v3.AssumeroleSessionuser`
        """
        
        

        self._agency_name = None
        self._domain_id = None
        self._domain_name = None
        self._duration_seconds = None
        self._session_user = None
        self.discriminator = None

        self.agency_name = agency_name
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if duration_seconds is not None:
            self.duration_seconds = duration_seconds
        if session_user is not None:
            self.session_user = session_user

    @property
    def agency_name(self):
        """Gets the agency_name of this IdentityAssumerole.

        委托名。

        :return: The agency_name of this IdentityAssumerole.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        """Sets the agency_name of this IdentityAssumerole.

        委托名。

        :param agency_name: The agency_name of this IdentityAssumerole.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def domain_id(self):
        """Gets the domain_id of this IdentityAssumerole.

        委托方的账号ID。“domain_id”与“domain_name”至少填写一个。

        :return: The domain_id of this IdentityAssumerole.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this IdentityAssumerole.

        委托方的账号ID。“domain_id”与“domain_name”至少填写一个。

        :param domain_id: The domain_id of this IdentityAssumerole.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        """Gets the domain_name of this IdentityAssumerole.

        委托方的账号名。“domain_id”与“domain_name”至少填写一个。

        :return: The domain_name of this IdentityAssumerole.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this IdentityAssumerole.

        委托方的账号名。“domain_id”与“domain_name”至少填写一个。

        :param domain_name: The domain_name of this IdentityAssumerole.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def duration_seconds(self):
        """Gets the duration_seconds of this IdentityAssumerole.

        AK/SK和securitytoken的有效期，时间单位为秒。取值范围：15min ~ 24h ，默认为15min。

        :return: The duration_seconds of this IdentityAssumerole.
        :rtype: int
        """
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, duration_seconds):
        """Sets the duration_seconds of this IdentityAssumerole.

        AK/SK和securitytoken的有效期，时间单位为秒。取值范围：15min ~ 24h ，默认为15min。

        :param duration_seconds: The duration_seconds of this IdentityAssumerole.
        :type duration_seconds: int
        """
        self._duration_seconds = duration_seconds

    @property
    def session_user(self):
        """Gets the session_user of this IdentityAssumerole.


        :return: The session_user of this IdentityAssumerole.
        :rtype: :class:`huaweicloudsdkiam.v3.AssumeroleSessionuser`
        """
        return self._session_user

    @session_user.setter
    def session_user(self, session_user):
        """Sets the session_user of this IdentityAssumerole.


        :param session_user: The session_user of this IdentityAssumerole.
        :type session_user: :class:`huaweicloudsdkiam.v3.AssumeroleSessionuser`
        """
        self._session_user = session_user

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
        if not isinstance(other, IdentityAssumerole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
