# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetPublicLibAndAwsResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aw_tag': 'str',
        'document_link': 'str',
        'is_favorite': 'int',
        'public_aw_description': 'str',
        'public_aw_id': 'str',
        'public_aw_lib_id': 'str',
        'public_aw_lib_name': 'str',
        'public_aw_mark': 'int',
        'public_aw_name': 'str'
    }

    attribute_map = {
        'aw_tag': 'aw_tag',
        'document_link': 'document_link',
        'is_favorite': 'is_favorite',
        'public_aw_description': 'public_aw_description',
        'public_aw_id': 'public_aw_id',
        'public_aw_lib_id': 'public_aw_lib_id',
        'public_aw_lib_name': 'public_aw_lib_name',
        'public_aw_mark': 'public_aw_mark',
        'public_aw_name': 'public_aw_name'
    }

    def __init__(self, aw_tag=None, document_link=None, is_favorite=None, public_aw_description=None, public_aw_id=None, public_aw_lib_id=None, public_aw_lib_name=None, public_aw_mark=None, public_aw_name=None):
        r"""GetPublicLibAndAwsResp

        The model defined in huaweicloud sdk

        :param aw_tag: 公共关键字分组信息
        :type aw_tag: str
        :param document_link: 公共关键字帮助文档链接
        :type document_link: str
        :param is_favorite: 保留字段
        :type is_favorite: int
        :param public_aw_description: 公共关键字描述
        :type public_aw_description: str
        :param public_aw_id: 公共关键字唯一ID
        :type public_aw_id: str
        :param public_aw_lib_id: 公共关键库唯一ID
        :type public_aw_lib_id: str
        :param public_aw_lib_name: 公共关键字库名称
        :type public_aw_lib_name: str
        :param public_aw_mark: 保留字段
        :type public_aw_mark: int
        :param public_aw_name: 公共关键字名称
        :type public_aw_name: str
        """
        
        

        self._aw_tag = None
        self._document_link = None
        self._is_favorite = None
        self._public_aw_description = None
        self._public_aw_id = None
        self._public_aw_lib_id = None
        self._public_aw_lib_name = None
        self._public_aw_mark = None
        self._public_aw_name = None
        self.discriminator = None

        if aw_tag is not None:
            self.aw_tag = aw_tag
        if document_link is not None:
            self.document_link = document_link
        if is_favorite is not None:
            self.is_favorite = is_favorite
        if public_aw_description is not None:
            self.public_aw_description = public_aw_description
        if public_aw_id is not None:
            self.public_aw_id = public_aw_id
        if public_aw_lib_id is not None:
            self.public_aw_lib_id = public_aw_lib_id
        if public_aw_lib_name is not None:
            self.public_aw_lib_name = public_aw_lib_name
        if public_aw_mark is not None:
            self.public_aw_mark = public_aw_mark
        if public_aw_name is not None:
            self.public_aw_name = public_aw_name

    @property
    def aw_tag(self):
        r"""Gets the aw_tag of this GetPublicLibAndAwsResp.

        公共关键字分组信息

        :return: The aw_tag of this GetPublicLibAndAwsResp.
        :rtype: str
        """
        return self._aw_tag

    @aw_tag.setter
    def aw_tag(self, aw_tag):
        r"""Sets the aw_tag of this GetPublicLibAndAwsResp.

        公共关键字分组信息

        :param aw_tag: The aw_tag of this GetPublicLibAndAwsResp.
        :type aw_tag: str
        """
        self._aw_tag = aw_tag

    @property
    def document_link(self):
        r"""Gets the document_link of this GetPublicLibAndAwsResp.

        公共关键字帮助文档链接

        :return: The document_link of this GetPublicLibAndAwsResp.
        :rtype: str
        """
        return self._document_link

    @document_link.setter
    def document_link(self, document_link):
        r"""Sets the document_link of this GetPublicLibAndAwsResp.

        公共关键字帮助文档链接

        :param document_link: The document_link of this GetPublicLibAndAwsResp.
        :type document_link: str
        """
        self._document_link = document_link

    @property
    def is_favorite(self):
        r"""Gets the is_favorite of this GetPublicLibAndAwsResp.

        保留字段

        :return: The is_favorite of this GetPublicLibAndAwsResp.
        :rtype: int
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        r"""Sets the is_favorite of this GetPublicLibAndAwsResp.

        保留字段

        :param is_favorite: The is_favorite of this GetPublicLibAndAwsResp.
        :type is_favorite: int
        """
        self._is_favorite = is_favorite

    @property
    def public_aw_description(self):
        r"""Gets the public_aw_description of this GetPublicLibAndAwsResp.

        公共关键字描述

        :return: The public_aw_description of this GetPublicLibAndAwsResp.
        :rtype: str
        """
        return self._public_aw_description

    @public_aw_description.setter
    def public_aw_description(self, public_aw_description):
        r"""Sets the public_aw_description of this GetPublicLibAndAwsResp.

        公共关键字描述

        :param public_aw_description: The public_aw_description of this GetPublicLibAndAwsResp.
        :type public_aw_description: str
        """
        self._public_aw_description = public_aw_description

    @property
    def public_aw_id(self):
        r"""Gets the public_aw_id of this GetPublicLibAndAwsResp.

        公共关键字唯一ID

        :return: The public_aw_id of this GetPublicLibAndAwsResp.
        :rtype: str
        """
        return self._public_aw_id

    @public_aw_id.setter
    def public_aw_id(self, public_aw_id):
        r"""Sets the public_aw_id of this GetPublicLibAndAwsResp.

        公共关键字唯一ID

        :param public_aw_id: The public_aw_id of this GetPublicLibAndAwsResp.
        :type public_aw_id: str
        """
        self._public_aw_id = public_aw_id

    @property
    def public_aw_lib_id(self):
        r"""Gets the public_aw_lib_id of this GetPublicLibAndAwsResp.

        公共关键库唯一ID

        :return: The public_aw_lib_id of this GetPublicLibAndAwsResp.
        :rtype: str
        """
        return self._public_aw_lib_id

    @public_aw_lib_id.setter
    def public_aw_lib_id(self, public_aw_lib_id):
        r"""Sets the public_aw_lib_id of this GetPublicLibAndAwsResp.

        公共关键库唯一ID

        :param public_aw_lib_id: The public_aw_lib_id of this GetPublicLibAndAwsResp.
        :type public_aw_lib_id: str
        """
        self._public_aw_lib_id = public_aw_lib_id

    @property
    def public_aw_lib_name(self):
        r"""Gets the public_aw_lib_name of this GetPublicLibAndAwsResp.

        公共关键字库名称

        :return: The public_aw_lib_name of this GetPublicLibAndAwsResp.
        :rtype: str
        """
        return self._public_aw_lib_name

    @public_aw_lib_name.setter
    def public_aw_lib_name(self, public_aw_lib_name):
        r"""Sets the public_aw_lib_name of this GetPublicLibAndAwsResp.

        公共关键字库名称

        :param public_aw_lib_name: The public_aw_lib_name of this GetPublicLibAndAwsResp.
        :type public_aw_lib_name: str
        """
        self._public_aw_lib_name = public_aw_lib_name

    @property
    def public_aw_mark(self):
        r"""Gets the public_aw_mark of this GetPublicLibAndAwsResp.

        保留字段

        :return: The public_aw_mark of this GetPublicLibAndAwsResp.
        :rtype: int
        """
        return self._public_aw_mark

    @public_aw_mark.setter
    def public_aw_mark(self, public_aw_mark):
        r"""Sets the public_aw_mark of this GetPublicLibAndAwsResp.

        保留字段

        :param public_aw_mark: The public_aw_mark of this GetPublicLibAndAwsResp.
        :type public_aw_mark: int
        """
        self._public_aw_mark = public_aw_mark

    @property
    def public_aw_name(self):
        r"""Gets the public_aw_name of this GetPublicLibAndAwsResp.

        公共关键字名称

        :return: The public_aw_name of this GetPublicLibAndAwsResp.
        :rtype: str
        """
        return self._public_aw_name

    @public_aw_name.setter
    def public_aw_name(self, public_aw_name):
        r"""Sets the public_aw_name of this GetPublicLibAndAwsResp.

        公共关键字名称

        :param public_aw_name: The public_aw_name of this GetPublicLibAndAwsResp.
        :type public_aw_name: str
        """
        self._public_aw_name = public_aw_name

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
        if not isinstance(other, GetPublicLibAndAwsResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
