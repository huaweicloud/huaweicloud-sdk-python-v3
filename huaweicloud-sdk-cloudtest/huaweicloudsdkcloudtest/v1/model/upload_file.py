# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadFile:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aw_ins_id': 'str',
        'create_time': 'str',
        'create_time_stamp': 'int',
        'create_time_string': 'str',
        'create_user': 'str',
        'current_size': 'int',
        'file_path': 'str',
        'id': 'str',
        'name': 'str',
        'origin_name': 'str',
        'project_id': 'str',
        'region': 'str',
        'testcase_id': 'str',
        'update_time': 'str',
        'update_time_stamp': 'int',
        'update_time_string': 'str',
        'update_user': 'str'
    }

    attribute_map = {
        'aw_ins_id': 'awInsId',
        'create_time': 'create_time',
        'create_time_stamp': 'create_time_stamp',
        'create_time_string': 'create_time_string',
        'create_user': 'create_user',
        'current_size': 'current_size',
        'file_path': 'filePath',
        'id': 'id',
        'name': 'name',
        'origin_name': 'originName',
        'project_id': 'projectId',
        'region': 'region',
        'testcase_id': 'testcase_id',
        'update_time': 'update_time',
        'update_time_stamp': 'update_time_stamp',
        'update_time_string': 'update_time_string',
        'update_user': 'update_user'
    }

    def __init__(self, aw_ins_id=None, create_time=None, create_time_stamp=None, create_time_string=None, create_user=None, current_size=None, file_path=None, id=None, name=None, origin_name=None, project_id=None, region=None, testcase_id=None, update_time=None, update_time_stamp=None, update_time_string=None, update_user=None):
        """UploadFile

        The model defined in huaweicloud sdk

        :param aw_ins_id: 所属的AWInstance的ID
        :type aw_ins_id: str
        :param create_time: 创建时间
        :type create_time: str
        :param create_time_stamp: 创建时间戳
        :type create_time_stamp: int
        :param create_time_string: 创建时间字符串
        :type create_time_string: str
        :param create_user: 创建人
        :type create_user: str
        :param current_size: 当前大小
        :type current_size: int
        :param file_path: 文件路径
        :type file_path: str
        :param id: id
        :type id: str
        :param name: 名称
        :type name: str
        :param origin_name: 文件的原名
        :type origin_name: str
        :param project_id: 项目ID
        :type project_id: str
        :param region: 区域名称
        :type region: str
        :param testcase_id: 测试用例的唯一标识符
        :type testcase_id: str
        :param update_time: 更新时间
        :type update_time: str
        :param update_time_stamp: 更新时间戳
        :type update_time_stamp: int
        :param update_time_string: 更新时间字符串
        :type update_time_string: str
        :param update_user: 更新人
        :type update_user: str
        """
        
        

        self._aw_ins_id = None
        self._create_time = None
        self._create_time_stamp = None
        self._create_time_string = None
        self._create_user = None
        self._current_size = None
        self._file_path = None
        self._id = None
        self._name = None
        self._origin_name = None
        self._project_id = None
        self._region = None
        self._testcase_id = None
        self._update_time = None
        self._update_time_stamp = None
        self._update_time_string = None
        self._update_user = None
        self.discriminator = None

        if aw_ins_id is not None:
            self.aw_ins_id = aw_ins_id
        if create_time is not None:
            self.create_time = create_time
        if create_time_stamp is not None:
            self.create_time_stamp = create_time_stamp
        if create_time_string is not None:
            self.create_time_string = create_time_string
        if create_user is not None:
            self.create_user = create_user
        if current_size is not None:
            self.current_size = current_size
        if file_path is not None:
            self.file_path = file_path
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if origin_name is not None:
            self.origin_name = origin_name
        if project_id is not None:
            self.project_id = project_id
        if region is not None:
            self.region = region
        if testcase_id is not None:
            self.testcase_id = testcase_id
        if update_time is not None:
            self.update_time = update_time
        if update_time_stamp is not None:
            self.update_time_stamp = update_time_stamp
        if update_time_string is not None:
            self.update_time_string = update_time_string
        if update_user is not None:
            self.update_user = update_user

    @property
    def aw_ins_id(self):
        """Gets the aw_ins_id of this UploadFile.

        所属的AWInstance的ID

        :return: The aw_ins_id of this UploadFile.
        :rtype: str
        """
        return self._aw_ins_id

    @aw_ins_id.setter
    def aw_ins_id(self, aw_ins_id):
        """Sets the aw_ins_id of this UploadFile.

        所属的AWInstance的ID

        :param aw_ins_id: The aw_ins_id of this UploadFile.
        :type aw_ins_id: str
        """
        self._aw_ins_id = aw_ins_id

    @property
    def create_time(self):
        """Gets the create_time of this UploadFile.

        创建时间

        :return: The create_time of this UploadFile.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UploadFile.

        创建时间

        :param create_time: The create_time of this UploadFile.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def create_time_stamp(self):
        """Gets the create_time_stamp of this UploadFile.

        创建时间戳

        :return: The create_time_stamp of this UploadFile.
        :rtype: int
        """
        return self._create_time_stamp

    @create_time_stamp.setter
    def create_time_stamp(self, create_time_stamp):
        """Sets the create_time_stamp of this UploadFile.

        创建时间戳

        :param create_time_stamp: The create_time_stamp of this UploadFile.
        :type create_time_stamp: int
        """
        self._create_time_stamp = create_time_stamp

    @property
    def create_time_string(self):
        """Gets the create_time_string of this UploadFile.

        创建时间字符串

        :return: The create_time_string of this UploadFile.
        :rtype: str
        """
        return self._create_time_string

    @create_time_string.setter
    def create_time_string(self, create_time_string):
        """Sets the create_time_string of this UploadFile.

        创建时间字符串

        :param create_time_string: The create_time_string of this UploadFile.
        :type create_time_string: str
        """
        self._create_time_string = create_time_string

    @property
    def create_user(self):
        """Gets the create_user of this UploadFile.

        创建人

        :return: The create_user of this UploadFile.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this UploadFile.

        创建人

        :param create_user: The create_user of this UploadFile.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def current_size(self):
        """Gets the current_size of this UploadFile.

        当前大小

        :return: The current_size of this UploadFile.
        :rtype: int
        """
        return self._current_size

    @current_size.setter
    def current_size(self, current_size):
        """Sets the current_size of this UploadFile.

        当前大小

        :param current_size: The current_size of this UploadFile.
        :type current_size: int
        """
        self._current_size = current_size

    @property
    def file_path(self):
        """Gets the file_path of this UploadFile.

        文件路径

        :return: The file_path of this UploadFile.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this UploadFile.

        文件路径

        :param file_path: The file_path of this UploadFile.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def id(self):
        """Gets the id of this UploadFile.

        id

        :return: The id of this UploadFile.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UploadFile.

        id

        :param id: The id of this UploadFile.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UploadFile.

        名称

        :return: The name of this UploadFile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UploadFile.

        名称

        :param name: The name of this UploadFile.
        :type name: str
        """
        self._name = name

    @property
    def origin_name(self):
        """Gets the origin_name of this UploadFile.

        文件的原名

        :return: The origin_name of this UploadFile.
        :rtype: str
        """
        return self._origin_name

    @origin_name.setter
    def origin_name(self, origin_name):
        """Sets the origin_name of this UploadFile.

        文件的原名

        :param origin_name: The origin_name of this UploadFile.
        :type origin_name: str
        """
        self._origin_name = origin_name

    @property
    def project_id(self):
        """Gets the project_id of this UploadFile.

        项目ID

        :return: The project_id of this UploadFile.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this UploadFile.

        项目ID

        :param project_id: The project_id of this UploadFile.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region(self):
        """Gets the region of this UploadFile.

        区域名称

        :return: The region of this UploadFile.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this UploadFile.

        区域名称

        :param region: The region of this UploadFile.
        :type region: str
        """
        self._region = region

    @property
    def testcase_id(self):
        """Gets the testcase_id of this UploadFile.

        测试用例的唯一标识符

        :return: The testcase_id of this UploadFile.
        :rtype: str
        """
        return self._testcase_id

    @testcase_id.setter
    def testcase_id(self, testcase_id):
        """Sets the testcase_id of this UploadFile.

        测试用例的唯一标识符

        :param testcase_id: The testcase_id of this UploadFile.
        :type testcase_id: str
        """
        self._testcase_id = testcase_id

    @property
    def update_time(self):
        """Gets the update_time of this UploadFile.

        更新时间

        :return: The update_time of this UploadFile.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this UploadFile.

        更新时间

        :param update_time: The update_time of this UploadFile.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def update_time_stamp(self):
        """Gets the update_time_stamp of this UploadFile.

        更新时间戳

        :return: The update_time_stamp of this UploadFile.
        :rtype: int
        """
        return self._update_time_stamp

    @update_time_stamp.setter
    def update_time_stamp(self, update_time_stamp):
        """Sets the update_time_stamp of this UploadFile.

        更新时间戳

        :param update_time_stamp: The update_time_stamp of this UploadFile.
        :type update_time_stamp: int
        """
        self._update_time_stamp = update_time_stamp

    @property
    def update_time_string(self):
        """Gets the update_time_string of this UploadFile.

        更新时间字符串

        :return: The update_time_string of this UploadFile.
        :rtype: str
        """
        return self._update_time_string

    @update_time_string.setter
    def update_time_string(self, update_time_string):
        """Sets the update_time_string of this UploadFile.

        更新时间字符串

        :param update_time_string: The update_time_string of this UploadFile.
        :type update_time_string: str
        """
        self._update_time_string = update_time_string

    @property
    def update_user(self):
        """Gets the update_user of this UploadFile.

        更新人

        :return: The update_user of this UploadFile.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """Sets the update_user of this UploadFile.

        更新人

        :param update_user: The update_user of this UploadFile.
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
        if not isinstance(other, UploadFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
