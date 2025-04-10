# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApigwTargetDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'invocation_http_parameters': 'InvocationHttpParameters'
    }

    attribute_map = {
        'url': 'url',
        'invocation_http_parameters': 'invocation_http_parameters'
    }

    def __init__(self, url=None, invocation_http_parameters=None):
        r"""ApigwTargetDetail

        The model defined in huaweicloud sdk

        :param url: 目标url
        :type url: str
        :param invocation_http_parameters: 
        :type invocation_http_parameters: :class:`huaweicloudsdkeg.v1.InvocationHttpParameters`
        """
        
        

        self._url = None
        self._invocation_http_parameters = None
        self.discriminator = None

        self.url = url
        if invocation_http_parameters is not None:
            self.invocation_http_parameters = invocation_http_parameters

    @property
    def url(self):
        r"""Gets the url of this ApigwTargetDetail.

        目标url

        :return: The url of this ApigwTargetDetail.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ApigwTargetDetail.

        目标url

        :param url: The url of this ApigwTargetDetail.
        :type url: str
        """
        self._url = url

    @property
    def invocation_http_parameters(self):
        r"""Gets the invocation_http_parameters of this ApigwTargetDetail.

        :return: The invocation_http_parameters of this ApigwTargetDetail.
        :rtype: :class:`huaweicloudsdkeg.v1.InvocationHttpParameters`
        """
        return self._invocation_http_parameters

    @invocation_http_parameters.setter
    def invocation_http_parameters(self, invocation_http_parameters):
        r"""Sets the invocation_http_parameters of this ApigwTargetDetail.

        :param invocation_http_parameters: The invocation_http_parameters of this ApigwTargetDetail.
        :type invocation_http_parameters: :class:`huaweicloudsdkeg.v1.InvocationHttpParameters`
        """
        self._invocation_http_parameters = invocation_http_parameters

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
        if not isinstance(other, ApigwTargetDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
