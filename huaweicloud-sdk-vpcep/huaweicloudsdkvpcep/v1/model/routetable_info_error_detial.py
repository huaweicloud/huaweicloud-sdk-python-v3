# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoutetableInfoErrorDetial:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'error_message': 'error_message'
    }

    def __init__(self, id=None, error_message=None):
        """RoutetableInfoErrorDetial

        The model defined in huaweicloud sdk

        :param id: 路由表ID。
        :type id: str
        :param error_message: 详细错误信息。
        :type error_message: str
        """
        
        

        self._id = None
        self._error_message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if error_message is not None:
            self.error_message = error_message

    @property
    def id(self):
        """Gets the id of this RoutetableInfoErrorDetial.

        路由表ID。

        :return: The id of this RoutetableInfoErrorDetial.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RoutetableInfoErrorDetial.

        路由表ID。

        :param id: The id of this RoutetableInfoErrorDetial.
        :type id: str
        """
        self._id = id

    @property
    def error_message(self):
        """Gets the error_message of this RoutetableInfoErrorDetial.

        详细错误信息。

        :return: The error_message of this RoutetableInfoErrorDetial.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this RoutetableInfoErrorDetial.

        详细错误信息。

        :param error_message: The error_message of this RoutetableInfoErrorDetial.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, RoutetableInfoErrorDetial):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
