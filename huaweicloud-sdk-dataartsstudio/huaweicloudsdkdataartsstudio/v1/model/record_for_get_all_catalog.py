# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordForGetAllCatalog:

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
        'pid': 'str',
        'name': 'str',
        'description': 'str',
        'api_catalog_type': 'str',
        'create_time': 'int',
        'create_user': 'str',
        'update_time': 'int',
        'update_user': 'str'
    }

    attribute_map = {
        'catalog_id': 'catalog_id',
        'pid': 'pid',
        'name': 'name',
        'description': 'description',
        'api_catalog_type': 'api_catalog_type',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'update_time': 'update_time',
        'update_user': 'update_user'
    }

    def __init__(self, catalog_id=None, pid=None, name=None, description=None, api_catalog_type=None, create_time=None, create_user=None, update_time=None, update_user=None):
        """RecordForGetAllCatalog

        The model defined in huaweicloud sdk

        :param catalog_id: 目录编号
        :type catalog_id: str
        :param pid: 父目录编号
        :type pid: str
        :param name: 名称
        :type name: str
        :param description: 目录描述
        :type description: str
        :param api_catalog_type: 目录类型
        :type api_catalog_type: str
        :param create_time: 创建时间
        :type create_time: int
        :param create_user: 创建者
        :type create_user: str
        :param update_time: 更新时间
        :type update_time: int
        :param update_user: 更新者
        :type update_user: str
        """
        
        

        self._catalog_id = None
        self._pid = None
        self._name = None
        self._description = None
        self._api_catalog_type = None
        self._create_time = None
        self._create_user = None
        self._update_time = None
        self._update_user = None
        self.discriminator = None

        if catalog_id is not None:
            self.catalog_id = catalog_id
        if pid is not None:
            self.pid = pid
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if api_catalog_type is not None:
            self.api_catalog_type = api_catalog_type
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
        """Gets the catalog_id of this RecordForGetAllCatalog.

        目录编号

        :return: The catalog_id of this RecordForGetAllCatalog.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """Sets the catalog_id of this RecordForGetAllCatalog.

        目录编号

        :param catalog_id: The catalog_id of this RecordForGetAllCatalog.
        :type catalog_id: str
        """
        self._catalog_id = catalog_id

    @property
    def pid(self):
        """Gets the pid of this RecordForGetAllCatalog.

        父目录编号

        :return: The pid of this RecordForGetAllCatalog.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this RecordForGetAllCatalog.

        父目录编号

        :param pid: The pid of this RecordForGetAllCatalog.
        :type pid: str
        """
        self._pid = pid

    @property
    def name(self):
        """Gets the name of this RecordForGetAllCatalog.

        名称

        :return: The name of this RecordForGetAllCatalog.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RecordForGetAllCatalog.

        名称

        :param name: The name of this RecordForGetAllCatalog.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this RecordForGetAllCatalog.

        目录描述

        :return: The description of this RecordForGetAllCatalog.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RecordForGetAllCatalog.

        目录描述

        :param description: The description of this RecordForGetAllCatalog.
        :type description: str
        """
        self._description = description

    @property
    def api_catalog_type(self):
        """Gets the api_catalog_type of this RecordForGetAllCatalog.

        目录类型

        :return: The api_catalog_type of this RecordForGetAllCatalog.
        :rtype: str
        """
        return self._api_catalog_type

    @api_catalog_type.setter
    def api_catalog_type(self, api_catalog_type):
        """Sets the api_catalog_type of this RecordForGetAllCatalog.

        目录类型

        :param api_catalog_type: The api_catalog_type of this RecordForGetAllCatalog.
        :type api_catalog_type: str
        """
        self._api_catalog_type = api_catalog_type

    @property
    def create_time(self):
        """Gets the create_time of this RecordForGetAllCatalog.

        创建时间

        :return: The create_time of this RecordForGetAllCatalog.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this RecordForGetAllCatalog.

        创建时间

        :param create_time: The create_time of this RecordForGetAllCatalog.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this RecordForGetAllCatalog.

        创建者

        :return: The create_user of this RecordForGetAllCatalog.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this RecordForGetAllCatalog.

        创建者

        :param create_user: The create_user of this RecordForGetAllCatalog.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def update_time(self):
        """Gets the update_time of this RecordForGetAllCatalog.

        更新时间

        :return: The update_time of this RecordForGetAllCatalog.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this RecordForGetAllCatalog.

        更新时间

        :param update_time: The update_time of this RecordForGetAllCatalog.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def update_user(self):
        """Gets the update_user of this RecordForGetAllCatalog.

        更新者

        :return: The update_user of this RecordForGetAllCatalog.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this RecordForGetAllCatalog.

        更新者

        :param update_user: The update_user of this RecordForGetAllCatalog.
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
        if not isinstance(other, RecordForGetAllCatalog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
