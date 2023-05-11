# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'base_info': 'JobBaseInfo',
        'source_endpoint': 'list[JobEndpointInfo]',
        'target_endpoint': 'list[JobEndpointInfo]',
        'period_order': 'PeriodOrderInfo',
        'node_info': 'JobNodeInfo'
    }

    attribute_map = {
        'base_info': 'base_info',
        'source_endpoint': 'source_endpoint',
        'target_endpoint': 'target_endpoint',
        'period_order': 'period_order',
        'node_info': 'node_info'
    }

    def __init__(self, base_info=None, source_endpoint=None, target_endpoint=None, period_order=None, node_info=None):
        """CreateJobReq

        The model defined in huaweicloud sdk

        :param base_info: 
        :type base_info: :class:`huaweicloudsdkdrs.v5.JobBaseInfo`
        :param source_endpoint: 创建任务数据库信息体。
        :type source_endpoint: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        :param target_endpoint: 创建任务数据库信息体。
        :type target_endpoint: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        :param period_order: 
        :type period_order: :class:`huaweicloudsdkdrs.v5.PeriodOrderInfo`
        :param node_info: 
        :type node_info: :class:`huaweicloudsdkdrs.v5.JobNodeInfo`
        """
        
        

        self._base_info = None
        self._source_endpoint = None
        self._target_endpoint = None
        self._period_order = None
        self._node_info = None
        self.discriminator = None

        self.base_info = base_info
        self.source_endpoint = source_endpoint
        self.target_endpoint = target_endpoint
        if period_order is not None:
            self.period_order = period_order
        self.node_info = node_info

    @property
    def base_info(self):
        """Gets the base_info of this CreateJobReq.

        :return: The base_info of this CreateJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.JobBaseInfo`
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        """Sets the base_info of this CreateJobReq.

        :param base_info: The base_info of this CreateJobReq.
        :type base_info: :class:`huaweicloudsdkdrs.v5.JobBaseInfo`
        """
        self._base_info = base_info

    @property
    def source_endpoint(self):
        """Gets the source_endpoint of this CreateJobReq.

        创建任务数据库信息体。

        :return: The source_endpoint of this CreateJobReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        """
        return self._source_endpoint

    @source_endpoint.setter
    def source_endpoint(self, source_endpoint):
        """Sets the source_endpoint of this CreateJobReq.

        创建任务数据库信息体。

        :param source_endpoint: The source_endpoint of this CreateJobReq.
        :type source_endpoint: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        """
        self._source_endpoint = source_endpoint

    @property
    def target_endpoint(self):
        """Gets the target_endpoint of this CreateJobReq.

        创建任务数据库信息体。

        :return: The target_endpoint of this CreateJobReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        """
        return self._target_endpoint

    @target_endpoint.setter
    def target_endpoint(self, target_endpoint):
        """Sets the target_endpoint of this CreateJobReq.

        创建任务数据库信息体。

        :param target_endpoint: The target_endpoint of this CreateJobReq.
        :type target_endpoint: list[:class:`huaweicloudsdkdrs.v5.JobEndpointInfo`]
        """
        self._target_endpoint = target_endpoint

    @property
    def period_order(self):
        """Gets the period_order of this CreateJobReq.

        :return: The period_order of this CreateJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.PeriodOrderInfo`
        """
        return self._period_order

    @period_order.setter
    def period_order(self, period_order):
        """Sets the period_order of this CreateJobReq.

        :param period_order: The period_order of this CreateJobReq.
        :type period_order: :class:`huaweicloudsdkdrs.v5.PeriodOrderInfo`
        """
        self._period_order = period_order

    @property
    def node_info(self):
        """Gets the node_info of this CreateJobReq.

        :return: The node_info of this CreateJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.JobNodeInfo`
        """
        return self._node_info

    @node_info.setter
    def node_info(self, node_info):
        """Sets the node_info of this CreateJobReq.

        :param node_info: The node_info of this CreateJobReq.
        :type node_info: :class:`huaweicloudsdkdrs.v5.JobNodeInfo`
        """
        self._node_info = node_info

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
        if not isinstance(other, CreateJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
