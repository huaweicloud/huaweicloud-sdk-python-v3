# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryMigrationObjectProgressInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'migration_object_overview': 'list[MigrationObjectOverviewInfo]',
        'create_time': 'date',
        'full_start_time': 'date',
        'full_complete_time': 'date',
        'incr_start_time': 'date',
        'end_time': 'str'
    }

    attribute_map = {
        'migration_object_overview': 'migration_object_overview',
        'create_time': 'create_time',
        'full_start_time': 'full_start_time',
        'full_complete_time': 'full_complete_time',
        'incr_start_time': 'incr_start_time',
        'end_time': 'end_time'
    }

    def __init__(self, migration_object_overview=None, create_time=None, full_start_time=None, full_complete_time=None, incr_start_time=None, end_time=None):
        """QueryMigrationObjectProgressInfo

        The model defined in huaweicloud sdk

        :param migration_object_overview: 概览详情。
        :type migration_object_overview: list[:class:`huaweicloudsdkdrs.v5.MigrationObjectOverviewInfo`]
        :param create_time: 数据生成时间。
        :type create_time: date
        :param full_start_time: 全量开始时间。
        :type full_start_time: date
        :param full_complete_time: 全量完成时间。
        :type full_complete_time: date
        :param incr_start_time: 增量开始时间。
        :type incr_start_time: date
        :param end_time: 结束时间。
        :type end_time: str
        """
        
        

        self._migration_object_overview = None
        self._create_time = None
        self._full_start_time = None
        self._full_complete_time = None
        self._incr_start_time = None
        self._end_time = None
        self.discriminator = None

        if migration_object_overview is not None:
            self.migration_object_overview = migration_object_overview
        if create_time is not None:
            self.create_time = create_time
        if full_start_time is not None:
            self.full_start_time = full_start_time
        if full_complete_time is not None:
            self.full_complete_time = full_complete_time
        if incr_start_time is not None:
            self.incr_start_time = incr_start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def migration_object_overview(self):
        """Gets the migration_object_overview of this QueryMigrationObjectProgressInfo.

        概览详情。

        :return: The migration_object_overview of this QueryMigrationObjectProgressInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.MigrationObjectOverviewInfo`]
        """
        return self._migration_object_overview

    @migration_object_overview.setter
    def migration_object_overview(self, migration_object_overview):
        """Sets the migration_object_overview of this QueryMigrationObjectProgressInfo.

        概览详情。

        :param migration_object_overview: The migration_object_overview of this QueryMigrationObjectProgressInfo.
        :type migration_object_overview: list[:class:`huaweicloudsdkdrs.v5.MigrationObjectOverviewInfo`]
        """
        self._migration_object_overview = migration_object_overview

    @property
    def create_time(self):
        """Gets the create_time of this QueryMigrationObjectProgressInfo.

        数据生成时间。

        :return: The create_time of this QueryMigrationObjectProgressInfo.
        :rtype: date
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this QueryMigrationObjectProgressInfo.

        数据生成时间。

        :param create_time: The create_time of this QueryMigrationObjectProgressInfo.
        :type create_time: date
        """
        self._create_time = create_time

    @property
    def full_start_time(self):
        """Gets the full_start_time of this QueryMigrationObjectProgressInfo.

        全量开始时间。

        :return: The full_start_time of this QueryMigrationObjectProgressInfo.
        :rtype: date
        """
        return self._full_start_time

    @full_start_time.setter
    def full_start_time(self, full_start_time):
        """Sets the full_start_time of this QueryMigrationObjectProgressInfo.

        全量开始时间。

        :param full_start_time: The full_start_time of this QueryMigrationObjectProgressInfo.
        :type full_start_time: date
        """
        self._full_start_time = full_start_time

    @property
    def full_complete_time(self):
        """Gets the full_complete_time of this QueryMigrationObjectProgressInfo.

        全量完成时间。

        :return: The full_complete_time of this QueryMigrationObjectProgressInfo.
        :rtype: date
        """
        return self._full_complete_time

    @full_complete_time.setter
    def full_complete_time(self, full_complete_time):
        """Sets the full_complete_time of this QueryMigrationObjectProgressInfo.

        全量完成时间。

        :param full_complete_time: The full_complete_time of this QueryMigrationObjectProgressInfo.
        :type full_complete_time: date
        """
        self._full_complete_time = full_complete_time

    @property
    def incr_start_time(self):
        """Gets the incr_start_time of this QueryMigrationObjectProgressInfo.

        增量开始时间。

        :return: The incr_start_time of this QueryMigrationObjectProgressInfo.
        :rtype: date
        """
        return self._incr_start_time

    @incr_start_time.setter
    def incr_start_time(self, incr_start_time):
        """Sets the incr_start_time of this QueryMigrationObjectProgressInfo.

        增量开始时间。

        :param incr_start_time: The incr_start_time of this QueryMigrationObjectProgressInfo.
        :type incr_start_time: date
        """
        self._incr_start_time = incr_start_time

    @property
    def end_time(self):
        """Gets the end_time of this QueryMigrationObjectProgressInfo.

        结束时间。

        :return: The end_time of this QueryMigrationObjectProgressInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this QueryMigrationObjectProgressInfo.

        结束时间。

        :param end_time: The end_time of this QueryMigrationObjectProgressInfo.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, QueryMigrationObjectProgressInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
