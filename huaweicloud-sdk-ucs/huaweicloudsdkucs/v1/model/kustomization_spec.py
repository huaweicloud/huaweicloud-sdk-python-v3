# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KustomizationSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'interval': 'str',
        'timeout': 'str',
        'source_ref': 'SourceRef',
        'target_namespace': 'str',
        'prune': 'bool'
    }

    attribute_map = {
        'path': 'path',
        'interval': 'interval',
        'timeout': 'timeout',
        'source_ref': 'sourceRef',
        'target_namespace': 'targetNamespace',
        'prune': 'prune'
    }

    def __init__(self, path=None, interval=None, timeout=None, source_ref=None, target_namespace=None, prune=None):
        r"""KustomizationSpec

        The model defined in huaweicloud sdk

        :param path: kustomization.yaml文件的路径
        :type path: str
        :param interval: 用于指定控制器执行 Kustomization同步与校验的时间间隔
        :type interval: str
        :param timeout: 用于定义验证、应用和健康检查操作的超时
        :type timeout: str
        :param source_ref: 
        :type source_ref: :class:`huaweicloudsdkucs.v1.SourceRef`
        :param target_namespace: 用于设置或覆盖kustomization.yaml文件中的命名空间
        :type target_namespace: str
        :param prune: 是否启用垃圾回收功能
        :type prune: bool
        """
        
        

        self._path = None
        self._interval = None
        self._timeout = None
        self._source_ref = None
        self._target_namespace = None
        self._prune = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if interval is not None:
            self.interval = interval
        if timeout is not None:
            self.timeout = timeout
        if source_ref is not None:
            self.source_ref = source_ref
        if target_namespace is not None:
            self.target_namespace = target_namespace
        if prune is not None:
            self.prune = prune

    @property
    def path(self):
        r"""Gets the path of this KustomizationSpec.

        kustomization.yaml文件的路径

        :return: The path of this KustomizationSpec.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this KustomizationSpec.

        kustomization.yaml文件的路径

        :param path: The path of this KustomizationSpec.
        :type path: str
        """
        self._path = path

    @property
    def interval(self):
        r"""Gets the interval of this KustomizationSpec.

        用于指定控制器执行 Kustomization同步与校验的时间间隔

        :return: The interval of this KustomizationSpec.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this KustomizationSpec.

        用于指定控制器执行 Kustomization同步与校验的时间间隔

        :param interval: The interval of this KustomizationSpec.
        :type interval: str
        """
        self._interval = interval

    @property
    def timeout(self):
        r"""Gets the timeout of this KustomizationSpec.

        用于定义验证、应用和健康检查操作的超时

        :return: The timeout of this KustomizationSpec.
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this KustomizationSpec.

        用于定义验证、应用和健康检查操作的超时

        :param timeout: The timeout of this KustomizationSpec.
        :type timeout: str
        """
        self._timeout = timeout

    @property
    def source_ref(self):
        r"""Gets the source_ref of this KustomizationSpec.

        :return: The source_ref of this KustomizationSpec.
        :rtype: :class:`huaweicloudsdkucs.v1.SourceRef`
        """
        return self._source_ref

    @source_ref.setter
    def source_ref(self, source_ref):
        r"""Sets the source_ref of this KustomizationSpec.

        :param source_ref: The source_ref of this KustomizationSpec.
        :type source_ref: :class:`huaweicloudsdkucs.v1.SourceRef`
        """
        self._source_ref = source_ref

    @property
    def target_namespace(self):
        r"""Gets the target_namespace of this KustomizationSpec.

        用于设置或覆盖kustomization.yaml文件中的命名空间

        :return: The target_namespace of this KustomizationSpec.
        :rtype: str
        """
        return self._target_namespace

    @target_namespace.setter
    def target_namespace(self, target_namespace):
        r"""Sets the target_namespace of this KustomizationSpec.

        用于设置或覆盖kustomization.yaml文件中的命名空间

        :param target_namespace: The target_namespace of this KustomizationSpec.
        :type target_namespace: str
        """
        self._target_namespace = target_namespace

    @property
    def prune(self):
        r"""Gets the prune of this KustomizationSpec.

        是否启用垃圾回收功能

        :return: The prune of this KustomizationSpec.
        :rtype: bool
        """
        return self._prune

    @prune.setter
    def prune(self, prune):
        r"""Sets the prune of this KustomizationSpec.

        是否启用垃圾回收功能

        :param prune: The prune of this KustomizationSpec.
        :type prune: bool
        """
        self._prune = prune

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
        if not isinstance(other, KustomizationSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
