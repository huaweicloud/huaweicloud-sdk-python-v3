# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutLogicalVolume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'need_migration': 'bool',
        'adjust_size': 'int'
    }

    attribute_map = {
        'id': 'id',
        'need_migration': 'need_migration',
        'adjust_size': 'adjust_size'
    }

    def __init__(self, id=None, need_migration=None, adjust_size=None):
        r"""PutLogicalVolume

        The model defined in huaweicloud sdk

        :param id: 逻辑卷ID
        :type id: str
        :param need_migration: 是否迁移
        :type need_migration: bool
        :param adjust_size: 调整大小
        :type adjust_size: int
        """
        
        

        self._id = None
        self._need_migration = None
        self._adjust_size = None
        self.discriminator = None

        self.id = id
        if need_migration is not None:
            self.need_migration = need_migration
        if adjust_size is not None:
            self.adjust_size = adjust_size

    @property
    def id(self):
        r"""Gets the id of this PutLogicalVolume.

        逻辑卷ID

        :return: The id of this PutLogicalVolume.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PutLogicalVolume.

        逻辑卷ID

        :param id: The id of this PutLogicalVolume.
        :type id: str
        """
        self._id = id

    @property
    def need_migration(self):
        r"""Gets the need_migration of this PutLogicalVolume.

        是否迁移

        :return: The need_migration of this PutLogicalVolume.
        :rtype: bool
        """
        return self._need_migration

    @need_migration.setter
    def need_migration(self, need_migration):
        r"""Sets the need_migration of this PutLogicalVolume.

        是否迁移

        :param need_migration: The need_migration of this PutLogicalVolume.
        :type need_migration: bool
        """
        self._need_migration = need_migration

    @property
    def adjust_size(self):
        r"""Gets the adjust_size of this PutLogicalVolume.

        调整大小

        :return: The adjust_size of this PutLogicalVolume.
        :rtype: int
        """
        return self._adjust_size

    @adjust_size.setter
    def adjust_size(self, adjust_size):
        r"""Sets the adjust_size of this PutLogicalVolume.

        调整大小

        :param adjust_size: The adjust_size of this PutLogicalVolume.
        :type adjust_size: int
        """
        self._adjust_size = adjust_size

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
        if not isinstance(other, PutLogicalVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
