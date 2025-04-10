# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataConnectorReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_connector': 'DataConnector'
    }

    attribute_map = {
        'data_connector': 'data_connector'
    }

    def __init__(self, data_connector=None):
        r"""DataConnectorReq

        The model defined in huaweicloud sdk

        :param data_connector: 
        :type data_connector: :class:`huaweicloudsdkmrs.v2.DataConnector`
        """
        
        

        self._data_connector = None
        self.discriminator = None

        self.data_connector = data_connector

    @property
    def data_connector(self):
        r"""Gets the data_connector of this DataConnectorReq.

        :return: The data_connector of this DataConnectorReq.
        :rtype: :class:`huaweicloudsdkmrs.v2.DataConnector`
        """
        return self._data_connector

    @data_connector.setter
    def data_connector(self, data_connector):
        r"""Sets the data_connector of this DataConnectorReq.

        :param data_connector: The data_connector of this DataConnectorReq.
        :type data_connector: :class:`huaweicloudsdkmrs.v2.DataConnector`
        """
        self._data_connector = data_connector

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
        if not isinstance(other, DataConnectorReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
