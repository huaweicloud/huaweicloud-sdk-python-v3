# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeContentCompareOverviewResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_db': 'str',
        'target_db': 'str',
        'status': 'int'
    }

    attribute_map = {
        'source_db': 'source_db',
        'target_db': 'target_db',
        'status': 'status'
    }

    def __init__(self, source_db=None, target_db=None, status=None):
        """NodeContentCompareOverviewResult

        The model defined in huaweicloud sdk

        :param source_db: 源库名称。
        :type source_db: str
        :param target_db: 目标库名称。
        :type target_db: str
        :param status: 对比状态。 - 0：对比不一致 - 2：对比一致 - 3：目标库表不存在 - 4：对比失败 - 5：正在对比中 - 6：等待对比中 - 7：任务已取消 - 8：源库为空 - 9：目标库为空 - 10：源库和目标库都为空 - 11：源表不存在 - 12：目标表不存在 - 13：原表和目标表都不存在 - 14：源数据库连接失败 - 15：目标库数据库连接失败 - 16：源数据库执行SQL超时 - 17：目标数据库执行SQL超时 - 18：源数据库执行SQL错误 - 19：目标数据库执行SQL错误 - 20：源库和目标库都不存在 - 21：源库不存在 - 22：目标库不存在 - 23：行数为亿行，未进行对比 - 27：超时
        :type status: int
        """
        
        

        self._source_db = None
        self._target_db = None
        self._status = None
        self.discriminator = None

        if source_db is not None:
            self.source_db = source_db
        if target_db is not None:
            self.target_db = target_db
        if status is not None:
            self.status = status

    @property
    def source_db(self):
        """Gets the source_db of this NodeContentCompareOverviewResult.

        源库名称。

        :return: The source_db of this NodeContentCompareOverviewResult.
        :rtype: str
        """
        return self._source_db

    @source_db.setter
    def source_db(self, source_db):
        """Sets the source_db of this NodeContentCompareOverviewResult.

        源库名称。

        :param source_db: The source_db of this NodeContentCompareOverviewResult.
        :type source_db: str
        """
        self._source_db = source_db

    @property
    def target_db(self):
        """Gets the target_db of this NodeContentCompareOverviewResult.

        目标库名称。

        :return: The target_db of this NodeContentCompareOverviewResult.
        :rtype: str
        """
        return self._target_db

    @target_db.setter
    def target_db(self, target_db):
        """Sets the target_db of this NodeContentCompareOverviewResult.

        目标库名称。

        :param target_db: The target_db of this NodeContentCompareOverviewResult.
        :type target_db: str
        """
        self._target_db = target_db

    @property
    def status(self):
        """Gets the status of this NodeContentCompareOverviewResult.

        对比状态。 - 0：对比不一致 - 2：对比一致 - 3：目标库表不存在 - 4：对比失败 - 5：正在对比中 - 6：等待对比中 - 7：任务已取消 - 8：源库为空 - 9：目标库为空 - 10：源库和目标库都为空 - 11：源表不存在 - 12：目标表不存在 - 13：原表和目标表都不存在 - 14：源数据库连接失败 - 15：目标库数据库连接失败 - 16：源数据库执行SQL超时 - 17：目标数据库执行SQL超时 - 18：源数据库执行SQL错误 - 19：目标数据库执行SQL错误 - 20：源库和目标库都不存在 - 21：源库不存在 - 22：目标库不存在 - 23：行数为亿行，未进行对比 - 27：超时

        :return: The status of this NodeContentCompareOverviewResult.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodeContentCompareOverviewResult.

        对比状态。 - 0：对比不一致 - 2：对比一致 - 3：目标库表不存在 - 4：对比失败 - 5：正在对比中 - 6：等待对比中 - 7：任务已取消 - 8：源库为空 - 9：目标库为空 - 10：源库和目标库都为空 - 11：源表不存在 - 12：目标表不存在 - 13：原表和目标表都不存在 - 14：源数据库连接失败 - 15：目标库数据库连接失败 - 16：源数据库执行SQL超时 - 17：目标数据库执行SQL超时 - 18：源数据库执行SQL错误 - 19：目标数据库执行SQL错误 - 20：源库和目标库都不存在 - 21：源库不存在 - 22：目标库不存在 - 23：行数为亿行，未进行对比 - 27：超时

        :param status: The status of this NodeContentCompareOverviewResult.
        :type status: int
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
        if not isinstance(other, NodeContentCompareOverviewResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
