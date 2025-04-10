# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateApplicationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_urn': 'str',
        'body': 'UpdateApplicationRequestBody'
    }

    attribute_map = {
        'application_urn': 'application_urn',
        'body': 'body'
    }

    def __init__(self, application_urn=None, body=None):
        r"""UpdateApplicationRequest

        The model defined in huaweicloud sdk

        :param application_urn: Application的唯一资源标识，可通过[查询Application](smn_api_57004.xml)获取该标识。
        :type application_urn: str
        :param body: Body of the UpdateApplicationRequest
        :type body: :class:`huaweicloudsdksmn.v2.UpdateApplicationRequestBody`
        """
        
        

        self._application_urn = None
        self._body = None
        self.discriminator = None

        self.application_urn = application_urn
        if body is not None:
            self.body = body

    @property
    def application_urn(self):
        r"""Gets the application_urn of this UpdateApplicationRequest.

        Application的唯一资源标识，可通过[查询Application](smn_api_57004.xml)获取该标识。

        :return: The application_urn of this UpdateApplicationRequest.
        :rtype: str
        """
        return self._application_urn

    @application_urn.setter
    def application_urn(self, application_urn):
        r"""Sets the application_urn of this UpdateApplicationRequest.

        Application的唯一资源标识，可通过[查询Application](smn_api_57004.xml)获取该标识。

        :param application_urn: The application_urn of this UpdateApplicationRequest.
        :type application_urn: str
        """
        self._application_urn = application_urn

    @property
    def body(self):
        r"""Gets the body of this UpdateApplicationRequest.

        :return: The body of this UpdateApplicationRequest.
        :rtype: :class:`huaweicloudsdksmn.v2.UpdateApplicationRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateApplicationRequest.

        :param body: The body of this UpdateApplicationRequest.
        :type body: :class:`huaweicloudsdksmn.v2.UpdateApplicationRequestBody`
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
        if not isinstance(other, UpdateApplicationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
