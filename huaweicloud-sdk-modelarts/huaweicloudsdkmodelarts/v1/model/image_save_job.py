# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageSaveJob:

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
        'namespace': 'str',
        'tag': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'tag': 'tag',
        'description': 'description'
    }

    def __init__(self, name=None, namespace=None, tag=None, description=None):
        r"""ImageSaveJob

        The model defined in huaweicloud sdk

        :param name: 镜像名称，长度限制512个字符，支持小写字母、数字、中划线、下划线和点。
        :type name: str
        :param namespace: 镜像所属组织，可以在SWR控制台“组织管理”创建和查看。
        :type namespace: str
        :param tag: 镜像tag，长度限制64个字符， 支持大小写字母、数字、中划线、下划线和点。
        :type tag: str
        :param description: 该镜像所对应的描述信息，长度限制512个字符。
        :type description: str
        """
        
        

        self._name = None
        self._namespace = None
        self._tag = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if tag is not None:
            self.tag = tag
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this ImageSaveJob.

        镜像名称，长度限制512个字符，支持小写字母、数字、中划线、下划线和点。

        :return: The name of this ImageSaveJob.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ImageSaveJob.

        镜像名称，长度限制512个字符，支持小写字母、数字、中划线、下划线和点。

        :param name: The name of this ImageSaveJob.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this ImageSaveJob.

        镜像所属组织，可以在SWR控制台“组织管理”创建和查看。

        :return: The namespace of this ImageSaveJob.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ImageSaveJob.

        镜像所属组织，可以在SWR控制台“组织管理”创建和查看。

        :param namespace: The namespace of this ImageSaveJob.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def tag(self):
        r"""Gets the tag of this ImageSaveJob.

        镜像tag，长度限制64个字符， 支持大小写字母、数字、中划线、下划线和点。

        :return: The tag of this ImageSaveJob.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ImageSaveJob.

        镜像tag，长度限制64个字符， 支持大小写字母、数字、中划线、下划线和点。

        :param tag: The tag of this ImageSaveJob.
        :type tag: str
        """
        self._tag = tag

    @property
    def description(self):
        r"""Gets the description of this ImageSaveJob.

        该镜像所对应的描述信息，长度限制512个字符。

        :return: The description of this ImageSaveJob.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ImageSaveJob.

        该镜像所对应的描述信息，长度限制512个字符。

        :param description: The description of this ImageSaveJob.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ImageSaveJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
