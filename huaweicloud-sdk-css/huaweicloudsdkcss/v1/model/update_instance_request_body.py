# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'migrate_data': 'str'
    }

    attribute_map = {
        'migrate_data': 'migrate_data'
    }

    def __init__(self, migrate_data=None):
        """UpdateInstanceRequestBody

        The model defined in huaweicloud sdk

        :param migrate_data: 是否迁移数据。 - \&quot;true\&quot;：迁移数据。 - \&quot;false\&quot;：不迁移数据。
        :type migrate_data: str
        """
        
        

        self._migrate_data = None
        self.discriminator = None

        if migrate_data is not None:
            self.migrate_data = migrate_data

    @property
    def migrate_data(self):
        """Gets the migrate_data of this UpdateInstanceRequestBody.

        是否迁移数据。 - \"true\"：迁移数据。 - \"false\"：不迁移数据。

        :return: The migrate_data of this UpdateInstanceRequestBody.
        :rtype: str
        """
        return self._migrate_data

    @migrate_data.setter
    def migrate_data(self, migrate_data):
        """Sets the migrate_data of this UpdateInstanceRequestBody.

        是否迁移数据。 - \"true\"：迁移数据。 - \"false\"：不迁移数据。

        :param migrate_data: The migrate_data of this UpdateInstanceRequestBody.
        :type migrate_data: str
        """
        self._migrate_data = migrate_data

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
        if not isinstance(other, UpdateInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
