# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuntimeStack:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'version': 'str',
        'deploy_mode': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'version': 'version',
        'deploy_mode': 'deploy_mode'
    }

    def __init__(self, name=None, type=None, version=None, deploy_mode=None):
        r"""RuntimeStack

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param type: 
        :type type: str
        :param version: 
        :type version: str
        :param deploy_mode: 
        :type deploy_mode: str
        """
        
        

        self._name = None
        self._type = None
        self._version = None
        self._deploy_mode = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.version = version
        self.deploy_mode = deploy_mode

    @property
    def name(self):
        r"""Gets the name of this RuntimeStack.

        :return: The name of this RuntimeStack.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RuntimeStack.

        :param name: The name of this RuntimeStack.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this RuntimeStack.

        :return: The type of this RuntimeStack.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RuntimeStack.

        :param type: The type of this RuntimeStack.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this RuntimeStack.

        :return: The version of this RuntimeStack.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this RuntimeStack.

        :param version: The version of this RuntimeStack.
        :type version: str
        """
        self._version = version

    @property
    def deploy_mode(self):
        r"""Gets the deploy_mode of this RuntimeStack.

        :return: The deploy_mode of this RuntimeStack.
        :rtype: str
        """
        return self._deploy_mode

    @deploy_mode.setter
    def deploy_mode(self, deploy_mode):
        r"""Sets the deploy_mode of this RuntimeStack.

        :param deploy_mode: The deploy_mode of this RuntimeStack.
        :type deploy_mode: str
        """
        self._deploy_mode = deploy_mode

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
        if not isinstance(other, RuntimeStack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
