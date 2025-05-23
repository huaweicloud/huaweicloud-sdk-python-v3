# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCatalogDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'catalog_id': 'str',
        'name': 'str',
        'path': 'str',
        'catalog_total': 'int',
        'api_total': 'int',
        'description': 'str',
        'create_time': 'int',
        'create_user': 'str',
        'update_time': 'int',
        'update_user': 'str'
    }

    attribute_map = {
        'catalog_id': 'catalog_id',
        'name': 'name',
        'path': 'path',
        'catalog_total': 'catalog_total',
        'api_total': 'api_total',
        'description': 'description',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'update_time': 'update_time',
        'update_user': 'update_user'
    }

    def __init__(self, catalog_id=None, name=None, path=None, catalog_total=None, api_total=None, description=None, create_time=None, create_user=None, update_time=None, update_user=None):
        r"""ShowCatalogDetailResponse

        The model defined in huaweicloud sdk

        :param catalog_id: 目录编号
        :type catalog_id: str
        :param name: 名称
        :type name: str
        :param path: 路径
        :type path: str
        :param catalog_total: 子目录数
        :type catalog_total: int
        :param api_total: 子API数
        :type api_total: int
        :param description: 描述
        :type description: str
        :param create_time: 创建时间
        :type create_time: int
        :param create_user: 创建者
        :type create_user: str
        :param update_time: 更新时间
        :type update_time: int
        :param update_user: 更新者
        :type update_user: str
        """
        
        super(ShowCatalogDetailResponse, self).__init__()

        self._catalog_id = None
        self._name = None
        self._path = None
        self._catalog_total = None
        self._api_total = None
        self._description = None
        self._create_time = None
        self._create_user = None
        self._update_time = None
        self._update_user = None
        self.discriminator = None

        if catalog_id is not None:
            self.catalog_id = catalog_id
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if catalog_total is not None:
            self.catalog_total = catalog_total
        if api_total is not None:
            self.api_total = api_total
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if update_time is not None:
            self.update_time = update_time
        if update_user is not None:
            self.update_user = update_user

    @property
    def catalog_id(self):
        r"""Gets the catalog_id of this ShowCatalogDetailResponse.

        目录编号

        :return: The catalog_id of this ShowCatalogDetailResponse.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        r"""Sets the catalog_id of this ShowCatalogDetailResponse.

        目录编号

        :param catalog_id: The catalog_id of this ShowCatalogDetailResponse.
        :type catalog_id: str
        """
        self._catalog_id = catalog_id

    @property
    def name(self):
        r"""Gets the name of this ShowCatalogDetailResponse.

        名称

        :return: The name of this ShowCatalogDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowCatalogDetailResponse.

        名称

        :param name: The name of this ShowCatalogDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def path(self):
        r"""Gets the path of this ShowCatalogDetailResponse.

        路径

        :return: The path of this ShowCatalogDetailResponse.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ShowCatalogDetailResponse.

        路径

        :param path: The path of this ShowCatalogDetailResponse.
        :type path: str
        """
        self._path = path

    @property
    def catalog_total(self):
        r"""Gets the catalog_total of this ShowCatalogDetailResponse.

        子目录数

        :return: The catalog_total of this ShowCatalogDetailResponse.
        :rtype: int
        """
        return self._catalog_total

    @catalog_total.setter
    def catalog_total(self, catalog_total):
        r"""Sets the catalog_total of this ShowCatalogDetailResponse.

        子目录数

        :param catalog_total: The catalog_total of this ShowCatalogDetailResponse.
        :type catalog_total: int
        """
        self._catalog_total = catalog_total

    @property
    def api_total(self):
        r"""Gets the api_total of this ShowCatalogDetailResponse.

        子API数

        :return: The api_total of this ShowCatalogDetailResponse.
        :rtype: int
        """
        return self._api_total

    @api_total.setter
    def api_total(self, api_total):
        r"""Sets the api_total of this ShowCatalogDetailResponse.

        子API数

        :param api_total: The api_total of this ShowCatalogDetailResponse.
        :type api_total: int
        """
        self._api_total = api_total

    @property
    def description(self):
        r"""Gets the description of this ShowCatalogDetailResponse.

        描述

        :return: The description of this ShowCatalogDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowCatalogDetailResponse.

        描述

        :param description: The description of this ShowCatalogDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowCatalogDetailResponse.

        创建时间

        :return: The create_time of this ShowCatalogDetailResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowCatalogDetailResponse.

        创建时间

        :param create_time: The create_time of this ShowCatalogDetailResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def create_user(self):
        r"""Gets the create_user of this ShowCatalogDetailResponse.

        创建者

        :return: The create_user of this ShowCatalogDetailResponse.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ShowCatalogDetailResponse.

        创建者

        :param create_user: The create_user of this ShowCatalogDetailResponse.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowCatalogDetailResponse.

        更新时间

        :return: The update_time of this ShowCatalogDetailResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowCatalogDetailResponse.

        更新时间

        :param update_time: The update_time of this ShowCatalogDetailResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def update_user(self):
        r"""Gets the update_user of this ShowCatalogDetailResponse.

        更新者

        :return: The update_user of this ShowCatalogDetailResponse.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this ShowCatalogDetailResponse.

        更新者

        :param update_user: The update_user of this ShowCatalogDetailResponse.
        :type update_user: str
        """
        self._update_user = update_user

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
        if not isinstance(other, ShowCatalogDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
