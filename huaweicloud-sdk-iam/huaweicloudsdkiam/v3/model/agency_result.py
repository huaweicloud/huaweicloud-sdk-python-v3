# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgencyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'create_time': 'str',
        'description': 'str',
        'domain_id': 'str',
        'duration': 'str',
        'expire_time': 'str',
        'id': 'str',
        'name': 'str',
        'trust_domain_id': 'str',
        'trust_domain_name': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'description': 'description',
        'domain_id': 'domain_id',
        'duration': 'duration',
        'expire_time': 'expire_time',
        'id': 'id',
        'name': 'name',
        'trust_domain_id': 'trust_domain_id',
        'trust_domain_name': 'trust_domain_name'
    }

    def __init__(self, create_time=None, description=None, domain_id=None, duration=None, expire_time=None, id=None, name=None, trust_domain_id=None, trust_domain_name=None):
        """AgencyResult

        The model defined in huaweicloud sdk

        :param create_time: 委托创建时间。
        :type create_time: str
        :param description: 委托描述信息。
        :type description: str
        :param domain_id: 委托方账号ID。
        :type domain_id: str
        :param duration: 委托的期限。取值为\&quot;FOREVER\&quot;或“null”表示委托的期限为永久，取值为\&quot;ONEDAY\&quot;表示委托的期限为一天。
        :type duration: str
        :param expire_time: 委托过期时间。“null”表示不过期。
        :type expire_time: str
        :param id: 委托ID。
        :type id: str
        :param name: 委托名。
        :type name: str
        :param trust_domain_id: 被委托方账号ID。
        :type trust_domain_id: str
        :param trust_domain_name: 被委托方账号名。
        :type trust_domain_name: str
        """
        
        

        self._create_time = None
        self._description = None
        self._domain_id = None
        self._duration = None
        self._expire_time = None
        self._id = None
        self._name = None
        self._trust_domain_id = None
        self._trust_domain_name = None
        self.discriminator = None

        self.create_time = create_time
        self.description = description
        if domain_id is not None:
            self.domain_id = domain_id
        self.duration = duration
        self.expire_time = expire_time
        self.id = id
        self.name = name
        if trust_domain_id is not None:
            self.trust_domain_id = trust_domain_id
        if trust_domain_name is not None:
            self.trust_domain_name = trust_domain_name

    @property
    def create_time(self):
        """Gets the create_time of this AgencyResult.

        委托创建时间。

        :return: The create_time of this AgencyResult.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AgencyResult.

        委托创建时间。

        :param create_time: The create_time of this AgencyResult.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this AgencyResult.

        委托描述信息。

        :return: The description of this AgencyResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AgencyResult.

        委托描述信息。

        :param description: The description of this AgencyResult.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        """Gets the domain_id of this AgencyResult.

        委托方账号ID。

        :return: The domain_id of this AgencyResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this AgencyResult.

        委托方账号ID。

        :param domain_id: The domain_id of this AgencyResult.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def duration(self):
        """Gets the duration of this AgencyResult.

        委托的期限。取值为\"FOREVER\"或“null”表示委托的期限为永久，取值为\"ONEDAY\"表示委托的期限为一天。

        :return: The duration of this AgencyResult.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this AgencyResult.

        委托的期限。取值为\"FOREVER\"或“null”表示委托的期限为永久，取值为\"ONEDAY\"表示委托的期限为一天。

        :param duration: The duration of this AgencyResult.
        :type duration: str
        """
        self._duration = duration

    @property
    def expire_time(self):
        """Gets the expire_time of this AgencyResult.

        委托过期时间。“null”表示不过期。

        :return: The expire_time of this AgencyResult.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this AgencyResult.

        委托过期时间。“null”表示不过期。

        :param expire_time: The expire_time of this AgencyResult.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def id(self):
        """Gets the id of this AgencyResult.

        委托ID。

        :return: The id of this AgencyResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AgencyResult.

        委托ID。

        :param id: The id of this AgencyResult.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AgencyResult.

        委托名。

        :return: The name of this AgencyResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AgencyResult.

        委托名。

        :param name: The name of this AgencyResult.
        :type name: str
        """
        self._name = name

    @property
    def trust_domain_id(self):
        """Gets the trust_domain_id of this AgencyResult.

        被委托方账号ID。

        :return: The trust_domain_id of this AgencyResult.
        :rtype: str
        """
        return self._trust_domain_id

    @trust_domain_id.setter
    def trust_domain_id(self, trust_domain_id):
        """Sets the trust_domain_id of this AgencyResult.

        被委托方账号ID。

        :param trust_domain_id: The trust_domain_id of this AgencyResult.
        :type trust_domain_id: str
        """
        self._trust_domain_id = trust_domain_id

    @property
    def trust_domain_name(self):
        """Gets the trust_domain_name of this AgencyResult.

        被委托方账号名。

        :return: The trust_domain_name of this AgencyResult.
        :rtype: str
        """
        return self._trust_domain_name

    @trust_domain_name.setter
    def trust_domain_name(self, trust_domain_name):
        """Sets the trust_domain_name of this AgencyResult.

        被委托方账号名。

        :param trust_domain_name: The trust_domain_name of this AgencyResult.
        :type trust_domain_name: str
        """
        self._trust_domain_name = trust_domain_name

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
        if not isinstance(other, AgencyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
