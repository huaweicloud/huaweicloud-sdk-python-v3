# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterClusterMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uid': 'str',
        'name': 'str',
        'labels': 'dict(str, str)',
        'annotations': 'dict(str, str)'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'labels': 'labels',
        'annotations': 'annotations'
    }

    def __init__(self, uid=None, name=None, labels=None, annotations=None):
        r"""RegisterClusterMetadata

        The model defined in huaweicloud sdk

        :param uid: 集群ID信息，仅在注册CCE导入集群时使用，其他类型集群无需填写。
        :type uid: str
        :param name: CCE集群填写CCE集群名称，其他类型集群自定义
        :type name: str
        :param labels: 标签信息。可为空，不为空时，必须满足kurbenetes label规范,最多可支持100个标签。
        :type labels: dict(str, str)
        :param annotations: 集群annotations信息。 附着集群必填一个kubeconfig字段，取值是kubeconfig文件的内容。kubeconfig文件获取方法请参见[获取KubeConfig文件](https://support.huaweicloud.com/usermanual-ucs/ucs_01_0138.html)
        :type annotations: dict(str, str)
        """
        
        

        self._uid = None
        self._name = None
        self._labels = None
        self._annotations = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        self.name = name
        if labels is not None:
            self.labels = labels
        if annotations is not None:
            self.annotations = annotations

    @property
    def uid(self):
        r"""Gets the uid of this RegisterClusterMetadata.

        集群ID信息，仅在注册CCE导入集群时使用，其他类型集群无需填写。

        :return: The uid of this RegisterClusterMetadata.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this RegisterClusterMetadata.

        集群ID信息，仅在注册CCE导入集群时使用，其他类型集群无需填写。

        :param uid: The uid of this RegisterClusterMetadata.
        :type uid: str
        """
        self._uid = uid

    @property
    def name(self):
        r"""Gets the name of this RegisterClusterMetadata.

        CCE集群填写CCE集群名称，其他类型集群自定义

        :return: The name of this RegisterClusterMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RegisterClusterMetadata.

        CCE集群填写CCE集群名称，其他类型集群自定义

        :param name: The name of this RegisterClusterMetadata.
        :type name: str
        """
        self._name = name

    @property
    def labels(self):
        r"""Gets the labels of this RegisterClusterMetadata.

        标签信息。可为空，不为空时，必须满足kurbenetes label规范,最多可支持100个标签。

        :return: The labels of this RegisterClusterMetadata.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this RegisterClusterMetadata.

        标签信息。可为空，不为空时，必须满足kurbenetes label规范,最多可支持100个标签。

        :param labels: The labels of this RegisterClusterMetadata.
        :type labels: dict(str, str)
        """
        self._labels = labels

    @property
    def annotations(self):
        r"""Gets the annotations of this RegisterClusterMetadata.

        集群annotations信息。 附着集群必填一个kubeconfig字段，取值是kubeconfig文件的内容。kubeconfig文件获取方法请参见[获取KubeConfig文件](https://support.huaweicloud.com/usermanual-ucs/ucs_01_0138.html)

        :return: The annotations of this RegisterClusterMetadata.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this RegisterClusterMetadata.

        集群annotations信息。 附着集群必填一个kubeconfig字段，取值是kubeconfig文件的内容。kubeconfig文件获取方法请参见[获取KubeConfig文件](https://support.huaweicloud.com/usermanual-ucs/ucs_01_0138.html)

        :param annotations: The annotations of this RegisterClusterMetadata.
        :type annotations: dict(str, str)
        """
        self._annotations = annotations

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
        if not isinstance(other, RegisterClusterMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
