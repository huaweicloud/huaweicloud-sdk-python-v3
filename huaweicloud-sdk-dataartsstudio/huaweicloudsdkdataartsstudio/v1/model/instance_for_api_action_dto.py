# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceForApiActionDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_type': 'str',
        'name': 'str',
        'action': 'str',
        'result': 'bool',
        'cause': 'str',
        'api_status': 'str',
        'api_debug': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_type': 'instance_type',
        'name': 'name',
        'action': 'action',
        'result': 'result',
        'cause': 'cause',
        'api_status': 'api_status',
        'api_debug': 'api_debug'
    }

    def __init__(self, instance_id=None, instance_type=None, name=None, action=None, result=None, cause=None, api_status=None, api_debug=None):
        """InstanceForApiActionDTO

        The model defined in huaweicloud sdk

        :param instance_id: 集群编号
        :type instance_id: str
        :param instance_type: 集群类型
        :type instance_type: str
        :param name: 集群名称
        :type name: str
        :param action: api操作
        :type action: str
        :param result: 校验结果
        :type result: bool
        :param cause: 校验失败的原因
        :type cause: str
        :param api_status: api状态
        :type api_status: str
        :param api_debug: api调试状态
        :type api_debug: str
        """
        
        

        self._instance_id = None
        self._instance_type = None
        self._name = None
        self._action = None
        self._result = None
        self._cause = None
        self._api_status = None
        self._api_debug = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_type is not None:
            self.instance_type = instance_type
        if name is not None:
            self.name = name
        if action is not None:
            self.action = action
        if result is not None:
            self.result = result
        if cause is not None:
            self.cause = cause
        if api_status is not None:
            self.api_status = api_status
        if api_debug is not None:
            self.api_debug = api_debug

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceForApiActionDTO.

        集群编号

        :return: The instance_id of this InstanceForApiActionDTO.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceForApiActionDTO.

        集群编号

        :param instance_id: The instance_id of this InstanceForApiActionDTO.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_type(self):
        """Gets the instance_type of this InstanceForApiActionDTO.

        集群类型

        :return: The instance_type of this InstanceForApiActionDTO.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this InstanceForApiActionDTO.

        集群类型

        :param instance_type: The instance_type of this InstanceForApiActionDTO.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def name(self):
        """Gets the name of this InstanceForApiActionDTO.

        集群名称

        :return: The name of this InstanceForApiActionDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstanceForApiActionDTO.

        集群名称

        :param name: The name of this InstanceForApiActionDTO.
        :type name: str
        """
        self._name = name

    @property
    def action(self):
        """Gets the action of this InstanceForApiActionDTO.

        api操作

        :return: The action of this InstanceForApiActionDTO.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this InstanceForApiActionDTO.

        api操作

        :param action: The action of this InstanceForApiActionDTO.
        :type action: str
        """
        self._action = action

    @property
    def result(self):
        """Gets the result of this InstanceForApiActionDTO.

        校验结果

        :return: The result of this InstanceForApiActionDTO.
        :rtype: bool
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this InstanceForApiActionDTO.

        校验结果

        :param result: The result of this InstanceForApiActionDTO.
        :type result: bool
        """
        self._result = result

    @property
    def cause(self):
        """Gets the cause of this InstanceForApiActionDTO.

        校验失败的原因

        :return: The cause of this InstanceForApiActionDTO.
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this InstanceForApiActionDTO.

        校验失败的原因

        :param cause: The cause of this InstanceForApiActionDTO.
        :type cause: str
        """
        self._cause = cause

    @property
    def api_status(self):
        """Gets the api_status of this InstanceForApiActionDTO.

        api状态

        :return: The api_status of this InstanceForApiActionDTO.
        :rtype: str
        """
        return self._api_status

    @api_status.setter
    def api_status(self, api_status):
        """Sets the api_status of this InstanceForApiActionDTO.

        api状态

        :param api_status: The api_status of this InstanceForApiActionDTO.
        :type api_status: str
        """
        self._api_status = api_status

    @property
    def api_debug(self):
        """Gets the api_debug of this InstanceForApiActionDTO.

        api调试状态

        :return: The api_debug of this InstanceForApiActionDTO.
        :rtype: str
        """
        return self._api_debug

    @api_debug.setter
    def api_debug(self, api_debug):
        """Sets the api_debug of this InstanceForApiActionDTO.

        api调试状态

        :param api_debug: The api_debug of this InstanceForApiActionDTO.
        :type api_debug: str
        """
        self._api_debug = api_debug

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
        if not isinstance(other, InstanceForApiActionDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
