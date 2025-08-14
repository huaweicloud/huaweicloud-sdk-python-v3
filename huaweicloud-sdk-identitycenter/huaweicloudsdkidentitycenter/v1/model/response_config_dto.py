# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponseConfigDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'properties': 'dict(str, ResponseSourceDetailsDto)',
        'subject': 'ResponseSourceDetailsDto',
        'relay_state': 'str',
        'ttl': 'str'
    }

    attribute_map = {
        'properties': 'properties',
        'subject': 'subject',
        'relay_state': 'relay_state',
        'ttl': 'ttl'
    }

    def __init__(self, properties=None, subject=None, relay_state=None, ttl=None):
        r"""ResponseConfigDto

        The model defined in huaweicloud sdk

        :param properties: 额外添加的属性映射配置
        :type properties: dict(str, ResponseSourceDetailsDto)
        :param subject: 
        :type subject: :class:`huaweicloudsdkidentitycenter.v1.ResponseSourceDetailsDto`
        :param relay_state: 中继状态
        :type relay_state: str
        :param ttl: 会话过期时间
        :type ttl: str
        """
        
        

        self._properties = None
        self._subject = None
        self._relay_state = None
        self._ttl = None
        self.discriminator = None

        if properties is not None:
            self.properties = properties
        if subject is not None:
            self.subject = subject
        if relay_state is not None:
            self.relay_state = relay_state
        self.ttl = ttl

    @property
    def properties(self):
        r"""Gets the properties of this ResponseConfigDto.

        额外添加的属性映射配置

        :return: The properties of this ResponseConfigDto.
        :rtype: dict(str, ResponseSourceDetailsDto)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this ResponseConfigDto.

        额外添加的属性映射配置

        :param properties: The properties of this ResponseConfigDto.
        :type properties: dict(str, ResponseSourceDetailsDto)
        """
        self._properties = properties

    @property
    def subject(self):
        r"""Gets the subject of this ResponseConfigDto.

        :return: The subject of this ResponseConfigDto.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.ResponseSourceDetailsDto`
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this ResponseConfigDto.

        :param subject: The subject of this ResponseConfigDto.
        :type subject: :class:`huaweicloudsdkidentitycenter.v1.ResponseSourceDetailsDto`
        """
        self._subject = subject

    @property
    def relay_state(self):
        r"""Gets the relay_state of this ResponseConfigDto.

        中继状态

        :return: The relay_state of this ResponseConfigDto.
        :rtype: str
        """
        return self._relay_state

    @relay_state.setter
    def relay_state(self, relay_state):
        r"""Sets the relay_state of this ResponseConfigDto.

        中继状态

        :param relay_state: The relay_state of this ResponseConfigDto.
        :type relay_state: str
        """
        self._relay_state = relay_state

    @property
    def ttl(self):
        r"""Gets the ttl of this ResponseConfigDto.

        会话过期时间

        :return: The ttl of this ResponseConfigDto.
        :rtype: str
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this ResponseConfigDto.

        会话过期时间

        :param ttl: The ttl of this ResponseConfigDto.
        :type ttl: str
        """
        self._ttl = ttl

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
        if not isinstance(other, ResponseConfigDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
