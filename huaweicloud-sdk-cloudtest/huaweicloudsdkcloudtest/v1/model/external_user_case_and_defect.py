# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalUserCaseAndDefect:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creator': 'NameAndIdVo',
        'defect_count': 'int',
        'defect_ids': 'list[str]',
        'testcase_id': 'str',
        'branch_id': 'str'
    }

    attribute_map = {
        'creator': 'creator',
        'defect_count': 'defect_count',
        'defect_ids': 'defect_ids',
        'testcase_id': 'testcase_id',
        'branch_id': 'branch_id'
    }

    def __init__(self, creator=None, defect_count=None, defect_ids=None, testcase_id=None, branch_id=None):
        r"""ExternalUserCaseAndDefect

        The model defined in huaweicloud sdk

        :param creator: 
        :type creator: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        :param defect_count: 缺陷数
        :type defect_count: int
        :param defect_ids: 缺陷ID列表
        :type defect_ids: list[str]
        :param testcase_id: 用例ID
        :type testcase_id: str
        :param branch_id: 分支ID
        :type branch_id: str
        """
        
        

        self._creator = None
        self._defect_count = None
        self._defect_ids = None
        self._testcase_id = None
        self._branch_id = None
        self.discriminator = None

        if creator is not None:
            self.creator = creator
        if defect_count is not None:
            self.defect_count = defect_count
        if defect_ids is not None:
            self.defect_ids = defect_ids
        if testcase_id is not None:
            self.testcase_id = testcase_id
        if branch_id is not None:
            self.branch_id = branch_id

    @property
    def creator(self):
        r"""Gets the creator of this ExternalUserCaseAndDefect.

        :return: The creator of this ExternalUserCaseAndDefect.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ExternalUserCaseAndDefect.

        :param creator: The creator of this ExternalUserCaseAndDefect.
        :type creator: :class:`huaweicloudsdkcloudtest.v1.NameAndIdVo`
        """
        self._creator = creator

    @property
    def defect_count(self):
        r"""Gets the defect_count of this ExternalUserCaseAndDefect.

        缺陷数

        :return: The defect_count of this ExternalUserCaseAndDefect.
        :rtype: int
        """
        return self._defect_count

    @defect_count.setter
    def defect_count(self, defect_count):
        r"""Sets the defect_count of this ExternalUserCaseAndDefect.

        缺陷数

        :param defect_count: The defect_count of this ExternalUserCaseAndDefect.
        :type defect_count: int
        """
        self._defect_count = defect_count

    @property
    def defect_ids(self):
        r"""Gets the defect_ids of this ExternalUserCaseAndDefect.

        缺陷ID列表

        :return: The defect_ids of this ExternalUserCaseAndDefect.
        :rtype: list[str]
        """
        return self._defect_ids

    @defect_ids.setter
    def defect_ids(self, defect_ids):
        r"""Sets the defect_ids of this ExternalUserCaseAndDefect.

        缺陷ID列表

        :param defect_ids: The defect_ids of this ExternalUserCaseAndDefect.
        :type defect_ids: list[str]
        """
        self._defect_ids = defect_ids

    @property
    def testcase_id(self):
        r"""Gets the testcase_id of this ExternalUserCaseAndDefect.

        用例ID

        :return: The testcase_id of this ExternalUserCaseAndDefect.
        :rtype: str
        """
        return self._testcase_id

    @testcase_id.setter
    def testcase_id(self, testcase_id):
        r"""Sets the testcase_id of this ExternalUserCaseAndDefect.

        用例ID

        :param testcase_id: The testcase_id of this ExternalUserCaseAndDefect.
        :type testcase_id: str
        """
        self._testcase_id = testcase_id

    @property
    def branch_id(self):
        r"""Gets the branch_id of this ExternalUserCaseAndDefect.

        分支ID

        :return: The branch_id of this ExternalUserCaseAndDefect.
        :rtype: str
        """
        return self._branch_id

    @branch_id.setter
    def branch_id(self, branch_id):
        r"""Sets the branch_id of this ExternalUserCaseAndDefect.

        分支ID

        :param branch_id: The branch_id of this ExternalUserCaseAndDefect.
        :type branch_id: str
        """
        self._branch_id = branch_id

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
        if not isinstance(other, ExternalUserCaseAndDefect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
