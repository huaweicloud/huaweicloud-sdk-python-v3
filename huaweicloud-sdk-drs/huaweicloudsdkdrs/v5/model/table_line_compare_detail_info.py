# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableLineCompareDetailInfo:

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
        'source_row_num': 'str',
        'target_table_name': 'str',
        'target_row_num': 'str',
        'difference_row_num': 'str',
        'status': 'str',
        'message': 'str'
    }

    attribute_map = {
        'source_table_name': 'source_table_name',
        'source_row_num': 'source_row_num',
        'target_table_name': 'target_table_name',
        'target_row_num': 'target_row_num',
        'difference_row_num': 'difference_row_num',
        'status': 'status',
        'message': 'message'
    }

    def __init__(self, source_table_name=None, source_row_num=None, target_table_name=None, target_row_num=None, difference_row_num=None, status=None, message=None):
        r"""TableLineCompareDetailInfo

        The model defined in huaweicloud sdk

        :param source_table_name: 源库表名称。
        :type source_table_name: str
        :param source_row_num: 源库表行数。
        :type source_row_num: str
        :param target_table_name: 目标库表名称。
        :type target_table_name: str
        :param target_row_num: 目标库表行数。
        :type target_row_num: str
        :param difference_row_num: 差异值。
        :type difference_row_num: str
        :param status: 对比结果。取值： - CONSISTENT：一致。 - INCONSISTENT：不一致。 - COMPARING：正在对比。 - WAITING_FOR_COMPARISON：等待对比。 - FAILED_TO_COMPARE：对比失败。 - TARGET_DB_NOT_EXIST：目标库不存在。 - CAN_NOT_COMPARE：无法对比。
        :type status: str
        :param message: 信息。
        :type message: str
        """
        
        

        self._source_table_name = None
        self._source_row_num = None
        self._target_table_name = None
        self._target_row_num = None
        self._difference_row_num = None
        self._status = None
        self._message = None
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
        if message is not None:
            self.message = message

    @property
    def source_table_name(self):
        r"""Gets the source_table_name of this TableLineCompareDetailInfo.

        源库表名称。

        :return: The source_table_name of this TableLineCompareDetailInfo.
        :rtype: str
        """
        return self._source_table_name

    @source_table_name.setter
    def source_table_name(self, source_table_name):
        r"""Sets the source_table_name of this TableLineCompareDetailInfo.

        源库表名称。

        :param source_table_name: The source_table_name of this TableLineCompareDetailInfo.
        :type source_table_name: str
        """
        self._source_table_name = source_table_name

    @property
    def source_row_num(self):
        r"""Gets the source_row_num of this TableLineCompareDetailInfo.

        源库表行数。

        :return: The source_row_num of this TableLineCompareDetailInfo.
        :rtype: str
        """
        return self._source_row_num

    @source_row_num.setter
    def source_row_num(self, source_row_num):
        r"""Sets the source_row_num of this TableLineCompareDetailInfo.

        源库表行数。

        :param source_row_num: The source_row_num of this TableLineCompareDetailInfo.
        :type source_row_num: str
        """
        self._source_row_num = source_row_num

    @property
    def target_table_name(self):
        r"""Gets the target_table_name of this TableLineCompareDetailInfo.

        目标库表名称。

        :return: The target_table_name of this TableLineCompareDetailInfo.
        :rtype: str
        """
        return self._target_table_name

    @target_table_name.setter
    def target_table_name(self, target_table_name):
        r"""Sets the target_table_name of this TableLineCompareDetailInfo.

        目标库表名称。

        :param target_table_name: The target_table_name of this TableLineCompareDetailInfo.
        :type target_table_name: str
        """
        self._target_table_name = target_table_name

    @property
    def target_row_num(self):
        r"""Gets the target_row_num of this TableLineCompareDetailInfo.

        目标库表行数。

        :return: The target_row_num of this TableLineCompareDetailInfo.
        :rtype: str
        """
        return self._target_row_num

    @target_row_num.setter
    def target_row_num(self, target_row_num):
        r"""Sets the target_row_num of this TableLineCompareDetailInfo.

        目标库表行数。

        :param target_row_num: The target_row_num of this TableLineCompareDetailInfo.
        :type target_row_num: str
        """
        self._target_row_num = target_row_num

    @property
    def difference_row_num(self):
        r"""Gets the difference_row_num of this TableLineCompareDetailInfo.

        差异值。

        :return: The difference_row_num of this TableLineCompareDetailInfo.
        :rtype: str
        """
        return self._difference_row_num

    @difference_row_num.setter
    def difference_row_num(self, difference_row_num):
        r"""Sets the difference_row_num of this TableLineCompareDetailInfo.

        差异值。

        :param difference_row_num: The difference_row_num of this TableLineCompareDetailInfo.
        :type difference_row_num: str
        """
        self._difference_row_num = difference_row_num

    @property
    def status(self):
        r"""Gets the status of this TableLineCompareDetailInfo.

        对比结果。取值： - CONSISTENT：一致。 - INCONSISTENT：不一致。 - COMPARING：正在对比。 - WAITING_FOR_COMPARISON：等待对比。 - FAILED_TO_COMPARE：对比失败。 - TARGET_DB_NOT_EXIST：目标库不存在。 - CAN_NOT_COMPARE：无法对比。

        :return: The status of this TableLineCompareDetailInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TableLineCompareDetailInfo.

        对比结果。取值： - CONSISTENT：一致。 - INCONSISTENT：不一致。 - COMPARING：正在对比。 - WAITING_FOR_COMPARISON：等待对比。 - FAILED_TO_COMPARE：对比失败。 - TARGET_DB_NOT_EXIST：目标库不存在。 - CAN_NOT_COMPARE：无法对比。

        :param status: The status of this TableLineCompareDetailInfo.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this TableLineCompareDetailInfo.

        信息。

        :return: The message of this TableLineCompareDetailInfo.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this TableLineCompareDetailInfo.

        信息。

        :param message: The message of this TableLineCompareDetailInfo.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, TableLineCompareDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
