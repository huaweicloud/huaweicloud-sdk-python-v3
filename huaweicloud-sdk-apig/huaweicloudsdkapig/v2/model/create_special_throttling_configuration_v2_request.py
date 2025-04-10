# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSpecialThrottlingConfigurationV2Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'throttle_id': 'str',
        'body': 'ThrottleSpecialCreate'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'throttle_id': 'throttle_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, throttle_id=None, body=None):
        r"""CreateSpecialThrottlingConfigurationV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param throttle_id: 流控策略的编号
        :type throttle_id: str
        :param body: Body of the CreateSpecialThrottlingConfigurationV2Request
        :type body: :class:`huaweicloudsdkapig.v2.ThrottleSpecialCreate`
        """
        
        

        self._instance_id = None
        self._throttle_id = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.throttle_id = throttle_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this CreateSpecialThrottlingConfigurationV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this CreateSpecialThrottlingConfigurationV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this CreateSpecialThrottlingConfigurationV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this CreateSpecialThrottlingConfigurationV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def throttle_id(self):
        r"""Gets the throttle_id of this CreateSpecialThrottlingConfigurationV2Request.

        流控策略的编号

        :return: The throttle_id of this CreateSpecialThrottlingConfigurationV2Request.
        :rtype: str
        """
        return self._throttle_id

    @throttle_id.setter
    def throttle_id(self, throttle_id):
        r"""Sets the throttle_id of this CreateSpecialThrottlingConfigurationV2Request.

        流控策略的编号

        :param throttle_id: The throttle_id of this CreateSpecialThrottlingConfigurationV2Request.
        :type throttle_id: str
        """
        self._throttle_id = throttle_id

    @property
    def body(self):
        r"""Gets the body of this CreateSpecialThrottlingConfigurationV2Request.

        :return: The body of this CreateSpecialThrottlingConfigurationV2Request.
        :rtype: :class:`huaweicloudsdkapig.v2.ThrottleSpecialCreate`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateSpecialThrottlingConfigurationV2Request.

        :param body: The body of this CreateSpecialThrottlingConfigurationV2Request.
        :type body: :class:`huaweicloudsdkapig.v2.ThrottleSpecialCreate`
        """
        self._body = body

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
        if not isinstance(other, CreateSpecialThrottlingConfigurationV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
