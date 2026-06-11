# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlterTableInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alter_params': 'dict(str, str)',
        'version_id': 'str',
        'table': 'UpdateTableInput',
        'is_async': 'bool'
    }

    attribute_map = {
        'alter_params': 'alter_params',
        'version_id': 'version_id',
        'table': 'table',
        'is_async': 'is_async'
    }

    def __init__(self, alter_params=None, version_id=None, table=None, is_async=None):
        r"""AlterTableInput

        The model defined in huaweicloud sdk

        :param alter_params: 修改表参数映射信息，支持的参数如下： CASCADE: 级联删除列，如果为true则会把partition中的列也删除；如果为false则不会 DO_NOT_UPDATE_STATS: 不更新文件级别统计信息。true则不更新；false则更新。 STATS_GENERATED：记录本次更新的发起者。可填：TASK/UNSET。具体作用未明确。
        :type alter_params: dict(str, str)
        :param version_id: 版本ID
        :type version_id: str
        :param table: 
        :type table: :class:`huaweicloudsdklakeformation.v1.UpdateTableInput`
        :param is_async: 是否异步修改，默认为false。
        :type is_async: bool
        """
        
        

        self._alter_params = None
        self._version_id = None
        self._table = None
        self._is_async = None
        self.discriminator = None

        if alter_params is not None:
            self.alter_params = alter_params
        if version_id is not None:
            self.version_id = version_id
        self.table = table
        if is_async is not None:
            self.is_async = is_async

    @property
    def alter_params(self):
        r"""Gets the alter_params of this AlterTableInput.

        修改表参数映射信息，支持的参数如下： CASCADE: 级联删除列，如果为true则会把partition中的列也删除；如果为false则不会 DO_NOT_UPDATE_STATS: 不更新文件级别统计信息。true则不更新；false则更新。 STATS_GENERATED：记录本次更新的发起者。可填：TASK/UNSET。具体作用未明确。

        :return: The alter_params of this AlterTableInput.
        :rtype: dict(str, str)
        """
        return self._alter_params

    @alter_params.setter
    def alter_params(self, alter_params):
        r"""Sets the alter_params of this AlterTableInput.

        修改表参数映射信息，支持的参数如下： CASCADE: 级联删除列，如果为true则会把partition中的列也删除；如果为false则不会 DO_NOT_UPDATE_STATS: 不更新文件级别统计信息。true则不更新；false则更新。 STATS_GENERATED：记录本次更新的发起者。可填：TASK/UNSET。具体作用未明确。

        :param alter_params: The alter_params of this AlterTableInput.
        :type alter_params: dict(str, str)
        """
        self._alter_params = alter_params

    @property
    def version_id(self):
        r"""Gets the version_id of this AlterTableInput.

        版本ID

        :return: The version_id of this AlterTableInput.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this AlterTableInput.

        版本ID

        :param version_id: The version_id of this AlterTableInput.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def table(self):
        r"""Gets the table of this AlterTableInput.

        :return: The table of this AlterTableInput.
        :rtype: :class:`huaweicloudsdklakeformation.v1.UpdateTableInput`
        """
        return self._table

    @table.setter
    def table(self, table):
        r"""Sets the table of this AlterTableInput.

        :param table: The table of this AlterTableInput.
        :type table: :class:`huaweicloudsdklakeformation.v1.UpdateTableInput`
        """
        self._table = table

    @property
    def is_async(self):
        r"""Gets the is_async of this AlterTableInput.

        是否异步修改，默认为false。

        :return: The is_async of this AlterTableInput.
        :rtype: bool
        """
        return self._is_async

    @is_async.setter
    def is_async(self, is_async):
        r"""Sets the is_async of this AlterTableInput.

        是否异步修改，默认为false。

        :param is_async: The is_async of this AlterTableInput.
        :type is_async: bool
        """
        self._is_async = is_async

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
        if not isinstance(other, AlterTableInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
