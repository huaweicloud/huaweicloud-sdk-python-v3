# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgencyV2:

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
        'name': 'str',
        'duration': 'str',
        'trust_domain_name': 'str',
        'trust_domain_id': 'str',
        'create_time': 'str',
        'expire_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'duration': 'duration',
        'trust_domain_name': 'trust_domain_name',
        'trust_domain_id': 'trust_domain_id',
        'create_time': 'create_time',
        'expire_time': 'expire_time'
    }

    def __init__(self, id=None, name=None, duration=None, trust_domain_name=None, trust_domain_id=None, create_time=None, expire_time=None):
        r"""AgencyV2

        The model defined in huaweicloud sdk

        :param id: 委托id
        :type id: str
        :param name: 委托名称
        :type name: str
        :param duration: 委托的期限
        :type duration: str
        :param trust_domain_name: 委托的账号名称
        :type trust_domain_name: str
        :param trust_domain_id: 委托的账号id
        :type trust_domain_id: str
        :param create_time: 创建时间
        :type create_time: str
        :param expire_time: 超期时间
        :type expire_time: str
        """
        
        

        self._id = None
        self._name = None
        self._duration = None
        self._trust_domain_name = None
        self._trust_domain_id = None
        self._create_time = None
        self._expire_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if duration is not None:
            self.duration = duration
        if trust_domain_name is not None:
            self.trust_domain_name = trust_domain_name
        if trust_domain_id is not None:
            self.trust_domain_id = trust_domain_id
        if create_time is not None:
            self.create_time = create_time
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def id(self):
        r"""Gets the id of this AgencyV2.

        委托id

        :return: The id of this AgencyV2.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AgencyV2.

        委托id

        :param id: The id of this AgencyV2.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AgencyV2.

        委托名称

        :return: The name of this AgencyV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AgencyV2.

        委托名称

        :param name: The name of this AgencyV2.
        :type name: str
        """
        self._name = name

    @property
    def duration(self):
        r"""Gets the duration of this AgencyV2.

        委托的期限

        :return: The duration of this AgencyV2.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this AgencyV2.

        委托的期限

        :param duration: The duration of this AgencyV2.
        :type duration: str
        """
        self._duration = duration

    @property
    def trust_domain_name(self):
        r"""Gets the trust_domain_name of this AgencyV2.

        委托的账号名称

        :return: The trust_domain_name of this AgencyV2.
        :rtype: str
        """
        return self._trust_domain_name

    @trust_domain_name.setter
    def trust_domain_name(self, trust_domain_name):
        r"""Sets the trust_domain_name of this AgencyV2.

        委托的账号名称

        :param trust_domain_name: The trust_domain_name of this AgencyV2.
        :type trust_domain_name: str
        """
        self._trust_domain_name = trust_domain_name

    @property
    def trust_domain_id(self):
        r"""Gets the trust_domain_id of this AgencyV2.

        委托的账号id

        :return: The trust_domain_id of this AgencyV2.
        :rtype: str
        """
        return self._trust_domain_id

    @trust_domain_id.setter
    def trust_domain_id(self, trust_domain_id):
        r"""Sets the trust_domain_id of this AgencyV2.

        委托的账号id

        :param trust_domain_id: The trust_domain_id of this AgencyV2.
        :type trust_domain_id: str
        """
        self._trust_domain_id = trust_domain_id

    @property
    def create_time(self):
        r"""Gets the create_time of this AgencyV2.

        创建时间

        :return: The create_time of this AgencyV2.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AgencyV2.

        创建时间

        :param create_time: The create_time of this AgencyV2.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this AgencyV2.

        超期时间

        :return: The expire_time of this AgencyV2.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this AgencyV2.

        超期时间

        :param expire_time: The expire_time of this AgencyV2.
        :type expire_time: str
        """
        self._expire_time = expire_time

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
        if not isinstance(other, AgencyV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
