# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'manage_state': 'str',
        'marker': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'manage_state': 'manage_state',
        'marker': 'marker',
        'limit': 'limit'
    }

    def __init__(self, manage_state=None, marker=None, limit=None):
        r"""ListServersRequest

        The model defined in huaweicloud sdk

        :param manage_state: 服务器资产管理状态： - delivering：等待物料。 - received：到货，物料到货进场。 - onboard：上架，对物理服务器进行机柜机架、物理组网、BMC地址配置等，可通过BMC远程管理。 - ready：可用，完成网调、软调及转维验收。 - in-use：使用中，创建裸机实例。 - frozen：冻结，因欠费导致资源冻结。 - offboarding：下架中。
        :type manage_state: str
        :param marker: 上一页数据的最后一条记录的id
        :type marker: str
        :param limit: 分页查询时每页行数。最大值为 1000。  默认值： 当不设置值或设置的值小于 10 时，默认值为 10。 当设置的值大于 1000 时，默认值为 1000。
        :type limit: int
        """
        
        

        self._manage_state = None
        self._marker = None
        self._limit = None
        self.discriminator = None

        if manage_state is not None:
            self.manage_state = manage_state
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit

    @property
    def manage_state(self):
        r"""Gets the manage_state of this ListServersRequest.

        服务器资产管理状态： - delivering：等待物料。 - received：到货，物料到货进场。 - onboard：上架，对物理服务器进行机柜机架、物理组网、BMC地址配置等，可通过BMC远程管理。 - ready：可用，完成网调、软调及转维验收。 - in-use：使用中，创建裸机实例。 - frozen：冻结，因欠费导致资源冻结。 - offboarding：下架中。

        :return: The manage_state of this ListServersRequest.
        :rtype: str
        """
        return self._manage_state

    @manage_state.setter
    def manage_state(self, manage_state):
        r"""Sets the manage_state of this ListServersRequest.

        服务器资产管理状态： - delivering：等待物料。 - received：到货，物料到货进场。 - onboard：上架，对物理服务器进行机柜机架、物理组网、BMC地址配置等，可通过BMC远程管理。 - ready：可用，完成网调、软调及转维验收。 - in-use：使用中，创建裸机实例。 - frozen：冻结，因欠费导致资源冻结。 - offboarding：下架中。

        :param manage_state: The manage_state of this ListServersRequest.
        :type manage_state: str
        """
        self._manage_state = manage_state

    @property
    def marker(self):
        r"""Gets the marker of this ListServersRequest.

        上一页数据的最后一条记录的id

        :return: The marker of this ListServersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListServersRequest.

        上一页数据的最后一条记录的id

        :param marker: The marker of this ListServersRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListServersRequest.

        分页查询时每页行数。最大值为 1000。  默认值： 当不设置值或设置的值小于 10 时，默认值为 10。 当设置的值大于 1000 时，默认值为 1000。

        :return: The limit of this ListServersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListServersRequest.

        分页查询时每页行数。最大值为 1000。  默认值： 当不设置值或设置的值小于 10 时，默认值为 10。 当设置的值大于 1000 时，默认值为 1000。

        :param limit: The limit of this ListServersRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListServersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
