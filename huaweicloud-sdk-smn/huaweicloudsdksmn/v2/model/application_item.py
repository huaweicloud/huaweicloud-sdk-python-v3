# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicationItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'platform': 'str',
        'create_time': 'str',
        'application_urn': 'str',
        'application_id': 'str',
        'enabled': 'str',
        'apple_certificate_expiration_date': 'str'
    }

    attribute_map = {
        'name': 'name',
        'platform': 'platform',
        'create_time': 'create_time',
        'application_urn': 'application_urn',
        'application_id': 'application_id',
        'enabled': 'enabled',
        'apple_certificate_expiration_date': 'apple_certificate_expiration_date'
    }

    def __init__(self, name=None, platform=None, create_time=None, application_urn=None, application_id=None, enabled=None, apple_certificate_expiration_date=None):
        """ApplicationItem

        The model defined in huaweicloud sdk

        :param name: 创建application的名字。
        :type name: str
        :param platform: 应用平台。
        :type platform: str
        :param create_time: 创建application的时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。
        :type create_time: str
        :param application_urn: Application的唯一资源标识。
        :type application_urn: str
        :param application_id: Application的唯一标识ID。
        :type application_id: str
        :param enabled: 应用平台是否启用。
        :type enabled: str
        :param apple_certificate_expiration_date: 苹果证书过期时间APNS、APNS_SANDBOX平台特有属性时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。
        :type apple_certificate_expiration_date: str
        """
        
        

        self._name = None
        self._platform = None
        self._create_time = None
        self._application_urn = None
        self._application_id = None
        self._enabled = None
        self._apple_certificate_expiration_date = None
        self.discriminator = None

        self.name = name
        self.platform = platform
        self.create_time = create_time
        self.application_urn = application_urn
        self.application_id = application_id
        self.enabled = enabled
        if apple_certificate_expiration_date is not None:
            self.apple_certificate_expiration_date = apple_certificate_expiration_date

    @property
    def name(self):
        """Gets the name of this ApplicationItem.

        创建application的名字。

        :return: The name of this ApplicationItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationItem.

        创建application的名字。

        :param name: The name of this ApplicationItem.
        :type name: str
        """
        self._name = name

    @property
    def platform(self):
        """Gets the platform of this ApplicationItem.

        应用平台。

        :return: The platform of this ApplicationItem.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this ApplicationItem.

        应用平台。

        :param platform: The platform of this ApplicationItem.
        :type platform: str
        """
        self._platform = platform

    @property
    def create_time(self):
        """Gets the create_time of this ApplicationItem.

        创建application的时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :return: The create_time of this ApplicationItem.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ApplicationItem.

        创建application的时间。时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :param create_time: The create_time of this ApplicationItem.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def application_urn(self):
        """Gets the application_urn of this ApplicationItem.

        Application的唯一资源标识。

        :return: The application_urn of this ApplicationItem.
        :rtype: str
        """
        return self._application_urn

    @application_urn.setter
    def application_urn(self, application_urn):
        """Sets the application_urn of this ApplicationItem.

        Application的唯一资源标识。

        :param application_urn: The application_urn of this ApplicationItem.
        :type application_urn: str
        """
        self._application_urn = application_urn

    @property
    def application_id(self):
        """Gets the application_id of this ApplicationItem.

        Application的唯一标识ID。

        :return: The application_id of this ApplicationItem.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ApplicationItem.

        Application的唯一标识ID。

        :param application_id: The application_id of this ApplicationItem.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def enabled(self):
        """Gets the enabled of this ApplicationItem.

        应用平台是否启用。

        :return: The enabled of this ApplicationItem.
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ApplicationItem.

        应用平台是否启用。

        :param enabled: The enabled of this ApplicationItem.
        :type enabled: str
        """
        self._enabled = enabled

    @property
    def apple_certificate_expiration_date(self):
        """Gets the apple_certificate_expiration_date of this ApplicationItem.

        苹果证书过期时间APNS、APNS_SANDBOX平台特有属性时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :return: The apple_certificate_expiration_date of this ApplicationItem.
        :rtype: str
        """
        return self._apple_certificate_expiration_date

    @apple_certificate_expiration_date.setter
    def apple_certificate_expiration_date(self, apple_certificate_expiration_date):
        """Sets the apple_certificate_expiration_date of this ApplicationItem.

        苹果证书过期时间APNS、APNS_SANDBOX平台特有属性时间格式为UTC时间，YYYY-MM-DDTHH:MM:SSZ。

        :param apple_certificate_expiration_date: The apple_certificate_expiration_date of this ApplicationItem.
        :type apple_certificate_expiration_date: str
        """
        self._apple_certificate_expiration_date = apple_certificate_expiration_date

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
        if not isinstance(other, ApplicationItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
