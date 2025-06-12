# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListKeystoreSearchResponseBodyResultKeystoreList:

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
        'permission': 'ListKeystoreSearchResponseBodyResultPermission',
        'create_time_stamp': 'str',
        'update_time_stamp': 'str',
        'domain_id': 'str',
        'domain_name': 'str',
        'keystore_name': 'str',
        'create_user_id': 'str',
        'create_user_name': 'str',
        'update_user_id': 'str',
        'update_user_name': 'str',
        'share': 'float',
        'create_time': 'str',
        'update_time': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'permission': 'permission',
        'create_time_stamp': 'create_time_stamp',
        'update_time_stamp': 'update_time_stamp',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'keystore_name': 'keystore_name',
        'create_user_id': 'create_user_id',
        'create_user_name': 'create_user_name',
        'update_user_id': 'update_user_id',
        'update_user_name': 'update_user_name',
        'share': 'share',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'description': 'description'
    }

    def __init__(self, id=None, permission=None, create_time_stamp=None, update_time_stamp=None, domain_id=None, domain_name=None, keystore_name=None, create_user_id=None, create_user_name=None, update_user_id=None, update_user_name=None, share=None, create_time=None, update_time=None, description=None):
        r"""ListKeystoreSearchResponseBodyResultKeystoreList

        The model defined in huaweicloud sdk

        :param id: 文件ID
        :type id: str
        :param permission: 
        :type permission: :class:`huaweicloudsdkcodeartsbuild.v3.ListKeystoreSearchResponseBodyResultPermission`
        :param create_time_stamp: 创建时间戳
        :type create_time_stamp: str
        :param update_time_stamp: 修改时间戳
        :type update_time_stamp: str
        :param domain_id: 租户ID
        :type domain_id: str
        :param domain_name: 租户名
        :type domain_name: str
        :param keystore_name: 文件名
        :type keystore_name: str
        :param create_user_id: 文件创建者用户ID
        :type create_user_id: str
        :param create_user_name: 文件创建者用户名
        :type create_user_name: str
        :param update_user_id: 文件修改者用户ID
        :type update_user_id: str
        :param update_user_name: 文件修改者用户名
        :type update_user_name: str
        :param share: 是否共享，开启后允许租户内所有成员在编译构建中使用该文件
        :type share: float
        :param create_time: 更新时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param description: 描述信息
        :type description: str
        """
        
        

        self._id = None
        self._permission = None
        self._create_time_stamp = None
        self._update_time_stamp = None
        self._domain_id = None
        self._domain_name = None
        self._keystore_name = None
        self._create_user_id = None
        self._create_user_name = None
        self._update_user_id = None
        self._update_user_name = None
        self._share = None
        self._create_time = None
        self._update_time = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if permission is not None:
            self.permission = permission
        if create_time_stamp is not None:
            self.create_time_stamp = create_time_stamp
        if update_time_stamp is not None:
            self.update_time_stamp = update_time_stamp
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if keystore_name is not None:
            self.keystore_name = keystore_name
        if create_user_id is not None:
            self.create_user_id = create_user_id
        if create_user_name is not None:
            self.create_user_name = create_user_name
        if update_user_id is not None:
            self.update_user_id = update_user_id
        if update_user_name is not None:
            self.update_user_name = update_user_name
        if share is not None:
            self.share = share
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this ListKeystoreSearchResponseBodyResultKeystoreList.

        文件ID

        :return: The id of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListKeystoreSearchResponseBodyResultKeystoreList.

        文件ID

        :param id: The id of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :type id: str
        """
        self._id = id

    @property
    def permission(self):
        r"""Gets the permission of this ListKeystoreSearchResponseBodyResultKeystoreList.

        :return: The permission of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :rtype: :class:`huaweicloudsdkcodeartsbuild.v3.ListKeystoreSearchResponseBodyResultPermission`
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this ListKeystoreSearchResponseBodyResultKeystoreList.

        :param permission: The permission of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :type permission: :class:`huaweicloudsdkcodeartsbuild.v3.ListKeystoreSearchResponseBodyResultPermission`
        """
        self._permission = permission

    @property
    def create_time_stamp(self):
        r"""Gets the create_time_stamp of this ListKeystoreSearchResponseBodyResultKeystoreList.

        创建时间戳

        :return: The create_time_stamp of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :rtype: str
        """
        return self._create_time_stamp

    @create_time_stamp.setter
    def create_time_stamp(self, create_time_stamp):
        r"""Sets the create_time_stamp of this ListKeystoreSearchResponseBodyResultKeystoreList.

        创建时间戳

        :param create_time_stamp: The create_time_stamp of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :type create_time_stamp: str
        """
        self._create_time_stamp = create_time_stamp

    @property
    def update_time_stamp(self):
        r"""Gets the update_time_stamp of this ListKeystoreSearchResponseBodyResultKeystoreList.

        修改时间戳

        :return: The update_time_stamp of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :rtype: str
        """
        return self._update_time_stamp

    @update_time_stamp.setter
    def update_time_stamp(self, update_time_stamp):
        r"""Sets the update_time_stamp of this ListKeystoreSearchResponseBodyResultKeystoreList.

        修改时间戳

        :param update_time_stamp: The update_time_stamp of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :type update_time_stamp: str
        """
        self._update_time_stamp = update_time_stamp

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListKeystoreSearchResponseBodyResultKeystoreList.

        租户ID

        :return: The domain_id of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListKeystoreSearchResponseBodyResultKeystoreList.

        租户ID

        :param domain_id: The domain_id of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ListKeystoreSearchResponseBodyResultKeystoreList.

        租户名

        :return: The domain_name of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ListKeystoreSearchResponseBodyResultKeystoreList.

        租户名

        :param domain_name: The domain_name of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def keystore_name(self):
        r"""Gets the keystore_name of this ListKeystoreSearchResponseBodyResultKeystoreList.

        文件名

        :return: The keystore_name of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :rtype: str
        """
        return self._keystore_name

    @keystore_name.setter
    def keystore_name(self, keystore_name):
        r"""Sets the keystore_name of this ListKeystoreSearchResponseBodyResultKeystoreList.

        文件名

        :param keystore_name: The keystore_name of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :type keystore_name: str
        """
        self._keystore_name = keystore_name

    @property
    def create_user_id(self):
        r"""Gets the create_user_id of this ListKeystoreSearchResponseBodyResultKeystoreList.

        文件创建者用户ID

        :return: The create_user_id of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :rtype: str
        """
        return self._create_user_id

    @create_user_id.setter
    def create_user_id(self, create_user_id):
        r"""Sets the create_user_id of this ListKeystoreSearchResponseBodyResultKeystoreList.

        文件创建者用户ID

        :param create_user_id: The create_user_id of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :type create_user_id: str
        """
        self._create_user_id = create_user_id

    @property
    def create_user_name(self):
        r"""Gets the create_user_name of this ListKeystoreSearchResponseBodyResultKeystoreList.

        文件创建者用户名

        :return: The create_user_name of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :rtype: str
        """
        return self._create_user_name

    @create_user_name.setter
    def create_user_name(self, create_user_name):
        r"""Sets the create_user_name of this ListKeystoreSearchResponseBodyResultKeystoreList.

        文件创建者用户名

        :param create_user_name: The create_user_name of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :type create_user_name: str
        """
        self._create_user_name = create_user_name

    @property
    def update_user_id(self):
        r"""Gets the update_user_id of this ListKeystoreSearchResponseBodyResultKeystoreList.

        文件修改者用户ID

        :return: The update_user_id of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :rtype: str
        """
        return self._update_user_id

    @update_user_id.setter
    def update_user_id(self, update_user_id):
        r"""Sets the update_user_id of this ListKeystoreSearchResponseBodyResultKeystoreList.

        文件修改者用户ID

        :param update_user_id: The update_user_id of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :type update_user_id: str
        """
        self._update_user_id = update_user_id

    @property
    def update_user_name(self):
        r"""Gets the update_user_name of this ListKeystoreSearchResponseBodyResultKeystoreList.

        文件修改者用户名

        :return: The update_user_name of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :rtype: str
        """
        return self._update_user_name

    @update_user_name.setter
    def update_user_name(self, update_user_name):
        r"""Sets the update_user_name of this ListKeystoreSearchResponseBodyResultKeystoreList.

        文件修改者用户名

        :param update_user_name: The update_user_name of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :type update_user_name: str
        """
        self._update_user_name = update_user_name

    @property
    def share(self):
        r"""Gets the share of this ListKeystoreSearchResponseBodyResultKeystoreList.

        是否共享，开启后允许租户内所有成员在编译构建中使用该文件

        :return: The share of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :rtype: float
        """
        return self._share

    @share.setter
    def share(self, share):
        r"""Sets the share of this ListKeystoreSearchResponseBodyResultKeystoreList.

        是否共享，开启后允许租户内所有成员在编译构建中使用该文件

        :param share: The share of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :type share: float
        """
        self._share = share

    @property
    def create_time(self):
        r"""Gets the create_time of this ListKeystoreSearchResponseBodyResultKeystoreList.

        更新时间

        :return: The create_time of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListKeystoreSearchResponseBodyResultKeystoreList.

        更新时间

        :param create_time: The create_time of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ListKeystoreSearchResponseBodyResultKeystoreList.

        更新时间

        :return: The update_time of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ListKeystoreSearchResponseBodyResultKeystoreList.

        更新时间

        :param update_time: The update_time of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def description(self):
        r"""Gets the description of this ListKeystoreSearchResponseBodyResultKeystoreList.

        描述信息

        :return: The description of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListKeystoreSearchResponseBodyResultKeystoreList.

        描述信息

        :param description: The description of this ListKeystoreSearchResponseBodyResultKeystoreList.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ListKeystoreSearchResponseBodyResultKeystoreList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
