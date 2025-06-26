# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadQueueUserReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queue_name': 'str',
        'user_list': 'list[WorkloadQueueUserReqUserList]'
    }

    attribute_map = {
        'queue_name': 'queue_name',
        'user_list': 'user_list'
    }

    def __init__(self, queue_name=None, user_list=None):
        r"""WorkloadQueueUserReq

        The model defined in huaweicloud sdk

        :param queue_name: **参数解释**： 资源池名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type queue_name: str
        :param user_list: **参数解释**： 资源池用户列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type user_list: list[:class:`huaweicloudsdkdws.v2.WorkloadQueueUserReqUserList`]
        """
        
        

        self._queue_name = None
        self._user_list = None
        self.discriminator = None

        self.queue_name = queue_name
        self.user_list = user_list

    @property
    def queue_name(self):
        r"""Gets the queue_name of this WorkloadQueueUserReq.

        **参数解释**： 资源池名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The queue_name of this WorkloadQueueUserReq.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this WorkloadQueueUserReq.

        **参数解释**： 资源池名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param queue_name: The queue_name of this WorkloadQueueUserReq.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def user_list(self):
        r"""Gets the user_list of this WorkloadQueueUserReq.

        **参数解释**： 资源池用户列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The user_list of this WorkloadQueueUserReq.
        :rtype: list[:class:`huaweicloudsdkdws.v2.WorkloadQueueUserReqUserList`]
        """
        return self._user_list

    @user_list.setter
    def user_list(self, user_list):
        r"""Sets the user_list of this WorkloadQueueUserReq.

        **参数解释**： 资源池用户列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param user_list: The user_list of this WorkloadQueueUserReq.
        :type user_list: list[:class:`huaweicloudsdkdws.v2.WorkloadQueueUserReqUserList`]
        """
        self._user_list = user_list

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
        if not isinstance(other, WorkloadQueueUserReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
