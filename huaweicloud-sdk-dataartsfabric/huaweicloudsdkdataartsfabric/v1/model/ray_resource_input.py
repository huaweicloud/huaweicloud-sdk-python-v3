# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RayResourceInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'head_node_resource': 'HeadNodeResourceDemand',
        'work_node_resources': 'list[WorkNodeResourceDemand]'
    }

    attribute_map = {
        'head_node_resource': 'head_node_resource',
        'work_node_resources': 'work_node_resources'
    }

    def __init__(self, head_node_resource=None, work_node_resources=None):
        r"""RayResourceInput

        The model defined in huaweicloud sdk

        :param head_node_resource: 
        :type head_node_resource: :class:`huaweicloudsdkdataartsfabric.v1.HeadNodeResourceDemand`
        :param work_node_resources: 工作节点资源配置
        :type work_node_resources: list[:class:`huaweicloudsdkdataartsfabric.v1.WorkNodeResourceDemand`]
        """
        
        

        self._head_node_resource = None
        self._work_node_resources = None
        self.discriminator = None

        self.head_node_resource = head_node_resource
        self.work_node_resources = work_node_resources

    @property
    def head_node_resource(self):
        r"""Gets the head_node_resource of this RayResourceInput.

        :return: The head_node_resource of this RayResourceInput.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.HeadNodeResourceDemand`
        """
        return self._head_node_resource

    @head_node_resource.setter
    def head_node_resource(self, head_node_resource):
        r"""Sets the head_node_resource of this RayResourceInput.

        :param head_node_resource: The head_node_resource of this RayResourceInput.
        :type head_node_resource: :class:`huaweicloudsdkdataartsfabric.v1.HeadNodeResourceDemand`
        """
        self._head_node_resource = head_node_resource

    @property
    def work_node_resources(self):
        r"""Gets the work_node_resources of this RayResourceInput.

        工作节点资源配置

        :return: The work_node_resources of this RayResourceInput.
        :rtype: list[:class:`huaweicloudsdkdataartsfabric.v1.WorkNodeResourceDemand`]
        """
        return self._work_node_resources

    @work_node_resources.setter
    def work_node_resources(self, work_node_resources):
        r"""Sets the work_node_resources of this RayResourceInput.

        工作节点资源配置

        :param work_node_resources: The work_node_resources of this RayResourceInput.
        :type work_node_resources: list[:class:`huaweicloudsdkdataartsfabric.v1.WorkNodeResourceDemand`]
        """
        self._work_node_resources = work_node_resources

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
        if not isinstance(other, RayResourceInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
