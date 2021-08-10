# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodePoolStatus:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'current_node': 'int',
        'phase': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'current_node': 'currentNode',
        'phase': 'phase',
        'job_id': 'jobId'
    }

    def __init__(self, current_node=None, phase=None, job_id=None):
        """NodePoolStatus - a model defined in huaweicloud sdk"""
        
        

        self._current_node = None
        self._phase = None
        self._job_id = None
        self.discriminator = None

        if current_node is not None:
            self.current_node = current_node
        if phase is not None:
            self.phase = phase
        if job_id is not None:
            self.job_id = job_id

    @property
    def current_node(self):
        """Gets the current_node of this NodePoolStatus.

        当前节点池中节点数量

        :return: The current_node of this NodePoolStatus.
        :rtype: int
        """
        return self._current_node

    @current_node.setter
    def current_node(self, current_node):
        """Sets the current_node of this NodePoolStatus.

        当前节点池中节点数量

        :param current_node: The current_node of this NodePoolStatus.
        :type: int
        """
        self._current_node = current_node

    @property
    def phase(self):
        """Gets the phase of this NodePoolStatus.

        节点池状态，为空时节点池处于可用状态。 - Synchronizing：伸缩中 - Synchronized：节点池更新失败时会被置于此状态 - SoldOut：节点资源售罄 - Deleting：删除中 - Error：错误 

        :return: The phase of this NodePoolStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this NodePoolStatus.

        节点池状态，为空时节点池处于可用状态。 - Synchronizing：伸缩中 - Synchronized：节点池更新失败时会被置于此状态 - SoldOut：节点资源售罄 - Deleting：删除中 - Error：错误 

        :param phase: The phase of this NodePoolStatus.
        :type: str
        """
        self._phase = phase

    @property
    def job_id(self):
        """Gets the job_id of this NodePoolStatus.

        节点池删除时的 JobID

        :return: The job_id of this NodePoolStatus.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this NodePoolStatus.

        节点池删除时的 JobID

        :param job_id: The job_id of this NodePoolStatus.
        :type: str
        """
        self._job_id = job_id

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
        if not isinstance(other, NodePoolStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
