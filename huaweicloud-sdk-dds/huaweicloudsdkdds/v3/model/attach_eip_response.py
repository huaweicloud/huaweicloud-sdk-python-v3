# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachEipResponse(SdkResponse):

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
        'node_name': 'str',
        'public_ip_id': 'str',
        'public_ip': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'node_id': 'node_id',
        'node_name': 'node_name',
        'public_ip_id': 'public_ip_id',
        'public_ip': 'public_ip'
    }

    def __init__(self, job_id=None, node_id=None, node_name=None, public_ip_id=None, public_ip=None):
        r"""AttachEipResponse

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param node_id: 节点ID。
        :type node_id: str
        :param node_name: 节点名称。
        :type node_name: str
        :param public_ip_id: 公网IP的ID。
        :type public_ip_id: str
        :param public_ip: 公网IP。
        :type public_ip: str
        """
        
        super(AttachEipResponse, self).__init__()

        self._job_id = None
        self._node_id = None
        self._node_name = None
        self._public_ip_id = None
        self._public_ip = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if node_id is not None:
            self.node_id = node_id
        if node_name is not None:
            self.node_name = node_name
        if public_ip_id is not None:
            self.public_ip_id = public_ip_id
        if public_ip is not None:
            self.public_ip = public_ip

    @property
    def job_id(self):
        r"""Gets the job_id of this AttachEipResponse.

        任务ID。

        :return: The job_id of this AttachEipResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this AttachEipResponse.

        任务ID。

        :param job_id: The job_id of this AttachEipResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def node_id(self):
        r"""Gets the node_id of this AttachEipResponse.

        节点ID。

        :return: The node_id of this AttachEipResponse.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this AttachEipResponse.

        节点ID。

        :param node_id: The node_id of this AttachEipResponse.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        r"""Gets the node_name of this AttachEipResponse.

        节点名称。

        :return: The node_name of this AttachEipResponse.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this AttachEipResponse.

        节点名称。

        :param node_name: The node_name of this AttachEipResponse.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def public_ip_id(self):
        r"""Gets the public_ip_id of this AttachEipResponse.

        公网IP的ID。

        :return: The public_ip_id of this AttachEipResponse.
        :rtype: str
        """
        return self._public_ip_id

    @public_ip_id.setter
    def public_ip_id(self, public_ip_id):
        r"""Sets the public_ip_id of this AttachEipResponse.

        公网IP的ID。

        :param public_ip_id: The public_ip_id of this AttachEipResponse.
        :type public_ip_id: str
        """
        self._public_ip_id = public_ip_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this AttachEipResponse.

        公网IP。

        :return: The public_ip of this AttachEipResponse.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this AttachEipResponse.

        公网IP。

        :param public_ip: The public_ip of this AttachEipResponse.
        :type public_ip: str
        """
        self._public_ip = public_ip

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
        if not isinstance(other, AttachEipResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
