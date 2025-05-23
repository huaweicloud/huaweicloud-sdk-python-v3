# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHealthCheckRequest:

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
        'vpc_channel_id': 'str',
        'body': 'VpcHealthConfig'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'vpc_channel_id': 'vpc_channel_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, vpc_channel_id=None, body=None):
        r"""UpdateHealthCheckRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param vpc_channel_id: VPC通道的编号
        :type vpc_channel_id: str
        :param body: Body of the UpdateHealthCheckRequest
        :type body: :class:`huaweicloudsdkroma.v2.VpcHealthConfig`
        """
        
        

        self._instance_id = None
        self._vpc_channel_id = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.vpc_channel_id = vpc_channel_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateHealthCheckRequest.

        实例ID

        :return: The instance_id of this UpdateHealthCheckRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateHealthCheckRequest.

        实例ID

        :param instance_id: The instance_id of this UpdateHealthCheckRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def vpc_channel_id(self):
        r"""Gets the vpc_channel_id of this UpdateHealthCheckRequest.

        VPC通道的编号

        :return: The vpc_channel_id of this UpdateHealthCheckRequest.
        :rtype: str
        """
        return self._vpc_channel_id

    @vpc_channel_id.setter
    def vpc_channel_id(self, vpc_channel_id):
        r"""Sets the vpc_channel_id of this UpdateHealthCheckRequest.

        VPC通道的编号

        :param vpc_channel_id: The vpc_channel_id of this UpdateHealthCheckRequest.
        :type vpc_channel_id: str
        """
        self._vpc_channel_id = vpc_channel_id

    @property
    def body(self):
        r"""Gets the body of this UpdateHealthCheckRequest.

        :return: The body of this UpdateHealthCheckRequest.
        :rtype: :class:`huaweicloudsdkroma.v2.VpcHealthConfig`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateHealthCheckRequest.

        :param body: The body of this UpdateHealthCheckRequest.
        :type body: :class:`huaweicloudsdkroma.v2.VpcHealthConfig`
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
        if not isinstance(other, UpdateHealthCheckRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
