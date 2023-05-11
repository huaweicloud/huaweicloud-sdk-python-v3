# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyExecutionPlanRequest:

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
        'body': 'ApplyExecutionPlanRequestBody'
    }

    attribute_map = {
        'client_request_id': 'Client-Request-Id',
        'stack_name': 'stack_name',
        'execution_plan_name': 'execution_plan_name',
        'body': 'body'
    }

    def __init__(self, client_request_id=None, stack_name=None, execution_plan_name=None, body=None):
        """ApplyExecutionPlanRequest

        The model defined in huaweicloud sdk

        :param client_request_id: 用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID
        :type client_request_id: str
        :param stack_name: 资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type stack_name: str
        :param execution_plan_name: 执行计划的名称。此名字在domain_id+区域+project_id+stack_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type execution_plan_name: str
        :param body: Body of the ApplyExecutionPlanRequest
        :type body: :class:`huaweicloudsdkaos.v1.ApplyExecutionPlanRequestBody`
        """
        
        

        self._client_request_id = None
        self._stack_name = None
        self._execution_plan_name = None
        self._body = None
        self.discriminator = None

        self.client_request_id = client_request_id
        self.stack_name = stack_name
        self.execution_plan_name = execution_plan_name
        if body is not None:
            self.body = body

    @property
    def client_request_id(self):
        """Gets the client_request_id of this ApplyExecutionPlanRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :return: The client_request_id of this ApplyExecutionPlanRequest.
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        """Sets the client_request_id of this ApplyExecutionPlanRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :param client_request_id: The client_request_id of this ApplyExecutionPlanRequest.
        :type client_request_id: str
        """
        self._client_request_id = client_request_id

    @property
    def stack_name(self):
        """Gets the stack_name of this ApplyExecutionPlanRequest.

        资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The stack_name of this ApplyExecutionPlanRequest.
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        """Sets the stack_name of this ApplyExecutionPlanRequest.

        资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param stack_name: The stack_name of this ApplyExecutionPlanRequest.
        :type stack_name: str
        """
        self._stack_name = stack_name

    @property
    def execution_plan_name(self):
        """Gets the execution_plan_name of this ApplyExecutionPlanRequest.

        执行计划的名称。此名字在domain_id+区域+project_id+stack_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The execution_plan_name of this ApplyExecutionPlanRequest.
        :rtype: str
        """
        return self._execution_plan_name

    @execution_plan_name.setter
    def execution_plan_name(self, execution_plan_name):
        """Sets the execution_plan_name of this ApplyExecutionPlanRequest.

        执行计划的名称。此名字在domain_id+区域+project_id+stack_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param execution_plan_name: The execution_plan_name of this ApplyExecutionPlanRequest.
        :type execution_plan_name: str
        """
        self._execution_plan_name = execution_plan_name

    @property
    def body(self):
        """Gets the body of this ApplyExecutionPlanRequest.

        :return: The body of this ApplyExecutionPlanRequest.
        :rtype: :class:`huaweicloudsdkaos.v1.ApplyExecutionPlanRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ApplyExecutionPlanRequest.

        :param body: The body of this ApplyExecutionPlanRequest.
        :type body: :class:`huaweicloudsdkaos.v1.ApplyExecutionPlanRequestBody`
        """
        self._body = body

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
        if not isinstance(other, ApplyExecutionPlanRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
