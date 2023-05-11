# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BehaviorGravity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'weaken_factor': 'float',
        'view_type': 'str',
        'algo_type': 'str'
    }

    attribute_map = {
        'weaken_factor': 'weaken_factor',
        'view_type': 'view_type',
        'algo_type': 'algo_type'
    }

    def __init__(self, weaken_factor=None, view_type=None, algo_type=None):
        """BehaviorGravity

        The model defined in huaweicloud sdk

        :param weaken_factor: 衰减因子。
        :type weaken_factor: float
        :param view_type: 行为次数统计方法： - pv，访问量 - uv，独立访客
        :type view_type: str
        :param algo_type: 算法类型: - normal，通用 - time，时间
        :type algo_type: str
        """
        
        

        self._weaken_factor = None
        self._view_type = None
        self._algo_type = None
        self.discriminator = None

        if weaken_factor is not None:
            self.weaken_factor = weaken_factor
        if view_type is not None:
            self.view_type = view_type
        if algo_type is not None:
            self.algo_type = algo_type

    @property
    def weaken_factor(self):
        """Gets the weaken_factor of this BehaviorGravity.

        衰减因子。

        :return: The weaken_factor of this BehaviorGravity.
        :rtype: float
        """
        return self._weaken_factor

    @weaken_factor.setter
    def weaken_factor(self, weaken_factor):
        """Sets the weaken_factor of this BehaviorGravity.

        衰减因子。

        :param weaken_factor: The weaken_factor of this BehaviorGravity.
        :type weaken_factor: float
        """
        self._weaken_factor = weaken_factor

    @property
    def view_type(self):
        """Gets the view_type of this BehaviorGravity.

        行为次数统计方法： - pv，访问量 - uv，独立访客

        :return: The view_type of this BehaviorGravity.
        :rtype: str
        """
        return self._view_type

    @view_type.setter
    def view_type(self, view_type):
        """Sets the view_type of this BehaviorGravity.

        行为次数统计方法： - pv，访问量 - uv，独立访客

        :param view_type: The view_type of this BehaviorGravity.
        :type view_type: str
        """
        self._view_type = view_type

    @property
    def algo_type(self):
        """Gets the algo_type of this BehaviorGravity.

        算法类型: - normal，通用 - time，时间

        :return: The algo_type of this BehaviorGravity.
        :rtype: str
        """
        return self._algo_type

    @algo_type.setter
    def algo_type(self, algo_type):
        """Sets the algo_type of this BehaviorGravity.

        算法类型: - normal，通用 - time，时间

        :param algo_type: The algo_type of this BehaviorGravity.
        :type algo_type: str
        """
        self._algo_type = algo_type

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
        if not isinstance(other, BehaviorGravity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
