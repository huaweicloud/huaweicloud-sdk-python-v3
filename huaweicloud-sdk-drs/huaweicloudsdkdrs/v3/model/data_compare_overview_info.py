# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataCompareOverviewInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_db_name': 'str',
        'target_db_name': 'str',
        'status': 'int',
        'compare_num': 'int',
        'compare_end_num': 'int',
        'data_inconsistent_num': 'int',
        'uncomparable_num': 'int'
    }

    attribute_map = {
        'source_db_name': 'source_db_name',
        'target_db_name': 'target_db_name',
        'status': 'status',
        'compare_num': 'compare_num',
        'compare_end_num': 'compare_end_num',
        'data_inconsistent_num': 'data_inconsistent_num',
        'uncomparable_num': 'uncomparable_num'
    }

    def __init__(self, source_db_name=None, target_db_name=None, status=None, compare_num=None, compare_end_num=None, data_inconsistent_num=None, uncomparable_num=None):
        r"""DataCompareOverviewInfo

        The model defined in huaweicloud sdk

        :param source_db_name: 源库库名
        :type source_db_name: str
        :param target_db_name: 目标库库名
        :type target_db_name: str
        :param status: 对比状态。 - 0：对比不一致 - 2：对比一致 - 3：目标库表不存在 - 4：对比失败 - 5：正在对比中 - 6：等待对比中 - 7：任务已取消 - 8：源库为空 - 9：目标库为空 - 10：源库和目标库都为空 - 11：源表不存在 - 12：目标表不存在 - 13：原表和目标表都不存在 - 14：源数据库连接失败 - 15：目标库数据库连接失败 - 16：源数据库执行SQL超时 - 17：目标数据库执行SQL超时 - 18：源数据库执行SQL错误 - 19：目标数据库执行SQL错误 - 20：源库和目标库都不存在 - 21：源库不存在 - 22：目标库不存在 - 23：行数为亿行，未进行对比 - 27：超时
        :type status: int
        :param compare_num: 总表数。
        :type compare_num: int
        :param compare_end_num: 已完成表数。
        :type compare_end_num: int
        :param data_inconsistent_num: 不一致表数。
        :type data_inconsistent_num: int
        :param uncomparable_num: 无法对比表数。
        :type uncomparable_num: int
        """
        
        

        self._source_db_name = None
        self._target_db_name = None
        self._status = None
        self._compare_num = None
        self._compare_end_num = None
        self._data_inconsistent_num = None
        self._uncomparable_num = None
        self.discriminator = None

        if source_db_name is not None:
            self.source_db_name = source_db_name
        if target_db_name is not None:
            self.target_db_name = target_db_name
        if status is not None:
            self.status = status
        if compare_num is not None:
            self.compare_num = compare_num
        if compare_end_num is not None:
            self.compare_end_num = compare_end_num
        if data_inconsistent_num is not None:
            self.data_inconsistent_num = data_inconsistent_num
        if uncomparable_num is not None:
            self.uncomparable_num = uncomparable_num

    @property
    def source_db_name(self):
        r"""Gets the source_db_name of this DataCompareOverviewInfo.

        源库库名

        :return: The source_db_name of this DataCompareOverviewInfo.
        :rtype: str
        """
        return self._source_db_name

    @source_db_name.setter
    def source_db_name(self, source_db_name):
        r"""Sets the source_db_name of this DataCompareOverviewInfo.

        源库库名

        :param source_db_name: The source_db_name of this DataCompareOverviewInfo.
        :type source_db_name: str
        """
        self._source_db_name = source_db_name

    @property
    def target_db_name(self):
        r"""Gets the target_db_name of this DataCompareOverviewInfo.

        目标库库名

        :return: The target_db_name of this DataCompareOverviewInfo.
        :rtype: str
        """
        return self._target_db_name

    @target_db_name.setter
    def target_db_name(self, target_db_name):
        r"""Sets the target_db_name of this DataCompareOverviewInfo.

        目标库库名

        :param target_db_name: The target_db_name of this DataCompareOverviewInfo.
        :type target_db_name: str
        """
        self._target_db_name = target_db_name

    @property
    def status(self):
        r"""Gets the status of this DataCompareOverviewInfo.

        对比状态。 - 0：对比不一致 - 2：对比一致 - 3：目标库表不存在 - 4：对比失败 - 5：正在对比中 - 6：等待对比中 - 7：任务已取消 - 8：源库为空 - 9：目标库为空 - 10：源库和目标库都为空 - 11：源表不存在 - 12：目标表不存在 - 13：原表和目标表都不存在 - 14：源数据库连接失败 - 15：目标库数据库连接失败 - 16：源数据库执行SQL超时 - 17：目标数据库执行SQL超时 - 18：源数据库执行SQL错误 - 19：目标数据库执行SQL错误 - 20：源库和目标库都不存在 - 21：源库不存在 - 22：目标库不存在 - 23：行数为亿行，未进行对比 - 27：超时

        :return: The status of this DataCompareOverviewInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DataCompareOverviewInfo.

        对比状态。 - 0：对比不一致 - 2：对比一致 - 3：目标库表不存在 - 4：对比失败 - 5：正在对比中 - 6：等待对比中 - 7：任务已取消 - 8：源库为空 - 9：目标库为空 - 10：源库和目标库都为空 - 11：源表不存在 - 12：目标表不存在 - 13：原表和目标表都不存在 - 14：源数据库连接失败 - 15：目标库数据库连接失败 - 16：源数据库执行SQL超时 - 17：目标数据库执行SQL超时 - 18：源数据库执行SQL错误 - 19：目标数据库执行SQL错误 - 20：源库和目标库都不存在 - 21：源库不存在 - 22：目标库不存在 - 23：行数为亿行，未进行对比 - 27：超时

        :param status: The status of this DataCompareOverviewInfo.
        :type status: int
        """
        self._status = status

    @property
    def compare_num(self):
        r"""Gets the compare_num of this DataCompareOverviewInfo.

        总表数。

        :return: The compare_num of this DataCompareOverviewInfo.
        :rtype: int
        """
        return self._compare_num

    @compare_num.setter
    def compare_num(self, compare_num):
        r"""Sets the compare_num of this DataCompareOverviewInfo.

        总表数。

        :param compare_num: The compare_num of this DataCompareOverviewInfo.
        :type compare_num: int
        """
        self._compare_num = compare_num

    @property
    def compare_end_num(self):
        r"""Gets the compare_end_num of this DataCompareOverviewInfo.

        已完成表数。

        :return: The compare_end_num of this DataCompareOverviewInfo.
        :rtype: int
        """
        return self._compare_end_num

    @compare_end_num.setter
    def compare_end_num(self, compare_end_num):
        r"""Sets the compare_end_num of this DataCompareOverviewInfo.

        已完成表数。

        :param compare_end_num: The compare_end_num of this DataCompareOverviewInfo.
        :type compare_end_num: int
        """
        self._compare_end_num = compare_end_num

    @property
    def data_inconsistent_num(self):
        r"""Gets the data_inconsistent_num of this DataCompareOverviewInfo.

        不一致表数。

        :return: The data_inconsistent_num of this DataCompareOverviewInfo.
        :rtype: int
        """
        return self._data_inconsistent_num

    @data_inconsistent_num.setter
    def data_inconsistent_num(self, data_inconsistent_num):
        r"""Sets the data_inconsistent_num of this DataCompareOverviewInfo.

        不一致表数。

        :param data_inconsistent_num: The data_inconsistent_num of this DataCompareOverviewInfo.
        :type data_inconsistent_num: int
        """
        self._data_inconsistent_num = data_inconsistent_num

    @property
    def uncomparable_num(self):
        r"""Gets the uncomparable_num of this DataCompareOverviewInfo.

        无法对比表数。

        :return: The uncomparable_num of this DataCompareOverviewInfo.
        :rtype: int
        """
        return self._uncomparable_num

    @uncomparable_num.setter
    def uncomparable_num(self, uncomparable_num):
        r"""Sets the uncomparable_num of this DataCompareOverviewInfo.

        无法对比表数。

        :param uncomparable_num: The uncomparable_num of this DataCompareOverviewInfo.
        :type uncomparable_num: int
        """
        self._uncomparable_num = uncomparable_num

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
        if not isinstance(other, DataCompareOverviewInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
