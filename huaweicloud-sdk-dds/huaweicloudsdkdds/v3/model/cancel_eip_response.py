# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CancelEipResponse(SdkResponse):


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
        'node_name': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'node_id': 'node_id',
        'node_name': 'node_name'
    }

    def __init__(self, job_id=None, node_id=None, node_name=None):
        """CancelEipResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._job_id = None
        self._node_id = None
        self._node_name = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if node_id is not None:
            self.node_id = node_id
        if node_name is not None:
            self.node_name = node_name

    @property
    def job_id(self):
        """Gets the job_id of this CancelEipResponse.

        任务ID。

        :return: The job_id of this CancelEipResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CancelEipResponse.

        任务ID。

        :param job_id: The job_id of this CancelEipResponse.
        :type: str
        """
        self._job_id = job_id

    @property
    def node_id(self):
        """Gets the node_id of this CancelEipResponse.

        节点ID。

        :return: The node_id of this CancelEipResponse.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this CancelEipResponse.

        节点ID。

        :param node_id: The node_id of this CancelEipResponse.
        :type: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        """Gets the node_name of this CancelEipResponse.

        节点名称。

        :return: The node_name of this CancelEipResponse.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this CancelEipResponse.

        节点名称。

        :param node_name: The node_name of this CancelEipResponse.
        :type: str
        """
        self._node_name = node_name

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
        if not isinstance(other, CancelEipResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
