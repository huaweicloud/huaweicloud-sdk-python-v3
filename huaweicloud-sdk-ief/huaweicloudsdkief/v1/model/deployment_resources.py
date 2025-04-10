# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeploymentResources:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limits': 'dict(str, str)',
        'requests': 'dict(str, str)'
    }

    attribute_map = {
        'limits': 'limits',
        'requests': 'requests'
    }

    def __init__(self, limits=None, requests=None):
        r"""DeploymentResources

        The model defined in huaweicloud sdk

        :param limits: - 允许容器使用的最大资源，key值支持填写：cpu, memory, gpu, npu。 - 申请NPU资源时可填写指定的NPU芯片类型，支持填写：D310、D310B。注意：key值填写为npu时，默认使用npu_type字段指定的芯片类型。如果npu_type字段为空，默认使用D310芯片类型。
        :type limits: dict(str, str)
        :param requests: - 容器需要使用的最小资源，key值支持填写：cpu, memory, gpu, npu - 申请NPU资源时可填写指定的NPU芯片类型，支持填写：D310、D310B。注意：key值填写为npu时，默认使用npu_type字段指定的芯片类型。如果npu_type字段为空，默认使用D310芯片类型。
        :type requests: dict(str, str)
        """
        
        

        self._limits = None
        self._requests = None
        self.discriminator = None

        if limits is not None:
            self.limits = limits
        if requests is not None:
            self.requests = requests

    @property
    def limits(self):
        r"""Gets the limits of this DeploymentResources.

        - 允许容器使用的最大资源，key值支持填写：cpu, memory, gpu, npu。 - 申请NPU资源时可填写指定的NPU芯片类型，支持填写：D310、D310B。注意：key值填写为npu时，默认使用npu_type字段指定的芯片类型。如果npu_type字段为空，默认使用D310芯片类型。

        :return: The limits of this DeploymentResources.
        :rtype: dict(str, str)
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        r"""Sets the limits of this DeploymentResources.

        - 允许容器使用的最大资源，key值支持填写：cpu, memory, gpu, npu。 - 申请NPU资源时可填写指定的NPU芯片类型，支持填写：D310、D310B。注意：key值填写为npu时，默认使用npu_type字段指定的芯片类型。如果npu_type字段为空，默认使用D310芯片类型。

        :param limits: The limits of this DeploymentResources.
        :type limits: dict(str, str)
        """
        self._limits = limits

    @property
    def requests(self):
        r"""Gets the requests of this DeploymentResources.

        - 容器需要使用的最小资源，key值支持填写：cpu, memory, gpu, npu - 申请NPU资源时可填写指定的NPU芯片类型，支持填写：D310、D310B。注意：key值填写为npu时，默认使用npu_type字段指定的芯片类型。如果npu_type字段为空，默认使用D310芯片类型。

        :return: The requests of this DeploymentResources.
        :rtype: dict(str, str)
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        r"""Sets the requests of this DeploymentResources.

        - 容器需要使用的最小资源，key值支持填写：cpu, memory, gpu, npu - 申请NPU资源时可填写指定的NPU芯片类型，支持填写：D310、D310B。注意：key值填写为npu时，默认使用npu_type字段指定的芯片类型。如果npu_type字段为空，默认使用D310芯片类型。

        :param requests: The requests of this DeploymentResources.
        :type requests: dict(str, str)
        """
        self._requests = requests

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
        if not isinstance(other, DeploymentResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
