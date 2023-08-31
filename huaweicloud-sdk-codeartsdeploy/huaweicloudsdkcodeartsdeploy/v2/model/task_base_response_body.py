# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskBaseResponseBody:

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
        'state': 'str',
        'deploy_system': 'str'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state',
        'deploy_system': 'deploy_system'
    }

    def __init__(self, id=None, state=None, deploy_system=None):
        """TaskBaseResponseBody

        The model defined in huaweicloud sdk

        :param id: 部署任务id
        :type id: str
        :param state: 部署任务状态
        :type state: str
        :param deploy_system: 部署任务类型
        :type deploy_system: str
        """
        
        

        self._id = None
        self._state = None
        self._deploy_system = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if deploy_system is not None:
            self.deploy_system = deploy_system

    @property
    def id(self):
        """Gets the id of this TaskBaseResponseBody.

        部署任务id

        :return: The id of this TaskBaseResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskBaseResponseBody.

        部署任务id

        :param id: The id of this TaskBaseResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def state(self):
        """Gets the state of this TaskBaseResponseBody.

        部署任务状态

        :return: The state of this TaskBaseResponseBody.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TaskBaseResponseBody.

        部署任务状态

        :param state: The state of this TaskBaseResponseBody.
        :type state: str
        """
        self._state = state

    @property
    def deploy_system(self):
        """Gets the deploy_system of this TaskBaseResponseBody.

        部署任务类型

        :return: The deploy_system of this TaskBaseResponseBody.
        :rtype: str
        """
        return self._deploy_system

    @deploy_system.setter
    def deploy_system(self, deploy_system):
        """Sets the deploy_system of this TaskBaseResponseBody.

        部署任务类型

        :param deploy_system: The deploy_system of this TaskBaseResponseBody.
        :type deploy_system: str
        """
        self._deploy_system = deploy_system

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
        if not isinstance(other, TaskBaseResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
