# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentConfigCreate:

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
        'source': 'str',
        'envs': 'list[ComponentConfigEnvs]'
    }

    attribute_map = {
        'version': 'version',
        'source': 'source',
        'envs': 'envs'
    }

    def __init__(self, version=None, source=None, envs=None):
        """ComponentConfigCreate

        The model defined in huaweicloud sdk

        :param version: 
        :type version: str
        :param source: 来源版本号
        :type source: str
        :param envs: application environment parameters
        :type envs: list[:class:`huaweicloudsdkservicestage.v3.ComponentConfigEnvs`]
        """
        
        

        self._version = None
        self._source = None
        self._envs = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if source is not None:
            self.source = source
        if envs is not None:
            self.envs = envs

    @property
    def version(self):
        """Gets the version of this ComponentConfigCreate.

        :return: The version of this ComponentConfigCreate.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ComponentConfigCreate.

        :param version: The version of this ComponentConfigCreate.
        :type version: str
        """
        self._version = version

    @property
    def source(self):
        """Gets the source of this ComponentConfigCreate.

        来源版本号

        :return: The source of this ComponentConfigCreate.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ComponentConfigCreate.

        来源版本号

        :param source: The source of this ComponentConfigCreate.
        :type source: str
        """
        self._source = source

    @property
    def envs(self):
        """Gets the envs of this ComponentConfigCreate.

        application environment parameters

        :return: The envs of this ComponentConfigCreate.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ComponentConfigEnvs`]
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        """Sets the envs of this ComponentConfigCreate.

        application environment parameters

        :param envs: The envs of this ComponentConfigCreate.
        :type envs: list[:class:`huaweicloudsdkservicestage.v3.ComponentConfigEnvs`]
        """
        self._envs = envs

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
        if not isinstance(other, ComponentConfigCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
