# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetInstancesOpsResourceUsageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu': 'ResourceUsage',
        'mem': 'ResourceUsage',
        'disk': 'ResourceUsage',
        'io': 'ResourceUsage'
    }

    attribute_map = {
        'cpu': 'cpu',
        'mem': 'mem',
        'disk': 'disk',
        'io': 'io'
    }

    def __init__(self, cpu=None, mem=None, disk=None, io=None):
        r"""GetInstancesOpsResourceUsageResponse

        The model defined in huaweicloud sdk

        :param cpu: 
        :type cpu: :class:`huaweicloudsdkrds.v3.ResourceUsage`
        :param mem: 
        :type mem: :class:`huaweicloudsdkrds.v3.ResourceUsage`
        :param disk: 
        :type disk: :class:`huaweicloudsdkrds.v3.ResourceUsage`
        :param io: 
        :type io: :class:`huaweicloudsdkrds.v3.ResourceUsage`
        """
        
        super().__init__()

        self._cpu = None
        self._mem = None
        self._disk = None
        self._io = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if mem is not None:
            self.mem = mem
        if disk is not None:
            self.disk = disk
        if io is not None:
            self.io = io

    @property
    def cpu(self):
        r"""Gets the cpu of this GetInstancesOpsResourceUsageResponse.

        :return: The cpu of this GetInstancesOpsResourceUsageResponse.
        :rtype: :class:`huaweicloudsdkrds.v3.ResourceUsage`
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this GetInstancesOpsResourceUsageResponse.

        :param cpu: The cpu of this GetInstancesOpsResourceUsageResponse.
        :type cpu: :class:`huaweicloudsdkrds.v3.ResourceUsage`
        """
        self._cpu = cpu

    @property
    def mem(self):
        r"""Gets the mem of this GetInstancesOpsResourceUsageResponse.

        :return: The mem of this GetInstancesOpsResourceUsageResponse.
        :rtype: :class:`huaweicloudsdkrds.v3.ResourceUsage`
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        r"""Sets the mem of this GetInstancesOpsResourceUsageResponse.

        :param mem: The mem of this GetInstancesOpsResourceUsageResponse.
        :type mem: :class:`huaweicloudsdkrds.v3.ResourceUsage`
        """
        self._mem = mem

    @property
    def disk(self):
        r"""Gets the disk of this GetInstancesOpsResourceUsageResponse.

        :return: The disk of this GetInstancesOpsResourceUsageResponse.
        :rtype: :class:`huaweicloudsdkrds.v3.ResourceUsage`
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        r"""Sets the disk of this GetInstancesOpsResourceUsageResponse.

        :param disk: The disk of this GetInstancesOpsResourceUsageResponse.
        :type disk: :class:`huaweicloudsdkrds.v3.ResourceUsage`
        """
        self._disk = disk

    @property
    def io(self):
        r"""Gets the io of this GetInstancesOpsResourceUsageResponse.

        :return: The io of this GetInstancesOpsResourceUsageResponse.
        :rtype: :class:`huaweicloudsdkrds.v3.ResourceUsage`
        """
        return self._io

    @io.setter
    def io(self, io):
        r"""Sets the io of this GetInstancesOpsResourceUsageResponse.

        :param io: The io of this GetInstancesOpsResourceUsageResponse.
        :type io: :class:`huaweicloudsdkrds.v3.ResourceUsage`
        """
        self._io = io

    def to_dict(self):
        import warnings
        warnings.warn("GetInstancesOpsResourceUsageResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetInstancesOpsResourceUsageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
