# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Az2Migrate:

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
        'description': 'str',
        'status': 'str'
    }

    attribute_map = {
        'code': 'code',
        'description': 'description',
        'status': 'status'
    }

    def __init__(self, code=None, description=None, status=None):
        """Az2Migrate

        The model defined in huaweicloud sdk

        :param code: 可用区ID。
        :type code: str
        :param description: 可用区描述。
        :type description: str
        :param status: 当前可用区的的状态。 - ENABLED，表示该可用区（组合）可用。 - DISABLED，表示该可用区（组合）不可用。
        :type status: str
        """
        
        

        self._code = None
        self._description = None
        self._status = None
        self.discriminator = None

        self.code = code
        self.description = description
        self.status = status

    @property
    def code(self):
        """Gets the code of this Az2Migrate.

        可用区ID。

        :return: The code of this Az2Migrate.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Az2Migrate.

        可用区ID。

        :param code: The code of this Az2Migrate.
        :type code: str
        """
        self._code = code

    @property
    def description(self):
        """Gets the description of this Az2Migrate.

        可用区描述。

        :return: The description of this Az2Migrate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Az2Migrate.

        可用区描述。

        :param description: The description of this Az2Migrate.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this Az2Migrate.

        当前可用区的的状态。 - ENABLED，表示该可用区（组合）可用。 - DISABLED，表示该可用区（组合）不可用。

        :return: The status of this Az2Migrate.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Az2Migrate.

        当前可用区的的状态。 - ENABLED，表示该可用区（组合）可用。 - DISABLED，表示该可用区（组合）不可用。

        :param status: The status of this Az2Migrate.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, Az2Migrate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
