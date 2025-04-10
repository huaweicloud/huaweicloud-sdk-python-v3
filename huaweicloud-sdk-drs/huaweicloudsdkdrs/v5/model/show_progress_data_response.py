# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProgressDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'create_time': 'str',
        'flow_compare_data': 'list[FlowCompareData]'
    }

    attribute_map = {
        'count': 'count',
        'create_time': 'create_time',
        'flow_compare_data': 'flow_compare_data'
    }

    def __init__(self, count=None, create_time=None, flow_compare_data=None):
        r"""ShowProgressDataResponse

        The model defined in huaweicloud sdk

        :param count: 总数。
        :type count: int
        :param create_time: 数据生成时间，UTC时间，例如：2020-09-01T18:50:20.200Z
        :type create_time: str
        :param flow_compare_data: 对比结果。
        :type flow_compare_data: list[:class:`huaweicloudsdkdrs.v5.FlowCompareData`]
        """
        
        super(ShowProgressDataResponse, self).__init__()

        self._count = None
        self._create_time = None
        self._flow_compare_data = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if create_time is not None:
            self.create_time = create_time
        if flow_compare_data is not None:
            self.flow_compare_data = flow_compare_data

    @property
    def count(self):
        r"""Gets the count of this ShowProgressDataResponse.

        总数。

        :return: The count of this ShowProgressDataResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowProgressDataResponse.

        总数。

        :param count: The count of this ShowProgressDataResponse.
        :type count: int
        """
        self._count = count

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowProgressDataResponse.

        数据生成时间，UTC时间，例如：2020-09-01T18:50:20.200Z

        :return: The create_time of this ShowProgressDataResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowProgressDataResponse.

        数据生成时间，UTC时间，例如：2020-09-01T18:50:20.200Z

        :param create_time: The create_time of this ShowProgressDataResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def flow_compare_data(self):
        r"""Gets the flow_compare_data of this ShowProgressDataResponse.

        对比结果。

        :return: The flow_compare_data of this ShowProgressDataResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.FlowCompareData`]
        """
        return self._flow_compare_data

    @flow_compare_data.setter
    def flow_compare_data(self, flow_compare_data):
        r"""Sets the flow_compare_data of this ShowProgressDataResponse.

        对比结果。

        :param flow_compare_data: The flow_compare_data of this ShowProgressDataResponse.
        :type flow_compare_data: list[:class:`huaweicloudsdkdrs.v5.FlowCompareData`]
        """
        self._flow_compare_data = flow_compare_data

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
        if not isinstance(other, ShowProgressDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
