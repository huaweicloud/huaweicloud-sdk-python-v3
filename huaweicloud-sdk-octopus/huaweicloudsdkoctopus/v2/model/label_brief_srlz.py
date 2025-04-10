# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LabelBriefSrlz:

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
        'url': 'str',
        'id': 'int',
        'family': 'FamilyEnum',
        'root': 'int',
        'tag_type': 'str',
        'parent_names': 'list[object]'
    }

    attribute_map = {
        'name': 'name',
        'url': 'url',
        'id': 'id',
        'family': 'family',
        'root': 'root',
        'tag_type': 'tag_type',
        'parent_names': 'parent_names'
    }

    def __init__(self, name=None, url=None, id=None, family=None, root=None, tag_type=None, parent_names=None):
        r"""LabelBriefSrlz

        The model defined in huaweicloud sdk

        :param name: 标签名称
        :type name: str
        :param url: 标签地址
        :type url: str
        :param id: 标签ID
        :type id: int
        :param family: 
        :type family: :class:`huaweicloudsdkoctopus.v2.FamilyEnum`
        :param root: 根标签
        :type root: int
        :param tag_type: 标签类型
        :type tag_type: str
        :param parent_names: 父标签名称
        :type parent_names: list[object]
        """
        
        

        self._name = None
        self._url = None
        self._id = None
        self._family = None
        self._root = None
        self._tag_type = None
        self._parent_names = None
        self.discriminator = None

        self.name = name
        self.url = url
        self.id = id
        if family is not None:
            self.family = family
        self.root = root
        self.tag_type = tag_type
        self.parent_names = parent_names

    @property
    def name(self):
        r"""Gets the name of this LabelBriefSrlz.

        标签名称

        :return: The name of this LabelBriefSrlz.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LabelBriefSrlz.

        标签名称

        :param name: The name of this LabelBriefSrlz.
        :type name: str
        """
        self._name = name

    @property
    def url(self):
        r"""Gets the url of this LabelBriefSrlz.

        标签地址

        :return: The url of this LabelBriefSrlz.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this LabelBriefSrlz.

        标签地址

        :param url: The url of this LabelBriefSrlz.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        r"""Gets the id of this LabelBriefSrlz.

        标签ID

        :return: The id of this LabelBriefSrlz.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LabelBriefSrlz.

        标签ID

        :param id: The id of this LabelBriefSrlz.
        :type id: int
        """
        self._id = id

    @property
    def family(self):
        r"""Gets the family of this LabelBriefSrlz.

        :return: The family of this LabelBriefSrlz.
        :rtype: :class:`huaweicloudsdkoctopus.v2.FamilyEnum`
        """
        return self._family

    @family.setter
    def family(self, family):
        r"""Sets the family of this LabelBriefSrlz.

        :param family: The family of this LabelBriefSrlz.
        :type family: :class:`huaweicloudsdkoctopus.v2.FamilyEnum`
        """
        self._family = family

    @property
    def root(self):
        r"""Gets the root of this LabelBriefSrlz.

        根标签

        :return: The root of this LabelBriefSrlz.
        :rtype: int
        """
        return self._root

    @root.setter
    def root(self, root):
        r"""Sets the root of this LabelBriefSrlz.

        根标签

        :param root: The root of this LabelBriefSrlz.
        :type root: int
        """
        self._root = root

    @property
    def tag_type(self):
        r"""Gets the tag_type of this LabelBriefSrlz.

        标签类型

        :return: The tag_type of this LabelBriefSrlz.
        :rtype: str
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        r"""Sets the tag_type of this LabelBriefSrlz.

        标签类型

        :param tag_type: The tag_type of this LabelBriefSrlz.
        :type tag_type: str
        """
        self._tag_type = tag_type

    @property
    def parent_names(self):
        r"""Gets the parent_names of this LabelBriefSrlz.

        父标签名称

        :return: The parent_names of this LabelBriefSrlz.
        :rtype: list[object]
        """
        return self._parent_names

    @parent_names.setter
    def parent_names(self, parent_names):
        r"""Sets the parent_names of this LabelBriefSrlz.

        父标签名称

        :param parent_names: The parent_names of this LabelBriefSrlz.
        :type parent_names: list[object]
        """
        self._parent_names = parent_names

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
        if not isinstance(other, LabelBriefSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
