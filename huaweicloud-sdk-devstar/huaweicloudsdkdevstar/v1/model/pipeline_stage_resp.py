# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineStageResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'display_name': 'str',
        'status': 'str',
        'result': 'str'
    }

    attribute_map = {
        'display_name': 'display_name',
        'status': 'status',
        'result': 'result'
    }

    def __init__(self, display_name=None, status=None, result=None):
        """PipelineStageResp

        The model defined in huaweicloud sdk

        :param display_name: 阶段名称
        :type display_name: str
        :param status: 阶段状态
        :type status: str
        :param result: 阶段执行结果
        :type result: str
        """
        
        

        self._display_name = None
        self._status = None
        self._result = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if status is not None:
            self.status = status
        if result is not None:
            self.result = result

    @property
    def display_name(self):
        """Gets the display_name of this PipelineStageResp.

        阶段名称

        :return: The display_name of this PipelineStageResp.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PipelineStageResp.

        阶段名称

        :param display_name: The display_name of this PipelineStageResp.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def status(self):
        """Gets the status of this PipelineStageResp.

        阶段状态

        :return: The status of this PipelineStageResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PipelineStageResp.

        阶段状态

        :param status: The status of this PipelineStageResp.
        :type status: str
        """
        self._status = status

    @property
    def result(self):
        """Gets the result of this PipelineStageResp.

        阶段执行结果

        :return: The result of this PipelineStageResp.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this PipelineStageResp.

        阶段执行结果

        :param result: The result of this PipelineStageResp.
        :type result: str
        """
        self._result = result

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
        if not isinstance(other, PipelineStageResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
