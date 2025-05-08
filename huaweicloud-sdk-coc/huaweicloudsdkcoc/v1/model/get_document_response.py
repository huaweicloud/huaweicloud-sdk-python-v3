# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetDocumentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'document_id': 'str',
        'name': 'str',
        'content': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'version': 'str',
        'creator': 'str',
        'modifier': 'str',
        'enterprise_project_id': 'str',
        'versions': 'list[DocumentVersionVo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'document_id': 'document_id',
        'name': 'name',
        'content': 'content',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'version': 'version',
        'creator': 'creator',
        'modifier': 'modifier',
        'enterprise_project_id': 'enterprise_project_id',
        'versions': 'versions',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, id=None, document_id=None, name=None, content=None, create_time=None, update_time=None, version=None, creator=None, modifier=None, enterprise_project_id=None, versions=None, x_request_id=None):
        r"""GetDocumentResponse

        The model defined in huaweicloud sdk

        :param id: 作业id
        :type id: str
        :param document_id: 作业uuid
        :type document_id: str
        :param name: 作业名称
        :type name: str
        :param content: 作业内容，DSL语句
        :type content: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        :param version: 作业版本，如v1
        :type version: str
        :param creator: 创建人
        :type creator: str
        :param modifier: 修改人
        :type modifier: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param versions: 版本集合
        :type versions: list[:class:`huaweicloudsdkcoc.v1.DocumentVersionVo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(GetDocumentResponse, self).__init__()

        self._id = None
        self._document_id = None
        self._name = None
        self._content = None
        self._create_time = None
        self._update_time = None
        self._version = None
        self._creator = None
        self._modifier = None
        self._enterprise_project_id = None
        self._versions = None
        self._x_request_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if document_id is not None:
            self.document_id = document_id
        if name is not None:
            self.name = name
        if content is not None:
            self.content = content
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if version is not None:
            self.version = version
        if creator is not None:
            self.creator = creator
        if modifier is not None:
            self.modifier = modifier
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if versions is not None:
            self.versions = versions
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def id(self):
        r"""Gets the id of this GetDocumentResponse.

        作业id

        :return: The id of this GetDocumentResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GetDocumentResponse.

        作业id

        :param id: The id of this GetDocumentResponse.
        :type id: str
        """
        self._id = id

    @property
    def document_id(self):
        r"""Gets the document_id of this GetDocumentResponse.

        作业uuid

        :return: The document_id of this GetDocumentResponse.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        r"""Sets the document_id of this GetDocumentResponse.

        作业uuid

        :param document_id: The document_id of this GetDocumentResponse.
        :type document_id: str
        """
        self._document_id = document_id

    @property
    def name(self):
        r"""Gets the name of this GetDocumentResponse.

        作业名称

        :return: The name of this GetDocumentResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GetDocumentResponse.

        作业名称

        :param name: The name of this GetDocumentResponse.
        :type name: str
        """
        self._name = name

    @property
    def content(self):
        r"""Gets the content of this GetDocumentResponse.

        作业内容，DSL语句

        :return: The content of this GetDocumentResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this GetDocumentResponse.

        作业内容，DSL语句

        :param content: The content of this GetDocumentResponse.
        :type content: str
        """
        self._content = content

    @property
    def create_time(self):
        r"""Gets the create_time of this GetDocumentResponse.

        创建时间

        :return: The create_time of this GetDocumentResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this GetDocumentResponse.

        创建时间

        :param create_time: The create_time of this GetDocumentResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this GetDocumentResponse.

        更新时间

        :return: The update_time of this GetDocumentResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this GetDocumentResponse.

        更新时间

        :param update_time: The update_time of this GetDocumentResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def version(self):
        r"""Gets the version of this GetDocumentResponse.

        作业版本，如v1

        :return: The version of this GetDocumentResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this GetDocumentResponse.

        作业版本，如v1

        :param version: The version of this GetDocumentResponse.
        :type version: str
        """
        self._version = version

    @property
    def creator(self):
        r"""Gets the creator of this GetDocumentResponse.

        创建人

        :return: The creator of this GetDocumentResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this GetDocumentResponse.

        创建人

        :param creator: The creator of this GetDocumentResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def modifier(self):
        r"""Gets the modifier of this GetDocumentResponse.

        修改人

        :return: The modifier of this GetDocumentResponse.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this GetDocumentResponse.

        修改人

        :param modifier: The modifier of this GetDocumentResponse.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this GetDocumentResponse.

        企业项目id

        :return: The enterprise_project_id of this GetDocumentResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this GetDocumentResponse.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this GetDocumentResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def versions(self):
        r"""Gets the versions of this GetDocumentResponse.

        版本集合

        :return: The versions of this GetDocumentResponse.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.DocumentVersionVo`]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        r"""Sets the versions of this GetDocumentResponse.

        版本集合

        :param versions: The versions of this GetDocumentResponse.
        :type versions: list[:class:`huaweicloudsdkcoc.v1.DocumentVersionVo`]
        """
        self._versions = versions

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this GetDocumentResponse.

        :return: The x_request_id of this GetDocumentResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this GetDocumentResponse.

        :param x_request_id: The x_request_id of this GetDocumentResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, GetDocumentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
