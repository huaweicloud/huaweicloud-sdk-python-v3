# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateServiceLinkedAgencyReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_principal': 'str',
        'description': 'str'
    }

    attribute_map = {
        'service_principal': 'service_principal',
        'description': 'description'
    }

    def __init__(self, service_principal=None, description=None):
        r"""CreateServiceLinkedAgencyReqBody

        The model defined in huaweicloud sdk

        :param service_principal: 服务主体，由\&quot;service.\&quot;开头，后跟一个长度为1到56个字符，只包含字母、数字和\&quot;-\&quot;的字符串。
        :type service_principal: str
        :param description: 服务关联委托描述信息，不能包含特定字符\&quot;@\&quot;、\&quot;#\&quot;、\&quot;%\&quot;、\&quot;&amp;\&quot;、\&quot;&lt;\&quot;、\&quot;&gt;\&quot;、\&quot;\\\\\&quot;、\&quot;$\&quot;、\&quot;^\&quot;和\&quot;*\&quot;的字符串。
        :type description: str
        """
        
        

        self._service_principal = None
        self._description = None
        self.discriminator = None

        self.service_principal = service_principal
        if description is not None:
            self.description = description

    @property
    def service_principal(self):
        r"""Gets the service_principal of this CreateServiceLinkedAgencyReqBody.

        服务主体，由\"service.\"开头，后跟一个长度为1到56个字符，只包含字母、数字和\"-\"的字符串。

        :return: The service_principal of this CreateServiceLinkedAgencyReqBody.
        :rtype: str
        """
        return self._service_principal

    @service_principal.setter
    def service_principal(self, service_principal):
        r"""Sets the service_principal of this CreateServiceLinkedAgencyReqBody.

        服务主体，由\"service.\"开头，后跟一个长度为1到56个字符，只包含字母、数字和\"-\"的字符串。

        :param service_principal: The service_principal of this CreateServiceLinkedAgencyReqBody.
        :type service_principal: str
        """
        self._service_principal = service_principal

    @property
    def description(self):
        r"""Gets the description of this CreateServiceLinkedAgencyReqBody.

        服务关联委托描述信息，不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\\\"、\"$\"、\"^\"和\"*\"的字符串。

        :return: The description of this CreateServiceLinkedAgencyReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateServiceLinkedAgencyReqBody.

        服务关联委托描述信息，不能包含特定字符\"@\"、\"#\"、\"%\"、\"&\"、\"<\"、\">\"、\"\\\\\"、\"$\"、\"^\"和\"*\"的字符串。

        :param description: The description of this CreateServiceLinkedAgencyReqBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateServiceLinkedAgencyReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
