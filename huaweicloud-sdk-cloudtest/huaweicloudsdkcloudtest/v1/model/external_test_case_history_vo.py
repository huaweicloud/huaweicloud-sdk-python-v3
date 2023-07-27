# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalTestCaseHistoryVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'author': 'str',
        'region': 'str',
        'changes': 'list[ResourceChangeExternalVo]',
        'id': 'str',
        'testcase_id': 'str',
        'creation_date': 'datetime',
        'create_date_timestamp': 'int',
        'author_name': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'author': 'author',
        'region': 'region',
        'changes': 'changes',
        'id': 'id',
        'testcase_id': 'testcase_id',
        'creation_date': 'creation_date',
        'create_date_timestamp': 'create_date_timestamp',
        'author_name': 'author_name',
        'project_id': 'project_id'
    }

    def __init__(self, author=None, region=None, changes=None, id=None, testcase_id=None, creation_date=None, create_date_timestamp=None, author_name=None, project_id=None):
        """ExternalTestCaseHistoryVo

        The model defined in huaweicloud sdk

        :param author: 资源历史记录创建人ID
        :type author: str
        :param region: 逻辑region
        :type region: str
        :param changes: 历史记录字段变更列表
        :type changes: list[:class:`huaweicloudsdkcloudtest.v1.ResourceChangeExternalVo`]
        :param id: 历史记录id
        :type id: str
        :param testcase_id: 用例id
        :type testcase_id: str
        :param creation_date: 创建时间
        :type creation_date: datetime
        :param create_date_timestamp: 创建时间时间戳
        :type create_date_timestamp: int
        :param author_name: 创建人名称
        :type author_name: str
        :param project_id: 项目id
        :type project_id: str
        """
        
        

        self._author = None
        self._region = None
        self._changes = None
        self._id = None
        self._testcase_id = None
        self._creation_date = None
        self._create_date_timestamp = None
        self._author_name = None
        self._project_id = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if region is not None:
            self.region = region
        if changes is not None:
            self.changes = changes
        if id is not None:
            self.id = id
        if testcase_id is not None:
            self.testcase_id = testcase_id
        if creation_date is not None:
            self.creation_date = creation_date
        if create_date_timestamp is not None:
            self.create_date_timestamp = create_date_timestamp
        if author_name is not None:
            self.author_name = author_name
        if project_id is not None:
            self.project_id = project_id

    @property
    def author(self):
        """Gets the author of this ExternalTestCaseHistoryVo.

        资源历史记录创建人ID

        :return: The author of this ExternalTestCaseHistoryVo.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ExternalTestCaseHistoryVo.

        资源历史记录创建人ID

        :param author: The author of this ExternalTestCaseHistoryVo.
        :type author: str
        """
        self._author = author

    @property
    def region(self):
        """Gets the region of this ExternalTestCaseHistoryVo.

        逻辑region

        :return: The region of this ExternalTestCaseHistoryVo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ExternalTestCaseHistoryVo.

        逻辑region

        :param region: The region of this ExternalTestCaseHistoryVo.
        :type region: str
        """
        self._region = region

    @property
    def changes(self):
        """Gets the changes of this ExternalTestCaseHistoryVo.

        历史记录字段变更列表

        :return: The changes of this ExternalTestCaseHistoryVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.ResourceChangeExternalVo`]
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this ExternalTestCaseHistoryVo.

        历史记录字段变更列表

        :param changes: The changes of this ExternalTestCaseHistoryVo.
        :type changes: list[:class:`huaweicloudsdkcloudtest.v1.ResourceChangeExternalVo`]
        """
        self._changes = changes

    @property
    def id(self):
        """Gets the id of this ExternalTestCaseHistoryVo.

        历史记录id

        :return: The id of this ExternalTestCaseHistoryVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalTestCaseHistoryVo.

        历史记录id

        :param id: The id of this ExternalTestCaseHistoryVo.
        :type id: str
        """
        self._id = id

    @property
    def testcase_id(self):
        """Gets the testcase_id of this ExternalTestCaseHistoryVo.

        用例id

        :return: The testcase_id of this ExternalTestCaseHistoryVo.
        :rtype: str
        """
        return self._testcase_id

    @testcase_id.setter
    def testcase_id(self, testcase_id):
        """Sets the testcase_id of this ExternalTestCaseHistoryVo.

        用例id

        :param testcase_id: The testcase_id of this ExternalTestCaseHistoryVo.
        :type testcase_id: str
        """
        self._testcase_id = testcase_id

    @property
    def creation_date(self):
        """Gets the creation_date of this ExternalTestCaseHistoryVo.

        创建时间

        :return: The creation_date of this ExternalTestCaseHistoryVo.
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ExternalTestCaseHistoryVo.

        创建时间

        :param creation_date: The creation_date of this ExternalTestCaseHistoryVo.
        :type creation_date: datetime
        """
        self._creation_date = creation_date

    @property
    def create_date_timestamp(self):
        """Gets the create_date_timestamp of this ExternalTestCaseHistoryVo.

        创建时间时间戳

        :return: The create_date_timestamp of this ExternalTestCaseHistoryVo.
        :rtype: int
        """
        return self._create_date_timestamp

    @create_date_timestamp.setter
    def create_date_timestamp(self, create_date_timestamp):
        """Sets the create_date_timestamp of this ExternalTestCaseHistoryVo.

        创建时间时间戳

        :param create_date_timestamp: The create_date_timestamp of this ExternalTestCaseHistoryVo.
        :type create_date_timestamp: int
        """
        self._create_date_timestamp = create_date_timestamp

    @property
    def author_name(self):
        """Gets the author_name of this ExternalTestCaseHistoryVo.

        创建人名称

        :return: The author_name of this ExternalTestCaseHistoryVo.
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        """Sets the author_name of this ExternalTestCaseHistoryVo.

        创建人名称

        :param author_name: The author_name of this ExternalTestCaseHistoryVo.
        :type author_name: str
        """
        self._author_name = author_name

    @property
    def project_id(self):
        """Gets the project_id of this ExternalTestCaseHistoryVo.

        项目id

        :return: The project_id of this ExternalTestCaseHistoryVo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ExternalTestCaseHistoryVo.

        项目id

        :param project_id: The project_id of this ExternalTestCaseHistoryVo.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, ExternalTestCaseHistoryVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
