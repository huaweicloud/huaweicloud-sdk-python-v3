# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_phone_id': 'str',
        'target_phone_id': 'str',
        'is_migrate_property': 'str'
    }

    attribute_map = {
        'source_phone_id': 'source_phone_id',
        'target_phone_id': 'target_phone_id',
        'is_migrate_property': 'is_migrate_property'
    }

    def __init__(self, source_phone_id=None, target_phone_id=None, is_migrate_property=None):
        """MigrateInfo

        The model defined in huaweicloud sdk

        :param source_phone_id: 源云手机ID
        :type source_phone_id: str
        :param target_phone_id: 目标云手机ID
        :type target_phone_id: str
        :param is_migrate_property: 是否迁移原手机的属性到目标手机。为\&quot;true\&quot;时迁移（忽略大小写），不填写或者其他值，则不迁移
        :type is_migrate_property: str
        """
        
        

        self._source_phone_id = None
        self._target_phone_id = None
        self._is_migrate_property = None
        self.discriminator = None

        self.source_phone_id = source_phone_id
        self.target_phone_id = target_phone_id
        if is_migrate_property is not None:
            self.is_migrate_property = is_migrate_property

    @property
    def source_phone_id(self):
        """Gets the source_phone_id of this MigrateInfo.

        源云手机ID

        :return: The source_phone_id of this MigrateInfo.
        :rtype: str
        """
        return self._source_phone_id

    @source_phone_id.setter
    def source_phone_id(self, source_phone_id):
        """Sets the source_phone_id of this MigrateInfo.

        源云手机ID

        :param source_phone_id: The source_phone_id of this MigrateInfo.
        :type source_phone_id: str
        """
        self._source_phone_id = source_phone_id

    @property
    def target_phone_id(self):
        """Gets the target_phone_id of this MigrateInfo.

        目标云手机ID

        :return: The target_phone_id of this MigrateInfo.
        :rtype: str
        """
        return self._target_phone_id

    @target_phone_id.setter
    def target_phone_id(self, target_phone_id):
        """Sets the target_phone_id of this MigrateInfo.

        目标云手机ID

        :param target_phone_id: The target_phone_id of this MigrateInfo.
        :type target_phone_id: str
        """
        self._target_phone_id = target_phone_id

    @property
    def is_migrate_property(self):
        """Gets the is_migrate_property of this MigrateInfo.

        是否迁移原手机的属性到目标手机。为\"true\"时迁移（忽略大小写），不填写或者其他值，则不迁移

        :return: The is_migrate_property of this MigrateInfo.
        :rtype: str
        """
        return self._is_migrate_property

    @is_migrate_property.setter
    def is_migrate_property(self, is_migrate_property):
        """Sets the is_migrate_property of this MigrateInfo.

        是否迁移原手机的属性到目标手机。为\"true\"时迁移（忽略大小写），不填写或者其他值，则不迁移

        :param is_migrate_property: The is_migrate_property of this MigrateInfo.
        :type is_migrate_property: str
        """
        self._is_migrate_property = is_migrate_property

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
        if not isinstance(other, MigrateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
