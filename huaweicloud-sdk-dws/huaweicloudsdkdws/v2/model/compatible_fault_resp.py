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
        r"""CompatibleFaultResp

        The model defined in huaweicloud sdk

        :param message: **参数解释**： 信息。 **取值范围**： 不涉及。
        :type message: str
        :param created: **参数解释**： 创建者。 **取值范围**： 不涉及。
        :type created: str
        :param details: **参数解释**： 详细内容。 **取值范围**： 不涉及。
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
        r"""Gets the message of this CompatibleFaultResp.

        **参数解释**： 信息。 **取值范围**： 不涉及。

        :return: The message of this CompatibleFaultResp.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CompatibleFaultResp.

        **参数解释**： 信息。 **取值范围**： 不涉及。

        :param message: The message of this CompatibleFaultResp.
        :type message: str
        """
        self._message = message

    @property
    def created(self):
        r"""Gets the created of this CompatibleFaultResp.

        **参数解释**： 创建者。 **取值范围**： 不涉及。

        :return: The created of this CompatibleFaultResp.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this CompatibleFaultResp.

        **参数解释**： 创建者。 **取值范围**： 不涉及。

        :param created: The created of this CompatibleFaultResp.
        :type created: str
        """
        self._created = created

    @property
    def details(self):
        r"""Gets the details of this CompatibleFaultResp.

        **参数解释**： 详细内容。 **取值范围**： 不涉及。

        :return: The details of this CompatibleFaultResp.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        r"""Sets the details of this CompatibleFaultResp.

        **参数解释**： 详细内容。 **取值范围**： 不涉及。

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
