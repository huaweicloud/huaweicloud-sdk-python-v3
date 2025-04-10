# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDomainRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protect_status': 'str',
        'description': 'str'
    }

    attribute_map = {
        'protect_status': 'protect_status',
        'description': 'description'
    }

    def __init__(self, protect_status=None, description=None):
        r"""UpdateDomainRequestBody

        The model defined in huaweicloud sdk

        :param protect_status: 防护状态:防护中-on;未防护-off
        :type protect_status: str
        :param description: 域名描述
        :type description: str
        """
        
        

        self._protect_status = None
        self._description = None
        self.discriminator = None

        if protect_status is not None:
            self.protect_status = protect_status
        if description is not None:
            self.description = description

    @property
    def protect_status(self):
        r"""Gets the protect_status of this UpdateDomainRequestBody.

        防护状态:防护中-on;未防护-off

        :return: The protect_status of this UpdateDomainRequestBody.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this UpdateDomainRequestBody.

        防护状态:防护中-on;未防护-off

        :param protect_status: The protect_status of this UpdateDomainRequestBody.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def description(self):
        r"""Gets the description of this UpdateDomainRequestBody.

        域名描述

        :return: The description of this UpdateDomainRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateDomainRequestBody.

        域名描述

        :param description: The description of this UpdateDomainRequestBody.
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
        if not isinstance(other, UpdateDomainRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
