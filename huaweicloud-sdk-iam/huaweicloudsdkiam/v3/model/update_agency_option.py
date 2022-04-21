# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAgencyOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'trust_domain_id': 'str',
        'trust_domain_name': 'str',
        'description': 'str',
        'duration': 'str'
    }

    attribute_map = {
        'trust_domain_id': 'trust_domain_id',
        'trust_domain_name': 'trust_domain_name',
        'description': 'description',
        'duration': 'duration'
    }

    def __init__(self, trust_domain_id=None, trust_domain_name=None, description=None, duration=None):
        """UpdateAgencyOption

        The model defined in huaweicloud sdk

        :param trust_domain_id: 被委托方账号ID。如果trust_domain_id和trust_domain_name都填写，则优先校验trust_domain_name。四个参数至少填写一个。
        :type trust_domain_id: str
        :param trust_domain_name: 被委托方账号名。如果trust_domain_id和trust_domain_name都填写，则优先校验trust_domain_name。四个参数至少填写一个。
        :type trust_domain_name: str
        :param description: 委托描述信息，长度不大于255位。四个参数至少填写一个。
        :type description: str
        :param duration: 委托的期限。取值为“FOREVER\&quot;表示委托的期限为永久，取值为\&quot;ONEDAY\&quot;表示委托的期限为一天。四个参数至少填写一个。
        :type duration: str
        """
        
        

        self._trust_domain_id = None
        self._trust_domain_name = None
        self._description = None
        self._duration = None
        self.discriminator = None

        if trust_domain_id is not None:
            self.trust_domain_id = trust_domain_id
        if trust_domain_name is not None:
            self.trust_domain_name = trust_domain_name
        if description is not None:
            self.description = description
        if duration is not None:
            self.duration = duration

    @property
    def trust_domain_id(self):
        """Gets the trust_domain_id of this UpdateAgencyOption.

        被委托方账号ID。如果trust_domain_id和trust_domain_name都填写，则优先校验trust_domain_name。四个参数至少填写一个。

        :return: The trust_domain_id of this UpdateAgencyOption.
        :rtype: str
        """
        return self._trust_domain_id

    @trust_domain_id.setter
    def trust_domain_id(self, trust_domain_id):
        """Sets the trust_domain_id of this UpdateAgencyOption.

        被委托方账号ID。如果trust_domain_id和trust_domain_name都填写，则优先校验trust_domain_name。四个参数至少填写一个。

        :param trust_domain_id: The trust_domain_id of this UpdateAgencyOption.
        :type trust_domain_id: str
        """
        self._trust_domain_id = trust_domain_id

    @property
    def trust_domain_name(self):
        """Gets the trust_domain_name of this UpdateAgencyOption.

        被委托方账号名。如果trust_domain_id和trust_domain_name都填写，则优先校验trust_domain_name。四个参数至少填写一个。

        :return: The trust_domain_name of this UpdateAgencyOption.
        :rtype: str
        """
        return self._trust_domain_name

    @trust_domain_name.setter
    def trust_domain_name(self, trust_domain_name):
        """Sets the trust_domain_name of this UpdateAgencyOption.

        被委托方账号名。如果trust_domain_id和trust_domain_name都填写，则优先校验trust_domain_name。四个参数至少填写一个。

        :param trust_domain_name: The trust_domain_name of this UpdateAgencyOption.
        :type trust_domain_name: str
        """
        self._trust_domain_name = trust_domain_name

    @property
    def description(self):
        """Gets the description of this UpdateAgencyOption.

        委托描述信息，长度不大于255位。四个参数至少填写一个。

        :return: The description of this UpdateAgencyOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateAgencyOption.

        委托描述信息，长度不大于255位。四个参数至少填写一个。

        :param description: The description of this UpdateAgencyOption.
        :type description: str
        """
        self._description = description

    @property
    def duration(self):
        """Gets the duration of this UpdateAgencyOption.

        委托的期限。取值为“FOREVER\"表示委托的期限为永久，取值为\"ONEDAY\"表示委托的期限为一天。四个参数至少填写一个。

        :return: The duration of this UpdateAgencyOption.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this UpdateAgencyOption.

        委托的期限。取值为“FOREVER\"表示委托的期限为永久，取值为\"ONEDAY\"表示委托的期限为一天。四个参数至少填写一个。

        :param duration: The duration of this UpdateAgencyOption.
        :type duration: str
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
        if not isinstance(other, UpdateAgencyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
