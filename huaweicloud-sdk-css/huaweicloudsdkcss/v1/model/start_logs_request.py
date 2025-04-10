# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'action': 'str',
        'body': 'StartLogsReq'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'action': 'action',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, action=None, body=None):
        r"""StartLogsRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 指定开启日志的集群ID。
        :type cluster_id: str
        :param action: action支持base_log_collect和real_time_log_collect两种，base就是之前历史的能力，real_time为实时采集能力，默认不传就是base，兼容之前的逻辑
        :type action: str
        :param body: Body of the StartLogsRequest
        :type body: :class:`huaweicloudsdkcss.v1.StartLogsReq`
        """
        
        

        self._cluster_id = None
        self._action = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if action is not None:
            self.action = action
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this StartLogsRequest.

        指定开启日志的集群ID。

        :return: The cluster_id of this StartLogsRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this StartLogsRequest.

        指定开启日志的集群ID。

        :param cluster_id: The cluster_id of this StartLogsRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def action(self):
        r"""Gets the action of this StartLogsRequest.

        action支持base_log_collect和real_time_log_collect两种，base就是之前历史的能力，real_time为实时采集能力，默认不传就是base，兼容之前的逻辑

        :return: The action of this StartLogsRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this StartLogsRequest.

        action支持base_log_collect和real_time_log_collect两种，base就是之前历史的能力，real_time为实时采集能力，默认不传就是base，兼容之前的逻辑

        :param action: The action of this StartLogsRequest.
        :type action: str
        """
        self._action = action

    @property
    def body(self):
        r"""Gets the body of this StartLogsRequest.

        :return: The body of this StartLogsRequest.
        :rtype: :class:`huaweicloudsdkcss.v1.StartLogsReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this StartLogsRequest.

        :param body: The body of this StartLogsRequest.
        :type body: :class:`huaweicloudsdkcss.v1.StartLogsReq`
        """
        self._body = body

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
        if not isinstance(other, StartLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
