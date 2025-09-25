# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSecurityDataCategoryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category_id': 'str',
        'category_name': 'str',
        'description': 'str',
        'category_level': 'int',
        'root_id': 'str',
        'parent_id': 'str',
        'category_path': 'str',
        'create_by': 'str',
        'create_time': 'int',
        'update_by': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'category_id': 'category_id',
        'category_name': 'category_name',
        'description': 'description',
        'category_level': 'category_level',
        'root_id': 'root_id',
        'parent_id': 'parent_id',
        'category_path': 'category_path',
        'create_by': 'create_by',
        'create_time': 'create_time',
        'update_by': 'update_by',
        'update_time': 'update_time'
    }

    def __init__(self, category_id=None, category_name=None, description=None, category_level=None, root_id=None, parent_id=None, category_path=None, create_by=None, create_time=None, update_by=None, update_time=None):
        r"""CreateSecurityDataCategoryResponse

        The model defined in huaweicloud sdk

        :param category_id: 数据分类id。
        :type category_id: str
        :param category_name: 数据分类名称。
        :type category_name: str
        :param description: 数据分类描述。
        :type description: str
        :param category_level: 数据分类层级。
        :type category_level: int
        :param root_id: 分类树根节点。
        :type root_id: str
        :param parent_id: 父分类节点。
        :type parent_id: str
        :param category_path: 分类树路径。
        :type category_path: str
        :param create_by: 创建者。
        :type create_by: str
        :param create_time: 创建时间。
        :type create_time: int
        :param update_by: 更新者。
        :type update_by: str
        :param update_time: 更新时间。
        :type update_time: int
        """
        
        super(CreateSecurityDataCategoryResponse, self).__init__()

        self._category_id = None
        self._category_name = None
        self._description = None
        self._category_level = None
        self._root_id = None
        self._parent_id = None
        self._category_path = None
        self._create_by = None
        self._create_time = None
        self._update_by = None
        self._update_time = None
        self.discriminator = None

        if category_id is not None:
            self.category_id = category_id
        if category_name is not None:
            self.category_name = category_name
        if description is not None:
            self.description = description
        if category_level is not None:
            self.category_level = category_level
        if root_id is not None:
            self.root_id = root_id
        if parent_id is not None:
            self.parent_id = parent_id
        if category_path is not None:
            self.category_path = category_path
        if create_by is not None:
            self.create_by = create_by
        if create_time is not None:
            self.create_time = create_time
        if update_by is not None:
            self.update_by = update_by
        if update_time is not None:
            self.update_time = update_time

    @property
    def category_id(self):
        r"""Gets the category_id of this CreateSecurityDataCategoryResponse.

        数据分类id。

        :return: The category_id of this CreateSecurityDataCategoryResponse.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        r"""Sets the category_id of this CreateSecurityDataCategoryResponse.

        数据分类id。

        :param category_id: The category_id of this CreateSecurityDataCategoryResponse.
        :type category_id: str
        """
        self._category_id = category_id

    @property
    def category_name(self):
        r"""Gets the category_name of this CreateSecurityDataCategoryResponse.

        数据分类名称。

        :return: The category_name of this CreateSecurityDataCategoryResponse.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        r"""Sets the category_name of this CreateSecurityDataCategoryResponse.

        数据分类名称。

        :param category_name: The category_name of this CreateSecurityDataCategoryResponse.
        :type category_name: str
        """
        self._category_name = category_name

    @property
    def description(self):
        r"""Gets the description of this CreateSecurityDataCategoryResponse.

        数据分类描述。

        :return: The description of this CreateSecurityDataCategoryResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateSecurityDataCategoryResponse.

        数据分类描述。

        :param description: The description of this CreateSecurityDataCategoryResponse.
        :type description: str
        """
        self._description = description

    @property
    def category_level(self):
        r"""Gets the category_level of this CreateSecurityDataCategoryResponse.

        数据分类层级。

        :return: The category_level of this CreateSecurityDataCategoryResponse.
        :rtype: int
        """
        return self._category_level

    @category_level.setter
    def category_level(self, category_level):
        r"""Sets the category_level of this CreateSecurityDataCategoryResponse.

        数据分类层级。

        :param category_level: The category_level of this CreateSecurityDataCategoryResponse.
        :type category_level: int
        """
        self._category_level = category_level

    @property
    def root_id(self):
        r"""Gets the root_id of this CreateSecurityDataCategoryResponse.

        分类树根节点。

        :return: The root_id of this CreateSecurityDataCategoryResponse.
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        r"""Sets the root_id of this CreateSecurityDataCategoryResponse.

        分类树根节点。

        :param root_id: The root_id of this CreateSecurityDataCategoryResponse.
        :type root_id: str
        """
        self._root_id = root_id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this CreateSecurityDataCategoryResponse.

        父分类节点。

        :return: The parent_id of this CreateSecurityDataCategoryResponse.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this CreateSecurityDataCategoryResponse.

        父分类节点。

        :param parent_id: The parent_id of this CreateSecurityDataCategoryResponse.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def category_path(self):
        r"""Gets the category_path of this CreateSecurityDataCategoryResponse.

        分类树路径。

        :return: The category_path of this CreateSecurityDataCategoryResponse.
        :rtype: str
        """
        return self._category_path

    @category_path.setter
    def category_path(self, category_path):
        r"""Sets the category_path of this CreateSecurityDataCategoryResponse.

        分类树路径。

        :param category_path: The category_path of this CreateSecurityDataCategoryResponse.
        :type category_path: str
        """
        self._category_path = category_path

    @property
    def create_by(self):
        r"""Gets the create_by of this CreateSecurityDataCategoryResponse.

        创建者。

        :return: The create_by of this CreateSecurityDataCategoryResponse.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this CreateSecurityDataCategoryResponse.

        创建者。

        :param create_by: The create_by of this CreateSecurityDataCategoryResponse.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateSecurityDataCategoryResponse.

        创建时间。

        :return: The create_time of this CreateSecurityDataCategoryResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateSecurityDataCategoryResponse.

        创建时间。

        :param create_time: The create_time of this CreateSecurityDataCategoryResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_by(self):
        r"""Gets the update_by of this CreateSecurityDataCategoryResponse.

        更新者。

        :return: The update_by of this CreateSecurityDataCategoryResponse.
        :rtype: str
        """
        return self._update_by

    @update_by.setter
    def update_by(self, update_by):
        r"""Sets the update_by of this CreateSecurityDataCategoryResponse.

        更新者。

        :param update_by: The update_by of this CreateSecurityDataCategoryResponse.
        :type update_by: str
        """
        self._update_by = update_by

    @property
    def update_time(self):
        r"""Gets the update_time of this CreateSecurityDataCategoryResponse.

        更新时间。

        :return: The update_time of this CreateSecurityDataCategoryResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CreateSecurityDataCategoryResponse.

        更新时间。

        :param update_time: The update_time of this CreateSecurityDataCategoryResponse.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, CreateSecurityDataCategoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
