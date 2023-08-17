# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentModifyCustomMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'port': 'int',
        'dimensions': 'str'
    }

    attribute_map = {
        'path': 'path',
        'port': 'port',
        'dimensions': 'dimensions'
    }

    def __init__(self, path=None, port=None, dimensions=None):
        """ComponentModifyCustomMetric

        The model defined in huaweicloud sdk

        :param path: 采集路径，例如/metrics
        :type path: str
        :param port: 采集端口，例如9090
        :type port: int
        :param dimensions: 监控维度，例如\&quot;cpu_usage,mem_usage\&quot;
        :type dimensions: str
        """
        
        

        self._path = None
        self._port = None
        self._dimensions = None
        self.discriminator = None

        self.path = path
        self.port = port
        self.dimensions = dimensions

    @property
    def path(self):
        """Gets the path of this ComponentModifyCustomMetric.

        采集路径，例如/metrics

        :return: The path of this ComponentModifyCustomMetric.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ComponentModifyCustomMetric.

        采集路径，例如/metrics

        :param path: The path of this ComponentModifyCustomMetric.
        :type path: str
        """
        self._path = path

    @property
    def port(self):
        """Gets the port of this ComponentModifyCustomMetric.

        采集端口，例如9090

        :return: The port of this ComponentModifyCustomMetric.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ComponentModifyCustomMetric.

        采集端口，例如9090

        :param port: The port of this ComponentModifyCustomMetric.
        :type port: int
        """
        self._port = port

    @property
    def dimensions(self):
        """Gets the dimensions of this ComponentModifyCustomMetric.

        监控维度，例如\"cpu_usage,mem_usage\"

        :return: The dimensions of this ComponentModifyCustomMetric.
        :rtype: str
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this ComponentModifyCustomMetric.

        监控维度，例如\"cpu_usage,mem_usage\"

        :param dimensions: The dimensions of this ComponentModifyCustomMetric.
        :type dimensions: str
        """
        self._dimensions = dimensions

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
        if not isinstance(other, ComponentModifyCustomMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
