# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWorkflowRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'states': 'list[State]',
        'inputs': 'list[Input]',
        'description': 'str',
        'mode': 'str',
        'express_config': 'ExpressConfig',
        'func_vpc': 'FuncVpc',
        'agency': 'str'
    }

    attribute_map = {
        'states': 'states',
        'inputs': 'inputs',
        'description': 'description',
        'mode': 'mode',
        'express_config': 'express_config',
        'func_vpc': 'func_vpc',
        'agency': 'agency'
    }

    def __init__(self, states=None, inputs=None, description=None, mode=None, express_config=None, func_vpc=None, agency=None):
        """CreateWorkflowRequestBody

        The model defined in huaweicloud sdk

        :param states: 工作流的编排定义,必须有TYPE，TYPE值必须是3种State（DELAY，OPERATION，END）中一种。每个state的名字是1-80长度的只含数字，字母，-和_的String。
        :type states: list[:class:`huaweicloudsdkdwr.v3.State`]
        :param inputs: 工作流中用户可修改的参数项
        :type inputs: list[:class:`huaweicloudsdkdwr.v3.Input`]
        :param description: 工作流的描述
        :type description: str
        :param mode: 工作流执行类型：同步（EXPRESS）、异步（NORMAL）
        :type mode: str
        :param express_config: 
        :type express_config: :class:`huaweicloudsdkdwr.v3.ExpressConfig`
        :param func_vpc: 
        :type func_vpc: :class:`huaweicloudsdkdwr.v3.FuncVpc`
        :param agency: 用戶传入用于创建工作流时使用的委托的委托名
        :type agency: str
        """
        
        

        self._states = None
        self._inputs = None
        self._description = None
        self._mode = None
        self._express_config = None
        self._func_vpc = None
        self._agency = None
        self.discriminator = None

        if states is not None:
            self.states = states
        if inputs is not None:
            self.inputs = inputs
        if description is not None:
            self.description = description
        if mode is not None:
            self.mode = mode
        if express_config is not None:
            self.express_config = express_config
        if func_vpc is not None:
            self.func_vpc = func_vpc
        if agency is not None:
            self.agency = agency

    @property
    def states(self):
        """Gets the states of this CreateWorkflowRequestBody.

        工作流的编排定义,必须有TYPE，TYPE值必须是3种State（DELAY，OPERATION，END）中一种。每个state的名字是1-80长度的只含数字，字母，-和_的String。

        :return: The states of this CreateWorkflowRequestBody.
        :rtype: list[:class:`huaweicloudsdkdwr.v3.State`]
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this CreateWorkflowRequestBody.

        工作流的编排定义,必须有TYPE，TYPE值必须是3种State（DELAY，OPERATION，END）中一种。每个state的名字是1-80长度的只含数字，字母，-和_的String。

        :param states: The states of this CreateWorkflowRequestBody.
        :type states: list[:class:`huaweicloudsdkdwr.v3.State`]
        """
        self._states = states

    @property
    def inputs(self):
        """Gets the inputs of this CreateWorkflowRequestBody.

        工作流中用户可修改的参数项

        :return: The inputs of this CreateWorkflowRequestBody.
        :rtype: list[:class:`huaweicloudsdkdwr.v3.Input`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this CreateWorkflowRequestBody.

        工作流中用户可修改的参数项

        :param inputs: The inputs of this CreateWorkflowRequestBody.
        :type inputs: list[:class:`huaweicloudsdkdwr.v3.Input`]
        """
        self._inputs = inputs

    @property
    def description(self):
        """Gets the description of this CreateWorkflowRequestBody.

        工作流的描述

        :return: The description of this CreateWorkflowRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateWorkflowRequestBody.

        工作流的描述

        :param description: The description of this CreateWorkflowRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def mode(self):
        """Gets the mode of this CreateWorkflowRequestBody.

        工作流执行类型：同步（EXPRESS）、异步（NORMAL）

        :return: The mode of this CreateWorkflowRequestBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this CreateWorkflowRequestBody.

        工作流执行类型：同步（EXPRESS）、异步（NORMAL）

        :param mode: The mode of this CreateWorkflowRequestBody.
        :type mode: str
        """
        self._mode = mode

    @property
    def express_config(self):
        """Gets the express_config of this CreateWorkflowRequestBody.

        :return: The express_config of this CreateWorkflowRequestBody.
        :rtype: :class:`huaweicloudsdkdwr.v3.ExpressConfig`
        """
        return self._express_config

    @express_config.setter
    def express_config(self, express_config):
        """Sets the express_config of this CreateWorkflowRequestBody.

        :param express_config: The express_config of this CreateWorkflowRequestBody.
        :type express_config: :class:`huaweicloudsdkdwr.v3.ExpressConfig`
        """
        self._express_config = express_config

    @property
    def func_vpc(self):
        """Gets the func_vpc of this CreateWorkflowRequestBody.

        :return: The func_vpc of this CreateWorkflowRequestBody.
        :rtype: :class:`huaweicloudsdkdwr.v3.FuncVpc`
        """
        return self._func_vpc

    @func_vpc.setter
    def func_vpc(self, func_vpc):
        """Sets the func_vpc of this CreateWorkflowRequestBody.

        :param func_vpc: The func_vpc of this CreateWorkflowRequestBody.
        :type func_vpc: :class:`huaweicloudsdkdwr.v3.FuncVpc`
        """
        self._func_vpc = func_vpc

    @property
    def agency(self):
        """Gets the agency of this CreateWorkflowRequestBody.

        用戶传入用于创建工作流时使用的委托的委托名

        :return: The agency of this CreateWorkflowRequestBody.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        """Sets the agency of this CreateWorkflowRequestBody.

        用戶传入用于创建工作流时使用的委托的委托名

        :param agency: The agency of this CreateWorkflowRequestBody.
        :type agency: str
        """
        self._agency = agency

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
        if not isinstance(other, CreateWorkflowRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
