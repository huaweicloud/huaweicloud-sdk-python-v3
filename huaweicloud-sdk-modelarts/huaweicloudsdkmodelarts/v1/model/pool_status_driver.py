# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolStatusDriver:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gpu': 'PoolDriverStatus',
        'npu': 'PoolDriverStatus'
    }

    attribute_map = {
        'gpu': 'gpu',
        'npu': 'npu'
    }

    def __init__(self, gpu=None, npu=None):
        r"""PoolStatusDriver

        The model defined in huaweicloud sdk

        :param gpu: 
        :type gpu: :class:`huaweicloudsdkmodelarts.v1.PoolDriverStatus`
        :param npu: 
        :type npu: :class:`huaweicloudsdkmodelarts.v1.PoolDriverStatus`
        """
        
        

        self._gpu = None
        self._npu = None
        self.discriminator = None

        if gpu is not None:
            self.gpu = gpu
        if npu is not None:
            self.npu = npu

    @property
    def gpu(self):
        r"""Gets the gpu of this PoolStatusDriver.

        :return: The gpu of this PoolStatusDriver.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolDriverStatus`
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        r"""Sets the gpu of this PoolStatusDriver.

        :param gpu: The gpu of this PoolStatusDriver.
        :type gpu: :class:`huaweicloudsdkmodelarts.v1.PoolDriverStatus`
        """
        self._gpu = gpu

    @property
    def npu(self):
        r"""Gets the npu of this PoolStatusDriver.

        :return: The npu of this PoolStatusDriver.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolDriverStatus`
        """
        return self._npu

    @npu.setter
    def npu(self, npu):
        r"""Sets the npu of this PoolStatusDriver.

        :param npu: The npu of this PoolStatusDriver.
        :type npu: :class:`huaweicloudsdkmodelarts.v1.PoolDriverStatus`
        """
        self._npu = npu

    def to_dict(self):
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
        if not isinstance(other, PoolStatusDriver):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
