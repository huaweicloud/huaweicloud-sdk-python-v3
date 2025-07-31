# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EpResourceStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extend_relation_id': 'str',
        'unhealthy': 'int',
        'total': 'int',
        'event_unhealthy': 'int',
        'namespaces': 'int'
    }

    attribute_map = {
        'extend_relation_id': 'extend_relation_id',
        'unhealthy': 'unhealthy',
        'total': 'total',
        'event_unhealthy': 'event_unhealthy',
        'namespaces': 'namespaces'
    }

    def __init__(self, extend_relation_id=None, unhealthy=None, total=None, event_unhealthy=None, namespaces=None):
        r"""EpResourceStatistics

        The model defined in huaweicloud sdk

        :param extend_relation_id: 企业项目ID
        :type extend_relation_id: str
        :param unhealthy: 告警中的资源数
        :type unhealthy: int
        :param total: 资源总数
        :type total: int
        :param event_unhealthy: 已触发的资源数
        :type event_unhealthy: int
        :param namespaces: 资源类型数
        :type namespaces: int
        """
        
        

        self._extend_relation_id = None
        self._unhealthy = None
        self._total = None
        self._event_unhealthy = None
        self._namespaces = None
        self.discriminator = None

        if extend_relation_id is not None:
            self.extend_relation_id = extend_relation_id
        if unhealthy is not None:
            self.unhealthy = unhealthy
        if total is not None:
            self.total = total
        if event_unhealthy is not None:
            self.event_unhealthy = event_unhealthy
        if namespaces is not None:
            self.namespaces = namespaces

    @property
    def extend_relation_id(self):
        r"""Gets the extend_relation_id of this EpResourceStatistics.

        企业项目ID

        :return: The extend_relation_id of this EpResourceStatistics.
        :rtype: str
        """
        return self._extend_relation_id

    @extend_relation_id.setter
    def extend_relation_id(self, extend_relation_id):
        r"""Sets the extend_relation_id of this EpResourceStatistics.

        企业项目ID

        :param extend_relation_id: The extend_relation_id of this EpResourceStatistics.
        :type extend_relation_id: str
        """
        self._extend_relation_id = extend_relation_id

    @property
    def unhealthy(self):
        r"""Gets the unhealthy of this EpResourceStatistics.

        告警中的资源数

        :return: The unhealthy of this EpResourceStatistics.
        :rtype: int
        """
        return self._unhealthy

    @unhealthy.setter
    def unhealthy(self, unhealthy):
        r"""Sets the unhealthy of this EpResourceStatistics.

        告警中的资源数

        :param unhealthy: The unhealthy of this EpResourceStatistics.
        :type unhealthy: int
        """
        self._unhealthy = unhealthy

    @property
    def total(self):
        r"""Gets the total of this EpResourceStatistics.

        资源总数

        :return: The total of this EpResourceStatistics.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this EpResourceStatistics.

        资源总数

        :param total: The total of this EpResourceStatistics.
        :type total: int
        """
        self._total = total

    @property
    def event_unhealthy(self):
        r"""Gets the event_unhealthy of this EpResourceStatistics.

        已触发的资源数

        :return: The event_unhealthy of this EpResourceStatistics.
        :rtype: int
        """
        return self._event_unhealthy

    @event_unhealthy.setter
    def event_unhealthy(self, event_unhealthy):
        r"""Sets the event_unhealthy of this EpResourceStatistics.

        已触发的资源数

        :param event_unhealthy: The event_unhealthy of this EpResourceStatistics.
        :type event_unhealthy: int
        """
        self._event_unhealthy = event_unhealthy

    @property
    def namespaces(self):
        r"""Gets the namespaces of this EpResourceStatistics.

        资源类型数

        :return: The namespaces of this EpResourceStatistics.
        :rtype: int
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        r"""Sets the namespaces of this EpResourceStatistics.

        资源类型数

        :param namespaces: The namespaces of this EpResourceStatistics.
        :type namespaces: int
        """
        self._namespaces = namespaces

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
        if not isinstance(other, EpResourceStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
