# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RouterDetailRespDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'route_id': 'str',
        'input_module_id': 'str',
        'output_module_id': 'str',
        'input': 'str',
        'output': 'str',
        'sql': 'str',
        'available': 'bool'
    }

    attribute_map = {
        'route_id': 'route_id',
        'input_module_id': 'input_module_id',
        'output_module_id': 'output_module_id',
        'input': 'input',
        'output': 'output',
        'sql': 'sql',
        'available': 'available'
    }

    def __init__(self, route_id=None, input_module_id=None, output_module_id=None, input=None, output=None, sql=None, available=None):
        """RouterDetailRespDTO

        The model defined in huaweicloud sdk

        :param route_id: 路由ID，节点下唯一
        :type route_id: str
        :param input_module_id: 输入点所在模块的模块ID
        :type input_module_id: str
        :param output_module_id: 输出点所在模块的模块ID
        :type output_module_id: str
        :param input: 输入点名称
        :type input: str
        :param output: 输出点名称
        :type output: str
        :param sql: sql參數
        :type sql: str
        :param available: 是否可用
        :type available: bool
        """
        
        

        self._route_id = None
        self._input_module_id = None
        self._output_module_id = None
        self._input = None
        self._output = None
        self._sql = None
        self._available = None
        self.discriminator = None

        self.route_id = route_id
        if input_module_id is not None:
            self.input_module_id = input_module_id
        if output_module_id is not None:
            self.output_module_id = output_module_id
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if sql is not None:
            self.sql = sql
        if available is not None:
            self.available = available

    @property
    def route_id(self):
        """Gets the route_id of this RouterDetailRespDTO.

        路由ID，节点下唯一

        :return: The route_id of this RouterDetailRespDTO.
        :rtype: str
        """
        return self._route_id

    @route_id.setter
    def route_id(self, route_id):
        """Sets the route_id of this RouterDetailRespDTO.

        路由ID，节点下唯一

        :param route_id: The route_id of this RouterDetailRespDTO.
        :type route_id: str
        """
        self._route_id = route_id

    @property
    def input_module_id(self):
        """Gets the input_module_id of this RouterDetailRespDTO.

        输入点所在模块的模块ID

        :return: The input_module_id of this RouterDetailRespDTO.
        :rtype: str
        """
        return self._input_module_id

    @input_module_id.setter
    def input_module_id(self, input_module_id):
        """Sets the input_module_id of this RouterDetailRespDTO.

        输入点所在模块的模块ID

        :param input_module_id: The input_module_id of this RouterDetailRespDTO.
        :type input_module_id: str
        """
        self._input_module_id = input_module_id

    @property
    def output_module_id(self):
        """Gets the output_module_id of this RouterDetailRespDTO.

        输出点所在模块的模块ID

        :return: The output_module_id of this RouterDetailRespDTO.
        :rtype: str
        """
        return self._output_module_id

    @output_module_id.setter
    def output_module_id(self, output_module_id):
        """Sets the output_module_id of this RouterDetailRespDTO.

        输出点所在模块的模块ID

        :param output_module_id: The output_module_id of this RouterDetailRespDTO.
        :type output_module_id: str
        """
        self._output_module_id = output_module_id

    @property
    def input(self):
        """Gets the input of this RouterDetailRespDTO.

        输入点名称

        :return: The input of this RouterDetailRespDTO.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this RouterDetailRespDTO.

        输入点名称

        :param input: The input of this RouterDetailRespDTO.
        :type input: str
        """
        self._input = input

    @property
    def output(self):
        """Gets the output of this RouterDetailRespDTO.

        输出点名称

        :return: The output of this RouterDetailRespDTO.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this RouterDetailRespDTO.

        输出点名称

        :param output: The output of this RouterDetailRespDTO.
        :type output: str
        """
        self._output = output

    @property
    def sql(self):
        """Gets the sql of this RouterDetailRespDTO.

        sql參數

        :return: The sql of this RouterDetailRespDTO.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        """Sets the sql of this RouterDetailRespDTO.

        sql參數

        :param sql: The sql of this RouterDetailRespDTO.
        :type sql: str
        """
        self._sql = sql

    @property
    def available(self):
        """Gets the available of this RouterDetailRespDTO.

        是否可用

        :return: The available of this RouterDetailRespDTO.
        :rtype: bool
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this RouterDetailRespDTO.

        是否可用

        :param available: The available of this RouterDetailRespDTO.
        :type available: bool
        """
        self._available = available

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
        if not isinstance(other, RouterDetailRespDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
