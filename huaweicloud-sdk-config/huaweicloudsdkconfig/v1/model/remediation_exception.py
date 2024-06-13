# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemediationException:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'message': 'str',
        'joined_at': 'str',
        'created_by': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'message': 'message',
        'joined_at': 'joined_at',
        'created_by': 'created_by'
    }

    def __init__(self, resource_id=None, message=None, joined_at=None, created_by=None):
        """RemediationException

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID。
        :type resource_id: str
        :param message: 加入合规规则修正例外的原因。
        :type message: str
        :param joined_at: 加入合规规则修正例外的时间。
        :type joined_at: str
        :param created_by: 合规规则修正例外的创建者。
        :type created_by: str
        """
        
        

        self._resource_id = None
        self._message = None
        self._joined_at = None
        self._created_by = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if message is not None:
            self.message = message
        if joined_at is not None:
            self.joined_at = joined_at
        if created_by is not None:
            self.created_by = created_by

    @property
    def resource_id(self):
        """Gets the resource_id of this RemediationException.

        资源ID。

        :return: The resource_id of this RemediationException.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this RemediationException.

        资源ID。

        :param resource_id: The resource_id of this RemediationException.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def message(self):
        """Gets the message of this RemediationException.

        加入合规规则修正例外的原因。

        :return: The message of this RemediationException.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this RemediationException.

        加入合规规则修正例外的原因。

        :param message: The message of this RemediationException.
        :type message: str
        """
        self._message = message

    @property
    def joined_at(self):
        """Gets the joined_at of this RemediationException.

        加入合规规则修正例外的时间。

        :return: The joined_at of this RemediationException.
        :rtype: str
        """
        return self._joined_at

    @joined_at.setter
    def joined_at(self, joined_at):
        """Sets the joined_at of this RemediationException.

        加入合规规则修正例外的时间。

        :param joined_at: The joined_at of this RemediationException.
        :type joined_at: str
        """
        self._joined_at = joined_at

    @property
    def created_by(self):
        """Gets the created_by of this RemediationException.

        合规规则修正例外的创建者。

        :return: The created_by of this RemediationException.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this RemediationException.

        合规规则修正例外的创建者。

        :param created_by: The created_by of this RemediationException.
        :type created_by: str
        """
        self._created_by = created_by

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
        if not isinstance(other, RemediationException):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
