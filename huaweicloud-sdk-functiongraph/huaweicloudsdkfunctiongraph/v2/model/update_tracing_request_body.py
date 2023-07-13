# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTracingRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tracing_ak': 'str',
        'tracing_sk': 'str'
    }

    attribute_map = {
        'tracing_ak': 'tracing_ak',
        'tracing_sk': 'tracing_sk'
    }

    def __init__(self, tracing_ak=None, tracing_sk=None):
        """UpdateTracingRequestBody

        The model defined in huaweicloud sdk

        :param tracing_ak: apm的ak
        :type tracing_ak: str
        :param tracing_sk: apm的sk
        :type tracing_sk: str
        """
        
        

        self._tracing_ak = None
        self._tracing_sk = None
        self.discriminator = None

        if tracing_ak is not None:
            self.tracing_ak = tracing_ak
        if tracing_sk is not None:
            self.tracing_sk = tracing_sk

    @property
    def tracing_ak(self):
        """Gets the tracing_ak of this UpdateTracingRequestBody.

        apm的ak

        :return: The tracing_ak of this UpdateTracingRequestBody.
        :rtype: str
        """
        return self._tracing_ak

    @tracing_ak.setter
    def tracing_ak(self, tracing_ak):
        """Sets the tracing_ak of this UpdateTracingRequestBody.

        apm的ak

        :param tracing_ak: The tracing_ak of this UpdateTracingRequestBody.
        :type tracing_ak: str
        """
        self._tracing_ak = tracing_ak

    @property
    def tracing_sk(self):
        """Gets the tracing_sk of this UpdateTracingRequestBody.

        apm的sk

        :return: The tracing_sk of this UpdateTracingRequestBody.
        :rtype: str
        """
        return self._tracing_sk

    @tracing_sk.setter
    def tracing_sk(self, tracing_sk):
        """Sets the tracing_sk of this UpdateTracingRequestBody.

        apm的sk

        :param tracing_sk: The tracing_sk of this UpdateTracingRequestBody.
        :type tracing_sk: str
        """
        self._tracing_sk = tracing_sk

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
        if not isinstance(other, UpdateTracingRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
