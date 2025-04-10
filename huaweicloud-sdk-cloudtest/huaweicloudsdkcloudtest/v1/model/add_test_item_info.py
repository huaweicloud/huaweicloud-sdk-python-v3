# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddTestItemInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'comment': 'str',
        'name': 'str',
        'number': 'str',
        'owner': 'str',
        'is_feature': 'str',
        'project_uuid': 'str',
        'parent_uri': 'str',
        'version_uri': 'str',
        'ignore_duplicate_name': 'bool'
    }

    attribute_map = {
        'comment': 'comment',
        'name': 'name',
        'number': 'number',
        'owner': 'owner',
        'is_feature': 'is_feature',
        'project_uuid': 'project_uuid',
        'parent_uri': 'parent_uri',
        'version_uri': 'version_uri',
        'ignore_duplicate_name': 'ignore_duplicate_name'
    }

    def __init__(self, comment=None, name=None, number=None, owner=None, is_feature=None, project_uuid=None, parent_uri=None, version_uri=None, ignore_duplicate_name=None):
        r"""AddTestItemInfo

        The model defined in huaweicloud sdk

        :param comment: 备注
        :type comment: str
        :param name: 名称
        :type name: str
        :param number: 编号
        :type number: str
        :param owner: 责任人
        :type owner: str
        :param is_feature: 是否为特性,1:特性 2:目录
        :type is_feature: str
        :param project_uuid: 项目uuid
        :type project_uuid: str
        :param parent_uri: 父节点uri
        :type parent_uri: str
        :param version_uri: 版本URI
        :type version_uri: str
        :param ignore_duplicate_name: 是否忽略名称重复
        :type ignore_duplicate_name: bool
        """
        
        

        self._comment = None
        self._name = None
        self._number = None
        self._owner = None
        self._is_feature = None
        self._project_uuid = None
        self._parent_uri = None
        self._version_uri = None
        self._ignore_duplicate_name = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        self.name = name
        if number is not None:
            self.number = number
        if owner is not None:
            self.owner = owner
        if is_feature is not None:
            self.is_feature = is_feature
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if parent_uri is not None:
            self.parent_uri = parent_uri
        if version_uri is not None:
            self.version_uri = version_uri
        if ignore_duplicate_name is not None:
            self.ignore_duplicate_name = ignore_duplicate_name

    @property
    def comment(self):
        r"""Gets the comment of this AddTestItemInfo.

        备注

        :return: The comment of this AddTestItemInfo.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this AddTestItemInfo.

        备注

        :param comment: The comment of this AddTestItemInfo.
        :type comment: str
        """
        self._comment = comment

    @property
    def name(self):
        r"""Gets the name of this AddTestItemInfo.

        名称

        :return: The name of this AddTestItemInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AddTestItemInfo.

        名称

        :param name: The name of this AddTestItemInfo.
        :type name: str
        """
        self._name = name

    @property
    def number(self):
        r"""Gets the number of this AddTestItemInfo.

        编号

        :return: The number of this AddTestItemInfo.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this AddTestItemInfo.

        编号

        :param number: The number of this AddTestItemInfo.
        :type number: str
        """
        self._number = number

    @property
    def owner(self):
        r"""Gets the owner of this AddTestItemInfo.

        责任人

        :return: The owner of this AddTestItemInfo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this AddTestItemInfo.

        责任人

        :param owner: The owner of this AddTestItemInfo.
        :type owner: str
        """
        self._owner = owner

    @property
    def is_feature(self):
        r"""Gets the is_feature of this AddTestItemInfo.

        是否为特性,1:特性 2:目录

        :return: The is_feature of this AddTestItemInfo.
        :rtype: str
        """
        return self._is_feature

    @is_feature.setter
    def is_feature(self, is_feature):
        r"""Sets the is_feature of this AddTestItemInfo.

        是否为特性,1:特性 2:目录

        :param is_feature: The is_feature of this AddTestItemInfo.
        :type is_feature: str
        """
        self._is_feature = is_feature

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this AddTestItemInfo.

        项目uuid

        :return: The project_uuid of this AddTestItemInfo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this AddTestItemInfo.

        项目uuid

        :param project_uuid: The project_uuid of this AddTestItemInfo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def parent_uri(self):
        r"""Gets the parent_uri of this AddTestItemInfo.

        父节点uri

        :return: The parent_uri of this AddTestItemInfo.
        :rtype: str
        """
        return self._parent_uri

    @parent_uri.setter
    def parent_uri(self, parent_uri):
        r"""Sets the parent_uri of this AddTestItemInfo.

        父节点uri

        :param parent_uri: The parent_uri of this AddTestItemInfo.
        :type parent_uri: str
        """
        self._parent_uri = parent_uri

    @property
    def version_uri(self):
        r"""Gets the version_uri of this AddTestItemInfo.

        版本URI

        :return: The version_uri of this AddTestItemInfo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this AddTestItemInfo.

        版本URI

        :param version_uri: The version_uri of this AddTestItemInfo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def ignore_duplicate_name(self):
        r"""Gets the ignore_duplicate_name of this AddTestItemInfo.

        是否忽略名称重复

        :return: The ignore_duplicate_name of this AddTestItemInfo.
        :rtype: bool
        """
        return self._ignore_duplicate_name

    @ignore_duplicate_name.setter
    def ignore_duplicate_name(self, ignore_duplicate_name):
        r"""Sets the ignore_duplicate_name of this AddTestItemInfo.

        是否忽略名称重复

        :param ignore_duplicate_name: The ignore_duplicate_name of this AddTestItemInfo.
        :type ignore_duplicate_name: bool
        """
        self._ignore_duplicate_name = ignore_duplicate_name

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
        if not isinstance(other, AddTestItemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
