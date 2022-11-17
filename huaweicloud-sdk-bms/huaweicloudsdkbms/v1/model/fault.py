# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Fault:

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
        'code': 'int',
        'details': 'str',
        'created': 'datetime'
    }

    attribute_map = {
        'message': 'message',
        'code': 'code',
        'details': 'details',
        'created': 'created'
    }

    def __init__(self, message=None, code=None, details=None, created=None):
        """Fault

        The model defined in huaweicloud sdk

        :param message: 故障信息
        :type message: str
        :param code: 故障code
        :type code: int
        :param details: 故障详情
        :type details: str
        :param created: 故障时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T03:30:52Z
        :type created: datetime
        """
        
        

        self._message = None
        self._code = None
        self._details = None
        self._created = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if details is not None:
            self.details = details
        if created is not None:
            self.created = created

    @property
    def message(self):
        """Gets the message of this Fault.

        故障信息

        :return: The message of this Fault.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Fault.

        故障信息

        :param message: The message of this Fault.
        :type message: str
        """
        self._message = message

    @property
    def code(self):
        """Gets the code of this Fault.

        故障code

        :return: The code of this Fault.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Fault.

        故障code

        :param code: The code of this Fault.
        :type code: int
        """
        self._code = code

    @property
    def details(self):
        """Gets the details of this Fault.

        故障详情

        :return: The details of this Fault.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Fault.

        故障详情

        :param details: The details of this Fault.
        :type details: str
        """
        self._details = details

    @property
    def created(self):
        """Gets the created of this Fault.

        故障时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T03:30:52Z

        :return: The created of this Fault.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Fault.

        故障时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T03:30:52Z

        :param created: The created of this Fault.
        :type created: datetime
        """
        self._created = created

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
        if not isinstance(other, Fault):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
