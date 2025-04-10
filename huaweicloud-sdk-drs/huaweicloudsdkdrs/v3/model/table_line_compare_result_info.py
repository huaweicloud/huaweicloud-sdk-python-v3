# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableLineCompareResultInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_table_name': 'str',
        'source_row_num': 'int',
        'target_table_name': 'str',
        'target_row_num': 'int',
        'difference_row_num': 'int',
        'status': 'int',
        'compare_line_config_filter': 'str'
    }

    attribute_map = {
        'source_table_name': 'source_table_name',
        'source_row_num': 'source_row_num',
        'target_table_name': 'target_table_name',
        'target_row_num': 'target_row_num',
        'difference_row_num': 'difference_row_num',
        'status': 'status',
        'compare_line_config_filter': 'compare_line_config_filter'
    }

    def __init__(self, source_table_name=None, source_row_num=None, target_table_name=None, target_row_num=None, difference_row_num=None, status=None, compare_line_config_filter=None):
        r"""TableLineCompareResultInfo

        The model defined in huaweicloud sdk

        :param source_table_name: 源库表名称
        :type source_table_name: str
        :param source_row_num: 源库表行数
        :type source_row_num: int
        :param target_table_name: 目标库表名称
        :type target_table_name: str
        :param target_row_num: 目标库表行数
        :type target_row_num: int
        :param difference_row_num: 行数差异值
        :type difference_row_num: int
        :param status: 对比状态。 - 0：对比不一致 - 2：对比一致 - 3：目标库表不存在 - 4：对比失败 - 5：正在对比中 - 6：等待对比中 - 7：任务已取消 - 8：源库为空 - 9：目标库为空 - 10：源库和目标库都为空 - 11：源表不存在 - 12：目标表不存在 - 13：原表和目标表都不存在 - 14：源数据库连接失败 - 15：目标库数据库连接失败 - 16：源数据库执行SQL超时 - 17：目标数据库执行SQL超时 - 18：源数据库执行SQL错误 - 19：目标数据库执行SQL错误 - 20：源库和目标库都不存在 - 21：源库不存在 - 22：目标库不存在 - 23：行数为亿行，未进行对比 - 27：超时
        :type status: int
        :param compare_line_config_filter: 行过滤配置条件
        :type compare_line_config_filter: str
        """
        
        

        self._source_table_name = None
        self._source_row_num = None
        self._target_table_name = None
        self._target_row_num = None
        self._difference_row_num = None
        self._status = None
        self._compare_line_config_filter = None
        self.discriminator = None

        if source_table_name is not None:
            self.source_table_name = source_table_name
        if source_row_num is not None:
            self.source_row_num = source_row_num
        if target_table_name is not None:
            self.target_table_name = target_table_name
        if target_row_num is not None:
            self.target_row_num = target_row_num
        if difference_row_num is not None:
            self.difference_row_num = difference_row_num
        if status is not None:
            self.status = status
        if compare_line_config_filter is not None:
            self.compare_line_config_filter = compare_line_config_filter

    @property
    def source_table_name(self):
        r"""Gets the source_table_name of this TableLineCompareResultInfo.

        源库表名称

        :return: The source_table_name of this TableLineCompareResultInfo.
        :rtype: str
        """
        return self._source_table_name

    @source_table_name.setter
    def source_table_name(self, source_table_name):
        r"""Sets the source_table_name of this TableLineCompareResultInfo.

        源库表名称

        :param source_table_name: The source_table_name of this TableLineCompareResultInfo.
        :type source_table_name: str
        """
        self._source_table_name = source_table_name

    @property
    def source_row_num(self):
        r"""Gets the source_row_num of this TableLineCompareResultInfo.

        源库表行数

        :return: The source_row_num of this TableLineCompareResultInfo.
        :rtype: int
        """
        return self._source_row_num

    @source_row_num.setter
    def source_row_num(self, source_row_num):
        r"""Sets the source_row_num of this TableLineCompareResultInfo.

        源库表行数

        :param source_row_num: The source_row_num of this TableLineCompareResultInfo.
        :type source_row_num: int
        """
        self._source_row_num = source_row_num

    @property
    def target_table_name(self):
        r"""Gets the target_table_name of this TableLineCompareResultInfo.

        目标库表名称

        :return: The target_table_name of this TableLineCompareResultInfo.
        :rtype: str
        """
        return self._target_table_name

    @target_table_name.setter
    def target_table_name(self, target_table_name):
        r"""Sets the target_table_name of this TableLineCompareResultInfo.

        目标库表名称

        :param target_table_name: The target_table_name of this TableLineCompareResultInfo.
        :type target_table_name: str
        """
        self._target_table_name = target_table_name

    @property
    def target_row_num(self):
        r"""Gets the target_row_num of this TableLineCompareResultInfo.

        目标库表行数

        :return: The target_row_num of this TableLineCompareResultInfo.
        :rtype: int
        """
        return self._target_row_num

    @target_row_num.setter
    def target_row_num(self, target_row_num):
        r"""Sets the target_row_num of this TableLineCompareResultInfo.

        目标库表行数

        :param target_row_num: The target_row_num of this TableLineCompareResultInfo.
        :type target_row_num: int
        """
        self._target_row_num = target_row_num

    @property
    def difference_row_num(self):
        r"""Gets the difference_row_num of this TableLineCompareResultInfo.

        行数差异值

        :return: The difference_row_num of this TableLineCompareResultInfo.
        :rtype: int
        """
        return self._difference_row_num

    @difference_row_num.setter
    def difference_row_num(self, difference_row_num):
        r"""Sets the difference_row_num of this TableLineCompareResultInfo.

        行数差异值

        :param difference_row_num: The difference_row_num of this TableLineCompareResultInfo.
        :type difference_row_num: int
        """
        self._difference_row_num = difference_row_num

    @property
    def status(self):
        r"""Gets the status of this TableLineCompareResultInfo.

        对比状态。 - 0：对比不一致 - 2：对比一致 - 3：目标库表不存在 - 4：对比失败 - 5：正在对比中 - 6：等待对比中 - 7：任务已取消 - 8：源库为空 - 9：目标库为空 - 10：源库和目标库都为空 - 11：源表不存在 - 12：目标表不存在 - 13：原表和目标表都不存在 - 14：源数据库连接失败 - 15：目标库数据库连接失败 - 16：源数据库执行SQL超时 - 17：目标数据库执行SQL超时 - 18：源数据库执行SQL错误 - 19：目标数据库执行SQL错误 - 20：源库和目标库都不存在 - 21：源库不存在 - 22：目标库不存在 - 23：行数为亿行，未进行对比 - 27：超时

        :return: The status of this TableLineCompareResultInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TableLineCompareResultInfo.

        对比状态。 - 0：对比不一致 - 2：对比一致 - 3：目标库表不存在 - 4：对比失败 - 5：正在对比中 - 6：等待对比中 - 7：任务已取消 - 8：源库为空 - 9：目标库为空 - 10：源库和目标库都为空 - 11：源表不存在 - 12：目标表不存在 - 13：原表和目标表都不存在 - 14：源数据库连接失败 - 15：目标库数据库连接失败 - 16：源数据库执行SQL超时 - 17：目标数据库执行SQL超时 - 18：源数据库执行SQL错误 - 19：目标数据库执行SQL错误 - 20：源库和目标库都不存在 - 21：源库不存在 - 22：目标库不存在 - 23：行数为亿行，未进行对比 - 27：超时

        :param status: The status of this TableLineCompareResultInfo.
        :type status: int
        """
        self._status = status

    @property
    def compare_line_config_filter(self):
        r"""Gets the compare_line_config_filter of this TableLineCompareResultInfo.

        行过滤配置条件

        :return: The compare_line_config_filter of this TableLineCompareResultInfo.
        :rtype: str
        """
        return self._compare_line_config_filter

    @compare_line_config_filter.setter
    def compare_line_config_filter(self, compare_line_config_filter):
        r"""Sets the compare_line_config_filter of this TableLineCompareResultInfo.

        行过滤配置条件

        :param compare_line_config_filter: The compare_line_config_filter of this TableLineCompareResultInfo.
        :type compare_line_config_filter: str
        """
        self._compare_line_config_filter = compare_line_config_filter

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
        if not isinstance(other, TableLineCompareResultInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
