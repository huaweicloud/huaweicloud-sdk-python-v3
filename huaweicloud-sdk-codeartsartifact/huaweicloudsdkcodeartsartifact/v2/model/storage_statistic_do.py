# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StorageStatisticDO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'files_count': 'int',
        'used_space_length': 'int',
        'used_space': 'str',
        'summary_date': 'str',
        'folders_count': 'int',
        'items_count': 'int'
    }

    attribute_map = {
        'files_count': 'filesCount',
        'used_space_length': 'usedSpaceLength',
        'used_space': 'usedSpace',
        'summary_date': 'summaryDate',
        'folders_count': 'foldersCount',
        'items_count': 'itemsCount'
    }

    def __init__(self, files_count=None, used_space_length=None, used_space=None, summary_date=None, folders_count=None, items_count=None):
        r"""StorageStatisticDO

        The model defined in huaweicloud sdk

        :param files_count: 参数解释: 文件总数。 取值范围: 不涉及。
        :type files_count: int
        :param used_space_length: 参数解释: 占用空间(字节)。 取值范围: 不涉及。
        :type used_space_length: int
        :param used_space: 参数解释: 占用空间。 取值范围: 不涉及。
        :type used_space: str
        :param summary_date: 参数解释: 统计日期。 取值范围: 不涉及。
        :type summary_date: str
        :param folders_count: 参数解释: 文件夹总数。 取值范围: 不涉及。
        :type folders_count: int
        :param items_count: 参数解释: 文件及文件夹总数。 取值范围: 不涉及。
        :type items_count: int
        """
        
        

        self._files_count = None
        self._used_space_length = None
        self._used_space = None
        self._summary_date = None
        self._folders_count = None
        self._items_count = None
        self.discriminator = None

        if files_count is not None:
            self.files_count = files_count
        if used_space_length is not None:
            self.used_space_length = used_space_length
        if used_space is not None:
            self.used_space = used_space
        if summary_date is not None:
            self.summary_date = summary_date
        if folders_count is not None:
            self.folders_count = folders_count
        if items_count is not None:
            self.items_count = items_count

    @property
    def files_count(self):
        r"""Gets the files_count of this StorageStatisticDO.

        参数解释: 文件总数。 取值范围: 不涉及。

        :return: The files_count of this StorageStatisticDO.
        :rtype: int
        """
        return self._files_count

    @files_count.setter
    def files_count(self, files_count):
        r"""Sets the files_count of this StorageStatisticDO.

        参数解释: 文件总数。 取值范围: 不涉及。

        :param files_count: The files_count of this StorageStatisticDO.
        :type files_count: int
        """
        self._files_count = files_count

    @property
    def used_space_length(self):
        r"""Gets the used_space_length of this StorageStatisticDO.

        参数解释: 占用空间(字节)。 取值范围: 不涉及。

        :return: The used_space_length of this StorageStatisticDO.
        :rtype: int
        """
        return self._used_space_length

    @used_space_length.setter
    def used_space_length(self, used_space_length):
        r"""Sets the used_space_length of this StorageStatisticDO.

        参数解释: 占用空间(字节)。 取值范围: 不涉及。

        :param used_space_length: The used_space_length of this StorageStatisticDO.
        :type used_space_length: int
        """
        self._used_space_length = used_space_length

    @property
    def used_space(self):
        r"""Gets the used_space of this StorageStatisticDO.

        参数解释: 占用空间。 取值范围: 不涉及。

        :return: The used_space of this StorageStatisticDO.
        :rtype: str
        """
        return self._used_space

    @used_space.setter
    def used_space(self, used_space):
        r"""Sets the used_space of this StorageStatisticDO.

        参数解释: 占用空间。 取值范围: 不涉及。

        :param used_space: The used_space of this StorageStatisticDO.
        :type used_space: str
        """
        self._used_space = used_space

    @property
    def summary_date(self):
        r"""Gets the summary_date of this StorageStatisticDO.

        参数解释: 统计日期。 取值范围: 不涉及。

        :return: The summary_date of this StorageStatisticDO.
        :rtype: str
        """
        return self._summary_date

    @summary_date.setter
    def summary_date(self, summary_date):
        r"""Sets the summary_date of this StorageStatisticDO.

        参数解释: 统计日期。 取值范围: 不涉及。

        :param summary_date: The summary_date of this StorageStatisticDO.
        :type summary_date: str
        """
        self._summary_date = summary_date

    @property
    def folders_count(self):
        r"""Gets the folders_count of this StorageStatisticDO.

        参数解释: 文件夹总数。 取值范围: 不涉及。

        :return: The folders_count of this StorageStatisticDO.
        :rtype: int
        """
        return self._folders_count

    @folders_count.setter
    def folders_count(self, folders_count):
        r"""Sets the folders_count of this StorageStatisticDO.

        参数解释: 文件夹总数。 取值范围: 不涉及。

        :param folders_count: The folders_count of this StorageStatisticDO.
        :type folders_count: int
        """
        self._folders_count = folders_count

    @property
    def items_count(self):
        r"""Gets the items_count of this StorageStatisticDO.

        参数解释: 文件及文件夹总数。 取值范围: 不涉及。

        :return: The items_count of this StorageStatisticDO.
        :rtype: int
        """
        return self._items_count

    @items_count.setter
    def items_count(self, items_count):
        r"""Sets the items_count of this StorageStatisticDO.

        参数解释: 文件及文件夹总数。 取值范围: 不涉及。

        :param items_count: The items_count of this StorageStatisticDO.
        :type items_count: int
        """
        self._items_count = items_count

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
        if not isinstance(other, StorageStatisticDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
