# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatastoreOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_version': 'str',
        'instance_mode': 'str'
    }

    attribute_map = {
        'engine_version': 'engine_version',
        'instance_mode': 'instance_mode'
    }

    def __init__(self, engine_version=None, instance_mode=None):
        """DatastoreOption

        The model defined in huaweicloud sdk

        :param engine_version: 数据库版本。支持2.3版本，取值为“2.3”。
        :type engine_version: str
        :param instance_mode: 部署形态。
        :type instance_mode: str
        """
        
        

        self._engine_version = None
        self._instance_mode = None
        self.discriminator = None

        self.engine_version = engine_version
        self.instance_mode = instance_mode

    @property
    def engine_version(self):
        """Gets the engine_version of this DatastoreOption.

        数据库版本。支持2.3版本，取值为“2.3”。

        :return: The engine_version of this DatastoreOption.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this DatastoreOption.

        数据库版本。支持2.3版本，取值为“2.3”。

        :param engine_version: The engine_version of this DatastoreOption.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def instance_mode(self):
        """Gets the instance_mode of this DatastoreOption.

        部署形态。

        :return: The instance_mode of this DatastoreOption.
        :rtype: str
        """
        return self._instance_mode

    @instance_mode.setter
    def instance_mode(self, instance_mode):
        """Sets the instance_mode of this DatastoreOption.

        部署形态。

        :param instance_mode: The instance_mode of this DatastoreOption.
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
        if not isinstance(other, DatastoreOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
