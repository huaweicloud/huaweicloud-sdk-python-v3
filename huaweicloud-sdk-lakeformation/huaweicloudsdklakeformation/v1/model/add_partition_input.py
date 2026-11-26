# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddPartitionInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'if_not_exist': 'bool',
        'partitions': 'list[PartitionInput]',
        'use_table_column': 'bool'
    }

    attribute_map = {
        'if_not_exist': 'if_not_exist',
        'partitions': 'partitions',
        'use_table_column': 'use_table_column'
    }

    def __init__(self, if_not_exist=None, partitions=None, use_table_column=None):
        r"""AddPartitionInput

        The model defined in huaweicloud sdk

        :param if_not_exist: 是否跳过已存在的分区
        :type if_not_exist: bool
        :param partitions: 添加的分区信息
        :type partitions: list[:class:`huaweicloudsdklakeformation.v1.PartitionInput`]
        :param use_table_column: 是否使用表的列作为分区中的列。默认为false
        :type use_table_column: bool
        """
        
        

        self._if_not_exist = None
        self._partitions = None
        self._use_table_column = None
        self.discriminator = None

        self.if_not_exist = if_not_exist
        self.partitions = partitions
        if use_table_column is not None:
            self.use_table_column = use_table_column

    @property
    def if_not_exist(self):
        r"""Gets the if_not_exist of this AddPartitionInput.

        是否跳过已存在的分区

        :return: The if_not_exist of this AddPartitionInput.
        :rtype: bool
        """
        return self._if_not_exist

    @if_not_exist.setter
    def if_not_exist(self, if_not_exist):
        r"""Sets the if_not_exist of this AddPartitionInput.

        是否跳过已存在的分区

        :param if_not_exist: The if_not_exist of this AddPartitionInput.
        :type if_not_exist: bool
        """
        self._if_not_exist = if_not_exist

    @property
    def partitions(self):
        r"""Gets the partitions of this AddPartitionInput.

        添加的分区信息

        :return: The partitions of this AddPartitionInput.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.PartitionInput`]
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        r"""Sets the partitions of this AddPartitionInput.

        添加的分区信息

        :param partitions: The partitions of this AddPartitionInput.
        :type partitions: list[:class:`huaweicloudsdklakeformation.v1.PartitionInput`]
        """
        self._partitions = partitions

    @property
    def use_table_column(self):
        r"""Gets the use_table_column of this AddPartitionInput.

        是否使用表的列作为分区中的列。默认为false

        :return: The use_table_column of this AddPartitionInput.
        :rtype: bool
        """
        return self._use_table_column

    @use_table_column.setter
    def use_table_column(self, use_table_column):
        r"""Sets the use_table_column of this AddPartitionInput.

        是否使用表的列作为分区中的列。默认为false

        :param use_table_column: The use_table_column of this AddPartitionInput.
        :type use_table_column: bool
        """
        self._use_table_column = use_table_column

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddPartitionInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
