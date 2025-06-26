# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadQueueUser:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'occupy_resource_list': 'list[OccupyResource]',
        'exec_result': 'int',
        'exec_log': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'occupy_resource_list': 'occupy_resource_list',
        'exec_result': 'exec_result',
        'exec_log': 'exec_log'
    }

    def __init__(self, user_name=None, occupy_resource_list=None, exec_result=None, exec_log=None):
        r"""WorkloadQueueUser

        The model defined in huaweicloud sdk

        :param user_name: **参数解释**： 用户名。 **取值范围**： 不涉及。
        :type user_name: str
        :param occupy_resource_list: **参数解释**： 执行计划阶段。 **取值范围**： 不涉及。
        :type occupy_resource_list: list[:class:`huaweicloudsdkdws.v2.OccupyResource`]
        :param exec_result: **参数解释**： 执行结果。 **取值范围**： 不涉及。
        :type exec_result: int
        :param exec_log: **参数解释**： 执行日志。 **取值范围**： 不涉及。
        :type exec_log: str
        """
        
        

        self._user_name = None
        self._occupy_resource_list = None
        self._exec_result = None
        self._exec_log = None
        self.discriminator = None

        self.user_name = user_name
        self.occupy_resource_list = occupy_resource_list
        if exec_result is not None:
            self.exec_result = exec_result
        if exec_log is not None:
            self.exec_log = exec_log

    @property
    def user_name(self):
        r"""Gets the user_name of this WorkloadQueueUser.

        **参数解释**： 用户名。 **取值范围**： 不涉及。

        :return: The user_name of this WorkloadQueueUser.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this WorkloadQueueUser.

        **参数解释**： 用户名。 **取值范围**： 不涉及。

        :param user_name: The user_name of this WorkloadQueueUser.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def occupy_resource_list(self):
        r"""Gets the occupy_resource_list of this WorkloadQueueUser.

        **参数解释**： 执行计划阶段。 **取值范围**： 不涉及。

        :return: The occupy_resource_list of this WorkloadQueueUser.
        :rtype: list[:class:`huaweicloudsdkdws.v2.OccupyResource`]
        """
        return self._occupy_resource_list

    @occupy_resource_list.setter
    def occupy_resource_list(self, occupy_resource_list):
        r"""Sets the occupy_resource_list of this WorkloadQueueUser.

        **参数解释**： 执行计划阶段。 **取值范围**： 不涉及。

        :param occupy_resource_list: The occupy_resource_list of this WorkloadQueueUser.
        :type occupy_resource_list: list[:class:`huaweicloudsdkdws.v2.OccupyResource`]
        """
        self._occupy_resource_list = occupy_resource_list

    @property
    def exec_result(self):
        r"""Gets the exec_result of this WorkloadQueueUser.

        **参数解释**： 执行结果。 **取值范围**： 不涉及。

        :return: The exec_result of this WorkloadQueueUser.
        :rtype: int
        """
        return self._exec_result

    @exec_result.setter
    def exec_result(self, exec_result):
        r"""Sets the exec_result of this WorkloadQueueUser.

        **参数解释**： 执行结果。 **取值范围**： 不涉及。

        :param exec_result: The exec_result of this WorkloadQueueUser.
        :type exec_result: int
        """
        self._exec_result = exec_result

    @property
    def exec_log(self):
        r"""Gets the exec_log of this WorkloadQueueUser.

        **参数解释**： 执行日志。 **取值范围**： 不涉及。

        :return: The exec_log of this WorkloadQueueUser.
        :rtype: str
        """
        return self._exec_log

    @exec_log.setter
    def exec_log(self, exec_log):
        r"""Sets the exec_log of this WorkloadQueueUser.

        **参数解释**： 执行日志。 **取值范围**： 不涉及。

        :param exec_log: The exec_log of this WorkloadQueueUser.
        :type exec_log: str
        """
        self._exec_log = exec_log

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
        if not isinstance(other, WorkloadQueueUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
