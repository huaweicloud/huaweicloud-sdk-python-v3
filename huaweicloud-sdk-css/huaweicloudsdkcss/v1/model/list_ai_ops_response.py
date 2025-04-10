# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiOpsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_size': 'int',
        'aiops_list': 'list[ListAiOpsRequestBodyAiopsList]'
    }

    attribute_map = {
        'total_size': 'total_size',
        'aiops_list': 'aiops_list'
    }

    def __init__(self, total_size=None, aiops_list=None):
        r"""ListAiOpsResponse

        The model defined in huaweicloud sdk

        :param total_size: 检测任务个数。
        :type total_size: int
        :param aiops_list: 创建一个集群检测任务。
        :type aiops_list: list[:class:`huaweicloudsdkcss.v1.ListAiOpsRequestBodyAiopsList`]
        """
        
        super(ListAiOpsResponse, self).__init__()

        self._total_size = None
        self._aiops_list = None
        self.discriminator = None

        if total_size is not None:
            self.total_size = total_size
        if aiops_list is not None:
            self.aiops_list = aiops_list

    @property
    def total_size(self):
        r"""Gets the total_size of this ListAiOpsResponse.

        检测任务个数。

        :return: The total_size of this ListAiOpsResponse.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        r"""Sets the total_size of this ListAiOpsResponse.

        检测任务个数。

        :param total_size: The total_size of this ListAiOpsResponse.
        :type total_size: int
        """
        self._total_size = total_size

    @property
    def aiops_list(self):
        r"""Gets the aiops_list of this ListAiOpsResponse.

        创建一个集群检测任务。

        :return: The aiops_list of this ListAiOpsResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.ListAiOpsRequestBodyAiopsList`]
        """
        return self._aiops_list

    @aiops_list.setter
    def aiops_list(self, aiops_list):
        r"""Sets the aiops_list of this ListAiOpsResponse.

        创建一个集群检测任务。

        :param aiops_list: The aiops_list of this ListAiOpsResponse.
        :type aiops_list: list[:class:`huaweicloudsdkcss.v1.ListAiOpsRequestBodyAiopsList`]
        """
        self._aiops_list = aiops_list

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
        if not isinstance(other, ListAiOpsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
