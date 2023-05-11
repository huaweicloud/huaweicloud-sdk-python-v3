# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteCertificateAuthorityRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ca_id': 'str',
        'pending_days': 'str'
    }

    attribute_map = {
        'ca_id': 'ca_id',
        'pending_days': 'pending_days'
    }

    def __init__(self, ca_id=None, pending_days=None):
        """DeleteCertificateAuthorityRequest

        The model defined in huaweicloud sdk

        :param ca_id: 所要计划删除的CA证书ID。
        :type ca_id: str
        :param pending_days: 延迟删除时间，单位为”天“。
        :type pending_days: str
        """
        
        

        self._ca_id = None
        self._pending_days = None
        self.discriminator = None

        self.ca_id = ca_id
        self.pending_days = pending_days

    @property
    def ca_id(self):
        """Gets the ca_id of this DeleteCertificateAuthorityRequest.

        所要计划删除的CA证书ID。

        :return: The ca_id of this DeleteCertificateAuthorityRequest.
        :rtype: str
        """
        return self._ca_id

    @ca_id.setter
    def ca_id(self, ca_id):
        """Sets the ca_id of this DeleteCertificateAuthorityRequest.

        所要计划删除的CA证书ID。

        :param ca_id: The ca_id of this DeleteCertificateAuthorityRequest.
        :type ca_id: str
        """
        self._ca_id = ca_id

    @property
    def pending_days(self):
        """Gets the pending_days of this DeleteCertificateAuthorityRequest.

        延迟删除时间，单位为”天“。

        :return: The pending_days of this DeleteCertificateAuthorityRequest.
        :rtype: str
        """
        return self._pending_days

    @pending_days.setter
    def pending_days(self, pending_days):
        """Sets the pending_days of this DeleteCertificateAuthorityRequest.

        延迟删除时间，单位为”天“。

        :param pending_days: The pending_days of this DeleteCertificateAuthorityRequest.
        :type pending_days: str
        """
        self._pending_days = pending_days

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
        if not isinstance(other, DeleteCertificateAuthorityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
