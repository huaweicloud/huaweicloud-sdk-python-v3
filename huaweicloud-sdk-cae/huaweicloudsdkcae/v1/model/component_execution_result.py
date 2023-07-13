# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentExecutionResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_name': 'str',
        'component_id': 'str',
        'status': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'component_name': 'component_name',
        'component_id': 'component_id',
        'status': 'status',
        'error_message': 'error_message'
    }

    def __init__(self, component_name=None, component_id=None, status=None, error_message=None):
        """ComponentExecutionResult

        The model defined in huaweicloud sdk

        :param component_name: 组件名称。
        :type component_name: str
        :param component_id: 组件ID。
        :type component_id: str
        :param status: 组件执行启停的结果：failed/success。
        :type status: str
        :param error_message: 组件执行启停的错误信息，如果执行结果为成功，则为空。
        :type error_message: str
        """
        
        

        self._component_name = None
        self._component_id = None
        self._status = None
        self._error_message = None
        self.discriminator = None

        if component_name is not None:
            self.component_name = component_name
        if component_id is not None:
            self.component_id = component_id
        if status is not None:
            self.status = status
        if error_message is not None:
            self.error_message = error_message

    @property
    def component_name(self):
        """Gets the component_name of this ComponentExecutionResult.

        组件名称。

        :return: The component_name of this ComponentExecutionResult.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """Sets the component_name of this ComponentExecutionResult.

        组件名称。

        :param component_name: The component_name of this ComponentExecutionResult.
        :type component_name: str
        """
        self._component_name = component_name

    @property
    def component_id(self):
        """Gets the component_id of this ComponentExecutionResult.

        组件ID。

        :return: The component_id of this ComponentExecutionResult.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this ComponentExecutionResult.

        组件ID。

        :param component_id: The component_id of this ComponentExecutionResult.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def status(self):
        """Gets the status of this ComponentExecutionResult.

        组件执行启停的结果：failed/success。

        :return: The status of this ComponentExecutionResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ComponentExecutionResult.

        组件执行启停的结果：failed/success。

        :param status: The status of this ComponentExecutionResult.
        :type status: str
        """
        self._status = status

    @property
    def error_message(self):
        """Gets the error_message of this ComponentExecutionResult.

        组件执行启停的错误信息，如果执行结果为成功，则为空。

        :return: The error_message of this ComponentExecutionResult.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ComponentExecutionResult.

        组件执行启停的错误信息，如果执行结果为成功，则为空。

        :param error_message: The error_message of this ComponentExecutionResult.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, ComponentExecutionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
