# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupportFastRestoreList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'is_support_fast_table_restore': 'bool',
        'is_support_fast_database_restore': 'bool'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'is_support_fast_table_restore': 'is_support_fast_table_restore',
        'is_support_fast_database_restore': 'is_support_fast_database_restore'
    }

    def __init__(self, instance_id=None, is_support_fast_table_restore=None, is_support_fast_database_restore=None):
        r"""SupportFastRestoreList

        The model defined in huaweicloud sdk

        :param instance_id: 实例id。
        :type instance_id: str
        :param is_support_fast_table_restore: 表级恢复是否支持极速恢复。
        :type is_support_fast_table_restore: bool
        :param is_support_fast_database_restore: 库级恢复是否支持极速恢复。
        :type is_support_fast_database_restore: bool
        """
        
        

        self._instance_id = None
        self._is_support_fast_table_restore = None
        self._is_support_fast_database_restore = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if is_support_fast_table_restore is not None:
            self.is_support_fast_table_restore = is_support_fast_table_restore
        if is_support_fast_database_restore is not None:
            self.is_support_fast_database_restore = is_support_fast_database_restore

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SupportFastRestoreList.

        实例id。

        :return: The instance_id of this SupportFastRestoreList.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SupportFastRestoreList.

        实例id。

        :param instance_id: The instance_id of this SupportFastRestoreList.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def is_support_fast_table_restore(self):
        r"""Gets the is_support_fast_table_restore of this SupportFastRestoreList.

        表级恢复是否支持极速恢复。

        :return: The is_support_fast_table_restore of this SupportFastRestoreList.
        :rtype: bool
        """
        return self._is_support_fast_table_restore

    @is_support_fast_table_restore.setter
    def is_support_fast_table_restore(self, is_support_fast_table_restore):
        r"""Sets the is_support_fast_table_restore of this SupportFastRestoreList.

        表级恢复是否支持极速恢复。

        :param is_support_fast_table_restore: The is_support_fast_table_restore of this SupportFastRestoreList.
        :type is_support_fast_table_restore: bool
        """
        self._is_support_fast_table_restore = is_support_fast_table_restore

    @property
    def is_support_fast_database_restore(self):
        r"""Gets the is_support_fast_database_restore of this SupportFastRestoreList.

        库级恢复是否支持极速恢复。

        :return: The is_support_fast_database_restore of this SupportFastRestoreList.
        :rtype: bool
        """
        return self._is_support_fast_database_restore

    @is_support_fast_database_restore.setter
    def is_support_fast_database_restore(self, is_support_fast_database_restore):
        r"""Sets the is_support_fast_database_restore of this SupportFastRestoreList.

        库级恢复是否支持极速恢复。

        :param is_support_fast_database_restore: The is_support_fast_database_restore of this SupportFastRestoreList.
        :type is_support_fast_database_restore: bool
        """
        self._is_support_fast_database_restore = is_support_fast_database_restore

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
        if not isinstance(other, SupportFastRestoreList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
