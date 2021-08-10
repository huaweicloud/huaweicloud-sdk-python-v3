# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCertificateAuthorityRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit': 'str',
        'name': 'str',
        'offset': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'name': 'name',
        'offset': 'offset',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, limit=None, name=None, offset=None, status=None, type=None):
        """ListCertificateAuthorityRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._name = None
        self._offset = None
        self._status = None
        self._type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type

    @property
    def limit(self):
        """Gets the limit of this ListCertificateAuthorityRequest.

        limit

        :return: The limit of this ListCertificateAuthorityRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCertificateAuthorityRequest.

        limit

        :param limit: The limit of this ListCertificateAuthorityRequest.
        :type: str
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListCertificateAuthorityRequest.

        name

        :return: The name of this ListCertificateAuthorityRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListCertificateAuthorityRequest.

        name

        :param name: The name of this ListCertificateAuthorityRequest.
        :type: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListCertificateAuthorityRequest.

        offset

        :return: The offset of this ListCertificateAuthorityRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCertificateAuthorityRequest.

        offset

        :param offset: The offset of this ListCertificateAuthorityRequest.
        :type: str
        """
        self._offset = offset

    @property
    def status(self):
        """Gets the status of this ListCertificateAuthorityRequest.

        status

        :return: The status of this ListCertificateAuthorityRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListCertificateAuthorityRequest.

        status

        :param status: The status of this ListCertificateAuthorityRequest.
        :type: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this ListCertificateAuthorityRequest.

        type

        :return: The type of this ListCertificateAuthorityRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListCertificateAuthorityRequest.

        type

        :param type: The type of this ListCertificateAuthorityRequest.
        :type: str
        """
        self._type = type

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
        if not isinstance(other, ListCertificateAuthorityRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
