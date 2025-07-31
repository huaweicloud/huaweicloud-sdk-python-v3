# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployTemplateInfoScheduleInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_selector': 'list[str]',
        'pod_tolerances': 'list[str]'
    }

    attribute_map = {
        'node_selector': 'node_selector',
        'pod_tolerances': 'pod_tolerances'
    }

    def __init__(self, node_selector=None, pod_tolerances=None):
        r"""DeployTemplateInfoScheduleInfo

        The model defined in huaweicloud sdk

        :param node_selector: 节点选择器
        :type node_selector: list[str]
        :param pod_tolerances: pod容忍度
        :type pod_tolerances: list[str]
        """
        
        

        self._node_selector = None
        self._pod_tolerances = None
        self.discriminator = None

        if node_selector is not None:
            self.node_selector = node_selector
        if pod_tolerances is not None:
            self.pod_tolerances = pod_tolerances

    @property
    def node_selector(self):
        r"""Gets the node_selector of this DeployTemplateInfoScheduleInfo.

        节点选择器

        :return: The node_selector of this DeployTemplateInfoScheduleInfo.
        :rtype: list[str]
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        r"""Sets the node_selector of this DeployTemplateInfoScheduleInfo.

        节点选择器

        :param node_selector: The node_selector of this DeployTemplateInfoScheduleInfo.
        :type node_selector: list[str]
        """
        self._node_selector = node_selector

    @property
    def pod_tolerances(self):
        r"""Gets the pod_tolerances of this DeployTemplateInfoScheduleInfo.

        pod容忍度

        :return: The pod_tolerances of this DeployTemplateInfoScheduleInfo.
        :rtype: list[str]
        """
        return self._pod_tolerances

    @pod_tolerances.setter
    def pod_tolerances(self, pod_tolerances):
        r"""Sets the pod_tolerances of this DeployTemplateInfoScheduleInfo.

        pod容忍度

        :param pod_tolerances: The pod_tolerances of this DeployTemplateInfoScheduleInfo.
        :type pod_tolerances: list[str]
        """
        self._pod_tolerances = pod_tolerances

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
        if not isinstance(other, DeployTemplateInfoScheduleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
