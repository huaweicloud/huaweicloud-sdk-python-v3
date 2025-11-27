# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTransitSubnetOption:

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
        'description': 'str',
        'virsubnet_id': 'str',
        'virsubnet_project_id': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'virsubnet_id': 'virsubnet_id',
        'virsubnet_project_id': 'virsubnet_project_id',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, virsubnet_id=None, virsubnet_project_id=None, tags=None):
        r"""CreateTransitSubnetOption

        The model defined in huaweicloud sdk

        :param name: 中转子网的名字。仅支持数字、字母、_（下划线）、-（中划线）、中文。
        :type name: str
        :param description: 中转子网的描述。长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param virsubnet_id: 中转子网的子网ID。
        :type virsubnet_id: str
        :param virsubnet_project_id: 中转子网的子网所属的项目ID。仅支持数字和小写字母。
        :type virsubnet_project_id: str
        :param tags: tag标签。
        :type tags: list[:class:`huaweicloudsdknat.v2.Tag`]
        """
        
        

        self._name = None
        self._description = None
        self._virsubnet_id = None
        self._virsubnet_project_id = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.virsubnet_id = virsubnet_id
        self.virsubnet_project_id = virsubnet_project_id
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this CreateTransitSubnetOption.

        中转子网的名字。仅支持数字、字母、_（下划线）、-（中划线）、中文。

        :return: The name of this CreateTransitSubnetOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateTransitSubnetOption.

        中转子网的名字。仅支持数字、字母、_（下划线）、-（中划线）、中文。

        :param name: The name of this CreateTransitSubnetOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateTransitSubnetOption.

        中转子网的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this CreateTransitSubnetOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateTransitSubnetOption.

        中转子网的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this CreateTransitSubnetOption.
        :type description: str
        """
        self._description = description

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this CreateTransitSubnetOption.

        中转子网的子网ID。

        :return: The virsubnet_id of this CreateTransitSubnetOption.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this CreateTransitSubnetOption.

        中转子网的子网ID。

        :param virsubnet_id: The virsubnet_id of this CreateTransitSubnetOption.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def virsubnet_project_id(self):
        r"""Gets the virsubnet_project_id of this CreateTransitSubnetOption.

        中转子网的子网所属的项目ID。仅支持数字和小写字母。

        :return: The virsubnet_project_id of this CreateTransitSubnetOption.
        :rtype: str
        """
        return self._virsubnet_project_id

    @virsubnet_project_id.setter
    def virsubnet_project_id(self, virsubnet_project_id):
        r"""Sets the virsubnet_project_id of this CreateTransitSubnetOption.

        中转子网的子网所属的项目ID。仅支持数字和小写字母。

        :param virsubnet_project_id: The virsubnet_project_id of this CreateTransitSubnetOption.
        :type virsubnet_project_id: str
        """
        self._virsubnet_project_id = virsubnet_project_id

    @property
    def tags(self):
        r"""Gets the tags of this CreateTransitSubnetOption.

        tag标签。

        :return: The tags of this CreateTransitSubnetOption.
        :rtype: list[:class:`huaweicloudsdknat.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateTransitSubnetOption.

        tag标签。

        :param tags: The tags of this CreateTransitSubnetOption.
        :type tags: list[:class:`huaweicloudsdknat.v2.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateTransitSubnetOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
