# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CocUpdateChangeRequestBodyV2SubTickets:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ticket_id': 'str',
        'change_result': 'str',
        'is_verified_in_change_time': 'bool',
        'verified_docs': 'str',
        'comment': 'str',
        'change_fail_type': 'str',
        'rollback_start_time': 'int',
        'rollback_end_time': 'int',
        'is_rollback_success': 'bool',
        'is_monitor_found': 'bool'
    }

    attribute_map = {
        'ticket_id': 'ticket_id',
        'change_result': 'change_result',
        'is_verified_in_change_time': 'is_verified_in_change_time',
        'verified_docs': 'verified_docs',
        'comment': 'comment',
        'change_fail_type': 'change_fail_type',
        'rollback_start_time': 'rollback_start_time',
        'rollback_end_time': 'rollback_end_time',
        'is_rollback_success': 'is_rollback_success',
        'is_monitor_found': 'is_monitor_found'
    }

    def __init__(self, ticket_id=None, change_result=None, is_verified_in_change_time=None, verified_docs=None, comment=None, change_fail_type=None, rollback_start_time=None, rollback_end_time=None, is_rollback_success=None, is_monitor_found=None):
        r"""CocUpdateChangeRequestBodyV2SubTickets

        The model defined in huaweicloud sdk

        :param ticket_id: 子单ID
        :type ticket_id: str
        :param change_result: 变更结果
        :type change_result: str
        :param is_verified_in_change_time: 在时间窗内是否可验证
        :type is_verified_in_change_time: bool
        :param verified_docs: 文档ID
        :type verified_docs: str
        :param comment: 失败原因描述
        :type comment: str
        :param change_fail_type: 变更失败类型
        :type change_fail_type: str
        :param rollback_start_time: 回退开始时间
        :type rollback_start_time: int
        :param rollback_end_time: 回退结束时间
        :type rollback_end_time: int
        :param is_rollback_success: 是否回退成功
        :type is_rollback_success: bool
        :param is_monitor_found: 是否监控发现
        :type is_monitor_found: bool
        """
        
        

        self._ticket_id = None
        self._change_result = None
        self._is_verified_in_change_time = None
        self._verified_docs = None
        self._comment = None
        self._change_fail_type = None
        self._rollback_start_time = None
        self._rollback_end_time = None
        self._is_rollback_success = None
        self._is_monitor_found = None
        self.discriminator = None

        if ticket_id is not None:
            self.ticket_id = ticket_id
        if change_result is not None:
            self.change_result = change_result
        if is_verified_in_change_time is not None:
            self.is_verified_in_change_time = is_verified_in_change_time
        if verified_docs is not None:
            self.verified_docs = verified_docs
        if comment is not None:
            self.comment = comment
        if change_fail_type is not None:
            self.change_fail_type = change_fail_type
        if rollback_start_time is not None:
            self.rollback_start_time = rollback_start_time
        if rollback_end_time is not None:
            self.rollback_end_time = rollback_end_time
        if is_rollback_success is not None:
            self.is_rollback_success = is_rollback_success
        if is_monitor_found is not None:
            self.is_monitor_found = is_monitor_found

    @property
    def ticket_id(self):
        r"""Gets the ticket_id of this CocUpdateChangeRequestBodyV2SubTickets.

        子单ID

        :return: The ticket_id of this CocUpdateChangeRequestBodyV2SubTickets.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        r"""Sets the ticket_id of this CocUpdateChangeRequestBodyV2SubTickets.

        子单ID

        :param ticket_id: The ticket_id of this CocUpdateChangeRequestBodyV2SubTickets.
        :type ticket_id: str
        """
        self._ticket_id = ticket_id

    @property
    def change_result(self):
        r"""Gets the change_result of this CocUpdateChangeRequestBodyV2SubTickets.

        变更结果

        :return: The change_result of this CocUpdateChangeRequestBodyV2SubTickets.
        :rtype: str
        """
        return self._change_result

    @change_result.setter
    def change_result(self, change_result):
        r"""Sets the change_result of this CocUpdateChangeRequestBodyV2SubTickets.

        变更结果

        :param change_result: The change_result of this CocUpdateChangeRequestBodyV2SubTickets.
        :type change_result: str
        """
        self._change_result = change_result

    @property
    def is_verified_in_change_time(self):
        r"""Gets the is_verified_in_change_time of this CocUpdateChangeRequestBodyV2SubTickets.

        在时间窗内是否可验证

        :return: The is_verified_in_change_time of this CocUpdateChangeRequestBodyV2SubTickets.
        :rtype: bool
        """
        return self._is_verified_in_change_time

    @is_verified_in_change_time.setter
    def is_verified_in_change_time(self, is_verified_in_change_time):
        r"""Sets the is_verified_in_change_time of this CocUpdateChangeRequestBodyV2SubTickets.

        在时间窗内是否可验证

        :param is_verified_in_change_time: The is_verified_in_change_time of this CocUpdateChangeRequestBodyV2SubTickets.
        :type is_verified_in_change_time: bool
        """
        self._is_verified_in_change_time = is_verified_in_change_time

    @property
    def verified_docs(self):
        r"""Gets the verified_docs of this CocUpdateChangeRequestBodyV2SubTickets.

        文档ID

        :return: The verified_docs of this CocUpdateChangeRequestBodyV2SubTickets.
        :rtype: str
        """
        return self._verified_docs

    @verified_docs.setter
    def verified_docs(self, verified_docs):
        r"""Sets the verified_docs of this CocUpdateChangeRequestBodyV2SubTickets.

        文档ID

        :param verified_docs: The verified_docs of this CocUpdateChangeRequestBodyV2SubTickets.
        :type verified_docs: str
        """
        self._verified_docs = verified_docs

    @property
    def comment(self):
        r"""Gets the comment of this CocUpdateChangeRequestBodyV2SubTickets.

        失败原因描述

        :return: The comment of this CocUpdateChangeRequestBodyV2SubTickets.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this CocUpdateChangeRequestBodyV2SubTickets.

        失败原因描述

        :param comment: The comment of this CocUpdateChangeRequestBodyV2SubTickets.
        :type comment: str
        """
        self._comment = comment

    @property
    def change_fail_type(self):
        r"""Gets the change_fail_type of this CocUpdateChangeRequestBodyV2SubTickets.

        变更失败类型

        :return: The change_fail_type of this CocUpdateChangeRequestBodyV2SubTickets.
        :rtype: str
        """
        return self._change_fail_type

    @change_fail_type.setter
    def change_fail_type(self, change_fail_type):
        r"""Sets the change_fail_type of this CocUpdateChangeRequestBodyV2SubTickets.

        变更失败类型

        :param change_fail_type: The change_fail_type of this CocUpdateChangeRequestBodyV2SubTickets.
        :type change_fail_type: str
        """
        self._change_fail_type = change_fail_type

    @property
    def rollback_start_time(self):
        r"""Gets the rollback_start_time of this CocUpdateChangeRequestBodyV2SubTickets.

        回退开始时间

        :return: The rollback_start_time of this CocUpdateChangeRequestBodyV2SubTickets.
        :rtype: int
        """
        return self._rollback_start_time

    @rollback_start_time.setter
    def rollback_start_time(self, rollback_start_time):
        r"""Sets the rollback_start_time of this CocUpdateChangeRequestBodyV2SubTickets.

        回退开始时间

        :param rollback_start_time: The rollback_start_time of this CocUpdateChangeRequestBodyV2SubTickets.
        :type rollback_start_time: int
        """
        self._rollback_start_time = rollback_start_time

    @property
    def rollback_end_time(self):
        r"""Gets the rollback_end_time of this CocUpdateChangeRequestBodyV2SubTickets.

        回退结束时间

        :return: The rollback_end_time of this CocUpdateChangeRequestBodyV2SubTickets.
        :rtype: int
        """
        return self._rollback_end_time

    @rollback_end_time.setter
    def rollback_end_time(self, rollback_end_time):
        r"""Sets the rollback_end_time of this CocUpdateChangeRequestBodyV2SubTickets.

        回退结束时间

        :param rollback_end_time: The rollback_end_time of this CocUpdateChangeRequestBodyV2SubTickets.
        :type rollback_end_time: int
        """
        self._rollback_end_time = rollback_end_time

    @property
    def is_rollback_success(self):
        r"""Gets the is_rollback_success of this CocUpdateChangeRequestBodyV2SubTickets.

        是否回退成功

        :return: The is_rollback_success of this CocUpdateChangeRequestBodyV2SubTickets.
        :rtype: bool
        """
        return self._is_rollback_success

    @is_rollback_success.setter
    def is_rollback_success(self, is_rollback_success):
        r"""Sets the is_rollback_success of this CocUpdateChangeRequestBodyV2SubTickets.

        是否回退成功

        :param is_rollback_success: The is_rollback_success of this CocUpdateChangeRequestBodyV2SubTickets.
        :type is_rollback_success: bool
        """
        self._is_rollback_success = is_rollback_success

    @property
    def is_monitor_found(self):
        r"""Gets the is_monitor_found of this CocUpdateChangeRequestBodyV2SubTickets.

        是否监控发现

        :return: The is_monitor_found of this CocUpdateChangeRequestBodyV2SubTickets.
        :rtype: bool
        """
        return self._is_monitor_found

    @is_monitor_found.setter
    def is_monitor_found(self, is_monitor_found):
        r"""Sets the is_monitor_found of this CocUpdateChangeRequestBodyV2SubTickets.

        是否监控发现

        :param is_monitor_found: The is_monitor_found of this CocUpdateChangeRequestBodyV2SubTickets.
        :type is_monitor_found: bool
        """
        self._is_monitor_found = is_monitor_found

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
        if not isinstance(other, CocUpdateChangeRequestBodyV2SubTickets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
