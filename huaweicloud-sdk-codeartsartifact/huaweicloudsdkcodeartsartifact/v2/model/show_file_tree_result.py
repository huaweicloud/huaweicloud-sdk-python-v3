# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFileTreeResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'upload_access': 'str',
        'total': 'str',
        'uri': 'str',
        'created': 'str',
        'children': 'list[ShowFileTreeResultChildren]'
    }

    attribute_map = {
        'upload_access': 'uploadAccess',
        'total': 'total',
        'uri': 'uri',
        'created': 'created',
        'children': 'children'
    }

    def __init__(self, upload_access=None, total=None, uri=None, created=None, children=None):
        r"""ShowFileTreeResult

        The model defined in huaweicloud sdk

        :param upload_access: **参数解释**: 上传权限。 **取值范围**: true：有权限。 false：无权限。 
        :type upload_access: str
        :param total: **参数解释**: 总数。 **取值范围**: 不涉及。 
        :type total: str
        :param uri: **参数解释**: 父路径。 **取值范围**: 不涉及。 
        :type uri: str
        :param created: **参数解释**: 创建时间。 **取值范围**: 不涉及。 
        :type created: str
        :param children: **参数解释**: 子文件及文件夹信息。 **取值范围**: 不涉及。 
        :type children: list[:class:`huaweicloudsdkcodeartsartifact.v2.ShowFileTreeResultChildren`]
        """
        
        

        self._upload_access = None
        self._total = None
        self._uri = None
        self._created = None
        self._children = None
        self.discriminator = None

        if upload_access is not None:
            self.upload_access = upload_access
        if total is not None:
            self.total = total
        if uri is not None:
            self.uri = uri
        if created is not None:
            self.created = created
        if children is not None:
            self.children = children

    @property
    def upload_access(self):
        r"""Gets the upload_access of this ShowFileTreeResult.

        **参数解释**: 上传权限。 **取值范围**: true：有权限。 false：无权限。 

        :return: The upload_access of this ShowFileTreeResult.
        :rtype: str
        """
        return self._upload_access

    @upload_access.setter
    def upload_access(self, upload_access):
        r"""Sets the upload_access of this ShowFileTreeResult.

        **参数解释**: 上传权限。 **取值范围**: true：有权限。 false：无权限。 

        :param upload_access: The upload_access of this ShowFileTreeResult.
        :type upload_access: str
        """
        self._upload_access = upload_access

    @property
    def total(self):
        r"""Gets the total of this ShowFileTreeResult.

        **参数解释**: 总数。 **取值范围**: 不涉及。 

        :return: The total of this ShowFileTreeResult.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowFileTreeResult.

        **参数解释**: 总数。 **取值范围**: 不涉及。 

        :param total: The total of this ShowFileTreeResult.
        :type total: str
        """
        self._total = total

    @property
    def uri(self):
        r"""Gets the uri of this ShowFileTreeResult.

        **参数解释**: 父路径。 **取值范围**: 不涉及。 

        :return: The uri of this ShowFileTreeResult.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this ShowFileTreeResult.

        **参数解释**: 父路径。 **取值范围**: 不涉及。 

        :param uri: The uri of this ShowFileTreeResult.
        :type uri: str
        """
        self._uri = uri

    @property
    def created(self):
        r"""Gets the created of this ShowFileTreeResult.

        **参数解释**: 创建时间。 **取值范围**: 不涉及。 

        :return: The created of this ShowFileTreeResult.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ShowFileTreeResult.

        **参数解释**: 创建时间。 **取值范围**: 不涉及。 

        :param created: The created of this ShowFileTreeResult.
        :type created: str
        """
        self._created = created

    @property
    def children(self):
        r"""Gets the children of this ShowFileTreeResult.

        **参数解释**: 子文件及文件夹信息。 **取值范围**: 不涉及。 

        :return: The children of this ShowFileTreeResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsartifact.v2.ShowFileTreeResultChildren`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this ShowFileTreeResult.

        **参数解释**: 子文件及文件夹信息。 **取值范围**: 不涉及。 

        :param children: The children of this ShowFileTreeResult.
        :type children: list[:class:`huaweicloudsdkcodeartsartifact.v2.ShowFileTreeResultChildren`]
        """
        self._children = children

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
        if not isinstance(other, ShowFileTreeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
