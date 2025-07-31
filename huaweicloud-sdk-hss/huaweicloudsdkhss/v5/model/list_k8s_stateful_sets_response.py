# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListK8sStatefulSetsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'last_update_time': 'int',
        'statefulset_info_list': 'list[ServerlessStatefulSetInfo]'
    }

    attribute_map = {
        'total_num': 'total_num',
        'last_update_time': 'last_update_time',
        'statefulset_info_list': 'statefulset_info_list'
    }

    def __init__(self, total_num=None, last_update_time=None, statefulset_info_list=None):
        r"""ListK8sStatefulSetsResponse

        The model defined in huaweicloud sdk

        :param total_num: 有状态工作负载总量
        :type total_num: int
        :param last_update_time: 最近更新时间
        :type last_update_time: int
        :param statefulset_info_list: 有状态工作负载基本信息列表
        :type statefulset_info_list: list[:class:`huaweicloudsdkhss.v5.ServerlessStatefulSetInfo`]
        """
        
        super(ListK8sStatefulSetsResponse, self).__init__()

        self._total_num = None
        self._last_update_time = None
        self._statefulset_info_list = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if statefulset_info_list is not None:
            self.statefulset_info_list = statefulset_info_list

    @property
    def total_num(self):
        r"""Gets the total_num of this ListK8sStatefulSetsResponse.

        有状态工作负载总量

        :return: The total_num of this ListK8sStatefulSetsResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListK8sStatefulSetsResponse.

        有状态工作负载总量

        :param total_num: The total_num of this ListK8sStatefulSetsResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this ListK8sStatefulSetsResponse.

        最近更新时间

        :return: The last_update_time of this ListK8sStatefulSetsResponse.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this ListK8sStatefulSetsResponse.

        最近更新时间

        :param last_update_time: The last_update_time of this ListK8sStatefulSetsResponse.
        :type last_update_time: int
        """
        self._last_update_time = last_update_time

    @property
    def statefulset_info_list(self):
        r"""Gets the statefulset_info_list of this ListK8sStatefulSetsResponse.

        有状态工作负载基本信息列表

        :return: The statefulset_info_list of this ListK8sStatefulSetsResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ServerlessStatefulSetInfo`]
        """
        return self._statefulset_info_list

    @statefulset_info_list.setter
    def statefulset_info_list(self, statefulset_info_list):
        r"""Sets the statefulset_info_list of this ListK8sStatefulSetsResponse.

        有状态工作负载基本信息列表

        :param statefulset_info_list: The statefulset_info_list of this ListK8sStatefulSetsResponse.
        :type statefulset_info_list: list[:class:`huaweicloudsdkhss.v5.ServerlessStatefulSetInfo`]
        """
        self._statefulset_info_list = statefulset_info_list

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
        if not isinstance(other, ListK8sStatefulSetsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
