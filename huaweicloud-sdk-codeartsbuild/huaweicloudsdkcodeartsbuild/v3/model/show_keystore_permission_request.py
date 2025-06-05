# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKeystorePermissionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keystore_id': 'str',
        'page_size': 'int',
        'page': 'str'
    }

    attribute_map = {
        'keystore_id': 'keystore_id',
        'page_size': 'page_size',
        'page': 'page'
    }

    def __init__(self, keystore_id=None, page_size=None, page=None):
        r"""ShowKeystorePermissionRequest

        The model defined in huaweicloud sdk

        :param keystore_id: 文件秘钥Id
        :type keystore_id: str
        :param page_size: **参数解释**： 每页显示的条目数量。 **约束限制**： 不涉及。 **取值范围**： 只能使用数字，小于等于100。
        :type page_size: int
        :param page: 分页页码，表示从此页开始查询，page大于等于1
        :type page: str
        """
        
        

        self._keystore_id = None
        self._page_size = None
        self._page = None
        self.discriminator = None

        self.keystore_id = keystore_id
        self.page_size = page_size
        self.page = page

    @property
    def keystore_id(self):
        r"""Gets the keystore_id of this ShowKeystorePermissionRequest.

        文件秘钥Id

        :return: The keystore_id of this ShowKeystorePermissionRequest.
        :rtype: str
        """
        return self._keystore_id

    @keystore_id.setter
    def keystore_id(self, keystore_id):
        r"""Sets the keystore_id of this ShowKeystorePermissionRequest.

        文件秘钥Id

        :param keystore_id: The keystore_id of this ShowKeystorePermissionRequest.
        :type keystore_id: str
        """
        self._keystore_id = keystore_id

    @property
    def page_size(self):
        r"""Gets the page_size of this ShowKeystorePermissionRequest.

        **参数解释**： 每页显示的条目数量。 **约束限制**： 不涉及。 **取值范围**： 只能使用数字，小于等于100。

        :return: The page_size of this ShowKeystorePermissionRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ShowKeystorePermissionRequest.

        **参数解释**： 每页显示的条目数量。 **约束限制**： 不涉及。 **取值范围**： 只能使用数字，小于等于100。

        :param page_size: The page_size of this ShowKeystorePermissionRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page(self):
        r"""Gets the page of this ShowKeystorePermissionRequest.

        分页页码，表示从此页开始查询，page大于等于1

        :return: The page of this ShowKeystorePermissionRequest.
        :rtype: str
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ShowKeystorePermissionRequest.

        分页页码，表示从此页开始查询，page大于等于1

        :param page: The page of this ShowKeystorePermissionRequest.
        :type page: str
        """
        self._page = page

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
        if not isinstance(other, ShowKeystorePermissionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
