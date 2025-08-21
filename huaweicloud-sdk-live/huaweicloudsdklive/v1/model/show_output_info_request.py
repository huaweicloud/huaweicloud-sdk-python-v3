# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOutputInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_display': 'str',
        'flow_id': 'str',
        'output_name': 'str'
    }

    attribute_map = {
        'data_display': 'data_display',
        'flow_id': 'flow_id',
        'output_name': 'output_name'
    }

    def __init__(self, data_display=None, flow_id=None, output_name=None):
        r"""ShowOutputInfoRequest

        The model defined in huaweicloud sdk

        :param data_display: true
        :type data_display: str
        :param flow_id: 流id
        :type flow_id: str
        :param output_name: 输出名称
        :type output_name: str
        """
        
        

        self._data_display = None
        self._flow_id = None
        self._output_name = None
        self.discriminator = None

        if data_display is not None:
            self.data_display = data_display
        self.flow_id = flow_id
        self.output_name = output_name

    @property
    def data_display(self):
        r"""Gets the data_display of this ShowOutputInfoRequest.

        true

        :return: The data_display of this ShowOutputInfoRequest.
        :rtype: str
        """
        return self._data_display

    @data_display.setter
    def data_display(self, data_display):
        r"""Sets the data_display of this ShowOutputInfoRequest.

        true

        :param data_display: The data_display of this ShowOutputInfoRequest.
        :type data_display: str
        """
        self._data_display = data_display

    @property
    def flow_id(self):
        r"""Gets the flow_id of this ShowOutputInfoRequest.

        流id

        :return: The flow_id of this ShowOutputInfoRequest.
        :rtype: str
        """
        return self._flow_id

    @flow_id.setter
    def flow_id(self, flow_id):
        r"""Sets the flow_id of this ShowOutputInfoRequest.

        流id

        :param flow_id: The flow_id of this ShowOutputInfoRequest.
        :type flow_id: str
        """
        self._flow_id = flow_id

    @property
    def output_name(self):
        r"""Gets the output_name of this ShowOutputInfoRequest.

        输出名称

        :return: The output_name of this ShowOutputInfoRequest.
        :rtype: str
        """
        return self._output_name

    @output_name.setter
    def output_name(self, output_name):
        r"""Sets the output_name of this ShowOutputInfoRequest.

        输出名称

        :param output_name: The output_name of this ShowOutputInfoRequest.
        :type output_name: str
        """
        self._output_name = output_name

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
        if not isinstance(other, ShowOutputInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
