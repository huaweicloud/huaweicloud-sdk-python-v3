# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeClusterRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scale_out': 'ScaleOut',
        'create_node_only': 'bool',
        'waiting_for_killing': 'int',
        'auto_redistribute': 'bool'
    }

    attribute_map = {
        'scale_out': 'scale_out',
        'create_node_only': 'create_node_only',
        'waiting_for_killing': 'waiting_for_killing',
        'auto_redistribute': 'auto_redistribute'
    }

    def __init__(self, scale_out=None, create_node_only=None, waiting_for_killing=None, auto_redistribute=None):
        r"""ResizeClusterRequestBody

        The model defined in huaweicloud sdk

        :param scale_out: 
        :type scale_out: :class:`huaweicloudsdkdws.v2.ScaleOut`
        :param create_node_only: **参数解释**： 当前是否仅添加空闲节点。 **约束限制**： 不涉及。 **取值范围**： true：仅添加节点，如需扩容则需要单独操作 false：添加节点并扩容集群 **默认取值**： false
        :type create_node_only: bool
        :param waiting_for_killing: **参数解释**： 自动查杀作业等待时间。 **约束限制**： guestAgent插件版本8.2.1及以上才支持。 **取值范围**： 30~1200 **默认取值**： 0，即不限制。
        :type waiting_for_killing: int
        :param auto_redistribute: **参数解释**： 扩容完成后是否自动启动重分布，默认是。如果设置为false，扩容后不进行重分布，此时集群任务信息处于“待重分布”状态，无法进行其他操作。 **约束限制**： 不涉及。 **取值范围**： true：扩容后立即重分布。 false：扩容后不进行重分布，此时集群任务信息处于“待重分布”状态。 **默认取值**： true
        :type auto_redistribute: bool
        """
        
        

        self._scale_out = None
        self._create_node_only = None
        self._waiting_for_killing = None
        self._auto_redistribute = None
        self.discriminator = None

        if scale_out is not None:
            self.scale_out = scale_out
        if create_node_only is not None:
            self.create_node_only = create_node_only
        if waiting_for_killing is not None:
            self.waiting_for_killing = waiting_for_killing
        if auto_redistribute is not None:
            self.auto_redistribute = auto_redistribute

    @property
    def scale_out(self):
        r"""Gets the scale_out of this ResizeClusterRequestBody.

        :return: The scale_out of this ResizeClusterRequestBody.
        :rtype: :class:`huaweicloudsdkdws.v2.ScaleOut`
        """
        return self._scale_out

    @scale_out.setter
    def scale_out(self, scale_out):
        r"""Sets the scale_out of this ResizeClusterRequestBody.

        :param scale_out: The scale_out of this ResizeClusterRequestBody.
        :type scale_out: :class:`huaweicloudsdkdws.v2.ScaleOut`
        """
        self._scale_out = scale_out

    @property
    def create_node_only(self):
        r"""Gets the create_node_only of this ResizeClusterRequestBody.

        **参数解释**： 当前是否仅添加空闲节点。 **约束限制**： 不涉及。 **取值范围**： true：仅添加节点，如需扩容则需要单独操作 false：添加节点并扩容集群 **默认取值**： false

        :return: The create_node_only of this ResizeClusterRequestBody.
        :rtype: bool
        """
        return self._create_node_only

    @create_node_only.setter
    def create_node_only(self, create_node_only):
        r"""Sets the create_node_only of this ResizeClusterRequestBody.

        **参数解释**： 当前是否仅添加空闲节点。 **约束限制**： 不涉及。 **取值范围**： true：仅添加节点，如需扩容则需要单独操作 false：添加节点并扩容集群 **默认取值**： false

        :param create_node_only: The create_node_only of this ResizeClusterRequestBody.
        :type create_node_only: bool
        """
        self._create_node_only = create_node_only

    @property
    def waiting_for_killing(self):
        r"""Gets the waiting_for_killing of this ResizeClusterRequestBody.

        **参数解释**： 自动查杀作业等待时间。 **约束限制**： guestAgent插件版本8.2.1及以上才支持。 **取值范围**： 30~1200 **默认取值**： 0，即不限制。

        :return: The waiting_for_killing of this ResizeClusterRequestBody.
        :rtype: int
        """
        return self._waiting_for_killing

    @waiting_for_killing.setter
    def waiting_for_killing(self, waiting_for_killing):
        r"""Sets the waiting_for_killing of this ResizeClusterRequestBody.

        **参数解释**： 自动查杀作业等待时间。 **约束限制**： guestAgent插件版本8.2.1及以上才支持。 **取值范围**： 30~1200 **默认取值**： 0，即不限制。

        :param waiting_for_killing: The waiting_for_killing of this ResizeClusterRequestBody.
        :type waiting_for_killing: int
        """
        self._waiting_for_killing = waiting_for_killing

    @property
    def auto_redistribute(self):
        r"""Gets the auto_redistribute of this ResizeClusterRequestBody.

        **参数解释**： 扩容完成后是否自动启动重分布，默认是。如果设置为false，扩容后不进行重分布，此时集群任务信息处于“待重分布”状态，无法进行其他操作。 **约束限制**： 不涉及。 **取值范围**： true：扩容后立即重分布。 false：扩容后不进行重分布，此时集群任务信息处于“待重分布”状态。 **默认取值**： true

        :return: The auto_redistribute of this ResizeClusterRequestBody.
        :rtype: bool
        """
        return self._auto_redistribute

    @auto_redistribute.setter
    def auto_redistribute(self, auto_redistribute):
        r"""Sets the auto_redistribute of this ResizeClusterRequestBody.

        **参数解释**： 扩容完成后是否自动启动重分布，默认是。如果设置为false，扩容后不进行重分布，此时集群任务信息处于“待重分布”状态，无法进行其他操作。 **约束限制**： 不涉及。 **取值范围**： true：扩容后立即重分布。 false：扩容后不进行重分布，此时集群任务信息处于“待重分布”状态。 **默认取值**： true

        :param auto_redistribute: The auto_redistribute of this ResizeClusterRequestBody.
        :type auto_redistribute: bool
        """
        self._auto_redistribute = auto_redistribute

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
        if not isinstance(other, ResizeClusterRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
