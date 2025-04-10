# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SinkFGParameters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'invoke_type': 'str',
        'urn': 'str',
        'agency': 'str'
    }

    attribute_map = {
        'invoke_type': 'invoke_type',
        'urn': 'urn',
        'agency': 'agency'
    }

    def __init__(self, invoke_type=None, urn=None, agency=None):
        r"""SinkFGParameters

        The model defined in huaweicloud sdk

        :param invoke_type: 函数执行方式,同步/异步
        :type invoke_type: str
        :param urn: 函数链接
        :type urn: str
        :param agency: 租户委托
        :type agency: str
        """
        
        

        self._invoke_type = None
        self._urn = None
        self._agency = None
        self.discriminator = None

        if invoke_type is not None:
            self.invoke_type = invoke_type
        if urn is not None:
            self.urn = urn
        if agency is not None:
            self.agency = agency

    @property
    def invoke_type(self):
        r"""Gets the invoke_type of this SinkFGParameters.

        函数执行方式,同步/异步

        :return: The invoke_type of this SinkFGParameters.
        :rtype: str
        """
        return self._invoke_type

    @invoke_type.setter
    def invoke_type(self, invoke_type):
        r"""Sets the invoke_type of this SinkFGParameters.

        函数执行方式,同步/异步

        :param invoke_type: The invoke_type of this SinkFGParameters.
        :type invoke_type: str
        """
        self._invoke_type = invoke_type

    @property
    def urn(self):
        r"""Gets the urn of this SinkFGParameters.

        函数链接

        :return: The urn of this SinkFGParameters.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this SinkFGParameters.

        函数链接

        :param urn: The urn of this SinkFGParameters.
        :type urn: str
        """
        self._urn = urn

    @property
    def agency(self):
        r"""Gets the agency of this SinkFGParameters.

        租户委托

        :return: The agency of this SinkFGParameters.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        r"""Sets the agency of this SinkFGParameters.

        租户委托

        :param agency: The agency of this SinkFGParameters.
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
        if not isinstance(other, SinkFGParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
