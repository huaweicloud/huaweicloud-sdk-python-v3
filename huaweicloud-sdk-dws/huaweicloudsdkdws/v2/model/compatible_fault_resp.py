# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompatibleFaultResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message': 'str',
        'created': 'str',
        'details': 'str'
    }

    attribute_map = {
        'message': 'message',
        'created': 'created',
        'details': 'details'
    }

    def __init__(self, message=None, created=None, details=None):
        """CompatibleFaultResp

        The model defined in huaweicloud sdk

        :param message: 信息
        :type message: str
        :param created: 创建者
        :type created: str
        :param details: 详细
        :type details: str
        """
        
        

        self._message = None
        self._created = None
        self._details = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if created is not None:
            self.created = created
        if details is not None:
            self.details = details

    @property
    def message(self):
        """Gets the message of this CompatibleFaultResp.

        信息

        :return: The message of this CompatibleFaultResp.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CompatibleFaultResp.

        信息

        :param message: The message of this CompatibleFaultResp.
        :type message: str
        """
        self._message = message

    @property
    def created(self):
        """Gets the created of this CompatibleFaultResp.

        创建者

        :return: The created of this CompatibleFaultResp.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CompatibleFaultResp.

        创建者

        :param created: The created of this CompatibleFaultResp.
        :type created: str
        """
        self._created = created

    @property
    def details(self):
        """Gets the details of this CompatibleFaultResp.

        详细

        :return: The details of this CompatibleFaultResp.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this CompatibleFaultResp.

        详细

        :param details: The details of this CompatibleFaultResp.
        :type details: str
        """
        self._details = details

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
        if not isinstance(other, CompatibleFaultResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
