# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteQueuesRequest:

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
        'vhost': 'str',
        'body': 'BatchDeleteBody'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'vhost': 'vhost',
        'body': 'body'
    }

    def __init__(self, instance_id=None, vhost=None, body=None):
        r"""BatchDeleteQueuesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param vhost: Vhost名称
        :type vhost: str
        :param body: Body of the BatchDeleteQueuesRequest
        :type body: :class:`huaweicloudsdkrabbitmq.v2.BatchDeleteBody`
        """
        
        

        self._instance_id = None
        self._vhost = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.vhost = vhost
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BatchDeleteQueuesRequest.

        实例ID

        :return: The instance_id of this BatchDeleteQueuesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BatchDeleteQueuesRequest.

        实例ID

        :param instance_id: The instance_id of this BatchDeleteQueuesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def vhost(self):
        r"""Gets the vhost of this BatchDeleteQueuesRequest.

        Vhost名称

        :return: The vhost of this BatchDeleteQueuesRequest.
        :rtype: str
        """
        return self._vhost

    @vhost.setter
    def vhost(self, vhost):
        r"""Sets the vhost of this BatchDeleteQueuesRequest.

        Vhost名称

        :param vhost: The vhost of this BatchDeleteQueuesRequest.
        :type vhost: str
        """
        self._vhost = vhost

    @property
    def body(self):
        r"""Gets the body of this BatchDeleteQueuesRequest.

        :return: The body of this BatchDeleteQueuesRequest.
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.BatchDeleteBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchDeleteQueuesRequest.

        :param body: The body of this BatchDeleteQueuesRequest.
        :type body: :class:`huaweicloudsdkrabbitmq.v2.BatchDeleteBody`
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
        if not isinstance(other, BatchDeleteQueuesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
