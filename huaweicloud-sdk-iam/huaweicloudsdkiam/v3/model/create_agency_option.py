# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAgencyOption:

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
        'domain_id': 'str',
        'trust_domain_id': 'str',
        'trust_domain_name': 'str',
        'description': 'str',
        'duration': 'object'
    }

    attribute_map = {
        'name': 'name',
        'domain_id': 'domain_id',
        'trust_domain_id': 'trust_domain_id',
        'trust_domain_name': 'trust_domain_name',
        'description': 'description',
        'duration': 'duration'
    }

    def __init__(self, name=None, domain_id=None, trust_domain_id=None, trust_domain_name=None, description=None, duration=None):
        r"""CreateAgencyOption

        The model defined in huaweicloud sdk

        :param name: 委托名，长度不大于64位。
        :type name: str
        :param domain_id: 委托方账号ID。
        :type domain_id: str
        :param trust_domain_id: 被委托方账号ID。trust_domain_id和trust_domain_name至少填写一个，若都填写优先校验trust_domain_name。
        :type trust_domain_id: str
        :param trust_domain_name: 被委托方账号名。trust_domain_id和trust_domain_name至少填写一个，若都填写优先校验trust_domain_name。
        :type trust_domain_name: str
        :param description: 委托描述信息，长度不大于255位。
        :type description: str
        :param duration: description: 委托的期限，单位为“天”。默认为FOREVER。取值为“FOREVER\&quot;表示委托的期限为永久，取值为\&quot;ONEDAY\&quot;表示委托的期限为一天,取值为自定义天数表示委托的期限为有限天数，如20。四个参数至少填写一个。
        :type duration: object
        """
        
        

        self._name = None
        self._domain_id = None
        self._trust_domain_id = None
        self._trust_domain_name = None
        self._description = None
        self._duration = None
        self.discriminator = None

        self.name = name
        self.domain_id = domain_id
        if trust_domain_id is not None:
            self.trust_domain_id = trust_domain_id
        if trust_domain_name is not None:
            self.trust_domain_name = trust_domain_name
        if description is not None:
            self.description = description
        if duration is not None:
            self.duration = duration

    @property
    def name(self):
        r"""Gets the name of this CreateAgencyOption.

        委托名，长度不大于64位。

        :return: The name of this CreateAgencyOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateAgencyOption.

        委托名，长度不大于64位。

        :param name: The name of this CreateAgencyOption.
        :type name: str
        """
        self._name = name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CreateAgencyOption.

        委托方账号ID。

        :return: The domain_id of this CreateAgencyOption.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CreateAgencyOption.

        委托方账号ID。

        :param domain_id: The domain_id of this CreateAgencyOption.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def trust_domain_id(self):
        r"""Gets the trust_domain_id of this CreateAgencyOption.

        被委托方账号ID。trust_domain_id和trust_domain_name至少填写一个，若都填写优先校验trust_domain_name。

        :return: The trust_domain_id of this CreateAgencyOption.
        :rtype: str
        """
        return self._trust_domain_id

    @trust_domain_id.setter
    def trust_domain_id(self, trust_domain_id):
        r"""Sets the trust_domain_id of this CreateAgencyOption.

        被委托方账号ID。trust_domain_id和trust_domain_name至少填写一个，若都填写优先校验trust_domain_name。

        :param trust_domain_id: The trust_domain_id of this CreateAgencyOption.
        :type trust_domain_id: str
        """
        self._trust_domain_id = trust_domain_id

    @property
    def trust_domain_name(self):
        r"""Gets the trust_domain_name of this CreateAgencyOption.

        被委托方账号名。trust_domain_id和trust_domain_name至少填写一个，若都填写优先校验trust_domain_name。

        :return: The trust_domain_name of this CreateAgencyOption.
        :rtype: str
        """
        return self._trust_domain_name

    @trust_domain_name.setter
    def trust_domain_name(self, trust_domain_name):
        r"""Sets the trust_domain_name of this CreateAgencyOption.

        被委托方账号名。trust_domain_id和trust_domain_name至少填写一个，若都填写优先校验trust_domain_name。

        :param trust_domain_name: The trust_domain_name of this CreateAgencyOption.
        :type trust_domain_name: str
        """
        self._trust_domain_name = trust_domain_name

    @property
    def description(self):
        r"""Gets the description of this CreateAgencyOption.

        委托描述信息，长度不大于255位。

        :return: The description of this CreateAgencyOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAgencyOption.

        委托描述信息，长度不大于255位。

        :param description: The description of this CreateAgencyOption.
        :type description: str
        """
        self._description = description

    @property
    def duration(self):
        r"""Gets the duration of this CreateAgencyOption.

        description: 委托的期限，单位为“天”。默认为FOREVER。取值为“FOREVER\"表示委托的期限为永久，取值为\"ONEDAY\"表示委托的期限为一天,取值为自定义天数表示委托的期限为有限天数，如20。四个参数至少填写一个。

        :return: The duration of this CreateAgencyOption.
        :rtype: object
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this CreateAgencyOption.

        description: 委托的期限，单位为“天”。默认为FOREVER。取值为“FOREVER\"表示委托的期限为永久，取值为\"ONEDAY\"表示委托的期限为一天,取值为自定义天数表示委托的期限为有限天数，如20。四个参数至少填写一个。

        :param duration: The duration of this CreateAgencyOption.
        :type duration: object
        """
        self._duration = duration

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
        if not isinstance(other, CreateAgencyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
