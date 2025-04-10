# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TestCaseReviewVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str',
        'testcase_name': 'str',
        'testcase_number': 'str',
        'testcase_stage': 'str',
        'testcase_last_modified': 'str',
        'testcase_last_modified_timestamp': 'int',
        'testcase_uri': 'str',
        'version_uri': 'str',
        'version_name': 'str',
        'comment': 'str',
        'close_comment': 'str',
        'reviewer': 'str',
        'creation_date': 'str',
        'creation_date_timestamp': 'int',
        'close_user_ids': 'list[NameAndIdVo]',
        'actual_close_person': 'str',
        'status': 'str',
        'close_date': 'str',
        'close_date_timestamp': 'int',
        'expect_close_date': 'str',
        'expect_close_date_timestamp': 'int'
    }

    attribute_map = {
        'uri': 'uri',
        'testcase_name': 'testcase_name',
        'testcase_number': 'testcase_number',
        'testcase_stage': 'testcase_stage',
        'testcase_last_modified': 'testcase_last_modified',
        'testcase_last_modified_timestamp': 'testcase_last_modified_timestamp',
        'testcase_uri': 'testcase_uri',
        'version_uri': 'version_uri',
        'version_name': 'version_name',
        'comment': 'comment',
        'close_comment': 'close_comment',
        'reviewer': 'reviewer',
        'creation_date': 'creation_date',
        'creation_date_timestamp': 'creation_date_timestamp',
        'close_user_ids': 'close_user_ids',
        'actual_close_person': 'actual_close_person',
        'status': 'status',
        'close_date': 'close_date',
        'close_date_timestamp': 'close_date_timestamp',
        'expect_close_date': 'expect_close_date',
        'expect_close_date_timestamp': 'expect_close_date_timestamp'
    }

    def __init__(self, uri=None, testcase_name=None, testcase_number=None, testcase_stage=None, testcase_last_modified=None, testcase_last_modified_timestamp=None, testcase_uri=None, version_uri=None, version_name=None, comment=None, close_comment=None, reviewer=None, creation_date=None, creation_date_timestamp=None, close_user_ids=None, actual_close_person=None, status=None, close_date=None, close_date_timestamp=None, expect_close_date=None, expect_close_date_timestamp=None):
        r"""TestCaseReviewVo

        The model defined in huaweicloud sdk

        :param uri: 评审URI
        :type uri: str
        :param testcase_name: 用例名称
        :type testcase_name: str
        :param testcase_number: 用例编号
        :type testcase_number: str
        :param testcase_stage: 用例阶段
        :type testcase_stage: str
        :param testcase_last_modified: 用例修改时间
        :type testcase_last_modified: str
        :param testcase_last_modified_timestamp: 用例修改时间时间戳
        :type testcase_last_modified_timestamp: int
        :param testcase_uri: 分支用例URI
        :type testcase_uri: str
        :param version_uri: 版本URI
        :type version_uri: str
        :param version_name: 版本名称
        :type version_name: str
        :param comment: 评审意见
        :type comment: str
        :param close_comment: 闭环意见
        :type close_comment: str
        :param reviewer: 评审人
        :type reviewer: str
        :param creation_date: 评审创建时间
        :type creation_date: str
        :param creation_date_timestamp: 评审创建时间时间戳
        :type creation_date_timestamp: int
        :param close_user_ids: 指定的闭环人列表
        :type close_user_ids: list[:class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`]
        :param actual_close_person: 实际闭环人
        :type actual_close_person: str
        :param status: 评审状态
        :type status: str
        :param close_date: 评审闭环时间
        :type close_date: str
        :param close_date_timestamp: 评审闭环时间时间戳
        :type close_date_timestamp: int
        :param expect_close_date: 期望闭环时间
        :type expect_close_date: str
        :param expect_close_date_timestamp: 期望闭环时间时间戳
        :type expect_close_date_timestamp: int
        """
        
        

        self._uri = None
        self._testcase_name = None
        self._testcase_number = None
        self._testcase_stage = None
        self._testcase_last_modified = None
        self._testcase_last_modified_timestamp = None
        self._testcase_uri = None
        self._version_uri = None
        self._version_name = None
        self._comment = None
        self._close_comment = None
        self._reviewer = None
        self._creation_date = None
        self._creation_date_timestamp = None
        self._close_user_ids = None
        self._actual_close_person = None
        self._status = None
        self._close_date = None
        self._close_date_timestamp = None
        self._expect_close_date = None
        self._expect_close_date_timestamp = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri
        if testcase_name is not None:
            self.testcase_name = testcase_name
        if testcase_number is not None:
            self.testcase_number = testcase_number
        if testcase_stage is not None:
            self.testcase_stage = testcase_stage
        if testcase_last_modified is not None:
            self.testcase_last_modified = testcase_last_modified
        if testcase_last_modified_timestamp is not None:
            self.testcase_last_modified_timestamp = testcase_last_modified_timestamp
        if testcase_uri is not None:
            self.testcase_uri = testcase_uri
        if version_uri is not None:
            self.version_uri = version_uri
        if version_name is not None:
            self.version_name = version_name
        if comment is not None:
            self.comment = comment
        if close_comment is not None:
            self.close_comment = close_comment
        if reviewer is not None:
            self.reviewer = reviewer
        if creation_date is not None:
            self.creation_date = creation_date
        if creation_date_timestamp is not None:
            self.creation_date_timestamp = creation_date_timestamp
        if close_user_ids is not None:
            self.close_user_ids = close_user_ids
        if actual_close_person is not None:
            self.actual_close_person = actual_close_person
        if status is not None:
            self.status = status
        if close_date is not None:
            self.close_date = close_date
        if close_date_timestamp is not None:
            self.close_date_timestamp = close_date_timestamp
        if expect_close_date is not None:
            self.expect_close_date = expect_close_date
        if expect_close_date_timestamp is not None:
            self.expect_close_date_timestamp = expect_close_date_timestamp

    @property
    def uri(self):
        r"""Gets the uri of this TestCaseReviewVo.

        评审URI

        :return: The uri of this TestCaseReviewVo.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this TestCaseReviewVo.

        评审URI

        :param uri: The uri of this TestCaseReviewVo.
        :type uri: str
        """
        self._uri = uri

    @property
    def testcase_name(self):
        r"""Gets the testcase_name of this TestCaseReviewVo.

        用例名称

        :return: The testcase_name of this TestCaseReviewVo.
        :rtype: str
        """
        return self._testcase_name

    @testcase_name.setter
    def testcase_name(self, testcase_name):
        r"""Sets the testcase_name of this TestCaseReviewVo.

        用例名称

        :param testcase_name: The testcase_name of this TestCaseReviewVo.
        :type testcase_name: str
        """
        self._testcase_name = testcase_name

    @property
    def testcase_number(self):
        r"""Gets the testcase_number of this TestCaseReviewVo.

        用例编号

        :return: The testcase_number of this TestCaseReviewVo.
        :rtype: str
        """
        return self._testcase_number

    @testcase_number.setter
    def testcase_number(self, testcase_number):
        r"""Sets the testcase_number of this TestCaseReviewVo.

        用例编号

        :param testcase_number: The testcase_number of this TestCaseReviewVo.
        :type testcase_number: str
        """
        self._testcase_number = testcase_number

    @property
    def testcase_stage(self):
        r"""Gets the testcase_stage of this TestCaseReviewVo.

        用例阶段

        :return: The testcase_stage of this TestCaseReviewVo.
        :rtype: str
        """
        return self._testcase_stage

    @testcase_stage.setter
    def testcase_stage(self, testcase_stage):
        r"""Sets the testcase_stage of this TestCaseReviewVo.

        用例阶段

        :param testcase_stage: The testcase_stage of this TestCaseReviewVo.
        :type testcase_stage: str
        """
        self._testcase_stage = testcase_stage

    @property
    def testcase_last_modified(self):
        r"""Gets the testcase_last_modified of this TestCaseReviewVo.

        用例修改时间

        :return: The testcase_last_modified of this TestCaseReviewVo.
        :rtype: str
        """
        return self._testcase_last_modified

    @testcase_last_modified.setter
    def testcase_last_modified(self, testcase_last_modified):
        r"""Sets the testcase_last_modified of this TestCaseReviewVo.

        用例修改时间

        :param testcase_last_modified: The testcase_last_modified of this TestCaseReviewVo.
        :type testcase_last_modified: str
        """
        self._testcase_last_modified = testcase_last_modified

    @property
    def testcase_last_modified_timestamp(self):
        r"""Gets the testcase_last_modified_timestamp of this TestCaseReviewVo.

        用例修改时间时间戳

        :return: The testcase_last_modified_timestamp of this TestCaseReviewVo.
        :rtype: int
        """
        return self._testcase_last_modified_timestamp

    @testcase_last_modified_timestamp.setter
    def testcase_last_modified_timestamp(self, testcase_last_modified_timestamp):
        r"""Sets the testcase_last_modified_timestamp of this TestCaseReviewVo.

        用例修改时间时间戳

        :param testcase_last_modified_timestamp: The testcase_last_modified_timestamp of this TestCaseReviewVo.
        :type testcase_last_modified_timestamp: int
        """
        self._testcase_last_modified_timestamp = testcase_last_modified_timestamp

    @property
    def testcase_uri(self):
        r"""Gets the testcase_uri of this TestCaseReviewVo.

        分支用例URI

        :return: The testcase_uri of this TestCaseReviewVo.
        :rtype: str
        """
        return self._testcase_uri

    @testcase_uri.setter
    def testcase_uri(self, testcase_uri):
        r"""Sets the testcase_uri of this TestCaseReviewVo.

        分支用例URI

        :param testcase_uri: The testcase_uri of this TestCaseReviewVo.
        :type testcase_uri: str
        """
        self._testcase_uri = testcase_uri

    @property
    def version_uri(self):
        r"""Gets the version_uri of this TestCaseReviewVo.

        版本URI

        :return: The version_uri of this TestCaseReviewVo.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this TestCaseReviewVo.

        版本URI

        :param version_uri: The version_uri of this TestCaseReviewVo.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def version_name(self):
        r"""Gets the version_name of this TestCaseReviewVo.

        版本名称

        :return: The version_name of this TestCaseReviewVo.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        r"""Sets the version_name of this TestCaseReviewVo.

        版本名称

        :param version_name: The version_name of this TestCaseReviewVo.
        :type version_name: str
        """
        self._version_name = version_name

    @property
    def comment(self):
        r"""Gets the comment of this TestCaseReviewVo.

        评审意见

        :return: The comment of this TestCaseReviewVo.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this TestCaseReviewVo.

        评审意见

        :param comment: The comment of this TestCaseReviewVo.
        :type comment: str
        """
        self._comment = comment

    @property
    def close_comment(self):
        r"""Gets the close_comment of this TestCaseReviewVo.

        闭环意见

        :return: The close_comment of this TestCaseReviewVo.
        :rtype: str
        """
        return self._close_comment

    @close_comment.setter
    def close_comment(self, close_comment):
        r"""Sets the close_comment of this TestCaseReviewVo.

        闭环意见

        :param close_comment: The close_comment of this TestCaseReviewVo.
        :type close_comment: str
        """
        self._close_comment = close_comment

    @property
    def reviewer(self):
        r"""Gets the reviewer of this TestCaseReviewVo.

        评审人

        :return: The reviewer of this TestCaseReviewVo.
        :rtype: str
        """
        return self._reviewer

    @reviewer.setter
    def reviewer(self, reviewer):
        r"""Sets the reviewer of this TestCaseReviewVo.

        评审人

        :param reviewer: The reviewer of this TestCaseReviewVo.
        :type reviewer: str
        """
        self._reviewer = reviewer

    @property
    def creation_date(self):
        r"""Gets the creation_date of this TestCaseReviewVo.

        评审创建时间

        :return: The creation_date of this TestCaseReviewVo.
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        r"""Sets the creation_date of this TestCaseReviewVo.

        评审创建时间

        :param creation_date: The creation_date of this TestCaseReviewVo.
        :type creation_date: str
        """
        self._creation_date = creation_date

    @property
    def creation_date_timestamp(self):
        r"""Gets the creation_date_timestamp of this TestCaseReviewVo.

        评审创建时间时间戳

        :return: The creation_date_timestamp of this TestCaseReviewVo.
        :rtype: int
        """
        return self._creation_date_timestamp

    @creation_date_timestamp.setter
    def creation_date_timestamp(self, creation_date_timestamp):
        r"""Sets the creation_date_timestamp of this TestCaseReviewVo.

        评审创建时间时间戳

        :param creation_date_timestamp: The creation_date_timestamp of this TestCaseReviewVo.
        :type creation_date_timestamp: int
        """
        self._creation_date_timestamp = creation_date_timestamp

    @property
    def close_user_ids(self):
        r"""Gets the close_user_ids of this TestCaseReviewVo.

        指定的闭环人列表

        :return: The close_user_ids of this TestCaseReviewVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`]
        """
        return self._close_user_ids

    @close_user_ids.setter
    def close_user_ids(self, close_user_ids):
        r"""Sets the close_user_ids of this TestCaseReviewVo.

        指定的闭环人列表

        :param close_user_ids: The close_user_ids of this TestCaseReviewVo.
        :type close_user_ids: list[:class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`]
        """
        self._close_user_ids = close_user_ids

    @property
    def actual_close_person(self):
        r"""Gets the actual_close_person of this TestCaseReviewVo.

        实际闭环人

        :return: The actual_close_person of this TestCaseReviewVo.
        :rtype: str
        """
        return self._actual_close_person

    @actual_close_person.setter
    def actual_close_person(self, actual_close_person):
        r"""Sets the actual_close_person of this TestCaseReviewVo.

        实际闭环人

        :param actual_close_person: The actual_close_person of this TestCaseReviewVo.
        :type actual_close_person: str
        """
        self._actual_close_person = actual_close_person

    @property
    def status(self):
        r"""Gets the status of this TestCaseReviewVo.

        评审状态

        :return: The status of this TestCaseReviewVo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TestCaseReviewVo.

        评审状态

        :param status: The status of this TestCaseReviewVo.
        :type status: str
        """
        self._status = status

    @property
    def close_date(self):
        r"""Gets the close_date of this TestCaseReviewVo.

        评审闭环时间

        :return: The close_date of this TestCaseReviewVo.
        :rtype: str
        """
        return self._close_date

    @close_date.setter
    def close_date(self, close_date):
        r"""Sets the close_date of this TestCaseReviewVo.

        评审闭环时间

        :param close_date: The close_date of this TestCaseReviewVo.
        :type close_date: str
        """
        self._close_date = close_date

    @property
    def close_date_timestamp(self):
        r"""Gets the close_date_timestamp of this TestCaseReviewVo.

        评审闭环时间时间戳

        :return: The close_date_timestamp of this TestCaseReviewVo.
        :rtype: int
        """
        return self._close_date_timestamp

    @close_date_timestamp.setter
    def close_date_timestamp(self, close_date_timestamp):
        r"""Sets the close_date_timestamp of this TestCaseReviewVo.

        评审闭环时间时间戳

        :param close_date_timestamp: The close_date_timestamp of this TestCaseReviewVo.
        :type close_date_timestamp: int
        """
        self._close_date_timestamp = close_date_timestamp

    @property
    def expect_close_date(self):
        r"""Gets the expect_close_date of this TestCaseReviewVo.

        期望闭环时间

        :return: The expect_close_date of this TestCaseReviewVo.
        :rtype: str
        """
        return self._expect_close_date

    @expect_close_date.setter
    def expect_close_date(self, expect_close_date):
        r"""Sets the expect_close_date of this TestCaseReviewVo.

        期望闭环时间

        :param expect_close_date: The expect_close_date of this TestCaseReviewVo.
        :type expect_close_date: str
        """
        self._expect_close_date = expect_close_date

    @property
    def expect_close_date_timestamp(self):
        r"""Gets the expect_close_date_timestamp of this TestCaseReviewVo.

        期望闭环时间时间戳

        :return: The expect_close_date_timestamp of this TestCaseReviewVo.
        :rtype: int
        """
        return self._expect_close_date_timestamp

    @expect_close_date_timestamp.setter
    def expect_close_date_timestamp(self, expect_close_date_timestamp):
        r"""Sets the expect_close_date_timestamp of this TestCaseReviewVo.

        期望闭环时间时间戳

        :param expect_close_date_timestamp: The expect_close_date_timestamp of this TestCaseReviewVo.
        :type expect_close_date_timestamp: int
        """
        self._expect_close_date_timestamp = expect_close_date_timestamp

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
        if not isinstance(other, TestCaseReviewVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
