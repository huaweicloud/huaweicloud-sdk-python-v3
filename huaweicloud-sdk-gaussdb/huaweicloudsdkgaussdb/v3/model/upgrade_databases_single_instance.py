# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeDatabasesSingleInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_version': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'current_version': 'current_version',
        'instance_id': 'instance_id'
    }

    def __init__(self, current_version=None, instance_id=None):
        r"""UpgradeDatabasesSingleInstance

        The model defined in huaweicloud sdk

        :param current_version: 实例当前的内核版本。
        :type current_version: str
        :param instance_id: 实例id。
        :type instance_id: str
        """
        
        

        self._current_version = None
        self._instance_id = None
        self.discriminator = None

        self.current_version = current_version
        self.instance_id = instance_id

    @property
    def current_version(self):
        r"""Gets the current_version of this UpgradeDatabasesSingleInstance.

        实例当前的内核版本。

        :return: The current_version of this UpgradeDatabasesSingleInstance.
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        r"""Sets the current_version of this UpgradeDatabasesSingleInstance.

        实例当前的内核版本。

        :param current_version: The current_version of this UpgradeDatabasesSingleInstance.
        :type current_version: str
        """
        self._current_version = current_version

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpgradeDatabasesSingleInstance.

        实例id。

        :return: The instance_id of this UpgradeDatabasesSingleInstance.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpgradeDatabasesSingleInstance.

        实例id。

        :param instance_id: The instance_id of this UpgradeDatabasesSingleInstance.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, UpgradeDatabasesSingleInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
