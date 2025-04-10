# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RayResourceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'head_group_spec': 'HeadGroupSpec',
        'worker_group_spec': 'list[WorkerGroupSpec]'
    }

    attribute_map = {
        'head_group_spec': 'head_group_spec',
        'worker_group_spec': 'worker_group_spec'
    }

    def __init__(self, head_group_spec=None, worker_group_spec=None):
        r"""RayResourceInfo

        The model defined in huaweicloud sdk

        :param head_group_spec: 
        :type head_group_spec: :class:`huaweicloudsdkdataartsfabric.v1.HeadGroupSpec`
        :param worker_group_spec: Ray worker group配置
        :type worker_group_spec: list[:class:`huaweicloudsdkdataartsfabric.v1.WorkerGroupSpec`]
        """
        
        

        self._head_group_spec = None
        self._worker_group_spec = None
        self.discriminator = None

        if head_group_spec is not None:
            self.head_group_spec = head_group_spec
        if worker_group_spec is not None:
            self.worker_group_spec = worker_group_spec

    @property
    def head_group_spec(self):
        r"""Gets the head_group_spec of this RayResourceInfo.

        :return: The head_group_spec of this RayResourceInfo.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.HeadGroupSpec`
        """
        return self._head_group_spec

    @head_group_spec.setter
    def head_group_spec(self, head_group_spec):
        r"""Sets the head_group_spec of this RayResourceInfo.

        :param head_group_spec: The head_group_spec of this RayResourceInfo.
        :type head_group_spec: :class:`huaweicloudsdkdataartsfabric.v1.HeadGroupSpec`
        """
        self._head_group_spec = head_group_spec

    @property
    def worker_group_spec(self):
        r"""Gets the worker_group_spec of this RayResourceInfo.

        Ray worker group配置

        :return: The worker_group_spec of this RayResourceInfo.
        :rtype: list[:class:`huaweicloudsdkdataartsfabric.v1.WorkerGroupSpec`]
        """
        return self._worker_group_spec

    @worker_group_spec.setter
    def worker_group_spec(self, worker_group_spec):
        r"""Sets the worker_group_spec of this RayResourceInfo.

        Ray worker group配置

        :param worker_group_spec: The worker_group_spec of this RayResourceInfo.
        :type worker_group_spec: list[:class:`huaweicloudsdkdataartsfabric.v1.WorkerGroupSpec`]
        """
        self._worker_group_spec = worker_group_spec

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
        if not isinstance(other, RayResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
