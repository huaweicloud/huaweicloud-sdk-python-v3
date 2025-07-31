# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteDaemonsetRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_ids': 'list[str]',
        'invoked_service': 'str'
    }

    attribute_map = {
        'cluster_ids': 'cluster_ids',
        'invoked_service': 'invoked_service'
    }

    def __init__(self, cluster_ids=None, invoked_service=None):
        r"""BatchDeleteDaemonsetRequestBody

        The model defined in huaweicloud sdk

        :param cluster_ids: 批量卸载列表
        :type cluster_ids: list[str]
        :param invoked_service: 调用服务，标识cce免费体检报告，cce调用传参为cce:    - hss hss服务    - cce cce服务
        :type invoked_service: str
        """
        
        

        self._cluster_ids = None
        self._invoked_service = None
        self.discriminator = None

        self.cluster_ids = cluster_ids
        if invoked_service is not None:
            self.invoked_service = invoked_service

    @property
    def cluster_ids(self):
        r"""Gets the cluster_ids of this BatchDeleteDaemonsetRequestBody.

        批量卸载列表

        :return: The cluster_ids of this BatchDeleteDaemonsetRequestBody.
        :rtype: list[str]
        """
        return self._cluster_ids

    @cluster_ids.setter
    def cluster_ids(self, cluster_ids):
        r"""Sets the cluster_ids of this BatchDeleteDaemonsetRequestBody.

        批量卸载列表

        :param cluster_ids: The cluster_ids of this BatchDeleteDaemonsetRequestBody.
        :type cluster_ids: list[str]
        """
        self._cluster_ids = cluster_ids

    @property
    def invoked_service(self):
        r"""Gets the invoked_service of this BatchDeleteDaemonsetRequestBody.

        调用服务，标识cce免费体检报告，cce调用传参为cce:    - hss hss服务    - cce cce服务

        :return: The invoked_service of this BatchDeleteDaemonsetRequestBody.
        :rtype: str
        """
        return self._invoked_service

    @invoked_service.setter
    def invoked_service(self, invoked_service):
        r"""Sets the invoked_service of this BatchDeleteDaemonsetRequestBody.

        调用服务，标识cce免费体检报告，cce调用传参为cce:    - hss hss服务    - cce cce服务

        :param invoked_service: The invoked_service of this BatchDeleteDaemonsetRequestBody.
        :type invoked_service: str
        """
        self._invoked_service = invoked_service

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
        if not isinstance(other, BatchDeleteDaemonsetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
