# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContentCompareOverviewInfo:

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
        'status': 'str',
        'compare_result': 'bool'
    }

    attribute_map = {
        'source_db': 'source_db',
        'target_db': 'target_db',
        'status': 'status',
        'compare_result': 'compare_result'
    }

    def __init__(self, source_db=None, target_db=None, status=None, compare_result=None):
        """ContentCompareOverviewInfo

        The model defined in huaweicloud sdk

        :param source_db: 源库库名。
        :type source_db: str
        :param target_db: 目标库库名。
        :type target_db: str
        :param status: 对比结果。取值： - CONSISTENT：一致。 - INCONSISTENT：不一致。 - COMPARING：正在对比。 - WAITING_FOR_COMPARISON：等待对比。 - FAILED_TO_COMPARE：对比失败。 - TARGET_DB_NOT_EXIST：目标库不存在。 - CAN_NOT_COMPARE：无法对比。
        :type status: str
        :param compare_result: 对比结果。
        :type compare_result: bool
        """
        
        

        self._source_db = None
        self._target_db = None
        self._status = None
        self._compare_result = None
        self.discriminator = None

        if source_db is not None:
            self.source_db = source_db
        if target_db is not None:
            self.target_db = target_db
        if status is not None:
            self.status = status
        if compare_result is not None:
            self.compare_result = compare_result

    @property
    def source_db(self):
        """Gets the source_db of this ContentCompareOverviewInfo.

        源库库名。

        :return: The source_db of this ContentCompareOverviewInfo.
        :rtype: str
        """
        return self._source_db

    @source_db.setter
    def source_db(self, source_db):
        """Sets the source_db of this ContentCompareOverviewInfo.

        源库库名。

        :param source_db: The source_db of this ContentCompareOverviewInfo.
        :type source_db: str
        """
        self._source_db = source_db

    @property
    def target_db(self):
        """Gets the target_db of this ContentCompareOverviewInfo.

        目标库库名。

        :return: The target_db of this ContentCompareOverviewInfo.
        :rtype: str
        """
        return self._target_db

    @target_db.setter
    def target_db(self, target_db):
        """Sets the target_db of this ContentCompareOverviewInfo.

        目标库库名。

        :param target_db: The target_db of this ContentCompareOverviewInfo.
        :type target_db: str
        """
        self._target_db = target_db

    @property
    def status(self):
        """Gets the status of this ContentCompareOverviewInfo.

        对比结果。取值： - CONSISTENT：一致。 - INCONSISTENT：不一致。 - COMPARING：正在对比。 - WAITING_FOR_COMPARISON：等待对比。 - FAILED_TO_COMPARE：对比失败。 - TARGET_DB_NOT_EXIST：目标库不存在。 - CAN_NOT_COMPARE：无法对比。

        :return: The status of this ContentCompareOverviewInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ContentCompareOverviewInfo.

        对比结果。取值： - CONSISTENT：一致。 - INCONSISTENT：不一致。 - COMPARING：正在对比。 - WAITING_FOR_COMPARISON：等待对比。 - FAILED_TO_COMPARE：对比失败。 - TARGET_DB_NOT_EXIST：目标库不存在。 - CAN_NOT_COMPARE：无法对比。

        :param status: The status of this ContentCompareOverviewInfo.
        :type status: str
        """
        self._status = status

    @property
    def compare_result(self):
        """Gets the compare_result of this ContentCompareOverviewInfo.

        对比结果。

        :return: The compare_result of this ContentCompareOverviewInfo.
        :rtype: bool
        """
        return self._compare_result

    @compare_result.setter
    def compare_result(self, compare_result):
        """Sets the compare_result of this ContentCompareOverviewInfo.

        对比结果。

        :param compare_result: The compare_result of this ContentCompareOverviewInfo.
        :type compare_result: bool
        """
        self._compare_result = compare_result

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
        if not isinstance(other, ContentCompareOverviewInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
