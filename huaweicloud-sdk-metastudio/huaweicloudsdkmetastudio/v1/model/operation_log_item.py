# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperationLogItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'int',
        'action': 'str',
        'operator': 'str',
        'external_info': 'OpExternalInfo'
    }

    attribute_map = {
        'time': 'time',
        'action': 'action',
        'operator': 'operator',
        'external_info': 'external_info'
    }

    def __init__(self, time=None, action=None, operator=None, external_info=None):
        r"""OperationLogItem

        The model defined in huaweicloud sdk

        :param time: 操作时间
        :type time: int
        :param action: 操作名称,当前已有的action为CREATE_JOB(创建任务),COMMIT_JOB(提交任务),SYSTEM_AUDIT_PASS(系统审核通过),ADMIN_AUDIT_PASS(管理员审核通过),AUDIT_NOT_PASS(审核未通过),TRAINING_FINISH(训练完成),UPLOADING_MODEL(上传语音模型),COMPLETE_JOB(任务完成)
        :type action: str
        :param operator: 操作者,USER(用户),ADMIN(管理员),SYSTEM(用户)
        :type operator: str
        :param external_info: 
        :type external_info: :class:`huaweicloudsdkmetastudio.v1.OpExternalInfo`
        """
        
        

        self._time = None
        self._action = None
        self._operator = None
        self._external_info = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if action is not None:
            self.action = action
        if operator is not None:
            self.operator = operator
        if external_info is not None:
            self.external_info = external_info

    @property
    def time(self):
        r"""Gets the time of this OperationLogItem.

        操作时间

        :return: The time of this OperationLogItem.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this OperationLogItem.

        操作时间

        :param time: The time of this OperationLogItem.
        :type time: int
        """
        self._time = time

    @property
    def action(self):
        r"""Gets the action of this OperationLogItem.

        操作名称,当前已有的action为CREATE_JOB(创建任务),COMMIT_JOB(提交任务),SYSTEM_AUDIT_PASS(系统审核通过),ADMIN_AUDIT_PASS(管理员审核通过),AUDIT_NOT_PASS(审核未通过),TRAINING_FINISH(训练完成),UPLOADING_MODEL(上传语音模型),COMPLETE_JOB(任务完成)

        :return: The action of this OperationLogItem.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this OperationLogItem.

        操作名称,当前已有的action为CREATE_JOB(创建任务),COMMIT_JOB(提交任务),SYSTEM_AUDIT_PASS(系统审核通过),ADMIN_AUDIT_PASS(管理员审核通过),AUDIT_NOT_PASS(审核未通过),TRAINING_FINISH(训练完成),UPLOADING_MODEL(上传语音模型),COMPLETE_JOB(任务完成)

        :param action: The action of this OperationLogItem.
        :type action: str
        """
        self._action = action

    @property
    def operator(self):
        r"""Gets the operator of this OperationLogItem.

        操作者,USER(用户),ADMIN(管理员),SYSTEM(用户)

        :return: The operator of this OperationLogItem.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this OperationLogItem.

        操作者,USER(用户),ADMIN(管理员),SYSTEM(用户)

        :param operator: The operator of this OperationLogItem.
        :type operator: str
        """
        self._operator = operator

    @property
    def external_info(self):
        r"""Gets the external_info of this OperationLogItem.

        :return: The external_info of this OperationLogItem.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.OpExternalInfo`
        """
        return self._external_info

    @external_info.setter
    def external_info(self, external_info):
        r"""Sets the external_info of this OperationLogItem.

        :param external_info: The external_info of this OperationLogItem.
        :type external_info: :class:`huaweicloudsdkmetastudio.v1.OpExternalInfo`
        """
        self._external_info = external_info

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
        if not isinstance(other, OperationLogItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
