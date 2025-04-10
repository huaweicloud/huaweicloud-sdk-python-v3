# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPhysicalProcessesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'physical_processes': 'list[PhysicalProcessInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'physical_processes': 'physical_processes',
        'total_count': 'total_count'
    }

    def __init__(self, physical_processes=None, total_count=None):
        r"""ShowPhysicalProcessesResponse

        The model defined in huaweicloud sdk

        :param physical_processes: 物理会话信息列表
        :type physical_processes: list[:class:`huaweicloudsdkddm.v1.PhysicalProcessInfo`]
        :param total_count: 总数
        :type total_count: int
        """
        
        super(ShowPhysicalProcessesResponse, self).__init__()

        self._physical_processes = None
        self._total_count = None
        self.discriminator = None

        if physical_processes is not None:
            self.physical_processes = physical_processes
        if total_count is not None:
            self.total_count = total_count

    @property
    def physical_processes(self):
        r"""Gets the physical_processes of this ShowPhysicalProcessesResponse.

        物理会话信息列表

        :return: The physical_processes of this ShowPhysicalProcessesResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.PhysicalProcessInfo`]
        """
        return self._physical_processes

    @physical_processes.setter
    def physical_processes(self, physical_processes):
        r"""Sets the physical_processes of this ShowPhysicalProcessesResponse.

        物理会话信息列表

        :param physical_processes: The physical_processes of this ShowPhysicalProcessesResponse.
        :type physical_processes: list[:class:`huaweicloudsdkddm.v1.PhysicalProcessInfo`]
        """
        self._physical_processes = physical_processes

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowPhysicalProcessesResponse.

        总数

        :return: The total_count of this ShowPhysicalProcessesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowPhysicalProcessesResponse.

        总数

        :param total_count: The total_count of this ShowPhysicalProcessesResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ShowPhysicalProcessesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
