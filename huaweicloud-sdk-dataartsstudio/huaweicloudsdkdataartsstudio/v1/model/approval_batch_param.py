# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApprovalBatchParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'biz_infos': 'list[BizInfoVO]',
        'approver_user_id': 'str',
        'approver_user_name': 'str',
        'email': 'str',
        'fast_approval': 'bool',
        'schedule_time': 'str'
    }

    attribute_map = {
        'biz_infos': 'biz_infos',
        'approver_user_id': 'approver_user_id',
        'approver_user_name': 'approver_user_name',
        'email': 'email',
        'fast_approval': 'fast_approval',
        'schedule_time': 'schedule_time'
    }

    def __init__(self, biz_infos=None, approver_user_id=None, approver_user_name=None, email=None, fast_approval=None, schedule_time=None):
        """ApprovalBatchParam

        The model defined in huaweicloud sdk

        :param biz_infos: 业务信息列表.
        :type biz_infos: list[:class:`huaweicloudsdkdataartsstudio.v1.BizInfoVO`]
        :param approver_user_id: 审批人user id
        :type approver_user_id: str
        :param approver_user_name: 审批人user name
        :type approver_user_name: str
        :param email: 审批人邮箱
        :type email: str
        :param fast_approval: 快速审批, 非正式场景，用于快速上手体验，仅在当前用户有审批权限时提供
        :type fast_approval: bool
        :param schedule_time: 作业调度时间
        :type schedule_time: str
        """
        
        

        self._biz_infos = None
        self._approver_user_id = None
        self._approver_user_name = None
        self._email = None
        self._fast_approval = None
        self._schedule_time = None
        self.discriminator = None

        self.biz_infos = biz_infos
        self.approver_user_id = approver_user_id
        self.approver_user_name = approver_user_name
        if email is not None:
            self.email = email
        if fast_approval is not None:
            self.fast_approval = fast_approval
        if schedule_time is not None:
            self.schedule_time = schedule_time

    @property
    def biz_infos(self):
        """Gets the biz_infos of this ApprovalBatchParam.

        业务信息列表.

        :return: The biz_infos of this ApprovalBatchParam.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.BizInfoVO`]
        """
        return self._biz_infos

    @biz_infos.setter
    def biz_infos(self, biz_infos):
        """Sets the biz_infos of this ApprovalBatchParam.

        业务信息列表.

        :param biz_infos: The biz_infos of this ApprovalBatchParam.
        :type biz_infos: list[:class:`huaweicloudsdkdataartsstudio.v1.BizInfoVO`]
        """
        self._biz_infos = biz_infos

    @property
    def approver_user_id(self):
        """Gets the approver_user_id of this ApprovalBatchParam.

        审批人user id

        :return: The approver_user_id of this ApprovalBatchParam.
        :rtype: str
        """
        return self._approver_user_id

    @approver_user_id.setter
    def approver_user_id(self, approver_user_id):
        """Sets the approver_user_id of this ApprovalBatchParam.

        审批人user id

        :param approver_user_id: The approver_user_id of this ApprovalBatchParam.
        :type approver_user_id: str
        """
        self._approver_user_id = approver_user_id

    @property
    def approver_user_name(self):
        """Gets the approver_user_name of this ApprovalBatchParam.

        审批人user name

        :return: The approver_user_name of this ApprovalBatchParam.
        :rtype: str
        """
        return self._approver_user_name

    @approver_user_name.setter
    def approver_user_name(self, approver_user_name):
        """Sets the approver_user_name of this ApprovalBatchParam.

        审批人user name

        :param approver_user_name: The approver_user_name of this ApprovalBatchParam.
        :type approver_user_name: str
        """
        self._approver_user_name = approver_user_name

    @property
    def email(self):
        """Gets the email of this ApprovalBatchParam.

        审批人邮箱

        :return: The email of this ApprovalBatchParam.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ApprovalBatchParam.

        审批人邮箱

        :param email: The email of this ApprovalBatchParam.
        :type email: str
        """
        self._email = email

    @property
    def fast_approval(self):
        """Gets the fast_approval of this ApprovalBatchParam.

        快速审批, 非正式场景，用于快速上手体验，仅在当前用户有审批权限时提供

        :return: The fast_approval of this ApprovalBatchParam.
        :rtype: bool
        """
        return self._fast_approval

    @fast_approval.setter
    def fast_approval(self, fast_approval):
        """Sets the fast_approval of this ApprovalBatchParam.

        快速审批, 非正式场景，用于快速上手体验，仅在当前用户有审批权限时提供

        :param fast_approval: The fast_approval of this ApprovalBatchParam.
        :type fast_approval: bool
        """
        self._fast_approval = fast_approval

    @property
    def schedule_time(self):
        """Gets the schedule_time of this ApprovalBatchParam.

        作业调度时间

        :return: The schedule_time of this ApprovalBatchParam.
        :rtype: str
        """
        return self._schedule_time

    @schedule_time.setter
    def schedule_time(self, schedule_time):
        """Sets the schedule_time of this ApprovalBatchParam.

        作业调度时间

        :param schedule_time: The schedule_time of this ApprovalBatchParam.
        :type schedule_time: str
        """
        self._schedule_time = schedule_time

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
        if not isinstance(other, ApprovalBatchParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
