# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VoiceTrainingAllocatedResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'charge_mode': 'ChardMode',
        'expire_time': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'charge_mode': 'charge_mode',
        'expire_time': 'expire_time'
    }

    def __init__(self, resource_id=None, charge_mode=None, expire_time=None):
        r"""VoiceTrainingAllocatedResource

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID。
        :type resource_id: str
        :param charge_mode: 
        :type charge_mode: :class:`huaweicloudsdkmetastudio.v1.ChardMode`
        :param expire_time: 资源过期时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;
        :type expire_time: str
        """
        
        

        self._resource_id = None
        self._charge_mode = None
        self._expire_time = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def resource_id(self):
        r"""Gets the resource_id of this VoiceTrainingAllocatedResource.

        资源ID。

        :return: The resource_id of this VoiceTrainingAllocatedResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this VoiceTrainingAllocatedResource.

        资源ID。

        :param resource_id: The resource_id of this VoiceTrainingAllocatedResource.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this VoiceTrainingAllocatedResource.

        :return: The charge_mode of this VoiceTrainingAllocatedResource.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ChardMode`
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this VoiceTrainingAllocatedResource.

        :param charge_mode: The charge_mode of this VoiceTrainingAllocatedResource.
        :type charge_mode: :class:`huaweicloudsdkmetastudio.v1.ChardMode`
        """
        self._charge_mode = charge_mode

    @property
    def expire_time(self):
        r"""Gets the expire_time of this VoiceTrainingAllocatedResource.

        资源过期时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :return: The expire_time of this VoiceTrainingAllocatedResource.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this VoiceTrainingAllocatedResource.

        资源过期时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :param expire_time: The expire_time of this VoiceTrainingAllocatedResource.
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
        if not isinstance(other, VoiceTrainingAllocatedResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
