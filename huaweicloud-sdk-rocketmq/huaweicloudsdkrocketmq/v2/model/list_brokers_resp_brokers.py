# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBrokersRespBrokers:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ids': 'list[float]',
        'broker_name': 'str'
    }

    attribute_map = {
        'ids': 'ids',
        'broker_name': 'broker_name'
    }

    def __init__(self, ids=None, broker_name=None):
        """ListBrokersRespBrokers

        The model defined in huaweicloud sdk

        :param ids: 全部代理ID。
        :type ids: list[float]
        :param broker_name: 节点名称。
        :type broker_name: str
        """
        
        

        self._ids = None
        self._broker_name = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if broker_name is not None:
            self.broker_name = broker_name

    @property
    def ids(self):
        """Gets the ids of this ListBrokersRespBrokers.

        全部代理ID。

        :return: The ids of this ListBrokersRespBrokers.
        :rtype: list[float]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this ListBrokersRespBrokers.

        全部代理ID。

        :param ids: The ids of this ListBrokersRespBrokers.
        :type ids: list[float]
        """
        self._ids = ids

    @property
    def broker_name(self):
        """Gets the broker_name of this ListBrokersRespBrokers.

        节点名称。

        :return: The broker_name of this ListBrokersRespBrokers.
        :rtype: str
        """
        return self._broker_name

    @broker_name.setter
    def broker_name(self, broker_name):
        """Sets the broker_name of this ListBrokersRespBrokers.

        节点名称。

        :param broker_name: The broker_name of this ListBrokersRespBrokers.
        :type broker_name: str
        """
        self._broker_name = broker_name

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
        if not isinstance(other, ListBrokersRespBrokers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
