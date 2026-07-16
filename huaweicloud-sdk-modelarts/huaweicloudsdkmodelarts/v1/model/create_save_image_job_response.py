# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSaveImageJobResponse(SdkResponse):

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
        'description': 'str',
        'status': 'str',
        'message': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'tag': 'tag',
        'description': 'description',
        'status': 'status',
        'message': 'message',
        'create_time': 'create_time'
    }

    def __init__(self, name=None, namespace=None, tag=None, description=None, status=None, message=None, create_time=None):
        r"""CreateSaveImageJobResponse

        The model defined in huaweicloud sdk

        :param name: 镜像名称，长度限制512个字符，支持小写字母、数字、中划线、下划线和点。
        :type name: str
        :param namespace: 镜像所属组织，可以在SWR控制台“组织管理”创建和查看。
        :type namespace: str
        :param tag: 镜像tag，长度限制64个字符， 支持大小写字母、数字、中划线、下划线和点。
        :type tag: str
        :param description: 该镜像所对应的描述信息，长度限制512个字符。
        :type description: str
        :param status: 镜像状态。枚举值如下： - INIT：初始化。 - CREATING：镜像保存中，此时训练作业不可用。 - CREATE_FAILED：镜像保存失败。 - ACTIVE：镜像保存成功，保存的镜像可以在SWR控制台查看，同时可以基于保存的镜像创建训练作业。
        :type status: str
        :param message: 镜像创建的时间，UTC毫秒。
        :type message: str
        :param create_time: 镜像保存操作过程中，展示构建信息。
        :type create_time: int
        """
        
        super().__init__()

        self._name = None
        self._namespace = None
        self._tag = None
        self._description = None
        self._status = None
        self._message = None
        self._create_time = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if tag is not None:
            self.tag = tag
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if create_time is not None:
            self.create_time = create_time

    @property
    def name(self):
        r"""Gets the name of this CreateSaveImageJobResponse.

        镜像名称，长度限制512个字符，支持小写字母、数字、中划线、下划线和点。

        :return: The name of this CreateSaveImageJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateSaveImageJobResponse.

        镜像名称，长度限制512个字符，支持小写字母、数字、中划线、下划线和点。

        :param name: The name of this CreateSaveImageJobResponse.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this CreateSaveImageJobResponse.

        镜像所属组织，可以在SWR控制台“组织管理”创建和查看。

        :return: The namespace of this CreateSaveImageJobResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this CreateSaveImageJobResponse.

        镜像所属组织，可以在SWR控制台“组织管理”创建和查看。

        :param namespace: The namespace of this CreateSaveImageJobResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def tag(self):
        r"""Gets the tag of this CreateSaveImageJobResponse.

        镜像tag，长度限制64个字符， 支持大小写字母、数字、中划线、下划线和点。

        :return: The tag of this CreateSaveImageJobResponse.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this CreateSaveImageJobResponse.

        镜像tag，长度限制64个字符， 支持大小写字母、数字、中划线、下划线和点。

        :param tag: The tag of this CreateSaveImageJobResponse.
        :type tag: str
        """
        self._tag = tag

    @property
    def description(self):
        r"""Gets the description of this CreateSaveImageJobResponse.

        该镜像所对应的描述信息，长度限制512个字符。

        :return: The description of this CreateSaveImageJobResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateSaveImageJobResponse.

        该镜像所对应的描述信息，长度限制512个字符。

        :param description: The description of this CreateSaveImageJobResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this CreateSaveImageJobResponse.

        镜像状态。枚举值如下： - INIT：初始化。 - CREATING：镜像保存中，此时训练作业不可用。 - CREATE_FAILED：镜像保存失败。 - ACTIVE：镜像保存成功，保存的镜像可以在SWR控制台查看，同时可以基于保存的镜像创建训练作业。

        :return: The status of this CreateSaveImageJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateSaveImageJobResponse.

        镜像状态。枚举值如下： - INIT：初始化。 - CREATING：镜像保存中，此时训练作业不可用。 - CREATE_FAILED：镜像保存失败。 - ACTIVE：镜像保存成功，保存的镜像可以在SWR控制台查看，同时可以基于保存的镜像创建训练作业。

        :param status: The status of this CreateSaveImageJobResponse.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this CreateSaveImageJobResponse.

        镜像创建的时间，UTC毫秒。

        :return: The message of this CreateSaveImageJobResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CreateSaveImageJobResponse.

        镜像创建的时间，UTC毫秒。

        :param message: The message of this CreateSaveImageJobResponse.
        :type message: str
        """
        self._message = message

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateSaveImageJobResponse.

        镜像保存操作过程中，展示构建信息。

        :return: The create_time of this CreateSaveImageJobResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateSaveImageJobResponse.

        镜像保存操作过程中，展示构建信息。

        :param create_time: The create_time of this CreateSaveImageJobResponse.
        :type create_time: int
        """
        self._create_time = create_time

    def to_dict(self):
        import warnings
        warnings.warn("CreateSaveImageJobResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateSaveImageJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
