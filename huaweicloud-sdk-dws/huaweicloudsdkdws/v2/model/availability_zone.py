# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailabilityZone:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'name': 'str',
        'status': 'str',
        'public_border_group': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'status': 'status',
        'public_border_group': 'public_border_group'
    }

    def __init__(self, code=None, name=None, status=None, public_border_group=None):
        """AvailabilityZone

        The model defined in huaweicloud sdk

        :param code: 可用区唯一编码。
        :type code: str
        :param name: 可用区名称。
        :type name: str
        :param status: 可用区状态。 - available：可用。 - unavailable：不可用。
        :type status: str
        :param public_border_group: 可用区组，如：center。
        :type public_border_group: str
        """
        
        

        self._code = None
        self._name = None
        self._status = None
        self._public_border_group = None
        self.discriminator = None

        self.code = code
        self.name = name
        self.status = status
        self.public_border_group = public_border_group

    @property
    def code(self):
        """Gets the code of this AvailabilityZone.

        可用区唯一编码。

        :return: The code of this AvailabilityZone.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AvailabilityZone.

        可用区唯一编码。

        :param code: The code of this AvailabilityZone.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        """Gets the name of this AvailabilityZone.

        可用区名称。

        :return: The name of this AvailabilityZone.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AvailabilityZone.

        可用区名称。

        :param name: The name of this AvailabilityZone.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this AvailabilityZone.

        可用区状态。 - available：可用。 - unavailable：不可用。

        :return: The status of this AvailabilityZone.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AvailabilityZone.

        可用区状态。 - available：可用。 - unavailable：不可用。

        :param status: The status of this AvailabilityZone.
        :type status: str
        """
        self._status = status

    @property
    def public_border_group(self):
        """Gets the public_border_group of this AvailabilityZone.

        可用区组，如：center。

        :return: The public_border_group of this AvailabilityZone.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this AvailabilityZone.

        可用区组，如：center。

        :param public_border_group: The public_border_group of this AvailabilityZone.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

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
        if not isinstance(other, AvailabilityZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
