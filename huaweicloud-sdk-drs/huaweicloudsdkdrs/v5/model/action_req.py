# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'action_name': 'str',
        'action_params': 'ActionParams'
    }

    attribute_map = {
        'job_id': 'job_id',
        'action_name': 'action_name',
        'action_params': 'action_params'
    }

    def __init__(self, job_id=None, action_name=None, action_params=None):
        """ActionReq

        The model defined in huaweicloud sdk

        :param job_id: 任务ID (对比任务相关操作，多任务场景传父任务详情返回的master_job_id)，批量操作时必填
        :type job_id: str
        :param action_name: 操作任务动作名称。取值： - network：测试连接源库/目标库。 - precheck：执行预检查。 - start：启动任务。 - stop：暂停任务。 - restart：重试任务。 - reset：重置任务。 - terminate：结束任务。 - skip_precheck：跳过预检查。 - create_compare：创建对比任务。 - cancel_compare：取消对比任务。
        :type action_name: str
        :param action_params: 
        :type action_params: :class:`huaweicloudsdkdrs.v5.ActionParams`
        """
        
        

        self._job_id = None
        self._action_name = None
        self._action_params = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        self.action_name = action_name
        if action_params is not None:
            self.action_params = action_params

    @property
    def job_id(self):
        """Gets the job_id of this ActionReq.

        任务ID (对比任务相关操作，多任务场景传父任务详情返回的master_job_id)，批量操作时必填

        :return: The job_id of this ActionReq.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ActionReq.

        任务ID (对比任务相关操作，多任务场景传父任务详情返回的master_job_id)，批量操作时必填

        :param job_id: The job_id of this ActionReq.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def action_name(self):
        """Gets the action_name of this ActionReq.

        操作任务动作名称。取值： - network：测试连接源库/目标库。 - precheck：执行预检查。 - start：启动任务。 - stop：暂停任务。 - restart：重试任务。 - reset：重置任务。 - terminate：结束任务。 - skip_precheck：跳过预检查。 - create_compare：创建对比任务。 - cancel_compare：取消对比任务。

        :return: The action_name of this ActionReq.
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        """Sets the action_name of this ActionReq.

        操作任务动作名称。取值： - network：测试连接源库/目标库。 - precheck：执行预检查。 - start：启动任务。 - stop：暂停任务。 - restart：重试任务。 - reset：重置任务。 - terminate：结束任务。 - skip_precheck：跳过预检查。 - create_compare：创建对比任务。 - cancel_compare：取消对比任务。

        :param action_name: The action_name of this ActionReq.
        :type action_name: str
        """
        self._action_name = action_name

    @property
    def action_params(self):
        """Gets the action_params of this ActionReq.

        :return: The action_params of this ActionReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.ActionParams`
        """
        return self._action_params

    @action_params.setter
    def action_params(self, action_params):
        """Sets the action_params of this ActionReq.

        :param action_params: The action_params of this ActionReq.
        :type action_params: :class:`huaweicloudsdkdrs.v5.ActionParams`
        """
        self._action_params = action_params

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
        if not isinstance(other, ActionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
