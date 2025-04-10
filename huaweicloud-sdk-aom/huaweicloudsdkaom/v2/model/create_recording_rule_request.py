# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRecordingRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'prometheus_instance': 'str',
        'body': 'RecordingRuleRequest'
    }

    attribute_map = {
        'prometheus_instance': 'prometheus_instance',
        'body': 'body'
    }

    def __init__(self, prometheus_instance=None, body=None):
        r"""CreateRecordingRuleRequest

        The model defined in huaweicloud sdk

        :param prometheus_instance: prometheus实例id。
        :type prometheus_instance: str
        :param body: Body of the CreateRecordingRuleRequest
        :type body: :class:`huaweicloudsdkaom.v2.RecordingRuleRequest`
        """
        
        

        self._prometheus_instance = None
        self._body = None
        self.discriminator = None

        self.prometheus_instance = prometheus_instance
        if body is not None:
            self.body = body

    @property
    def prometheus_instance(self):
        r"""Gets the prometheus_instance of this CreateRecordingRuleRequest.

        prometheus实例id。

        :return: The prometheus_instance of this CreateRecordingRuleRequest.
        :rtype: str
        """
        return self._prometheus_instance

    @prometheus_instance.setter
    def prometheus_instance(self, prometheus_instance):
        r"""Sets the prometheus_instance of this CreateRecordingRuleRequest.

        prometheus实例id。

        :param prometheus_instance: The prometheus_instance of this CreateRecordingRuleRequest.
        :type prometheus_instance: str
        """
        self._prometheus_instance = prometheus_instance

    @property
    def body(self):
        r"""Gets the body of this CreateRecordingRuleRequest.

        :return: The body of this CreateRecordingRuleRequest.
        :rtype: :class:`huaweicloudsdkaom.v2.RecordingRuleRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateRecordingRuleRequest.

        :param body: The body of this CreateRecordingRuleRequest.
        :type body: :class:`huaweicloudsdkaom.v2.RecordingRuleRequest`
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
        if not isinstance(other, CreateRecordingRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
