# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectsCompareOverviewInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'source_count': 'int',
        'target_count': 'int',
        'status': 'str'
    }

    attribute_map = {
        'type': 'type',
        'source_count': 'source_count',
        'target_count': 'target_count',
        'status': 'status'
    }

    def __init__(self, type=None, source_count=None, target_count=None, status=None):
        """ObjectsCompareOverviewInfo

        The model defined in huaweicloud sdk

        :param type: 对象类型。取值： - DB：数据库。 - TABLE：表。 - VIEW：视图。 - EVENT：事件。 - ROUTINE：存储过程和函数。 - INDEX：索引。 - TRIGGER：触发器。 - SYNONYM：同义词。 - FUNCTION：函数。 - PROCEDURE：存储过程。 - TYPE：自定义类型。 - RULE：规则。 - DEFAULT_TYPE：缺省值。 - PLAN_GUIDE：执行计划。 - CONSTRAINT：约束。 - FILE_GROUP：文件组。 - PARTITION_FUNCTION：分区函数。 - PARTITION_SCHEME：分区方案。 - TABLE_COLLATION：表的排序规则。 - EXTENSIONS：插件。
        :type type: str
        :param source_count: 源数量。
        :type source_count: int
        :param target_count: 目标数量。
        :type target_count: int
        :param status: 对比结果。取值： CONSISTENT：一致。 INCONSISTENT：不一致。 COMPARING：正在对比。 WAITING_FOR_COMPARISON：等待对比。 FAILED_TO_COMPARE：对比失败。 TARGET_DB_NOT_EXIST：目标库不存在。 CAN_NOT_COMPARE：无法对比。
        :type status: str
        """
        
        

        self._type = None
        self._source_count = None
        self._target_count = None
        self._status = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if source_count is not None:
            self.source_count = source_count
        if target_count is not None:
            self.target_count = target_count
        if status is not None:
            self.status = status

    @property
    def type(self):
        """Gets the type of this ObjectsCompareOverviewInfo.

        对象类型。取值： - DB：数据库。 - TABLE：表。 - VIEW：视图。 - EVENT：事件。 - ROUTINE：存储过程和函数。 - INDEX：索引。 - TRIGGER：触发器。 - SYNONYM：同义词。 - FUNCTION：函数。 - PROCEDURE：存储过程。 - TYPE：自定义类型。 - RULE：规则。 - DEFAULT_TYPE：缺省值。 - PLAN_GUIDE：执行计划。 - CONSTRAINT：约束。 - FILE_GROUP：文件组。 - PARTITION_FUNCTION：分区函数。 - PARTITION_SCHEME：分区方案。 - TABLE_COLLATION：表的排序规则。 - EXTENSIONS：插件。

        :return: The type of this ObjectsCompareOverviewInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ObjectsCompareOverviewInfo.

        对象类型。取值： - DB：数据库。 - TABLE：表。 - VIEW：视图。 - EVENT：事件。 - ROUTINE：存储过程和函数。 - INDEX：索引。 - TRIGGER：触发器。 - SYNONYM：同义词。 - FUNCTION：函数。 - PROCEDURE：存储过程。 - TYPE：自定义类型。 - RULE：规则。 - DEFAULT_TYPE：缺省值。 - PLAN_GUIDE：执行计划。 - CONSTRAINT：约束。 - FILE_GROUP：文件组。 - PARTITION_FUNCTION：分区函数。 - PARTITION_SCHEME：分区方案。 - TABLE_COLLATION：表的排序规则。 - EXTENSIONS：插件。

        :param type: The type of this ObjectsCompareOverviewInfo.
        :type type: str
        """
        self._type = type

    @property
    def source_count(self):
        """Gets the source_count of this ObjectsCompareOverviewInfo.

        源数量。

        :return: The source_count of this ObjectsCompareOverviewInfo.
        :rtype: int
        """
        return self._source_count

    @source_count.setter
    def source_count(self, source_count):
        """Sets the source_count of this ObjectsCompareOverviewInfo.

        源数量。

        :param source_count: The source_count of this ObjectsCompareOverviewInfo.
        :type source_count: int
        """
        self._source_count = source_count

    @property
    def target_count(self):
        """Gets the target_count of this ObjectsCompareOverviewInfo.

        目标数量。

        :return: The target_count of this ObjectsCompareOverviewInfo.
        :rtype: int
        """
        return self._target_count

    @target_count.setter
    def target_count(self, target_count):
        """Sets the target_count of this ObjectsCompareOverviewInfo.

        目标数量。

        :param target_count: The target_count of this ObjectsCompareOverviewInfo.
        :type target_count: int
        """
        self._target_count = target_count

    @property
    def status(self):
        """Gets the status of this ObjectsCompareOverviewInfo.

        对比结果。取值： CONSISTENT：一致。 INCONSISTENT：不一致。 COMPARING：正在对比。 WAITING_FOR_COMPARISON：等待对比。 FAILED_TO_COMPARE：对比失败。 TARGET_DB_NOT_EXIST：目标库不存在。 CAN_NOT_COMPARE：无法对比。

        :return: The status of this ObjectsCompareOverviewInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ObjectsCompareOverviewInfo.

        对比结果。取值： CONSISTENT：一致。 INCONSISTENT：不一致。 COMPARING：正在对比。 WAITING_FOR_COMPARISON：等待对比。 FAILED_TO_COMPARE：对比失败。 TARGET_DB_NOT_EXIST：目标库不存在。 CAN_NOT_COMPARE：无法对比。

        :param status: The status of this ObjectsCompareOverviewInfo.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ObjectsCompareOverviewInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
