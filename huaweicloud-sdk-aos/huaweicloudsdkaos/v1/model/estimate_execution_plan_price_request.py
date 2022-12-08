# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EstimateExecutionPlanPriceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_request_id': 'str',
        'stack_name': 'str',
        'execution_plan_name': 'str',
        'stack_id': 'str',
        'execution_plan_id': 'str'
    }

    attribute_map = {
        'client_request_id': 'Client-Request-Id',
        'stack_name': 'stack_name',
        'execution_plan_name': 'execution_plan_name',
        'stack_id': 'stack_id',
        'execution_plan_id': 'execution_plan_id'
    }

    def __init__(self, client_request_id=None, stack_name=None, execution_plan_name=None, stack_id=None, execution_plan_id=None):
        """EstimateExecutionPlanPriceRequest

        The model defined in huaweicloud sdk

        :param client_request_id: 用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID
        :type client_request_id: str
        :param stack_name: 用户希望操作的资源栈名
        :type stack_name: str
        :param execution_plan_name: 执行计划的名字。
        :type execution_plan_name: str
        :param stack_id: 用户希望描述的栈的Id。若stack_name和stack_id同时存在，则资源编排服务会检查是否两个匹配，否则返回400
        :type stack_id: str
        :param execution_plan_id: 执行计划ID(uuid)
        :type execution_plan_id: str
        """
        
        

        self._client_request_id = None
        self._stack_name = None
        self._execution_plan_name = None
        self._stack_id = None
        self._execution_plan_id = None
        self.discriminator = None

        self.client_request_id = client_request_id
        self.stack_name = stack_name
        self.execution_plan_name = execution_plan_name
        if stack_id is not None:
            self.stack_id = stack_id
        if execution_plan_id is not None:
            self.execution_plan_id = execution_plan_id

    @property
    def client_request_id(self):
        """Gets the client_request_id of this EstimateExecutionPlanPriceRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :return: The client_request_id of this EstimateExecutionPlanPriceRequest.
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        """Sets the client_request_id of this EstimateExecutionPlanPriceRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :param client_request_id: The client_request_id of this EstimateExecutionPlanPriceRequest.
        :type client_request_id: str
        """
        self._client_request_id = client_request_id

    @property
    def stack_name(self):
        """Gets the stack_name of this EstimateExecutionPlanPriceRequest.

        用户希望操作的资源栈名

        :return: The stack_name of this EstimateExecutionPlanPriceRequest.
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        """Sets the stack_name of this EstimateExecutionPlanPriceRequest.

        用户希望操作的资源栈名

        :param stack_name: The stack_name of this EstimateExecutionPlanPriceRequest.
        :type stack_name: str
        """
        self._stack_name = stack_name

    @property
    def execution_plan_name(self):
        """Gets the execution_plan_name of this EstimateExecutionPlanPriceRequest.

        执行计划的名字。

        :return: The execution_plan_name of this EstimateExecutionPlanPriceRequest.
        :rtype: str
        """
        return self._execution_plan_name

    @execution_plan_name.setter
    def execution_plan_name(self, execution_plan_name):
        """Sets the execution_plan_name of this EstimateExecutionPlanPriceRequest.

        执行计划的名字。

        :param execution_plan_name: The execution_plan_name of this EstimateExecutionPlanPriceRequest.
        :type execution_plan_name: str
        """
        self._execution_plan_name = execution_plan_name

    @property
    def stack_id(self):
        """Gets the stack_id of this EstimateExecutionPlanPriceRequest.

        用户希望描述的栈的Id。若stack_name和stack_id同时存在，则资源编排服务会检查是否两个匹配，否则返回400

        :return: The stack_id of this EstimateExecutionPlanPriceRequest.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this EstimateExecutionPlanPriceRequest.

        用户希望描述的栈的Id。若stack_name和stack_id同时存在，则资源编排服务会检查是否两个匹配，否则返回400

        :param stack_id: The stack_id of this EstimateExecutionPlanPriceRequest.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def execution_plan_id(self):
        """Gets the execution_plan_id of this EstimateExecutionPlanPriceRequest.

        执行计划ID(uuid)

        :return: The execution_plan_id of this EstimateExecutionPlanPriceRequest.
        :rtype: str
        """
        return self._execution_plan_id

    @execution_plan_id.setter
    def execution_plan_id(self, execution_plan_id):
        """Sets the execution_plan_id of this EstimateExecutionPlanPriceRequest.

        执行计划ID(uuid)

        :param execution_plan_id: The execution_plan_id of this EstimateExecutionPlanPriceRequest.
        :type execution_plan_id: str
        """
        self._execution_plan_id = execution_plan_id

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
        if not isinstance(other, EstimateExecutionPlanPriceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
