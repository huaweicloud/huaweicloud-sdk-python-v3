# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlgorithmOutput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'local_dir': 'str',
        'remote': 'Remote',
        'mode': 'str',
        'period': 'str'
    }

    attribute_map = {
        'name': 'name',
        'local_dir': 'local_dir',
        'remote': 'remote',
        'mode': 'mode',
        'period': 'period'
    }

    def __init__(self, name=None, local_dir=None, remote=None, mode=None, period=None):
        r"""AlgorithmOutput

        The model defined in huaweicloud sdk

        :param name: 数据输出通道名称。
        :type name: str
        :param local_dir: 数据输出通道映射的容器本地路径。
        :type local_dir: str
        :param remote: 
        :type remote: :class:`huaweicloudsdkmodelarts.v1.Remote`
        :param mode: 数据传输模式，默认为“upload_periodically”。
        :type mode: str
        :param period: 数据传输周期，默认为30s。
        :type period: str
        """
        
        

        self._name = None
        self._local_dir = None
        self._remote = None
        self._mode = None
        self._period = None
        self.discriminator = None

        self.name = name
        if local_dir is not None:
            self.local_dir = local_dir
        self.remote = remote
        if mode is not None:
            self.mode = mode
        if period is not None:
            self.period = period

    @property
    def name(self):
        r"""Gets the name of this AlgorithmOutput.

        数据输出通道名称。

        :return: The name of this AlgorithmOutput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AlgorithmOutput.

        数据输出通道名称。

        :param name: The name of this AlgorithmOutput.
        :type name: str
        """
        self._name = name

    @property
    def local_dir(self):
        r"""Gets the local_dir of this AlgorithmOutput.

        数据输出通道映射的容器本地路径。

        :return: The local_dir of this AlgorithmOutput.
        :rtype: str
        """
        return self._local_dir

    @local_dir.setter
    def local_dir(self, local_dir):
        r"""Sets the local_dir of this AlgorithmOutput.

        数据输出通道映射的容器本地路径。

        :param local_dir: The local_dir of this AlgorithmOutput.
        :type local_dir: str
        """
        self._local_dir = local_dir

    @property
    def remote(self):
        r"""Gets the remote of this AlgorithmOutput.

        :return: The remote of this AlgorithmOutput.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Remote`
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        r"""Sets the remote of this AlgorithmOutput.

        :param remote: The remote of this AlgorithmOutput.
        :type remote: :class:`huaweicloudsdkmodelarts.v1.Remote`
        """
        self._remote = remote

    @property
    def mode(self):
        r"""Gets the mode of this AlgorithmOutput.

        数据传输模式，默认为“upload_periodically”。

        :return: The mode of this AlgorithmOutput.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this AlgorithmOutput.

        数据传输模式，默认为“upload_periodically”。

        :param mode: The mode of this AlgorithmOutput.
        :type mode: str
        """
        self._mode = mode

    @property
    def period(self):
        r"""Gets the period of this AlgorithmOutput.

        数据传输周期，默认为30s。

        :return: The period of this AlgorithmOutput.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this AlgorithmOutput.

        数据传输周期，默认为30s。

        :param period: The period of this AlgorithmOutput.
        :type period: str
        """
        self._period = period

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
        if not isinstance(other, AlgorithmOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
