# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyPortRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port': 'int'
    }

    attribute_map = {
        'port': 'port'
    }

    def __init__(self, port=None):
        r"""ModifyPortRequestBody

        The model defined in huaweicloud sdk

        :param port: 新端口号。端口有效范围为2100~9500，暂不支持8636、8637和8638。GeminiDB Mongo副本集4.0数据库实例端口有效范围为2100~9500，暂不支持8636、8637和8638。 GeminiDB Cassandra数据库实例端口有效范围为2100~9500，暂不支持7000，7001，7199，8636，8479，8484，8999，8018，2180，2887，3887，8079，8091，8092。 GeminiDB Redis数据库实例端口有效范围为1024~65535，暂不支持2180、2887、3887、6377、6378、6380、8018、8079、8091、8479、8484、8999、12017、12333、50069。
        :type port: int
        """
        
        

        self._port = None
        self.discriminator = None

        self.port = port

    @property
    def port(self):
        r"""Gets the port of this ModifyPortRequestBody.

        新端口号。端口有效范围为2100~9500，暂不支持8636、8637和8638。GeminiDB Mongo副本集4.0数据库实例端口有效范围为2100~9500，暂不支持8636、8637和8638。 GeminiDB Cassandra数据库实例端口有效范围为2100~9500，暂不支持7000，7001，7199，8636，8479，8484，8999，8018，2180，2887，3887，8079，8091，8092。 GeminiDB Redis数据库实例端口有效范围为1024~65535，暂不支持2180、2887、3887、6377、6378、6380、8018、8079、8091、8479、8484、8999、12017、12333、50069。

        :return: The port of this ModifyPortRequestBody.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ModifyPortRequestBody.

        新端口号。端口有效范围为2100~9500，暂不支持8636、8637和8638。GeminiDB Mongo副本集4.0数据库实例端口有效范围为2100~9500，暂不支持8636、8637和8638。 GeminiDB Cassandra数据库实例端口有效范围为2100~9500，暂不支持7000，7001，7199，8636，8479，8484，8999，8018，2180，2887，3887，8079，8091，8092。 GeminiDB Redis数据库实例端口有效范围为1024~65535，暂不支持2180、2887、3887、6377、6378、6380、8018、8079、8091、8479、8484、8999、12017、12333、50069。

        :param port: The port of this ModifyPortRequestBody.
        :type port: int
        """
        self._port = port

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
        if not isinstance(other, ModifyPortRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
