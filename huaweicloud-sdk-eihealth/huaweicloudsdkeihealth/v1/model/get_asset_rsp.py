# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetAssetRsp:

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
        'category': 'str',
        'name': 'str',
        'title': 'str',
        'labels': 'list[str]',
        'picture': 'str',
        'vendor_id': 'str',
        'latest_version': 'VersionRsp',
        'versions': 'list[str]',
        'create_time': 'str',
        'update_time': 'str',
        'stars': 'int',
        'subscribes': 'int'
    }

    attribute_map = {
        'id': 'id',
        'category': 'category',
        'name': 'name',
        'title': 'title',
        'labels': 'labels',
        'picture': 'picture',
        'vendor_id': 'vendor_id',
        'latest_version': 'latest_version',
        'versions': 'versions',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'stars': 'stars',
        'subscribes': 'subscribes'
    }

    def __init__(self, id=None, category=None, name=None, title=None, labels=None, picture=None, vendor_id=None, latest_version=None, versions=None, create_time=None, update_time=None, stars=None, subscribes=None):
        """GetAssetRsp

        The model defined in huaweicloud sdk

        :param id: 资产id
        :type id: str
        :param category: 类别
        :type category: str
        :param name: 资产名
        :type name: str
        :param title: 资产展示名
        :type title: str
        :param labels: 资产标签列表
        :type labels: list[str]
        :param picture: 资产封面图访问链接
        :type picture: str
        :param vendor_id: 供应商id
        :type vendor_id: str
        :param latest_version: 
        :type latest_version: :class:`huaweicloudsdkeihealth.v1.VersionRsp`
        :param versions: 资产版本号列表
        :type versions: list[str]
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param stars: 收藏数
        :type stars: int
        :param subscribes: 订阅数
        :type subscribes: int
        """
        
        

        self._id = None
        self._category = None
        self._name = None
        self._title = None
        self._labels = None
        self._picture = None
        self._vendor_id = None
        self._latest_version = None
        self._versions = None
        self._create_time = None
        self._update_time = None
        self._stars = None
        self._subscribes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if category is not None:
            self.category = category
        if name is not None:
            self.name = name
        if title is not None:
            self.title = title
        if labels is not None:
            self.labels = labels
        if picture is not None:
            self.picture = picture
        if vendor_id is not None:
            self.vendor_id = vendor_id
        if latest_version is not None:
            self.latest_version = latest_version
        if versions is not None:
            self.versions = versions
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if stars is not None:
            self.stars = stars
        if subscribes is not None:
            self.subscribes = subscribes

    @property
    def id(self):
        """Gets the id of this GetAssetRsp.

        资产id

        :return: The id of this GetAssetRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetAssetRsp.

        资产id

        :param id: The id of this GetAssetRsp.
        :type id: str
        """
        self._id = id

    @property
    def category(self):
        """Gets the category of this GetAssetRsp.

        类别

        :return: The category of this GetAssetRsp.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this GetAssetRsp.

        类别

        :param category: The category of this GetAssetRsp.
        :type category: str
        """
        self._category = category

    @property
    def name(self):
        """Gets the name of this GetAssetRsp.

        资产名

        :return: The name of this GetAssetRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetAssetRsp.

        资产名

        :param name: The name of this GetAssetRsp.
        :type name: str
        """
        self._name = name

    @property
    def title(self):
        """Gets the title of this GetAssetRsp.

        资产展示名

        :return: The title of this GetAssetRsp.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GetAssetRsp.

        资产展示名

        :param title: The title of this GetAssetRsp.
        :type title: str
        """
        self._title = title

    @property
    def labels(self):
        """Gets the labels of this GetAssetRsp.

        资产标签列表

        :return: The labels of this GetAssetRsp.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this GetAssetRsp.

        资产标签列表

        :param labels: The labels of this GetAssetRsp.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def picture(self):
        """Gets the picture of this GetAssetRsp.

        资产封面图访问链接

        :return: The picture of this GetAssetRsp.
        :rtype: str
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        """Sets the picture of this GetAssetRsp.

        资产封面图访问链接

        :param picture: The picture of this GetAssetRsp.
        :type picture: str
        """
        self._picture = picture

    @property
    def vendor_id(self):
        """Gets the vendor_id of this GetAssetRsp.

        供应商id

        :return: The vendor_id of this GetAssetRsp.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """Sets the vendor_id of this GetAssetRsp.

        供应商id

        :param vendor_id: The vendor_id of this GetAssetRsp.
        :type vendor_id: str
        """
        self._vendor_id = vendor_id

    @property
    def latest_version(self):
        """Gets the latest_version of this GetAssetRsp.

        :return: The latest_version of this GetAssetRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.VersionRsp`
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this GetAssetRsp.

        :param latest_version: The latest_version of this GetAssetRsp.
        :type latest_version: :class:`huaweicloudsdkeihealth.v1.VersionRsp`
        """
        self._latest_version = latest_version

    @property
    def versions(self):
        """Gets the versions of this GetAssetRsp.

        资产版本号列表

        :return: The versions of this GetAssetRsp.
        :rtype: list[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this GetAssetRsp.

        资产版本号列表

        :param versions: The versions of this GetAssetRsp.
        :type versions: list[str]
        """
        self._versions = versions

    @property
    def create_time(self):
        """Gets the create_time of this GetAssetRsp.

        创建时间

        :return: The create_time of this GetAssetRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this GetAssetRsp.

        创建时间

        :param create_time: The create_time of this GetAssetRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this GetAssetRsp.

        更新时间

        :return: The update_time of this GetAssetRsp.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this GetAssetRsp.

        更新时间

        :param update_time: The update_time of this GetAssetRsp.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def stars(self):
        """Gets the stars of this GetAssetRsp.

        收藏数

        :return: The stars of this GetAssetRsp.
        :rtype: int
        """
        return self._stars

    @stars.setter
    def stars(self, stars):
        """Sets the stars of this GetAssetRsp.

        收藏数

        :param stars: The stars of this GetAssetRsp.
        :type stars: int
        """
        self._stars = stars

    @property
    def subscribes(self):
        """Gets the subscribes of this GetAssetRsp.

        订阅数

        :return: The subscribes of this GetAssetRsp.
        :rtype: int
        """
        return self._subscribes

    @subscribes.setter
    def subscribes(self, subscribes):
        """Sets the subscribes of this GetAssetRsp.

        订阅数

        :param subscribes: The subscribes of this GetAssetRsp.
        :type subscribes: int
        """
        self._subscribes = subscribes

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
        if not isinstance(other, GetAssetRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
