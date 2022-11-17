# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAssetVersionResponse(SdkResponse):

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
        'name': 'str',
        'title': 'str',
        'category': 'str',
        'labels': 'list[str]',
        'vendor_id': 'str',
        'version': 'VersionRsp',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'title': 'title',
        'category': 'category',
        'labels': 'labels',
        'vendor_id': 'vendor_id',
        'version': 'version',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, title=None, category=None, labels=None, vendor_id=None, version=None, create_time=None, update_time=None):
        """ShowAssetVersionResponse

        The model defined in huaweicloud sdk

        :param id: 资产id
        :type id: str
        :param name: 资产名
        :type name: str
        :param title: 资产展示名
        :type title: str
        :param category: 类别
        :type category: str
        :param labels: 资产标签列表
        :type labels: list[str]
        :param vendor_id: 供应商id
        :type vendor_id: str
        :param version: 
        :type version: :class:`huaweicloudsdkeihealth.v1.VersionRsp`
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        super(ShowAssetVersionResponse, self).__init__()

        self._id = None
        self._name = None
        self._title = None
        self._category = None
        self._labels = None
        self._vendor_id = None
        self._version = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if title is not None:
            self.title = title
        if category is not None:
            self.category = category
        if labels is not None:
            self.labels = labels
        if vendor_id is not None:
            self.vendor_id = vendor_id
        if version is not None:
            self.version = version
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this ShowAssetVersionResponse.

        资产id

        :return: The id of this ShowAssetVersionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowAssetVersionResponse.

        资产id

        :param id: The id of this ShowAssetVersionResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowAssetVersionResponse.

        资产名

        :return: The name of this ShowAssetVersionResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowAssetVersionResponse.

        资产名

        :param name: The name of this ShowAssetVersionResponse.
        :type name: str
        """
        self._name = name

    @property
    def title(self):
        """Gets the title of this ShowAssetVersionResponse.

        资产展示名

        :return: The title of this ShowAssetVersionResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ShowAssetVersionResponse.

        资产展示名

        :param title: The title of this ShowAssetVersionResponse.
        :type title: str
        """
        self._title = title

    @property
    def category(self):
        """Gets the category of this ShowAssetVersionResponse.

        类别

        :return: The category of this ShowAssetVersionResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ShowAssetVersionResponse.

        类别

        :param category: The category of this ShowAssetVersionResponse.
        :type category: str
        """
        self._category = category

    @property
    def labels(self):
        """Gets the labels of this ShowAssetVersionResponse.

        资产标签列表

        :return: The labels of this ShowAssetVersionResponse.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ShowAssetVersionResponse.

        资产标签列表

        :param labels: The labels of this ShowAssetVersionResponse.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def vendor_id(self):
        """Gets the vendor_id of this ShowAssetVersionResponse.

        供应商id

        :return: The vendor_id of this ShowAssetVersionResponse.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """Sets the vendor_id of this ShowAssetVersionResponse.

        供应商id

        :param vendor_id: The vendor_id of this ShowAssetVersionResponse.
        :type vendor_id: str
        """
        self._vendor_id = vendor_id

    @property
    def version(self):
        """Gets the version of this ShowAssetVersionResponse.

        :return: The version of this ShowAssetVersionResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.VersionRsp`
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowAssetVersionResponse.

        :param version: The version of this ShowAssetVersionResponse.
        :type version: :class:`huaweicloudsdkeihealth.v1.VersionRsp`
        """
        self._version = version

    @property
    def create_time(self):
        """Gets the create_time of this ShowAssetVersionResponse.

        创建时间

        :return: The create_time of this ShowAssetVersionResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowAssetVersionResponse.

        创建时间

        :param create_time: The create_time of this ShowAssetVersionResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowAssetVersionResponse.

        更新时间

        :return: The update_time of this ShowAssetVersionResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowAssetVersionResponse.

        更新时间

        :param update_time: The update_time of this ShowAssetVersionResponse.
        :type update_time: str
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
        if not isinstance(other, ShowAssetVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
