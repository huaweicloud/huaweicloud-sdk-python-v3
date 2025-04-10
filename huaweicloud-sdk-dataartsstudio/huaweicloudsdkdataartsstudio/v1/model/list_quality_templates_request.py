# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQualityTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category_id': 'int',
        'name': 'str',
        'system_template': 'bool',
        'creator': 'str',
        'limit': 'int',
        'offset': 'int',
        'workspace': 'str'
    }

    attribute_map = {
        'category_id': 'category_id',
        'name': 'name',
        'system_template': 'system_template',
        'creator': 'creator',
        'limit': 'limit',
        'offset': 'offset',
        'workspace': 'workspace'
    }

    def __init__(self, category_id=None, name=None, system_template=None, creator=None, limit=None, offset=None, workspace=None):
        r"""ListQualityTemplatesRequest

        The model defined in huaweicloud sdk

        :param category_id: category id
        :type category_id: int
        :param name: name
        :type name: str
        :param system_template: 是否只查询系统模板
        :type system_template: bool
        :param creator: 创建者
        :type creator: str
        :param limit: 分页时每页的条数,最大值为100
        :type limit: int
        :param offset: 分页偏移量
        :type offset: int
        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        """
        
        

        self._category_id = None
        self._name = None
        self._system_template = None
        self._creator = None
        self._limit = None
        self._offset = None
        self._workspace = None
        self.discriminator = None

        if category_id is not None:
            self.category_id = category_id
        if name is not None:
            self.name = name
        if system_template is not None:
            self.system_template = system_template
        if creator is not None:
            self.creator = creator
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.workspace = workspace

    @property
    def category_id(self):
        r"""Gets the category_id of this ListQualityTemplatesRequest.

        category id

        :return: The category_id of this ListQualityTemplatesRequest.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        r"""Sets the category_id of this ListQualityTemplatesRequest.

        category id

        :param category_id: The category_id of this ListQualityTemplatesRequest.
        :type category_id: int
        """
        self._category_id = category_id

    @property
    def name(self):
        r"""Gets the name of this ListQualityTemplatesRequest.

        name

        :return: The name of this ListQualityTemplatesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListQualityTemplatesRequest.

        name

        :param name: The name of this ListQualityTemplatesRequest.
        :type name: str
        """
        self._name = name

    @property
    def system_template(self):
        r"""Gets the system_template of this ListQualityTemplatesRequest.

        是否只查询系统模板

        :return: The system_template of this ListQualityTemplatesRequest.
        :rtype: bool
        """
        return self._system_template

    @system_template.setter
    def system_template(self, system_template):
        r"""Sets the system_template of this ListQualityTemplatesRequest.

        是否只查询系统模板

        :param system_template: The system_template of this ListQualityTemplatesRequest.
        :type system_template: bool
        """
        self._system_template = system_template

    @property
    def creator(self):
        r"""Gets the creator of this ListQualityTemplatesRequest.

        创建者

        :return: The creator of this ListQualityTemplatesRequest.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ListQualityTemplatesRequest.

        创建者

        :param creator: The creator of this ListQualityTemplatesRequest.
        :type creator: str
        """
        self._creator = creator

    @property
    def limit(self):
        r"""Gets the limit of this ListQualityTemplatesRequest.

        分页时每页的条数,最大值为100

        :return: The limit of this ListQualityTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListQualityTemplatesRequest.

        分页时每页的条数,最大值为100

        :param limit: The limit of this ListQualityTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListQualityTemplatesRequest.

        分页偏移量

        :return: The offset of this ListQualityTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListQualityTemplatesRequest.

        分页偏移量

        :param offset: The offset of this ListQualityTemplatesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def workspace(self):
        r"""Gets the workspace of this ListQualityTemplatesRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListQualityTemplatesRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListQualityTemplatesRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListQualityTemplatesRequest.
        :type workspace: str
        """
        self._workspace = workspace

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
        if not isinstance(other, ListQualityTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
