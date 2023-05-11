# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conference_id': 'str',
        'password': 'str'
    }

    attribute_map = {
        'conference_id': 'conferenceID',
        'password': 'password'
    }

    def __init__(self, conference_id=None, password=None):
        """StartRequest

        The model defined in huaweicloud sdk

        :param conference_id: 会议ID。
        :type conference_id: str
        :param password: 会议密码。
        :type password: str
        """
        
        

        self._conference_id = None
        self._password = None
        self.discriminator = None

        self.conference_id = conference_id
        self.password = password

    @property
    def conference_id(self):
        """Gets the conference_id of this StartRequest.

        会议ID。

        :return: The conference_id of this StartRequest.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this StartRequest.

        会议ID。

        :param conference_id: The conference_id of this StartRequest.
        :type conference_id: str
        """
        self._conference_id = conference_id

    @property
    def password(self):
        """Gets the password of this StartRequest.

        会议密码。

        :return: The password of this StartRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this StartRequest.

        会议密码。

        :param password: The password of this StartRequest.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, StartRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
