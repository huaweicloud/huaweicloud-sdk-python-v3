# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberCheckJobInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'result': 'MemberCheckJobResult',
        'created_at': 'str',
        'updated_at': 'str',
        'job_id': 'str',
        'check_item_total_num': 'int',
        'check_item_finished_num': 'int',
        'listener_id': 'str',
        'member_id': 'str'
    }

    attribute_map = {
        'status': 'status',
        'result': 'result',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'job_id': 'job_id',
        'check_item_total_num': 'check_item_total_num',
        'check_item_finished_num': 'check_item_finished_num',
        'listener_id': 'listener_id',
        'member_id': 'member_id'
    }

    def __init__(self, status=None, result=None, created_at=None, updated_at=None, job_id=None, check_item_total_num=None, check_item_finished_num=None, listener_id=None, member_id=None):
        r"""MemberCheckJobInfo

        The model defined in huaweicloud sdk

        :param status: **参数解释**：processed检查完成，processing检查中，failed检查失败。  **取值范围**：不涉及
        :type status: str
        :param result: 
        :type result: :class:`huaweicloudsdkelb.v3.MemberCheckJobResult`
        :param created_at: **参数解释**：任务创建时间。  **取值范围**：不涉及
        :type created_at: str
        :param updated_at: **参数解释**：任务更新时间。  **取值范围**：不涉及
        :type updated_at: str
        :param job_id: **参数解释**：任务ID。
        :type job_id: str
        :param check_item_total_num: **参数解释**：检查项总个数。  **取值范围**：不涉及
        :type check_item_total_num: int
        :param check_item_finished_num: **参数解释**：已检查完成的检查项个数。  **取值范围**：不涉及
        :type check_item_finished_num: int
        :param listener_id: **参数解释**：后端服务器所关联的监听器，查询在该监听器下后端服务器的状态。  **取值范围**：不涉及
        :type listener_id: str
        :param member_id: **参数解释**：后端服务器ID。  **取值范围**：不涉及
        :type member_id: str
        """
        
        

        self._status = None
        self._result = None
        self._created_at = None
        self._updated_at = None
        self._job_id = None
        self._check_item_total_num = None
        self._check_item_finished_num = None
        self._listener_id = None
        self._member_id = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if result is not None:
            self.result = result
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if job_id is not None:
            self.job_id = job_id
        if check_item_total_num is not None:
            self.check_item_total_num = check_item_total_num
        if check_item_finished_num is not None:
            self.check_item_finished_num = check_item_finished_num
        if listener_id is not None:
            self.listener_id = listener_id
        if member_id is not None:
            self.member_id = member_id

    @property
    def status(self):
        r"""Gets the status of this MemberCheckJobInfo.

        **参数解释**：processed检查完成，processing检查中，failed检查失败。  **取值范围**：不涉及

        :return: The status of this MemberCheckJobInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this MemberCheckJobInfo.

        **参数解释**：processed检查完成，processing检查中，failed检查失败。  **取值范围**：不涉及

        :param status: The status of this MemberCheckJobInfo.
        :type status: str
        """
        self._status = status

    @property
    def result(self):
        r"""Gets the result of this MemberCheckJobInfo.

        :return: The result of this MemberCheckJobInfo.
        :rtype: :class:`huaweicloudsdkelb.v3.MemberCheckJobResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this MemberCheckJobInfo.

        :param result: The result of this MemberCheckJobInfo.
        :type result: :class:`huaweicloudsdkelb.v3.MemberCheckJobResult`
        """
        self._result = result

    @property
    def created_at(self):
        r"""Gets the created_at of this MemberCheckJobInfo.

        **参数解释**：任务创建时间。  **取值范围**：不涉及

        :return: The created_at of this MemberCheckJobInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this MemberCheckJobInfo.

        **参数解释**：任务创建时间。  **取值范围**：不涉及

        :param created_at: The created_at of this MemberCheckJobInfo.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this MemberCheckJobInfo.

        **参数解释**：任务更新时间。  **取值范围**：不涉及

        :return: The updated_at of this MemberCheckJobInfo.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this MemberCheckJobInfo.

        **参数解释**：任务更新时间。  **取值范围**：不涉及

        :param updated_at: The updated_at of this MemberCheckJobInfo.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def job_id(self):
        r"""Gets the job_id of this MemberCheckJobInfo.

        **参数解释**：任务ID。

        :return: The job_id of this MemberCheckJobInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this MemberCheckJobInfo.

        **参数解释**：任务ID。

        :param job_id: The job_id of this MemberCheckJobInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def check_item_total_num(self):
        r"""Gets the check_item_total_num of this MemberCheckJobInfo.

        **参数解释**：检查项总个数。  **取值范围**：不涉及

        :return: The check_item_total_num of this MemberCheckJobInfo.
        :rtype: int
        """
        return self._check_item_total_num

    @check_item_total_num.setter
    def check_item_total_num(self, check_item_total_num):
        r"""Sets the check_item_total_num of this MemberCheckJobInfo.

        **参数解释**：检查项总个数。  **取值范围**：不涉及

        :param check_item_total_num: The check_item_total_num of this MemberCheckJobInfo.
        :type check_item_total_num: int
        """
        self._check_item_total_num = check_item_total_num

    @property
    def check_item_finished_num(self):
        r"""Gets the check_item_finished_num of this MemberCheckJobInfo.

        **参数解释**：已检查完成的检查项个数。  **取值范围**：不涉及

        :return: The check_item_finished_num of this MemberCheckJobInfo.
        :rtype: int
        """
        return self._check_item_finished_num

    @check_item_finished_num.setter
    def check_item_finished_num(self, check_item_finished_num):
        r"""Sets the check_item_finished_num of this MemberCheckJobInfo.

        **参数解释**：已检查完成的检查项个数。  **取值范围**：不涉及

        :param check_item_finished_num: The check_item_finished_num of this MemberCheckJobInfo.
        :type check_item_finished_num: int
        """
        self._check_item_finished_num = check_item_finished_num

    @property
    def listener_id(self):
        r"""Gets the listener_id of this MemberCheckJobInfo.

        **参数解释**：后端服务器所关联的监听器，查询在该监听器下后端服务器的状态。  **取值范围**：不涉及

        :return: The listener_id of this MemberCheckJobInfo.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        r"""Sets the listener_id of this MemberCheckJobInfo.

        **参数解释**：后端服务器所关联的监听器，查询在该监听器下后端服务器的状态。  **取值范围**：不涉及

        :param listener_id: The listener_id of this MemberCheckJobInfo.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def member_id(self):
        r"""Gets the member_id of this MemberCheckJobInfo.

        **参数解释**：后端服务器ID。  **取值范围**：不涉及

        :return: The member_id of this MemberCheckJobInfo.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        r"""Sets the member_id of this MemberCheckJobInfo.

        **参数解释**：后端服务器ID。  **取值范围**：不涉及

        :param member_id: The member_id of this MemberCheckJobInfo.
        :type member_id: str
        """
        self._member_id = member_id

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
        if not isinstance(other, MemberCheckJobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
