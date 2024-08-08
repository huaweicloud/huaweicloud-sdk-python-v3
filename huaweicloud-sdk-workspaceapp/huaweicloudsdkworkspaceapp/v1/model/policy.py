# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Policy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'statement': 'ObsPolicyStatement'
    }

    attribute_map = {
        'version': 'version',
        'statement': 'statement'
    }

    def __init__(self, version=None, statement=None):
        """Policy

        The model defined in huaweicloud sdk

        :param version: 版本号。
        :type version: str
        :param statement: 
        :type statement: :class:`huaweicloudsdkworkspaceapp.v1.ObsPolicyStatement`
        """
        
        

        self._version = None
        self._statement = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if statement is not None:
            self.statement = statement

    @property
    def version(self):
        """Gets the version of this Policy.

        版本号。

        :return: The version of this Policy.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Policy.

        版本号。

        :param version: The version of this Policy.
        :type version: str
        """
        self._version = version

    @property
    def statement(self):
        """Gets the statement of this Policy.

        :return: The statement of this Policy.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ObsPolicyStatement`
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        """Sets the statement of this Policy.

        :param statement: The statement of this Policy.
        :type statement: :class:`huaweicloudsdkworkspaceapp.v1.ObsPolicyStatement`
        """
        self._statement = statement

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
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
