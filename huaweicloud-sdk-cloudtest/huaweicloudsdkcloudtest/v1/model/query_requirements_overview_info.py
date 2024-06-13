# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryRequirementsOverviewInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fixed_version_id': 'str',
        'module_id': 'str',
        'key_word': 'str',
        'page_size': 'int',
        'page_no': 'int',
        'pi_filter': 'PiFilterInfo'
    }

    attribute_map = {
        'fixed_version_id': 'fixed_version_id',
        'module_id': 'module_id',
        'key_word': 'key_word',
        'page_size': 'page_size',
        'page_no': 'page_no',
        'pi_filter': 'pi_filter'
    }

    def __init__(self, fixed_version_id=None, module_id=None, key_word=None, page_size=None, page_no=None, pi_filter=None):
        """QueryRequirementsOverviewInfo

        The model defined in huaweicloud sdk

        :param fixed_version_id: 筛选迭代ID
        :type fixed_version_id: str
        :param module_id: 模块ID
        :type module_id: str
        :param key_word: 关键字
        :type key_word: str
        :param page_size: 每页数量
        :type page_size: int
        :param page_no: 页码
        :type page_no: int
        :param pi_filter: 
        :type pi_filter: :class:`huaweicloudsdkcloudtest.v1.PiFilterInfo`
        """
        
        

        self._fixed_version_id = None
        self._module_id = None
        self._key_word = None
        self._page_size = None
        self._page_no = None
        self._pi_filter = None
        self.discriminator = None

        if fixed_version_id is not None:
            self.fixed_version_id = fixed_version_id
        if module_id is not None:
            self.module_id = module_id
        if key_word is not None:
            self.key_word = key_word
        if page_size is not None:
            self.page_size = page_size
        if page_no is not None:
            self.page_no = page_no
        if pi_filter is not None:
            self.pi_filter = pi_filter

    @property
    def fixed_version_id(self):
        """Gets the fixed_version_id of this QueryRequirementsOverviewInfo.

        筛选迭代ID

        :return: The fixed_version_id of this QueryRequirementsOverviewInfo.
        :rtype: str
        """
        return self._fixed_version_id

    @fixed_version_id.setter
    def fixed_version_id(self, fixed_version_id):
        """Sets the fixed_version_id of this QueryRequirementsOverviewInfo.

        筛选迭代ID

        :param fixed_version_id: The fixed_version_id of this QueryRequirementsOverviewInfo.
        :type fixed_version_id: str
        """
        self._fixed_version_id = fixed_version_id

    @property
    def module_id(self):
        """Gets the module_id of this QueryRequirementsOverviewInfo.

        模块ID

        :return: The module_id of this QueryRequirementsOverviewInfo.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        """Sets the module_id of this QueryRequirementsOverviewInfo.

        模块ID

        :param module_id: The module_id of this QueryRequirementsOverviewInfo.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def key_word(self):
        """Gets the key_word of this QueryRequirementsOverviewInfo.

        关键字

        :return: The key_word of this QueryRequirementsOverviewInfo.
        :rtype: str
        """
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        """Sets the key_word of this QueryRequirementsOverviewInfo.

        关键字

        :param key_word: The key_word of this QueryRequirementsOverviewInfo.
        :type key_word: str
        """
        self._key_word = key_word

    @property
    def page_size(self):
        """Gets the page_size of this QueryRequirementsOverviewInfo.

        每页数量

        :return: The page_size of this QueryRequirementsOverviewInfo.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this QueryRequirementsOverviewInfo.

        每页数量

        :param page_size: The page_size of this QueryRequirementsOverviewInfo.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_no(self):
        """Gets the page_no of this QueryRequirementsOverviewInfo.

        页码

        :return: The page_no of this QueryRequirementsOverviewInfo.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this QueryRequirementsOverviewInfo.

        页码

        :param page_no: The page_no of this QueryRequirementsOverviewInfo.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def pi_filter(self):
        """Gets the pi_filter of this QueryRequirementsOverviewInfo.

        :return: The pi_filter of this QueryRequirementsOverviewInfo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.PiFilterInfo`
        """
        return self._pi_filter

    @pi_filter.setter
    def pi_filter(self, pi_filter):
        """Sets the pi_filter of this QueryRequirementsOverviewInfo.

        :param pi_filter: The pi_filter of this QueryRequirementsOverviewInfo.
        :type pi_filter: :class:`huaweicloudsdkcloudtest.v1.PiFilterInfo`
        """
        self._pi_filter = pi_filter

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
        if not isinstance(other, QueryRequirementsOverviewInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
