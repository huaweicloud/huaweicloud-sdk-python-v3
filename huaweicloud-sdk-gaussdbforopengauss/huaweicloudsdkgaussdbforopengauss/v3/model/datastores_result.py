# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatastoresResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'supported_versions': 'list[str]',
        'instance_mode': 'str'
    }

    attribute_map = {
        'supported_versions': 'supported_versions',
        'instance_mode': 'instance_mode'
    }

    def __init__(self, supported_versions=None, instance_mode=None):
        r"""DatastoresResult

        The model defined in huaweicloud sdk

        :param supported_versions: 部署形态支持的引擎版本列表
        :type supported_versions: list[str]
        :param instance_mode: 部署形态
        :type instance_mode: str
        """
        
        

        self._supported_versions = None
        self._instance_mode = None
        self.discriminator = None

        self.supported_versions = supported_versions
        self.instance_mode = instance_mode

    @property
    def supported_versions(self):
        r"""Gets the supported_versions of this DatastoresResult.

        部署形态支持的引擎版本列表

        :return: The supported_versions of this DatastoresResult.
        :rtype: list[str]
        """
        return self._supported_versions

    @supported_versions.setter
    def supported_versions(self, supported_versions):
        r"""Sets the supported_versions of this DatastoresResult.

        部署形态支持的引擎版本列表

        :param supported_versions: The supported_versions of this DatastoresResult.
        :type supported_versions: list[str]
        """
        self._supported_versions = supported_versions

    @property
    def instance_mode(self):
        r"""Gets the instance_mode of this DatastoresResult.

        部署形态

        :return: The instance_mode of this DatastoresResult.
        :rtype: str
        """
        return self._instance_mode

    @instance_mode.setter
    def instance_mode(self, instance_mode):
        r"""Sets the instance_mode of this DatastoresResult.

        部署形态

        :param instance_mode: The instance_mode of this DatastoresResult.
        :type instance_mode: str
        """
        self._instance_mode = instance_mode

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
        if not isinstance(other, DatastoresResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
