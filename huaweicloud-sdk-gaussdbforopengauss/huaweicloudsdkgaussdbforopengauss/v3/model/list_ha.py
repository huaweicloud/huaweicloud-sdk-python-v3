# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHa:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'consistency': 'str',
        'replication_mode': 'str'
    }

    attribute_map = {
        'consistency': 'consistency',
        'replication_mode': 'replication_mode'
    }

    def __init__(self, consistency=None, replication_mode=None):
        r"""ListHa

        The model defined in huaweicloud sdk

        :param consistency: 数据库一致性类型，分布式模式实例仅有。取值为“strong”、“eventual”，分别表示强一致性、最终一致性。
        :type consistency: str
        :param replication_mode: 备机同步参数。  取值：非空。  GaussDB为 “sync” 说明： “sync”为同步模式。
        :type replication_mode: str
        """
        
        

        self._consistency = None
        self._replication_mode = None
        self.discriminator = None

        self.consistency = consistency
        self.replication_mode = replication_mode

    @property
    def consistency(self):
        r"""Gets the consistency of this ListHa.

        数据库一致性类型，分布式模式实例仅有。取值为“strong”、“eventual”，分别表示强一致性、最终一致性。

        :return: The consistency of this ListHa.
        :rtype: str
        """
        return self._consistency

    @consistency.setter
    def consistency(self, consistency):
        r"""Sets the consistency of this ListHa.

        数据库一致性类型，分布式模式实例仅有。取值为“strong”、“eventual”，分别表示强一致性、最终一致性。

        :param consistency: The consistency of this ListHa.
        :type consistency: str
        """
        self._consistency = consistency

    @property
    def replication_mode(self):
        r"""Gets the replication_mode of this ListHa.

        备机同步参数。  取值：非空。  GaussDB为 “sync” 说明： “sync”为同步模式。

        :return: The replication_mode of this ListHa.
        :rtype: str
        """
        return self._replication_mode

    @replication_mode.setter
    def replication_mode(self, replication_mode):
        r"""Sets the replication_mode of this ListHa.

        备机同步参数。  取值：非空。  GaussDB为 “sync” 说明： “sync”为同步模式。

        :param replication_mode: The replication_mode of this ListHa.
        :type replication_mode: str
        """
        self._replication_mode = replication_mode

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
        if not isinstance(other, ListHa):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
