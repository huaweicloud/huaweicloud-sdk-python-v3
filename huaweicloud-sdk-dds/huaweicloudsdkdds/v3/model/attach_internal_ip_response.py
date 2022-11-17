# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachInternalIpResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'node_id': 'str',
        'new_ip': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'node_id': 'node_id',
        'new_ip': 'new_ip'
    }

    def __init__(self, job_id=None, node_id=None, new_ip=None):
        """AttachInternalIpResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param node_id: 节点ID。
        :type node_id: str
        :param new_ip: 新的内网IP。
        :type new_ip: str
        """
        
        super(AttachInternalIpResponse, self).__init__()

        self._job_id = None
        self._node_id = None
        self._new_ip = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if node_id is not None:
            self.node_id = node_id
        if new_ip is not None:
            self.new_ip = new_ip

    @property
    def job_id(self):
        """Gets the job_id of this AttachInternalIpResponse.

        任务ID。

        :return: The job_id of this AttachInternalIpResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this AttachInternalIpResponse.

        任务ID。

        :param job_id: The job_id of this AttachInternalIpResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def node_id(self):
        """Gets the node_id of this AttachInternalIpResponse.

        节点ID。

        :return: The node_id of this AttachInternalIpResponse.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this AttachInternalIpResponse.

        节点ID。

        :param node_id: The node_id of this AttachInternalIpResponse.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def new_ip(self):
        """Gets the new_ip of this AttachInternalIpResponse.

        新的内网IP。

        :return: The new_ip of this AttachInternalIpResponse.
        :rtype: str
        """
        return self._new_ip

    @new_ip.setter
    def new_ip(self, new_ip):
        """Sets the new_ip of this AttachInternalIpResponse.

        新的内网IP。

        :param new_ip: The new_ip of this AttachInternalIpResponse.
        :type new_ip: str
        """
        self._new_ip = new_ip

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
        if not isinstance(other, AttachInternalIpResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
