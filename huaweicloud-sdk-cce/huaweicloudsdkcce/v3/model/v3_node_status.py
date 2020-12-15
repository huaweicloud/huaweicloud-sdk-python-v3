# coding: utf-8

import pprint
import re

import six





class V3NodeStatus:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'delete_status': 'DeleteStatus',
        'job_id': 'str',
        'phase': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'server_id': 'str'
    }

    attribute_map = {
        'delete_status': 'deleteStatus',
        'job_id': 'jobID',
        'phase': 'phase',
        'private_ip': 'privateIP',
        'public_ip': 'publicIP',
        'server_id': 'serverId'
    }

    def __init__(self, delete_status=None, job_id=None, phase=None, private_ip=None, public_ip=None, server_id=None):
        """V3NodeStatus - a model defined in huaweicloud sdk"""
        
        

        self._delete_status = None
        self._job_id = None
        self._phase = None
        self._private_ip = None
        self._public_ip = None
        self._server_id = None
        self.discriminator = None

        if delete_status is not None:
            self.delete_status = delete_status
        if job_id is not None:
            self.job_id = job_id
        if phase is not None:
            self.phase = phase
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if server_id is not None:
            self.server_id = server_id

    @property
    def delete_status(self):
        """Gets the delete_status of this V3NodeStatus.


        :return: The delete_status of this V3NodeStatus.
        :rtype: DeleteStatus
        """
        return self._delete_status

    @delete_status.setter
    def delete_status(self, delete_status):
        """Sets the delete_status of this V3NodeStatus.


        :param delete_status: The delete_status of this V3NodeStatus.
        :type: DeleteStatus
        """
        self._delete_status = delete_status

    @property
    def job_id(self):
        """Gets the job_id of this V3NodeStatus.

        创建或删除时的任务ID。

        :return: The job_id of this V3NodeStatus.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this V3NodeStatus.

        创建或删除时的任务ID。

        :param job_id: The job_id of this V3NodeStatus.
        :type: str
        """
        self._job_id = job_id

    @property
    def phase(self):
        """Gets the phase of this V3NodeStatus.

        节点状态。

        :return: The phase of this V3NodeStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this V3NodeStatus.

        节点状态。

        :param phase: The phase of this V3NodeStatus.
        :type: str
        """
        self._phase = phase

    @property
    def private_ip(self):
        """Gets the private_ip of this V3NodeStatus.

        节点主网卡私有网段IP地址。

        :return: The private_ip of this V3NodeStatus.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this V3NodeStatus.

        节点主网卡私有网段IP地址。

        :param private_ip: The private_ip of this V3NodeStatus.
        :type: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this V3NodeStatus.

        节点弹性公网IP地址。

        :return: The public_ip of this V3NodeStatus.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this V3NodeStatus.

        节点弹性公网IP地址。

        :param public_ip: The public_ip of this V3NodeStatus.
        :type: str
        """
        self._public_ip = public_ip

    @property
    def server_id(self):
        """Gets the server_id of this V3NodeStatus.

        底层云服务器或裸金属节点ID。

        :return: The server_id of this V3NodeStatus.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this V3NodeStatus.

        底层云服务器或裸金属节点ID。

        :param server_id: The server_id of this V3NodeStatus.
        :type: str
        """
        self._server_id = server_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V3NodeStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
