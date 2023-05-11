# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Job:

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
        'path': 'str',
        'params': 'object'
    }

    attribute_map = {
        'name': 'name',
        'path': 'path',
        'params': 'params'
    }

    def __init__(self, name=None, path=None, params=None):
        """Job

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param path: 
        :type path: str
        :param params: 
        :type params: object
        """
        
        

        self._name = None
        self._path = None
        self._params = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if params is not None:
            self.params = params

    @property
    def name(self):
        """Gets the name of this Job.

        :return: The name of this Job.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Job.

        :param name: The name of this Job.
        :type name: str
        """
        self._name = name

    @property
    def path(self):
        """Gets the path of this Job.

        :return: The path of this Job.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Job.

        :param path: The path of this Job.
        :type path: str
        """
        self._path = path

    @property
    def params(self):
        """Gets the params of this Job.

        :return: The params of this Job.
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this Job.

        :param params: The params of this Job.
        :type params: object
        """
        self._params = params

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
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
