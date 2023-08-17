# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTestCaseAndDefectInfoRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'branch_id': 'str',
        'create_testcase_start_time': 'str',
        'create_testcase_end_time': 'str',
        'associate_defect_start_time': 'str',
        'associate_defect_end_time': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'branch_id': 'branch_id',
        'create_testcase_start_time': 'create_testcase_start_time',
        'create_testcase_end_time': 'create_testcase_end_time',
        'associate_defect_start_time': 'associate_defect_start_time',
        'associate_defect_end_time': 'associate_defect_end_time'
    }

    def __init__(self, offset=None, limit=None, branch_id=None, create_testcase_start_time=None, create_testcase_end_time=None, associate_defect_start_time=None, associate_defect_end_time=None):
        """ShowTestCaseAndDefectInfoRequestBody

        The model defined in huaweicloud sdk

        :param offset: 起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000
        :type offset: int
        :param limit: 每页显示的条目数量,最大支持100条
        :type limit: int
        :param branch_id: 分支ID
        :type branch_id: str
        :param create_testcase_start_time: 用例创建时间段开始
        :type create_testcase_start_time: str
        :param create_testcase_end_time: 用例创建时间段截止
        :type create_testcase_end_time: str
        :param associate_defect_start_time: 缺陷关联时间段开始
        :type associate_defect_start_time: str
        :param associate_defect_end_time: 缺陷关联时间段截止
        :type associate_defect_end_time: str
        """
        
        

        self._offset = None
        self._limit = None
        self._branch_id = None
        self._create_testcase_start_time = None
        self._create_testcase_end_time = None
        self._associate_defect_start_time = None
        self._associate_defect_end_time = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit
        if branch_id is not None:
            self.branch_id = branch_id
        self.create_testcase_start_time = create_testcase_start_time
        self.create_testcase_end_time = create_testcase_end_time
        if associate_defect_start_time is not None:
            self.associate_defect_start_time = associate_defect_start_time
        if associate_defect_end_time is not None:
            self.associate_defect_end_time = associate_defect_end_time

    @property
    def offset(self):
        """Gets the offset of this ShowTestCaseAndDefectInfoRequestBody.

        起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000

        :return: The offset of this ShowTestCaseAndDefectInfoRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowTestCaseAndDefectInfoRequestBody.

        起始偏移量，表示从此偏移量开始查询，offset大于等于0，小于等于100000

        :param offset: The offset of this ShowTestCaseAndDefectInfoRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowTestCaseAndDefectInfoRequestBody.

        每页显示的条目数量,最大支持100条

        :return: The limit of this ShowTestCaseAndDefectInfoRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowTestCaseAndDefectInfoRequestBody.

        每页显示的条目数量,最大支持100条

        :param limit: The limit of this ShowTestCaseAndDefectInfoRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def branch_id(self):
        """Gets the branch_id of this ShowTestCaseAndDefectInfoRequestBody.

        分支ID

        :return: The branch_id of this ShowTestCaseAndDefectInfoRequestBody.
        :rtype: str
        """
        return self._branch_id

    @branch_id.setter
    def branch_id(self, branch_id):
        """Sets the branch_id of this ShowTestCaseAndDefectInfoRequestBody.

        分支ID

        :param branch_id: The branch_id of this ShowTestCaseAndDefectInfoRequestBody.
        :type branch_id: str
        """
        self._branch_id = branch_id

    @property
    def create_testcase_start_time(self):
        """Gets the create_testcase_start_time of this ShowTestCaseAndDefectInfoRequestBody.

        用例创建时间段开始

        :return: The create_testcase_start_time of this ShowTestCaseAndDefectInfoRequestBody.
        :rtype: str
        """
        return self._create_testcase_start_time

    @create_testcase_start_time.setter
    def create_testcase_start_time(self, create_testcase_start_time):
        """Sets the create_testcase_start_time of this ShowTestCaseAndDefectInfoRequestBody.

        用例创建时间段开始

        :param create_testcase_start_time: The create_testcase_start_time of this ShowTestCaseAndDefectInfoRequestBody.
        :type create_testcase_start_time: str
        """
        self._create_testcase_start_time = create_testcase_start_time

    @property
    def create_testcase_end_time(self):
        """Gets the create_testcase_end_time of this ShowTestCaseAndDefectInfoRequestBody.

        用例创建时间段截止

        :return: The create_testcase_end_time of this ShowTestCaseAndDefectInfoRequestBody.
        :rtype: str
        """
        return self._create_testcase_end_time

    @create_testcase_end_time.setter
    def create_testcase_end_time(self, create_testcase_end_time):
        """Sets the create_testcase_end_time of this ShowTestCaseAndDefectInfoRequestBody.

        用例创建时间段截止

        :param create_testcase_end_time: The create_testcase_end_time of this ShowTestCaseAndDefectInfoRequestBody.
        :type create_testcase_end_time: str
        """
        self._create_testcase_end_time = create_testcase_end_time

    @property
    def associate_defect_start_time(self):
        """Gets the associate_defect_start_time of this ShowTestCaseAndDefectInfoRequestBody.

        缺陷关联时间段开始

        :return: The associate_defect_start_time of this ShowTestCaseAndDefectInfoRequestBody.
        :rtype: str
        """
        return self._associate_defect_start_time

    @associate_defect_start_time.setter
    def associate_defect_start_time(self, associate_defect_start_time):
        """Sets the associate_defect_start_time of this ShowTestCaseAndDefectInfoRequestBody.

        缺陷关联时间段开始

        :param associate_defect_start_time: The associate_defect_start_time of this ShowTestCaseAndDefectInfoRequestBody.
        :type associate_defect_start_time: str
        """
        self._associate_defect_start_time = associate_defect_start_time

    @property
    def associate_defect_end_time(self):
        """Gets the associate_defect_end_time of this ShowTestCaseAndDefectInfoRequestBody.

        缺陷关联时间段截止

        :return: The associate_defect_end_time of this ShowTestCaseAndDefectInfoRequestBody.
        :rtype: str
        """
        return self._associate_defect_end_time

    @associate_defect_end_time.setter
    def associate_defect_end_time(self, associate_defect_end_time):
        """Sets the associate_defect_end_time of this ShowTestCaseAndDefectInfoRequestBody.

        缺陷关联时间段截止

        :param associate_defect_end_time: The associate_defect_end_time of this ShowTestCaseAndDefectInfoRequestBody.
        :type associate_defect_end_time: str
        """
        self._associate_defect_end_time = associate_defect_end_time

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
        if not isinstance(other, ShowTestCaseAndDefectInfoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
