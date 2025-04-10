# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterCheckStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phase': 'str',
        'items_status': 'list[PreCheckItemStatus]'
    }

    attribute_map = {
        'phase': 'phase',
        'items_status': 'itemsStatus'
    }

    def __init__(self, phase=None, items_status=None):
        r"""ClusterCheckStatus

        The model defined in huaweicloud sdk

        :param phase: 状态，取值如下 - Init: 初始化 - Running 运行中 - Success 成功 - Failed 失败
        :type phase: str
        :param items_status: 检查项状态集合
        :type items_status: list[:class:`huaweicloudsdkcce.v3.PreCheckItemStatus`]
        """
        
        

        self._phase = None
        self._items_status = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase
        if items_status is not None:
            self.items_status = items_status

    @property
    def phase(self):
        r"""Gets the phase of this ClusterCheckStatus.

        状态，取值如下 - Init: 初始化 - Running 运行中 - Success 成功 - Failed 失败

        :return: The phase of this ClusterCheckStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this ClusterCheckStatus.

        状态，取值如下 - Init: 初始化 - Running 运行中 - Success 成功 - Failed 失败

        :param phase: The phase of this ClusterCheckStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def items_status(self):
        r"""Gets the items_status of this ClusterCheckStatus.

        检查项状态集合

        :return: The items_status of this ClusterCheckStatus.
        :rtype: list[:class:`huaweicloudsdkcce.v3.PreCheckItemStatus`]
        """
        return self._items_status

    @items_status.setter
    def items_status(self, items_status):
        r"""Sets the items_status of this ClusterCheckStatus.

        检查项状态集合

        :param items_status: The items_status of this ClusterCheckStatus.
        :type items_status: list[:class:`huaweicloudsdkcce.v3.PreCheckItemStatus`]
        """
        self._items_status = items_status

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
        if not isinstance(other, ClusterCheckStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
