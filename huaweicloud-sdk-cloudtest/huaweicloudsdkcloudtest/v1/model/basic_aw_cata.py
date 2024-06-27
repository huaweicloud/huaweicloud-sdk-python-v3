# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BasicAwCata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aw_dir': 'str',
        'cata_type': 'int',
        'create_time': 'str',
        'create_user': 'str',
        'create_user_id': 'str',
        'desc': 'str',
        'extra_info': 'str',
        'id': 'str',
        'is_folder': 'str',
        'name': 'str',
        'name_view': 'str',
        'parent_id': 'str',
        'project_id': 'str',
        'ref_cnt': 'int',
        'region': 'str',
        'update_time': 'str',
        'update_user': 'str'
    }

    attribute_map = {
        'aw_dir': 'aw_dir',
        'cata_type': 'cata_type',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'create_user_id': 'create_user_id',
        'desc': 'desc',
        'extra_info': 'extra_info',
        'id': 'id',
        'is_folder': 'is_folder',
        'name': 'name',
        'name_view': 'nameView',
        'parent_id': 'parent_id',
        'project_id': 'project_id',
        'ref_cnt': 'refCnt',
        'region': 'region',
        'update_time': 'update_time',
        'update_user': 'update_user'
    }

    def __init__(self, aw_dir=None, cata_type=None, create_time=None, create_user=None, create_user_id=None, desc=None, extra_info=None, id=None, is_folder=None, name=None, name_view=None, parent_id=None, project_id=None, ref_cnt=None, region=None, update_time=None, update_user=None):
        """BasicAwCata

        The model defined in huaweicloud sdk

        :param aw_dir: aw归属目录信息
        :type aw_dir: str
        :param cata_type: 目录层级
        :type cata_type: int
        :param create_time: 创建时间
        :type create_time: str
        :param create_user: 创建人
        :type create_user: str
        :param create_user_id: 创建人id
        :type create_user_id: str
        :param desc: 目录描述
        :type desc: str
        :param extra_info: 引用次数
        :type extra_info: str
        :param id: id
        :type id: str
        :param is_folder: 判断是否为文件夹的标识
        :type is_folder: str
        :param name: 名称
        :type name: str
        :param name_view: aw在页面上显示的名字
        :type name_view: str
        :param parent_id: aw目录父编号
        :type parent_id: str
        :param project_id: 工程ID
        :type project_id: str
        :param ref_cnt: 引用次数
        :type ref_cnt: int
        :param region: 区域名称
        :type region: str
        :param update_time: 更新时间
        :type update_time: str
        :param update_user: 更新人
        :type update_user: str
        """
        
        

        self._aw_dir = None
        self._cata_type = None
        self._create_time = None
        self._create_user = None
        self._create_user_id = None
        self._desc = None
        self._extra_info = None
        self._id = None
        self._is_folder = None
        self._name = None
        self._name_view = None
        self._parent_id = None
        self._project_id = None
        self._ref_cnt = None
        self._region = None
        self._update_time = None
        self._update_user = None
        self.discriminator = None

        if aw_dir is not None:
            self.aw_dir = aw_dir
        if cata_type is not None:
            self.cata_type = cata_type
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if create_user_id is not None:
            self.create_user_id = create_user_id
        if desc is not None:
            self.desc = desc
        if extra_info is not None:
            self.extra_info = extra_info
        if id is not None:
            self.id = id
        if is_folder is not None:
            self.is_folder = is_folder
        if name is not None:
            self.name = name
        if name_view is not None:
            self.name_view = name_view
        if parent_id is not None:
            self.parent_id = parent_id
        if project_id is not None:
            self.project_id = project_id
        if ref_cnt is not None:
            self.ref_cnt = ref_cnt
        if region is not None:
            self.region = region
        if update_time is not None:
            self.update_time = update_time
        if update_user is not None:
            self.update_user = update_user

    @property
    def aw_dir(self):
        """Gets the aw_dir of this BasicAwCata.

        aw归属目录信息

        :return: The aw_dir of this BasicAwCata.
        :rtype: str
        """
        return self._aw_dir

    @aw_dir.setter
    def aw_dir(self, aw_dir):
        """Sets the aw_dir of this BasicAwCata.

        aw归属目录信息

        :param aw_dir: The aw_dir of this BasicAwCata.
        :type aw_dir: str
        """
        self._aw_dir = aw_dir

    @property
    def cata_type(self):
        """Gets the cata_type of this BasicAwCata.

        目录层级

        :return: The cata_type of this BasicAwCata.
        :rtype: int
        """
        return self._cata_type

    @cata_type.setter
    def cata_type(self, cata_type):
        """Sets the cata_type of this BasicAwCata.

        目录层级

        :param cata_type: The cata_type of this BasicAwCata.
        :type cata_type: int
        """
        self._cata_type = cata_type

    @property
    def create_time(self):
        """Gets the create_time of this BasicAwCata.

        创建时间

        :return: The create_time of this BasicAwCata.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this BasicAwCata.

        创建时间

        :param create_time: The create_time of this BasicAwCata.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def create_user(self):
        """Gets the create_user of this BasicAwCata.

        创建人

        :return: The create_user of this BasicAwCata.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this BasicAwCata.

        创建人

        :param create_user: The create_user of this BasicAwCata.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def create_user_id(self):
        """Gets the create_user_id of this BasicAwCata.

        创建人id

        :return: The create_user_id of this BasicAwCata.
        :rtype: str
        """
        return self._create_user_id

    @create_user_id.setter
    def create_user_id(self, create_user_id):
        """Sets the create_user_id of this BasicAwCata.

        创建人id

        :param create_user_id: The create_user_id of this BasicAwCata.
        :type create_user_id: str
        """
        self._create_user_id = create_user_id

    @property
    def desc(self):
        """Gets the desc of this BasicAwCata.

        目录描述

        :return: The desc of this BasicAwCata.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this BasicAwCata.

        目录描述

        :param desc: The desc of this BasicAwCata.
        :type desc: str
        """
        self._desc = desc

    @property
    def extra_info(self):
        """Gets the extra_info of this BasicAwCata.

        引用次数

        :return: The extra_info of this BasicAwCata.
        :rtype: str
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this BasicAwCata.

        引用次数

        :param extra_info: The extra_info of this BasicAwCata.
        :type extra_info: str
        """
        self._extra_info = extra_info

    @property
    def id(self):
        """Gets the id of this BasicAwCata.

        id

        :return: The id of this BasicAwCata.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BasicAwCata.

        id

        :param id: The id of this BasicAwCata.
        :type id: str
        """
        self._id = id

    @property
    def is_folder(self):
        """Gets the is_folder of this BasicAwCata.

        判断是否为文件夹的标识

        :return: The is_folder of this BasicAwCata.
        :rtype: str
        """
        return self._is_folder

    @is_folder.setter
    def is_folder(self, is_folder):
        """Sets the is_folder of this BasicAwCata.

        判断是否为文件夹的标识

        :param is_folder: The is_folder of this BasicAwCata.
        :type is_folder: str
        """
        self._is_folder = is_folder

    @property
    def name(self):
        """Gets the name of this BasicAwCata.

        名称

        :return: The name of this BasicAwCata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BasicAwCata.

        名称

        :param name: The name of this BasicAwCata.
        :type name: str
        """
        self._name = name

    @property
    def name_view(self):
        """Gets the name_view of this BasicAwCata.

        aw在页面上显示的名字

        :return: The name_view of this BasicAwCata.
        :rtype: str
        """
        return self._name_view

    @name_view.setter
    def name_view(self, name_view):
        """Sets the name_view of this BasicAwCata.

        aw在页面上显示的名字

        :param name_view: The name_view of this BasicAwCata.
        :type name_view: str
        """
        self._name_view = name_view

    @property
    def parent_id(self):
        """Gets the parent_id of this BasicAwCata.

        aw目录父编号

        :return: The parent_id of this BasicAwCata.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this BasicAwCata.

        aw目录父编号

        :param parent_id: The parent_id of this BasicAwCata.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def project_id(self):
        """Gets the project_id of this BasicAwCata.

        工程ID

        :return: The project_id of this BasicAwCata.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BasicAwCata.

        工程ID

        :param project_id: The project_id of this BasicAwCata.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def ref_cnt(self):
        """Gets the ref_cnt of this BasicAwCata.

        引用次数

        :return: The ref_cnt of this BasicAwCata.
        :rtype: int
        """
        return self._ref_cnt

    @ref_cnt.setter
    def ref_cnt(self, ref_cnt):
        """Sets the ref_cnt of this BasicAwCata.

        引用次数

        :param ref_cnt: The ref_cnt of this BasicAwCata.
        :type ref_cnt: int
        """
        self._ref_cnt = ref_cnt

    @property
    def region(self):
        """Gets the region of this BasicAwCata.

        区域名称

        :return: The region of this BasicAwCata.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this BasicAwCata.

        区域名称

        :param region: The region of this BasicAwCata.
        :type region: str
        """
        self._region = region

    @property
    def update_time(self):
        """Gets the update_time of this BasicAwCata.

        更新时间

        :return: The update_time of this BasicAwCata.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this BasicAwCata.

        更新时间

        :param update_time: The update_time of this BasicAwCata.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def update_user(self):
        """Gets the update_user of this BasicAwCata.

        更新人

        :return: The update_user of this BasicAwCata.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this BasicAwCata.

        更新人

        :param update_user: The update_user of this BasicAwCata.
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
        if not isinstance(other, BasicAwCata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
