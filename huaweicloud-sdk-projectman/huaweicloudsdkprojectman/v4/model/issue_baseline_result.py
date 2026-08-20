# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueBaselineResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'modified_by': 'str',
        'baseline': 'str',
        'operation_id': 'str',
        'modified_date': 'str',
        'number': 'str',
        'title': 'str',
        'fail_message': 'str'
    }

    attribute_map = {
        'id': 'id',
        'modified_by': 'modified_by',
        'baseline': 'baseline',
        'operation_id': 'operation_id',
        'modified_date': 'modified_date',
        'number': 'number',
        'title': 'title',
        'fail_message': 'fail_message'
    }

    def __init__(self, id=None, modified_by=None, baseline=None, operation_id=None, modified_date=None, number=None, title=None, fail_message=None):
        r"""IssueBaselineResult

        The model defined in huaweicloud sdk

        :param id: 变更的工作项ID。
        :type id: str
        :param modified_by: 工作项变更人ID。
        :type modified_by: str
        :param baseline: 工作项基线结果。
        :type baseline: str
        :param operation_id: 工作项基线的操作记录ID。
        :type operation_id: str
        :param modified_date: 工作项完成基线的unix时间戳，单位：毫秒。
        :type modified_date: str
        :param number: 基线的工作项编号。 基线失败时返回。
        :type number: str
        :param title: 基线的工作项标题。 基线失败时返回。
        :type title: str
        :param fail_message: 工作项基线失败原因。 基线失败时返回。
        :type fail_message: str
        """
        
        

        self._id = None
        self._modified_by = None
        self._baseline = None
        self._operation_id = None
        self._modified_date = None
        self._number = None
        self._title = None
        self._fail_message = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if modified_by is not None:
            self.modified_by = modified_by
        if baseline is not None:
            self.baseline = baseline
        if operation_id is not None:
            self.operation_id = operation_id
        if modified_date is not None:
            self.modified_date = modified_date
        if number is not None:
            self.number = number
        if title is not None:
            self.title = title
        if fail_message is not None:
            self.fail_message = fail_message

    @property
    def id(self):
        r"""Gets the id of this IssueBaselineResult.

        变更的工作项ID。

        :return: The id of this IssueBaselineResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IssueBaselineResult.

        变更的工作项ID。

        :param id: The id of this IssueBaselineResult.
        :type id: str
        """
        self._id = id

    @property
    def modified_by(self):
        r"""Gets the modified_by of this IssueBaselineResult.

        工作项变更人ID。

        :return: The modified_by of this IssueBaselineResult.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this IssueBaselineResult.

        工作项变更人ID。

        :param modified_by: The modified_by of this IssueBaselineResult.
        :type modified_by: str
        """
        self._modified_by = modified_by

    @property
    def baseline(self):
        r"""Gets the baseline of this IssueBaselineResult.

        工作项基线结果。

        :return: The baseline of this IssueBaselineResult.
        :rtype: str
        """
        return self._baseline

    @baseline.setter
    def baseline(self, baseline):
        r"""Sets the baseline of this IssueBaselineResult.

        工作项基线结果。

        :param baseline: The baseline of this IssueBaselineResult.
        :type baseline: str
        """
        self._baseline = baseline

    @property
    def operation_id(self):
        r"""Gets the operation_id of this IssueBaselineResult.

        工作项基线的操作记录ID。

        :return: The operation_id of this IssueBaselineResult.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        r"""Sets the operation_id of this IssueBaselineResult.

        工作项基线的操作记录ID。

        :param operation_id: The operation_id of this IssueBaselineResult.
        :type operation_id: str
        """
        self._operation_id = operation_id

    @property
    def modified_date(self):
        r"""Gets the modified_date of this IssueBaselineResult.

        工作项完成基线的unix时间戳，单位：毫秒。

        :return: The modified_date of this IssueBaselineResult.
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        r"""Sets the modified_date of this IssueBaselineResult.

        工作项完成基线的unix时间戳，单位：毫秒。

        :param modified_date: The modified_date of this IssueBaselineResult.
        :type modified_date: str
        """
        self._modified_date = modified_date

    @property
    def number(self):
        r"""Gets the number of this IssueBaselineResult.

        基线的工作项编号。 基线失败时返回。

        :return: The number of this IssueBaselineResult.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this IssueBaselineResult.

        基线的工作项编号。 基线失败时返回。

        :param number: The number of this IssueBaselineResult.
        :type number: str
        """
        self._number = number

    @property
    def title(self):
        r"""Gets the title of this IssueBaselineResult.

        基线的工作项标题。 基线失败时返回。

        :return: The title of this IssueBaselineResult.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this IssueBaselineResult.

        基线的工作项标题。 基线失败时返回。

        :param title: The title of this IssueBaselineResult.
        :type title: str
        """
        self._title = title

    @property
    def fail_message(self):
        r"""Gets the fail_message of this IssueBaselineResult.

        工作项基线失败原因。 基线失败时返回。

        :return: The fail_message of this IssueBaselineResult.
        :rtype: str
        """
        return self._fail_message

    @fail_message.setter
    def fail_message(self, fail_message):
        r"""Sets the fail_message of this IssueBaselineResult.

        工作项基线失败原因。 基线失败时返回。

        :param fail_message: The fail_message of this IssueBaselineResult.
        :type fail_message: str
        """
        self._fail_message = fail_message

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
        if not isinstance(other, IssueBaselineResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
