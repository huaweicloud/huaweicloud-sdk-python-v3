# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DropPartitionsInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'if_exist': 'bool',
        'delete_data': 'bool',
        'partition_values': 'list[list[str]]'
    }

    attribute_map = {
        'if_exist': 'if_exist',
        'delete_data': 'delete_data',
        'partition_values': 'partition_values'
    }

    def __init__(self, if_exist=None, delete_data=None, partition_values=None):
        """DropPartitionsInput

        The model defined in huaweicloud sdk

        :param if_exist: 是否跳过不存在分区
        :type if_exist: bool
        :param delete_data: 非事务表：删除分区的数据；若if_purge为真，立即释放空间。 事务表：数据保留但不可见，待数据过期统一删除。
        :type delete_data: bool
        :param partition_values: 删除分区值
        :type partition_values: list[list[str]]
        """
        
        

        self._if_exist = None
        self._delete_data = None
        self._partition_values = None
        self.discriminator = None

        if if_exist is not None:
            self.if_exist = if_exist
        if delete_data is not None:
            self.delete_data = delete_data
        self.partition_values = partition_values

    @property
    def if_exist(self):
        """Gets the if_exist of this DropPartitionsInput.

        是否跳过不存在分区

        :return: The if_exist of this DropPartitionsInput.
        :rtype: bool
        """
        return self._if_exist

    @if_exist.setter
    def if_exist(self, if_exist):
        """Sets the if_exist of this DropPartitionsInput.

        是否跳过不存在分区

        :param if_exist: The if_exist of this DropPartitionsInput.
        :type if_exist: bool
        """
        self._if_exist = if_exist

    @property
    def delete_data(self):
        """Gets the delete_data of this DropPartitionsInput.

        非事务表：删除分区的数据；若if_purge为真，立即释放空间。 事务表：数据保留但不可见，待数据过期统一删除。

        :return: The delete_data of this DropPartitionsInput.
        :rtype: bool
        """
        return self._delete_data

    @delete_data.setter
    def delete_data(self, delete_data):
        """Sets the delete_data of this DropPartitionsInput.

        非事务表：删除分区的数据；若if_purge为真，立即释放空间。 事务表：数据保留但不可见，待数据过期统一删除。

        :param delete_data: The delete_data of this DropPartitionsInput.
        :type delete_data: bool
        """
        self._delete_data = delete_data

    @property
    def partition_values(self):
        """Gets the partition_values of this DropPartitionsInput.

        删除分区值

        :return: The partition_values of this DropPartitionsInput.
        :rtype: list[list[str]]
        """
        return self._partition_values

    @partition_values.setter
    def partition_values(self, partition_values):
        """Sets the partition_values of this DropPartitionsInput.

        删除分区值

        :param partition_values: The partition_values of this DropPartitionsInput.
        :type partition_values: list[list[str]]
        """
        self._partition_values = partition_values

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
        if not isinstance(other, DropPartitionsInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
