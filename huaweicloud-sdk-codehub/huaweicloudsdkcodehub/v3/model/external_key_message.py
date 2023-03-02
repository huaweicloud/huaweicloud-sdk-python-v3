# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalKeyMessage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'external_key_message': 'str',
        'external_service': 'str'
    }

    attribute_map = {
        'external_key_message': 'external_key_message',
        'external_service': 'external_service'
    }

    def __init__(self, external_key_message=None, external_service=None):
        """ExternalKeyMessage

        The model defined in huaweicloud sdk

        :param external_key_message: 第三方保存在代码托管的关键信息
        :type external_key_message: str
        :param external_service: 外部服务名称
        :type external_service: str
        """
        
        

        self._external_key_message = None
        self._external_service = None
        self.discriminator = None

        if external_key_message is not None:
            self.external_key_message = external_key_message
        if external_service is not None:
            self.external_service = external_service

    @property
    def external_key_message(self):
        """Gets the external_key_message of this ExternalKeyMessage.

        第三方保存在代码托管的关键信息

        :return: The external_key_message of this ExternalKeyMessage.
        :rtype: str
        """
        return self._external_key_message

    @external_key_message.setter
    def external_key_message(self, external_key_message):
        """Sets the external_key_message of this ExternalKeyMessage.

        第三方保存在代码托管的关键信息

        :param external_key_message: The external_key_message of this ExternalKeyMessage.
        :type external_key_message: str
        """
        self._external_key_message = external_key_message

    @property
    def external_service(self):
        """Gets the external_service of this ExternalKeyMessage.

        外部服务名称

        :return: The external_service of this ExternalKeyMessage.
        :rtype: str
        """
        return self._external_service

    @external_service.setter
    def external_service(self, external_service):
        """Sets the external_service of this ExternalKeyMessage.

        外部服务名称

        :param external_service: The external_service of this ExternalKeyMessage.
        :type external_service: str
        """
        self._external_service = external_service

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
        if not isinstance(other, ExternalKeyMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
